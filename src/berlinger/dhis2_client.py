"""DHIS2 Tracker API client."""

import os
from typing import Any

import httpx

from .dhis2_models import Enrollment, Event, EventsResult, EventSummary, TrackedEntityResult, TrackerPayload


class TrackedEntityNotFoundError(Exception):
    """Raised when no tracked entity is found for the given serial."""

    pass


class DHIS2Client:
    """Client for interacting with DHIS2 Tracker API."""

    # DHIS2 UIDs
    PROGRAM_UID = "EThvOOPdWdU"
    PROGRAM_STAGE_UID = "QfEdltht9gW"
    SERIAL_ATTRIBUTE_UID = "XHdkwj2Gzi8"

    def __init__(
        self,
        base_url: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ):
        self.base_url = (base_url or os.environ.get("DHIS2_URL", "")).rstrip("/")
        self.username = username or os.environ.get("DHIS2_USERNAME")
        self.password = password or os.environ.get("DHIS2_PASSWORD")
        if not self.base_url:
            raise ValueError("DHIS2_URL must be set in environment or .env file")
        if not self.username or not self.password:
            raise ValueError("DHIS2_USERNAME and DHIS2_PASSWORD must be set in environment or .env file")
        self.auth = httpx.BasicAuth(self.username, self.password)

    def search_tracked_entity(self, serial: int | str) -> TrackedEntityResult:
        """Search for a tracked entity by logger serial number.

        Args:
            serial: The logger serial number to search for.

        Returns:
            TrackedEntityResult with trackedEntity, orgUnit, and enrollments.

        Raises:
            TrackedEntityNotFoundError: If no tracked entity is found.
        """
        url = f"{self.base_url}/api/42/tracker/trackedEntities"
        params = {
            "filter": f"{self.SERIAL_ATTRIBUTE_UID}:like:{serial}",
            "fields": "trackedEntity,orgUnit,enrollments[enrollment,orgUnit]",
            "program": self.PROGRAM_UID,
            "orgUnitMode": "ACCESSIBLE",
        }

        with httpx.Client(auth=self.auth) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        tracked_entities = data.get("trackedEntities", [])
        if not tracked_entities:
            raise TrackedEntityNotFoundError(f"No tracked entity found for serial: {serial}")

        tracked_entity = tracked_entities[0]
        enrollments = [
            Enrollment(enrollment=e["enrollment"], orgUnit=e["orgUnit"]) for e in tracked_entity.get("enrollments", [])
        ]

        return TrackedEntityResult(
            trackedEntity=tracked_entity["trackedEntity"],
            orgUnit=tracked_entity["orgUnit"],
            enrollments=enrollments,
        )

    def get_events(self, serial: int | str) -> EventsResult:
        """Get events for a tracked entity by serial number.

        Args:
            serial: The logger serial number.

        Returns:
            EventsResult with tracked entity UID and events filtered by program stage.
        """
        url = f"{self.base_url}/api/42/tracker/trackedEntities"
        params = {
            "filter": f"{self.SERIAL_ATTRIBUTE_UID}:like:{serial}",
            "fields": "trackedEntity,enrollments[enrollment,events[event,occurredAt,status,programStage]]",
            "program": self.PROGRAM_UID,
            "orgUnitMode": "ACCESSIBLE",
        }

        with httpx.Client(auth=self.auth) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        tracked_entities = data.get("trackedEntities", [])
        if not tracked_entities:
            return EventsResult(trackedEntity=None, events=[])

        tracked_entity_uid = tracked_entities[0].get("trackedEntity")
        events: list[EventSummary] = []
        for enrollment in tracked_entities[0].get("enrollments", []):
            for e in enrollment.get("events", []):
                if e.get("programStage") == self.PROGRAM_STAGE_UID:
                    events.append(
                        EventSummary(
                            event=e["event"],
                            occurredAt=e["occurredAt"],
                            status=e["status"],
                        )
                    )

        # Sort by date descending
        events.sort(key=lambda x: x.occurredAt, reverse=True)
        return EventsResult(trackedEntity=tracked_entity_uid, events=events)

    def create_event(self, event: Event) -> dict[str, Any]:
        """Create a new event in the tracker.

        Args:
            event: The event to create.

        Returns:
            The response from the DHIS2 API.
        """
        url = f"{self.base_url}/api/42/tracker"
        params = {"async": "false"}
        payload = TrackerPayload(events=[event])

        with httpx.Client(auth=self.auth) as client:
            response = client.post(
                url,
                params=params,
                json=payload.model_dump(),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            result: dict[str, Any] = response.json()
            return result
