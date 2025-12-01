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

    orgUnit: str
    occurredAt: str
    status: EventStatus = EventStatus.ACTIVE
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
