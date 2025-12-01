"""Service layer for DHIS2 integration."""

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .dhis2_client import DHIS2Client, TrackedEntityNotFoundError
from .dhis2_models import DataValue, Event, EventStatus, TrackedEntityResult
from .fridgetag_parser import FridgeTagData, FridgeTagParser


class NoSerialFoundError(Exception):
    """Raised when no serial number is found in the parsed file."""

    pass


class NoEnrollmentFoundError(Exception):
    """Raised when no enrollment is found for the tracked entity."""

    pass


@dataclass
class SearchResult:
    """Result of searching for a tracked entity."""

    serial: int
    tracked_entity: TrackedEntityResult


@dataclass
class CreateEventResult:
    """Result of creating an event."""

    status: str
    created: int
    event_uid: str | None = None


class DHIS2Service:
    """Service for DHIS2 operations."""

    def __init__(self, client: DHIS2Client | None = None):
        self.client = client or DHIS2Client()
        self.parser = FridgeTagParser()

    def parse_file(self, file_path: str | Path) -> FridgeTagData:
        """Parse a FridgeTag file.

        Args:
            file_path: Path to the FridgeTag file.

        Returns:
            Parsed FridgeTagData.
        """
        return self.parser.parse_file(str(file_path))

    def get_serial(self, data: FridgeTagData) -> int:
        """Extract serial number from parsed data.

        Args:
            data: Parsed FridgeTag data.

        Returns:
            Serial number.

        Raises:
            NoSerialFoundError: If no serial number is found.
        """
        if not data.config.serial:
            raise NoSerialFoundError("No serial number found in file")
        return data.config.serial

    def search_by_file(self, file_path: str | Path) -> SearchResult:
        """Search for a tracked entity by parsing a FridgeTag file.

        Args:
            file_path: Path to the FridgeTag file.

        Returns:
            SearchResult with serial and tracked entity info.

        Raises:
            NoSerialFoundError: If no serial number is found in file.
            TrackedEntityNotFoundError: If no tracked entity is found.
        """
        data = self.parse_file(file_path)
        serial = self.get_serial(data)
        result = self.client.search_tracked_entity(serial)
        return SearchResult(serial=serial, tracked_entity=result)

    def search_by_serial(self, serial: int | str) -> TrackedEntityResult:
        """Search for a tracked entity by serial number.

        Args:
            serial: Logger serial number.

        Returns:
            TrackedEntityResult with tracked entity info.

        Raises:
            TrackedEntityNotFoundError: If no tracked entity is found.
        """
        return self.client.search_tracked_entity(serial)

    def build_event(
        self,
        tracked_entity: TrackedEntityResult,
        data: FridgeTagData,
        occurred_at: date | None = None,
        status: EventStatus = EventStatus.ACTIVE,
    ) -> Event:
        """Build an event for a tracked entity using parsed FridgeTag data.

        Args:
            tracked_entity: The tracked entity to create an event for.
            data: Parsed FridgeTag data.
            occurred_at: Date the event occurred (defaults to today).
            status: Event status (defaults to ACTIVE).

        Returns:
            Event ready to be posted.

        Raises:
            NoEnrollmentFoundError: If no enrollment is found.

        Note:
            Currently uses placeholder values. Real implementation will create
            one event per history record.
        """
        if not tracked_entity.enrollments:
            raise NoEnrollmentFoundError("No enrollments found for tracked entity")

        enrollment = tracked_entity.enrollments[0]

        return Event(
            orgUnit=tracked_entity.orgUnit,
            occurredAt=(occurred_at or date.today()).isoformat(),
            status=status,
            program=DHIS2Client.PROGRAM_UID,
            programStage=DHIS2Client.PROGRAM_STAGE_UID,
            trackedEntity=tracked_entity.trackedEntity,
            enrollment=enrollment.enrollment,
            dataValues=[
                DataValue(dataElement="ZkLhYyo0muJ", value="00:00"),  # Total time below -0.5°C
                DataValue(dataElement="iMon5EnL5tT", value="0"),  # Min. temp.
                DataValue(dataElement="lMGgg93GNCj", value="OK"),  # Status
                DataValue(dataElement="ITjXBXe4LHp", value="5"),  # Average storage temp
                DataValue(dataElement="DEMIzoie6FB", value="00:00"),  # Total low alarm time
                DataValue(dataElement="pXXv6fqYhhx", value="8"),  # Max. temp.
                DataValue(dataElement="uKw4f9GjumZ", value="00:00"),  # Total time above 8.0°C
                DataValue(dataElement="twdH0WRfqwl", value="00:00"),  # Total high alarm time
                DataValue(dataElement="ELbtzJtt9xI", value="20"),  # Average ambient temp
                DataValue(dataElement="XZHVruaj3BD", value="0"),  # Faults
                DataValue(dataElement="YBjvNW66Q78", value="OK"),  # Alarm condition
            ],
        )

    def create_event(self, event: Event) -> CreateEventResult:
        """Create an event in DHIS2.

        Args:
            event: The event to create.

        Returns:
            CreateEventResult with status and created count.
        """
        response = self.client.create_event(event)
        status = response.get("status", "UNKNOWN")
        stats = response.get("stats", {})

        # Extract event UID from bundle report if available
        event_uid = None
        bundle_report = response.get("bundleReport", {})
        type_report_map = bundle_report.get("typeReportMap", {})
        event_report = type_report_map.get("EVENT", {})
        object_reports = event_report.get("objectReports", [])
        if object_reports:
            event_uid = object_reports[0].get("uid")

        return CreateEventResult(
            status=status,
            created=stats.get("created", 0),
            event_uid=event_uid,
        )

    def create_event_from_file(
        self,
        file_path: str | Path,
        occurred_at: date | None = None,
        status: EventStatus = EventStatus.ACTIVE,
    ) -> CreateEventResult:
        """Create an event from a FridgeTag file.

        Args:
            file_path: Path to the FridgeTag file.
            occurred_at: Date the event occurred (defaults to report creation date or today).
            status: Event status (defaults to ACTIVE).

        Returns:
            CreateEventResult with status and created count.

        Raises:
            NoSerialFoundError: If no serial number is found in file.
            TrackedEntityNotFoundError: If no tracked entity is found.
            NoEnrollmentFoundError: If no enrollment is found.
        """
        data = self.parse_file(file_path)
        serial = self.get_serial(data)
        tracked_entity = self.client.search_tracked_entity(serial)
        event = self.build_event(
            tracked_entity=tracked_entity,
            data=data,
            occurred_at=occurred_at,
            status=status,
        )
        return self.create_event(event)
