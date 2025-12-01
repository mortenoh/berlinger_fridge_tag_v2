"""CLI for Berlinger FridgeTag to DHIS2 integration."""

from pathlib import Path

import typer
from dotenv import load_dotenv

load_dotenv()

from .dhis2_client import TrackedEntityNotFoundError
from .dhis2_service import DHIS2Service, NoEnrollmentFoundError, NoSerialFoundError

app = typer.Typer(help="Berlinger FridgeTag to DHIS2 CLI")


@app.command()
def search(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
):
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
def create_event(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
):
    """Create a DHIS2 event from a FridgeTag file."""
    service = DHIS2Service()

    try:
        # Parse file and get serial
        data = service.parse_file(file)
        serial = service.get_serial(data)
        typer.echo(f"Processing serial: {serial}")

        # Search for tracked entity
        tracked_entity = service.search_by_serial(serial)
        typer.echo(f"Found tracked entity: {tracked_entity.trackedEntity}")

        # Build and create event with parsed data
        event = service.build_event(tracked_entity, data)
        typer.echo("Creating event...")
        result = service.create_event(event)

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
        if result.event_uid:
            typer.echo(f"Event UID: {result.event_uid}")
    else:
        typer.echo(f"Response status: {result.status}", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
