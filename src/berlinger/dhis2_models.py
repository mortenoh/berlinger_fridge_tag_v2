"""Pydantic models for DHIS2 Tracker API."""

from enum import StrEnum

from pydantic import BaseModel


class EventStatus(StrEnum):
    """Status of a DHIS2 event."""

    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"


class DataValue(BaseModel):
    """A single data value in an event."""

    dataElement: str
    value: str


class Event(BaseModel):
    """A DHIS2 tracker event."""

    event: str | None = None  # Event UID (set when updating existing event)
    orgUnit: str
    occurredAt: str
    status: EventStatus = EventStatus.COMPLETED
    program: str
    programStage: str
    trackedEntity: str
    enrollment: str
    dataValues: list[DataValue]


class TrackerPayload(BaseModel):
    """Payload for posting events to the tracker API."""

    events: list[Event]


class Enrollment(BaseModel):
    """Enrollment information from search results."""

    enrollment: str
    orgUnit: str


class TrackedEntityResult(BaseModel):
    """Result from trackedEntity search."""

    trackedEntity: str
    orgUnit: str
    enrollments: list[Enrollment]


class EventSummary(BaseModel):
    """Summary of an event for listing."""

    event: str
    occurredAt: str
    status: str


class EventsResult(BaseModel):
    """Result from get_events with tracked entity info."""

    trackedEntity: str | None
    events: list[EventSummary]


class TrackedEntityAttribute(BaseModel):
    """Attribute for tracked entity."""

    attribute: str
    value: str


class EnrollmentPayload(BaseModel):
    """Enrollment to create."""

    program: str
    status: str = "ACTIVE"
    orgUnit: str
    occurredAt: str
    enrolledAt: str
    attributes: list[TrackedEntityAttribute]
    events: list[Event] = []


class TrackedEntityPayload(BaseModel):
    """Tracked entity to create with enrollment."""

    orgUnit: str
    trackedEntityType: str
    attributes: list[TrackedEntityAttribute]
    enrollments: list[EnrollmentPayload]


class TrackedEntitiesPayload(BaseModel):
    """Payload for creating tracked entities."""

    trackedEntities: list[TrackedEntityPayload]
