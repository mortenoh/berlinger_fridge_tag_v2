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

        # Build events for all history records
        events = service.build_events(tracked_entity, data)

        if dry_run:
            typer.echo(f"\n[DRY RUN] Would create {len(events)} event(s):")
            for i, event in enumerate(events, 1):
                typer.echo(f"\n--- Event {i} (date: {event.occurredAt}) ---")
                typer.echo(event.model_dump_json(indent=2))
            return

        # Create events
        typer.echo(f"Creating {len(events)} event(s)...")
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
        typer.echo(f"Success! Created {result.created} event(s)")
    else:
        typer.echo(f"Response status: {result.status}", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
