"""Service layer for DHIS2 integration."""

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .dhis2_client import DHIS2Client, TrackedEntityNotFoundError
from .dhis2_models import DataValue, Event, EventStatus, TrackedEntityResult
from .fridgetag_parser import FridgeTagData, FridgeTagParser, HistoryRecord


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

    def _minutes_to_hhmm(self, minutes: int) -> str:
        """Convert minutes to hh:mm format."""
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"

    def _get_alarm_minutes(self, record: HistoryRecord, level: int) -> int:
        """Get accumulated alarm minutes for a specific level."""
        for alarm in record.alarms:
            if alarm.level == level:
                return alarm.accumulated_minutes
        return 0

    def _get_alarm_condition(self, record: HistoryRecord) -> str:
        """Determine alarm condition from a history record."""
        cold_minutes = self._get_alarm_minutes(record, 0)
        heat_minutes = self._get_alarm_minutes(record, 1)

        if cold_minutes > 0 and heat_minutes > 0:
            return "BOTH"
        elif cold_minutes > 0:
            return "COLD"
        elif heat_minutes > 0:
            return "HEAT"
        return "OK"

    def _get_status(self, record: HistoryRecord) -> str:
        """Determine status from a history record."""
        condition = self._get_alarm_condition(record)
        return "ALARM" if condition != "OK" else "OK"

    def build_event_from_record(
        self,
        tracked_entity: TrackedEntityResult,
        record: HistoryRecord,
        status: EventStatus = EventStatus.ACTIVE,
    ) -> Event:
        """Build an event from a single history record.

        Args:
            tracked_entity: The tracked entity to create an event for.
            record: A single day's history record.
            status: Event status (defaults to ACTIVE).

        Returns:
            Event ready to be posted.

        Raises:
            NoEnrollmentFoundError: If no enrollment is found.
        """
        if not tracked_entity.enrollments:
            raise NoEnrollmentFoundError("No enrollments found for tracked entity")

        enrollment = tracked_entity.enrollments[0]

        cold_minutes = self._get_alarm_minutes(record, 0)
        heat_minutes = self._get_alarm_minutes(record, 1)

        return Event(
            orgUnit=tracked_entity.orgUnit,
            occurredAt=record.date,
            status=status,
            program=DHIS2Client.PROGRAM_UID,
            programStage=DHIS2Client.PROGRAM_STAGE_UID,
            trackedEntity=tracked_entity.trackedEntity,
            enrollment=enrollment.enrollment,
            dataValues=[
                DataValue(
                    dataElement="ZkLhYyo0muJ",  # Total time below -0.5°C (hh:mm)
                    value=self._minutes_to_hhmm(cold_minutes),
                ),
                DataValue(
                    dataElement="iMon5EnL5tT",  # Min. temp. (°C)
                    value=str(record.min_temp) if record.min_temp is not None else "0",
                ),
                DataValue(
                    dataElement="lMGgg93GNCj",  # Status
                    value=self._get_status(record),
                ),
                DataValue(
                    dataElement="ITjXBXe4LHp",  # Average storage temperature (°C)
                    value=str(record.avg_temp) if record.avg_temp is not None else "0",
                ),
                DataValue(
                    dataElement="DEMIzoie6FB",  # Total low alarm time (hh:mm)
                    value=self._minutes_to_hhmm(cold_minutes),
                ),
                DataValue(
                    dataElement="pXXv6fqYhhx",  # Max. temp. (°C)
                    value=str(record.max_temp) if record.max_temp is not None else "0",
                ),
                DataValue(
                    dataElement="uKw4f9GjumZ",  # Total time above 8.0°C (hh:mm)
                    value=self._minutes_to_hhmm(heat_minutes),
                ),
                DataValue(
                    dataElement="twdH0WRfqwl",  # Total high alarm time (hh:mm)
                    value=self._minutes_to_hhmm(heat_minutes),
                ),
                DataValue(
                    dataElement="ELbtzJtt9xI",  # Average ambient temp (°C)
                    value=str(record.avg_temp) if record.avg_temp is not None else "0",
                ),
                DataValue(
                    dataElement="XZHVruaj3BD",  # Faults
                    value=str(record.sensor_timeout_minutes),
                ),
                DataValue(
                    dataElement="YBjvNW66Q78",  # Alarm condition
                    value=self._get_alarm_condition(record),
                ),
            ],
        )

    def build_events(
        self,
        tracked_entity: TrackedEntityResult,
        data: FridgeTagData,
        status: EventStatus = EventStatus.ACTIVE,
    ) -> list[Event]:
        """Build events for all history records.

        Args:
            tracked_entity: The tracked entity to create events for.
            data: Parsed FridgeTag data.
            status: Event status (defaults to ACTIVE).

        Returns:
            List of events ready to be posted.

        Raises:
            NoEnrollmentFoundError: If no enrollment is found.
        """
        events = []
        for record in data.history.records:
            event = self.build_event_from_record(tracked_entity, record, status)
            events.append(event)
        return events

    def create_events(self, events: list[Event]) -> CreateEventResult:
        """Create multiple events in DHIS2.

        Args:
            events: List of events to create.

        Returns:
            CreateEventResult with status and created count.
        """
        from .dhis2_models import TrackerPayload

        url = f"{self.client.base_url}/api/42/tracker"
        params = {"async": "false"}
        payload = TrackerPayload(events=events)

        import httpx

        with httpx.Client(auth=self.client.auth) as client:
            response = client.post(
                url,
                params=params,
                json=payload.model_dump(),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            data = response.json()

        status = data.get("status", "UNKNOWN")
        stats = data.get("stats", {})

        return CreateEventResult(
            status=status,
            created=stats.get("created", 0),
            event_uid=None,
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
