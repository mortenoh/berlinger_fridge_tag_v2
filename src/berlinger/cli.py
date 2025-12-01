"""CLI for Berlinger FridgeTag to DHIS2 integration."""

from pathlib import Path

import typer
from dotenv import load_dotenv

from .dhis2_client import TrackedEntityNotFoundError
from .dhis2_service import DHIS2Service, NoEnrollmentFoundError, NoSerialFoundError

load_dotenv()

app = typer.Typer(help="Berlinger FridgeTag to DHIS2 CLI")


@app.command()
def search(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
) -> None:
    """Search for a tracked entity by parsing the serial from a FridgeTag file."""
    service = DHIS2Service()

    try:
        result = service.search_by_file(file)
    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except TrackedEntityNotFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

    # Print nicely formatted output
    typer.echo(f"Searching for serial: {result.serial}")
    typer.echo("")
    typer.echo("Found tracked entity:")
    typer.echo(f"  Serial:          {result.serial}")
    typer.echo(f"  TrackedEntity:   {result.tracked_entity.trackedEntity}")
    typer.echo(f"  OrgUnit:         {result.tracked_entity.orgUnit}")

    if result.tracked_entity.enrollments:
        enrollment = result.tracked_entity.enrollments[0]
        typer.echo(f"  Enrollment:      {enrollment.enrollment}")
        typer.echo(f"  Enrollment Org:  {enrollment.orgUnit}")


@app.command()
def get_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
) -> None:
    """Get existing events for a tracked entity from a FridgeTag file."""
    service = DHIS2Service()

    try:
        data = service.parse_file(file)
        serial = service.get_serial(data)

        # Get dates from the input file
        file_dates = {record.date for record in data.history.records}

        result = service.client.get_events(serial)

        if result.trackedEntity:
            typer.echo(f"Serial: {serial}, TrackedEntity: {result.trackedEntity}")
        else:
            typer.echo(f"Serial: {serial}, TrackedEntity: not found")
            return

        typer.echo(f"File records: {len(file_dates)} date(s)")

        # Track which file dates have been matched
        matched_file_dates = set()

        typer.echo("")
        # Print table header
        typer.echo(f"{'UID':<15} {'Date':<12} {'Status':<10} {'Match':<8}")
        typer.echo("-" * 48)

        for event in result.events:
            date = event.occurredAt[:10] if len(event.occurredAt) >= 10 else event.occurredAt
            if date in file_dates:
                match = "yes"
                matched_file_dates.add(date)
            else:
                match = "-"
            typer.echo(f"{event.event:<15} {date:<12} {event.status:<10} {match:<8}")

        typer.echo("")
        typer.echo(f"Total: {len(result.events)} event(s)")

        # Show unmatched file dates
        unmatched_file_dates = file_dates - matched_file_dates
        if unmatched_file_dates:
            typer.echo(f"Unmatched file dates ({len(unmatched_file_dates)}): {', '.join(sorted(unmatched_file_dates))}")

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def enroll(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    org_unit: str = typer.Option(..., "--org-unit", "-o", help="Organisation unit UID"),
    manufacturer: str = typer.Option("", "--manufacturer", "-m", help="Appliance manufacturer"),
    model: str = typer.Option("", "--model", help="Appliance model"),
    pqs_code: str = typer.Option("", "--pqs-code", help="Appliance PQS code"),
    appliance_serial: str = typer.Option("", "--appliance-serial", help="Appliance manufacturer serial number"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be done without making changes"),
) -> None:
    """Create tracked entity with enrollment from a FridgeTag file."""
    from datetime import date

    service = DHIS2Service()

    try:
        data = service.parse_file(file)
        serial = service.get_serial(data)
        typer.echo(f"Serial: {serial}")

        # Check if already exists
        try:
            tracked_entity = service.search_by_serial(serial)
            typer.echo(f"TrackedEntity: {tracked_entity.trackedEntity} (already exists)")
            typer.echo(f"OrgUnit: {tracked_entity.orgUnit}")

            if tracked_entity.enrollments:
                typer.echo(f"Enrollments: {len(tracked_entity.enrollments)}")
                for enrollment in tracked_entity.enrollments:
                    typer.echo(f"  - {enrollment.enrollment} (orgUnit: {enrollment.orgUnit})")
            else:
                typer.echo("Enrollments: none")
            return

        except TrackedEntityNotFoundError:
            typer.echo("TrackedEntity: not found, will create")

        enrolled_at = date.today().isoformat()

        if dry_run:
            from .dhis2_client import DHIS2Client
            from .dhis2_models import (
                EnrollmentPayload,
                TrackedEntitiesPayload,
                TrackedEntityAttribute,
                TrackedEntityPayload,
            )

            attrs = [
                TrackedEntityAttribute(attribute=DHIS2Client.MANUFACTURER_ATTRIBUTE_UID, value=manufacturer),
                TrackedEntityAttribute(attribute=DHIS2Client.MODEL_ATTRIBUTE_UID, value=model),
                TrackedEntityAttribute(attribute=DHIS2Client.PQS_CODE_ATTRIBUTE_UID, value=pqs_code),
                TrackedEntityAttribute(attribute=DHIS2Client.APPLIANCE_SERIAL_ATTRIBUTE_UID, value=appliance_serial),
                TrackedEntityAttribute(attribute=DHIS2Client.SERIAL_ATTRIBUTE_UID, value=str(serial)),
            ]

            enroll_payload = EnrollmentPayload(
                program=DHIS2Client.PROGRAM_UID,
                status="ACTIVE",
                orgUnit=org_unit,
                occurredAt=enrolled_at,
                enrolledAt=enrolled_at,
                attributes=attrs,
                events=[],
            )

            te_payload = TrackedEntityPayload(
                orgUnit=org_unit,
                trackedEntityType=DHIS2Client.TRACKED_ENTITY_TYPE_UID,
                attributes=attrs,
                enrollments=[enroll_payload],
            )

            payload = TrackedEntitiesPayload(trackedEntities=[te_payload])

            typer.echo("")
            typer.echo("[DRY RUN] Would POST to /api/42/tracker:")
            typer.echo(payload.model_dump_json(indent=2))
            return

        # Create tracked entity with enrollment
        result = service.client.create_tracked_entity_with_enrollment(
            org_unit=org_unit,
            serial=str(serial),
            manufacturer=manufacturer,
            model=model,
            pqs_code=pqs_code,
            appliance_serial=appliance_serial,
            enrolled_at=enrolled_at,
        )

        status = result.get("status", "UNKNOWN")
        if status == "OK":
            typer.echo("Success! Created tracked entity with enrollment.")
        else:
            typer.echo(f"Response status: {status}", err=True)
            raise typer.Exit(1)

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def check_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
) -> None:
    """Check for duplicate events (same date) that may cause data issues."""
    from collections import defaultdict

    service = DHIS2Service()

    try:
        data = service.parse_file(file)
        serial = service.get_serial(data)

        result = service.client.get_events(serial)

        if result.trackedEntity:
            typer.echo(f"Serial: {serial}, TrackedEntity: {result.trackedEntity}")
        else:
            typer.echo(f"Serial: {serial}, TrackedEntity: not found")
            return

        typer.echo(f"Found {len(result.events)} existing event(s)")

        # Group events by date
        events_by_date: dict[str, list[str]] = defaultdict(list)
        for ev in result.events:
            date = ev.occurredAt[:10] if len(ev.occurredAt) >= 10 else ev.occurredAt
            events_by_date[date].append(ev.event)

        # Find duplicates
        duplicates = {date: uids for date, uids in events_by_date.items() if len(uids) > 1}

        if duplicates:
            typer.echo("")
            typer.echo("Duplicate dates found:")
            for date in sorted(duplicates.keys()):
                uids = duplicates[date]
                typer.echo(f"  {date}: {len(uids)} events ({', '.join(uids)})")
            typer.echo("")
            typer.echo(f"Warning: {len(duplicates)} date(s) have duplicate events")
        else:
            typer.echo("No duplicate dates found.")

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def create_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be created without sending"),
) -> None:
    """Create DHIS2 events from a FridgeTag file (one per history record)."""
    service = DHIS2Service()

    try:
        # Parse file and get serial
        data = service.parse_file(file)
        serial = service.get_serial(data)
        typer.echo(f"Processing serial: {serial}")
        typer.echo(f"Found {len(data.history.records)} history record(s)")

        # Search for tracked entity
        tracked_entity = service.search_by_serial(serial)
        typer.echo(f"Found tracked entity: {tracked_entity.trackedEntity}")

        # Fetch existing events and create date -> event UID mapping
        existing_result = service.client.get_events(serial)
        existing_events: dict[str, str] = {}
        duplicate_dates: set[str] = set()
        for ev in existing_result.events:
            date = ev.occurredAt[:10] if len(ev.occurredAt) >= 10 else ev.occurredAt
            if date in existing_events:
                duplicate_dates.add(date)
            else:
                existing_events[date] = ev.event

        # Remove duplicates from mapping (will create new instead of update)
        for dup_date in duplicate_dates:
            existing_events.pop(dup_date, None)

        typer.echo(f"Found {len(existing_result.events)} existing event(s)")
        if duplicate_dates:
            dup_list = ", ".join(sorted(duplicate_dates))
            typer.echo(f"Warning: {len(duplicate_dates)} date(s) have duplicates, will create new: {dup_list}")

        # Build events for all history records
        events = service.build_events(tracked_entity, data, existing_events=existing_events)

        # Count updates vs creates
        updates = sum(1 for e in events if e.event is not None)
        creates = len(events) - updates

        if dry_run:
            typer.echo(f"\n[DRY RUN] Would process {len(events)} event(s): {creates} create, {updates} update")
            for i, event in enumerate(events, 1):
                action = "UPDATE" if event.event else "CREATE"
                typer.echo(f"\n--- Event {i} ({action}, date: {event.occurredAt}) ---")
                typer.echo(event.model_dump_json(indent=2, exclude_none=True))
            return

        # Create/update events
        typer.echo(f"Processing {len(events)} event(s): {creates} create, {updates} update...")
        result = service.create_events(events)

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except TrackedEntityNotFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except NoEnrollmentFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

    if result.status == "OK":
        typer.echo(f"Success! Processed {len(events)} event(s): {creates} created, {updates} updated")
    else:
        typer.echo(f"Response status: {result.status}", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
