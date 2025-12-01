"""DHIS2 Tracker API client."""

import os
from typing import Any

import httpx

from .dhis2_models import (
    Enrollment,
    EnrollmentPayload,
    Event,
    EventsResult,
    EventSummary,
    TrackedEntitiesPayload,
    TrackedEntityAttribute,
    TrackedEntityPayload,
    TrackedEntityResult,
    TrackerPayload,
)


class TrackedEntityNotFoundError(Exception):
    """Raised when no tracked entity is found for the given serial."""

    pass


class DHIS2Client:
    """Client for interacting with DHIS2 Tracker API."""

    # DHIS2 UIDs
    PROGRAM_UID = "EThvOOPdWdU"
    PROGRAM_STAGE_UID = "QfEdltht9gW"
    TRACKED_ENTITY_TYPE_UID = "R3gvyQLmyX8"

    # Attribute UIDs
    SERIAL_ATTRIBUTE_UID = "XHdkwj2Gzi8"  # Logger serial number
    MANUFACTURER_ATTRIBUTE_UID = "Dm1zMbsU05X"  # Appliance manufacturer
    MODEL_ATTRIBUTE_UID = "juBTPqs6hyQ"  # Appliance model
    PQS_CODE_ATTRIBUTE_UID = "iFqrxSsWh6j"  # Appliance PQS code
    APPLIANCE_SERIAL_ATTRIBUTE_UID = "qfRUZvkBj3D"  # Appliance manufacturer serial number

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

    def create_tracked_entity_with_enrollment(
        self,
        org_unit: str,
        serial: str,
        manufacturer: str,
        model: str,
        pqs_code: str,
        appliance_serial: str,
        enrolled_at: str,
    ) -> dict[str, Any]:
        """Create a new tracked entity with enrollment.

        Args:
            org_unit: Organisation unit UID.
            serial: Logger serial number.
            manufacturer: Appliance manufacturer.
            model: Appliance model.
            pqs_code: Appliance PQS code.
            appliance_serial: Appliance manufacturer serial number.
            enrolled_at: Enrollment date (YYYY-MM-DD).

        Returns:
            The response from the DHIS2 API.
        """
        attributes = [
            TrackedEntityAttribute(attribute=self.MANUFACTURER_ATTRIBUTE_UID, value=manufacturer),
            TrackedEntityAttribute(attribute=self.MODEL_ATTRIBUTE_UID, value=model),
            TrackedEntityAttribute(attribute=self.PQS_CODE_ATTRIBUTE_UID, value=pqs_code),
            TrackedEntityAttribute(attribute=self.APPLIANCE_SERIAL_ATTRIBUTE_UID, value=appliance_serial),
            TrackedEntityAttribute(attribute=self.SERIAL_ATTRIBUTE_UID, value=serial),
        ]

        enrollment = EnrollmentPayload(
            program=self.PROGRAM_UID,
            status="ACTIVE",
            orgUnit=org_unit,
            occurredAt=enrolled_at,
            enrolledAt=enrolled_at,
            attributes=attributes,
            events=[],
        )

        tracked_entity = TrackedEntityPayload(
            orgUnit=org_unit,
            trackedEntityType=self.TRACKED_ENTITY_TYPE_UID,
            attributes=attributes,
            enrollments=[enrollment],
        )

        payload = TrackedEntitiesPayload(trackedEntities=[tracked_entity])

        url = f"{self.base_url}/api/42/tracker"
        params = {"async": "false"}

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
