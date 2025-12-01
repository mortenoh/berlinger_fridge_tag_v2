

# DHIS2 APIs needed for Berlinger Fridge-Tag integration

## UID Reference Table

| UID | Type | Name | Description |
|-----|------|------|-------------|
| XHdkwj2Gzi8 | Attribute | Logger serial number | Manufacturer serial number |
| EThvOOPdWdU | Program | Equipment Monitoring System - Data logger | |
| FV43JisquSm | OrgUnit | 0001 CH Mahosot | Central Hospital |
| QfEdltht9gW | ProgramStage | Performance management recording | |
| ZkLhYyo0muJ | DataElement | Total time below -0.5°C (hh:mm) | |
| iMon5EnL5tT | DataElement | Min. temp. (°C) | |
| lMGgg93GNCj | DataElement | Status | |
| ITjXBXe4LHp | DataElement | Average storage temperature (°C) | |
| DEMIzoie6FB | DataElement | Total low alarm time (hh:mm) | |
| pXXv6fqYhhx | DataElement | Max. temp. (°C) | |
| uKw4f9GjumZ | DataElement | Total time above 8.0°C (hh:mm) | |
| twdH0WRfqwl | DataElement | Total high alarm time (hh:mm) | |
| ELbtzJtt9xI | DataElement | Average ambient temp (°C) | |
| XZHVruaj3BD | DataElement | Faults | |
| YBjvNW66Q78 | DataElement | Alarm condition | |

## API Endpoints

https://lmis.integration.dhis2.org/sandbox/api/42/tracker/trackedEntities?filter=XHdkwj2Gzi8:like:160400343951&fields=attributes,enrollments,trackedEntity,orgUnit&program=EThvOOPdWdU&orgUnitMode=ACCESSIBLE

- `XHdkwj2Gzi8` (filter): Logger serial number
- `EThvOOPdWdU` (program): Equipment Monitoring System - Data logger

```json
{
    "events": [
        {
            "orgUnit": "FV43JisquSm",
            "orgUnitName": "0001 CH Mahosot",
            "orgUnitDescription": "Central Hospital",
            "occurredAt": "2025-12-01",
            "notes": [],
            "status": "ACTIVE",
            "event": "M7zy90acyz6",
            "program": "EThvOOPdWdU",
            "programName": "Equipment Monitoring System - Data logger",
            "programDescription": "",
            "programStage": "QfEdltht9gW",
            "programStageName": "Performance management recording",
            "programStageDescription": "",
            "trackedEntity": "EKLYtZXpFgm",
            "enrollment": "fyJHUAp6ULj",
            "updatedAt": "2025-12-01T10:35:39",
            "dataValues": [
                {
                    "dataElement": "ZkLhYyo0muJ",
                    "dataElementName": "Total time below -0.5°C (hh:mm)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "00:00"
                },
                {
                    "dataElement": "iMon5EnL5tT",
                    "dataElementName": "Min. temp. (°C)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "0"
                },
                {
                    "dataElement": "lMGgg93GNCj",
                    "dataElementName": "Status",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "Hello"
                },
                {
                    "dataElement": "ITjXBXe4LHp",
                    "dataElementName": "Average storage temperature (°C)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "15"
                },
                {
                    "dataElement": "DEMIzoie6FB",
                    "dataElementName": "Total low alarm time (hh:mm)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "01:00"
                },
                {
                    "dataElement": "pXXv6fqYhhx",
                    "dataElementName": "Max. temp. (°C)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "30"
                },
                {
                    "dataElement": "uKw4f9GjumZ",
                    "dataElementName": "Total time above 8.0°C (hh:mm)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "01:00"
                },
                {
                    "dataElement": "twdH0WRfqwl",
                    "dataElementName": "Total high alarm time (hh:mm)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "02:00"
                },
                {
                    "dataElement": "ELbtzJtt9xI",
                    "dataElementName": "Average ambient temp (°C)",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "20"
                },
                {
                    "dataElement": "XZHVruaj3BD",
                    "dataElementName": "Faults",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "3"
                },
                {
                    "dataElement": "YBjvNW66Q78",
                    "dataElementName": "Alarm condition",
                    "dataElementDescription": "",
                    "dataElementOptionSet": false,
                    "value": "COND"
                }
            ]
        }
    ]
}
```
