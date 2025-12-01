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
