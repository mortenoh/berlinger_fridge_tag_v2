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
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug info (URLs, JSON)"),
) -> None:
    """Search for a tracked entity by parsing the serial from a FridgeTag file."""
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    console = Console()
    service = DHIS2Service()

    try:
        result = service.search_by_file(file)
    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except TrackedEntityNotFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

    console.print(f"Searching for serial: [cyan]{result.serial}[/cyan]")

    if debug:
        from .dhis2_client import DHIS2Client

        url = f"{service.client.base_url}/api/42/tracker/trackedEntities"
        params = {
            "filter": f"{DHIS2Client.SERIAL_ATTRIBUTE_UID}:like:{result.serial}",
            "fields": "trackedEntity,orgUnit,enrollments[enrollment,orgUnit]",
            "program": DHIS2Client.PROGRAM_UID,
            "orgUnitMode": "ACCESSIBLE",
        }
        params_str = "&".join(f"{k}={v}" for k, v in params.items())
        console.print(f"[dim]GET {url}?{params_str}[/dim]")
        syntax = Syntax(result.tracked_entity.model_dump_json(indent=2), "json", theme="monokai")
        console.print(syntax)

    table = Table(title="Tracked Entity")
    table.add_column("Field", style="bold")
    table.add_column("Value", style="cyan")

    table.add_row("Serial", str(result.serial))
    table.add_row("TrackedEntity", result.tracked_entity.trackedEntity)
    table.add_row("OrgUnit", result.tracked_entity.orgUnit)

    if result.tracked_entity.enrollments:
        enrollment = result.tracked_entity.enrollments[0]
        table.add_row("Enrollment", enrollment.enrollment)
        table.add_row("Enrollment Org", enrollment.orgUnit)

    console.print(table)


@app.command()
def get_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug info (URLs, JSON)"),
) -> None:
    """Get existing events for a tracked entity from a FridgeTag file."""
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    console = Console()
    service = DHIS2Service()

    try:
        data = service.parse_file(file)
        serial = service.get_serial(data)

        # Get dates from the input file
        file_dates = {record.date for record in data.history.records}

        result = service.client.get_events(serial)

        if result.trackedEntity:
            console.print(f"Serial: {serial}, TrackedEntity: {result.trackedEntity}")
        else:
            console.print(f"Serial: {serial}, TrackedEntity: not found")
            return

        if debug:
            from .dhis2_client import DHIS2Client

            url = f"{service.client.base_url}/api/42/tracker/trackedEntities"
            params = {
                "filter": f"{DHIS2Client.SERIAL_ATTRIBUTE_UID}:like:{serial}",
                "fields": "trackedEntity,enrollments[enrollment,events[event,occurredAt,status,programStage]]",
                "program": DHIS2Client.PROGRAM_UID,
                "orgUnitMode": "ACCESSIBLE",
            }
            params_str = "&".join(f"{k}={v}" for k, v in params.items())
            console.print(f"[dim]GET {url}?{params_str}[/dim]")
            syntax = Syntax(result.model_dump_json(indent=2), "json", theme="monokai")
            console.print(syntax)

        console.print(f"File records: {len(file_dates)} date(s)")

        # Track which file dates have been matched
        matched_file_dates: set[str] = set()

        # Build table
        table = Table(title=f"Events ({len(result.events)})")
        table.add_column("ID", style="cyan")
        table.add_column("Date")
        table.add_column("Status")
        table.add_column("Match", style="green")

        for event in result.events:
            date = event.occurredAt[:10] if len(event.occurredAt) >= 10 else event.occurredAt
            if date in file_dates:
                match = "yes"
                matched_file_dates.add(date)
            else:
                match = "-"
            table.add_row(event.event, date, event.status, match)

        console.print(table)

        # Show unmatched file dates
        unmatched_file_dates = file_dates - matched_file_dates
        if unmatched_file_dates:
            dates_str = ", ".join(sorted(unmatched_file_dates))
            console.print(f"[yellow]Unmatched file dates ({len(unmatched_file_dates)}): {dates_str}[/yellow]")

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def enroll(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    org_unit: str = typer.Option(..., "--org-unit", "-o", help="Organisation unit ID"),
    manufacturer: str = typer.Option("", "--manufacturer", "-m", help="Appliance manufacturer"),
    model: str = typer.Option("", "--model", help="Appliance model"),
    pqs_code: str = typer.Option("", "--pqs-code", help="Appliance PQS code"),
    appliance_serial: str = typer.Option("", "--appliance-serial", help="Appliance manufacturer serial number"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be done without making changes"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug info (URLs, JSON)"),
) -> None:
    """Create tracked entity with enrollment from a FridgeTag file."""
    from datetime import date

    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    console = Console()
    service = DHIS2Service()

    try:
        from .dhis2_client import DHIS2Client
        from .dhis2_models import (
            EnrollmentPayload,
            TrackedEntitiesPayload,
            TrackedEntityAttribute,
            TrackedEntityPayload,
        )

        data = service.parse_file(file)
        serial = service.get_serial(data)
        console.print(f"Serial: [cyan]{serial}[/cyan]")

        # Check if already exists
        already_exists = False
        try:
            tracked_entity = service.search_by_serial(serial)
            already_exists = True
            console.print(
                f"TrackedEntity: [cyan]{tracked_entity.trackedEntity}[/cyan] [yellow](already exists)[/yellow]"
            )
            console.print(f"OrgUnit: [cyan]{tracked_entity.orgUnit}[/cyan]")

            if tracked_entity.enrollments:
                table = Table(title=f"Enrollments ({len(tracked_entity.enrollments)})")
                table.add_column("Enrollment", style="cyan")
                table.add_column("OrgUnit")
                for enrollment in tracked_entity.enrollments:
                    table.add_row(enrollment.enrollment, enrollment.orgUnit)
                console.print(table)
            else:
                console.print("Enrollments: [dim]none[/dim]")

        except TrackedEntityNotFoundError:
            console.print("TrackedEntity: [green]not found, will create[/green]")

        enrolled_at = date.today().isoformat()

        # Build payload for display or actual creation
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

        if debug:
            url = f"{service.client.base_url}/api/42/tracker?async=false"
            console.print(f"\n[dim]POST {url}[/dim]")
            syntax = Syntax(payload.model_dump_json(indent=2), "json", theme="monokai")
            console.print(syntax)

        if dry_run or already_exists:
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
            console.print("[green]Success![/green] Created tracked entity with enrollment.")
        else:
            console.print(f"[red]Error: Response status: {status}[/red]", style="bold")
            raise typer.Exit(1)

    except NoSerialFoundError as e:
        console.print(f"[red]Error: {e}[/red]", style="bold")
        raise typer.Exit(1)


@app.command()
def check_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug info (URLs, JSON)"),
) -> None:
    """Check for duplicate events (same date) that may cause data issues."""
    from collections import defaultdict

    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    console = Console()
    service = DHIS2Service()

    try:
        data = service.parse_file(file)
        serial = service.get_serial(data)

        result = service.client.get_events(serial)

        if result.trackedEntity:
            console.print(f"Serial: {serial}, TrackedEntity: {result.trackedEntity}")
        else:
            console.print(f"Serial: {serial}, TrackedEntity: not found")
            return

        if debug:
            from .dhis2_client import DHIS2Client

            url = f"{service.client.base_url}/api/42/tracker/trackedEntities"
            params = {
                "filter": f"{DHIS2Client.SERIAL_ATTRIBUTE_UID}:like:{serial}",
                "fields": "trackedEntity,enrollments[enrollment,events[event,occurredAt,status,programStage]]",
                "program": DHIS2Client.PROGRAM_UID,
                "orgUnitMode": "ACCESSIBLE",
            }
            params_str = "&".join(f"{k}={v}" for k, v in params.items())
            console.print(f"[dim]GET {url}?{params_str}[/dim]")
            syntax = Syntax(result.model_dump_json(indent=2), "json", theme="monokai")
            console.print(syntax)

        console.print(f"Found {len(result.events)} existing event(s)")

        # Group events by date
        events_by_date: dict[str, list[str]] = defaultdict(list)
        for ev in result.events:
            date = ev.occurredAt[:10] if len(ev.occurredAt) >= 10 else ev.occurredAt
            events_by_date[date].append(ev.event)

        # Find duplicates
        duplicates = {date: uids for date, uids in events_by_date.items() if len(uids) > 1}

        if duplicates:
            table = Table(title="Duplicate Events")
            table.add_column("Date", style="yellow")
            table.add_column("Count", justify="right")
            table.add_column("Event IDs", style="cyan")

            for date in sorted(duplicates.keys()):
                uids = duplicates[date]
                table.add_row(date, str(len(uids)), ", ".join(uids))

            console.print(table)
            console.print(f"[yellow]Warning: {len(duplicates)} date(s) have duplicate events[/yellow]")
        else:
            console.print("[green]No duplicate dates found.[/green]")

    except NoSerialFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def create_events(
    file: Path = typer.Argument(..., help="Input FridgeTag file"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be created without sending"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Show debug info (URLs, JSON)"),
) -> None:
    """Create DHIS2 events from a FridgeTag file (one per history record)."""
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    from .dhis2_models import TrackerPayload

    console = Console()
    service = DHIS2Service()

    try:
        # Parse file and get serial
        data = service.parse_file(file)
        serial = service.get_serial(data)
        console.print(f"Serial: [cyan]{serial}[/cyan], Records: {len(data.history.records)}")

        # Get dates from input file
        input_dates = {record.date for record in data.history.records}

        # Search for tracked entity
        tracked_entity = service.search_by_serial(serial)
        console.print(f"TrackedEntity: [cyan]{tracked_entity.trackedEntity}[/cyan]")

        # Fetch existing events and create date -> event ID mapping
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

        console.print(f"Existing events: {len(existing_result.events)}")

        # Warn about duplicates - distinguish between those in input file vs not
        if duplicate_dates:
            affected = duplicate_dates & input_dates
            unaffected = duplicate_dates - input_dates
            if affected:
                dup_list = ", ".join(sorted(affected))
                console.print(
                    f"[yellow]Warning: {len(affected)} duplicate date(s) in input, will create new: {dup_list}[/yellow]"
                )
            if unaffected:
                dup_list = ", ".join(sorted(unaffected))
                console.print(f"[dim]Note: {len(unaffected)} duplicate date(s) not in input: {dup_list}[/dim]")

        # Build events for all history records
        events = service.build_events(tracked_entity, data, existing_events=existing_events)

        # Count updates vs creates
        updates = sum(1 for e in events if e.event is not None)
        creates = len(events) - updates

        # Show summary table
        table = Table(title="Summary")
        table.add_column("#", justify="right", style="dim")
        table.add_column("Action", style="bold")
        table.add_column("Date")
        table.add_column("Event ID", style="cyan")

        for i, event in enumerate(events, 1):
            action = "[yellow]UPDATE[/yellow]" if event.event else "[green]CREATE[/green]"
            table.add_row(str(i), action, event.occurredAt, event.event or "-")

        console.print(table)
        console.print(f"Total: [green]{creates} create[/green], [yellow]{updates} update[/yellow]")

        # Show JSON payload only if debug
        if debug:
            payload = TrackerPayload(events=events)
            url = f"{service.client.base_url}/api/42/tracker?async=false"
            console.print(f"\n[dim]POST {url}[/dim]")
            syntax = Syntax(payload.model_dump_json(indent=2, exclude_none=True), "json", theme="monokai")
            console.print(syntax)

        if dry_run:
            return

        # Create/update events
        console.print(f"Processing {len(events)} event(s): {creates} create, {updates} update...")
        result = service.create_events(events)

    except NoSerialFoundError as e:
        console.print(f"[red]Error: {e}[/red]", style="bold")
        raise typer.Exit(1)
    except TrackedEntityNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]", style="bold")
        raise typer.Exit(1)
    except NoEnrollmentFoundError as e:
        console.print(f"[red]Error: {e}[/red]", style="bold")
        raise typer.Exit(1)

    if result.status == "OK":
        console.print(f"[green]Success![/green] Processed {len(events)} event(s): {creates} created, {updates} updated")
    else:
        console.print(f"[red]Error: Response status: {result.status}[/red]", style="bold")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
