# DHIS2 Tracker API Documentation

This document describes the DHIS2 Tracker API integration for Berlinger FridgeTag data logger monitoring.

## Base URL

```
https://lmis.integration.dhis2.org/sandbox
```

Authentication: HTTP Basic Auth

## UID Reference

### Program & Structure

| ID | Type | Name |
|----|------|------|
| `EThvOOPdWdU` | Program | Equipment Monitoring System - Data logger |
| `QfEdltht9gW` | Program Stage | Performance management recording |
| `R3gvyQLmyX8` | Tracked Entity Type | Equipment |

### Tracked Entity Attributes

| ID | Name | Description |
|----|------|-------------|
| `XHdkwj2Gzi8` | Logger serial number | Berlinger device serial (used for search) |
| `Dm1zMbsU05X` | Appliance manufacturer | Equipment manufacturer |
| `juBTPqs6hyQ` | Appliance model | Equipment model |
| `iFqrxSsWh6j` | Appliance PQS code | WHO PQS prequalification code |
| `qfRUZvkBj3D` | Appliance manufacturer serial number | Equipment serial number |

### Data Elements (Event Data)

| ID | Name | Format |
|----|------|--------|
| `ZkLhYyo0muJ` | Total time below -0.5°C | `hh:mm` |
| `iMon5EnL5tT` | Min. temp. (°C) | numeric |
| `lMGgg93GNCj` | Status | `OK` or `ALARM` |
| `ITjXBXe4LHp` | Average storage temperature (°C) | numeric |
| `DEMIzoie6FB` | Total low alarm time | `hh:mm` |
| `pXXv6fqYhhx` | Max. temp. (°C) | numeric |
| `uKw4f9GjumZ` | Total time above 8.0°C | `hh:mm` |
| `twdH0WRfqwl` | Total high alarm time | `hh:mm` |
| `ELbtzJtt9xI` | Average ambient temp (°C) | numeric |
| `XZHVruaj3BD` | Faults | numeric (sensor timeout minutes) |
| `YBjvNW66Q78` | Alarm condition | `OK`, `COLD`, `HEAT`, or `BOTH` |

---

## API Endpoints

### 1. Search Tracked Entity

Find a tracked entity by logger serial number.

**Request:**
```
GET /api/42/tracker/trackedEntities
```

**Query Parameters:**
| Parameter | Value |
|-----------|-------|
| `filter` | `XHdkwj2Gzi8:like:{serial}` |
| `fields` | `trackedEntity,orgUnit,enrollments[enrollment,orgUnit]` |
| `program` | `EThvOOPdWdU` |
| `orgUnitMode` | `ACCESSIBLE` |

**Example:**
```
GET /api/42/tracker/trackedEntities?filter=XHdkwj2Gzi8:like:160400343951&fields=trackedEntity,orgUnit,enrollments[enrollment,orgUnit]&program=EThvOOPdWdU&orgUnitMode=ACCESSIBLE
```

**Response:**
```json
{
  "trackedEntities": [
    {
      "trackedEntity": "EKLYtZXpFgm",
      "orgUnit": "FV43JisquSm",
      "enrollments": [
        {
          "enrollment": "fyJHUAp6ULj",
          "orgUnit": "FV43JisquSm"
        }
      ]
    }
  ]
}
```

---

### 2. Get Events for Tracked Entity

Retrieve events (daily monitoring records) for a tracked entity.

**Request:**
```
GET /api/42/tracker/trackedEntities
```

**Query Parameters:**
| Parameter | Value |
|-----------|-------|
| `filter` | `XHdkwj2Gzi8:like:{serial}` |
| `fields` | `trackedEntity,enrollments[enrollment,events[event,occurredAt,status,programStage]]` |
| `program` | `EThvOOPdWdU` |
| `orgUnitMode` | `ACCESSIBLE` |

**Response:**
```json
{
  "trackedEntities": [
    {
      "trackedEntity": "EKLYtZXpFgm",
      "enrollments": [
        {
          "enrollment": "fyJHUAp6ULj",
          "events": [
            {
              "event": "M7zy90acyz6",
              "occurredAt": "2025-12-01",
              "status": "ACTIVE",
              "programStage": "QfEdltht9gW"
            }
          ]
        }
      ]
    }
  ]
}
```

---

### 3. Create/Update Events

Create or update monitoring events (daily records from FridgeTag).

**Request:**
```
POST /api/42/tracker?async=false
```

**Payload (TrackerPayload):**
```json
{
  "events": [
    {
      "event": null,
      "orgUnit": "FV43JisquSm",
      "occurredAt": "2025-12-01",
      "status": "ACTIVE",
      "program": "EThvOOPdWdU",
      "programStage": "QfEdltht9gW",
      "trackedEntity": "EKLYtZXpFgm",
      "enrollment": "fyJHUAp6ULj",
      "dataValues": [
        { "dataElement": "ZkLhYyo0muJ", "value": "00:00" },
        { "dataElement": "iMon5EnL5tT", "value": "2.5" },
        { "dataElement": "lMGgg93GNCj", "value": "OK" },
        { "dataElement": "ITjXBXe4LHp", "value": "4.2" },
        { "dataElement": "DEMIzoie6FB", "value": "00:00" },
        { "dataElement": "pXXv6fqYhhx", "value": "6.8" },
        { "dataElement": "uKw4f9GjumZ", "value": "00:00" },
        { "dataElement": "twdH0WRfqwl", "value": "00:00" },
        { "dataElement": "ELbtzJtt9xI", "value": "4.2" },
        { "dataElement": "XZHVruaj3BD", "value": "0" },
        { "dataElement": "YBjvNW66Q78", "value": "OK" }
      ]
    }
  ]
}
```

**Update Existing Event:**
Include the `event` ID to update instead of create:
```json
{
  "events": [
    {
      "event": "M7zy90acyz6",
      ...
    }
  ]
}
```

**Response:**
```json
{
  "status": "OK",
  "stats": {
    "created": 1,
    "updated": 0,
    "deleted": 0,
    "ignored": 0,
    "total": 1
  },
  "bundleReport": {
    "typeReportMap": {
      "EVENT": {
        "objectReports": [
          { "uid": "ABC123XYZ" }
        ]
      }
    }
  }
}
```

---

### 4. Create Tracked Entity with Enrollment

Register a new FridgeTag device as a tracked entity.

**Request:**
```
POST /api/42/tracker?async=false
```

**Payload (TrackedEntitiesPayload):**
```json
{
  "trackedEntities": [
    {
      "orgUnit": "FV43JisquSm",
      "trackedEntityType": "R3gvyQLmyX8",
      "attributes": [
        { "attribute": "Dm1zMbsU05X", "value": "Berlinger" },
        { "attribute": "juBTPqs6hyQ", "value": "Fridge-tag 2" },
        { "attribute": "iFqrxSsWh6j", "value": "E003/001" },
        { "attribute": "qfRUZvkBj3D", "value": "FRIDGE-001" },
        { "attribute": "XHdkwj2Gzi8", "value": "160400343951" }
      ],
      "enrollments": [
        {
          "program": "EThvOOPdWdU",
          "status": "ACTIVE",
          "orgUnit": "FV43JisquSm",
          "occurredAt": "2025-01-01",
          "enrolledAt": "2025-01-01",
          "attributes": [
            { "attribute": "Dm1zMbsU05X", "value": "Berlinger" },
            { "attribute": "juBTPqs6hyQ", "value": "Fridge-tag 2" },
            { "attribute": "iFqrxSsWh6j", "value": "E003/001" },
            { "attribute": "qfRUZvkBj3D", "value": "FRIDGE-001" },
            { "attribute": "XHdkwj2Gzi8", "value": "160400343951" }
          ],
          "events": []
        }
      ]
    }
  ]
}
```

**Response:**
```json
{
  "status": "OK",
  "stats": {
    "created": 1,
    "updated": 0,
    "deleted": 0,
    "ignored": 0,
    "total": 1
  }
}
```

---

## CLI Commands

The `fridgetag-dhis2` CLI provides these commands:

| Command | Description |
|---------|-------------|
| `search <file>` | Search for tracked entity by serial from file |
| `get-events <file>` | Get events for tracked entity |
| `check-events <file>` | Compare file dates with existing events |
| `create-events <file>` | Create/update events from file data |
| `enroll <file> -o <orgunit>` | Enroll new tracked entity |

**Common Options:**
- `-n, --dry-run` - Show what would happen without making changes
- `-d, --debug` - Show URLs and JSON payloads

---

## Data Mapping

FridgeTag history records map to DHIS2 events:

| FridgeTag Field | Data Element | Transformation |
|-----------------|--------------|----------------|
| `record.date` | `occurredAt` | Direct (YYYY-MM-DD) |
| `record.min_temp` | `iMon5EnL5tT` | Direct |
| `record.max_temp` | `pXXv6fqYhhx` | Direct |
| `record.avg_temp` | `ITjXBXe4LHp`, `ELbtzJtt9xI` | Direct |
| `alarm[0].accumulated_minutes` | `ZkLhYyo0muJ`, `DEMIzoie6FB` | Minutes → `hh:mm` |
| `alarm[1].accumulated_minutes` | `uKw4f9GjumZ`, `twdH0WRfqwl` | Minutes → `hh:mm` |
| `sensor_timeout_minutes` | `XZHVruaj3BD` | Direct |
| (computed) | `lMGgg93GNCj` | `OK` if no alarms, else `ALARM` |
| (computed) | `YBjvNW66Q78` | `OK`, `COLD`, `HEAT`, or `BOTH` |
