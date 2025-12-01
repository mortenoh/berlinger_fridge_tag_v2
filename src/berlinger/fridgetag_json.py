#!/usr/bin/env python3
"""FridgeTag JSON Export - Parse and output clean JSON.

Parses Berlinger Fridge-tag export files and outputs structured JSON.

Usage:
    uv run -m berlinger.fridgetag_json FILE                    # Parse file, output to stdout
    uv run -m berlinger.fridgetag_json FILE -o output.json     # Write to file
    uv run -m berlinger.fridgetag_json FILE --compact          # Compact JSON
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from berlinger.fridgetag_parser import FridgeTagData, FridgeTagParser


def clean_num(value: float | int | None) -> float | int | None:
    """Convert float to int if it has no fractional part."""
    if value is None:
        return None
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def clean_version(value: str | None) -> str | None:
    """Clean version string (remove trailing .0)."""
    if value is None:
        return None
    if value.endswith(".0"):
        return value[:-2]
    return value


def to_json(data: FridgeTagData) -> dict:
    """Convert FridgeTagData to a clean JSON-serializable structure."""
    return {
        "device": {
            "name": data.device,
            "version": data.version,
            "firmwareVersion": data.fw_version,
            "sensorCount": data.sensor,
        },
        "config": {
            "serial": data.config.serial,
            "pcb": data.config.pcb,
            "cid": data.config.cid,
            "lot": data.config.lot,
            "zone": clean_num(data.config.zone),
            "alarmThresholds": [
                {
                    "level": t.level,
                    "type": "cold" if t.level == 0 else "hot",
                    "temperatureLimit": clean_num(t.temp_limit),
                    "durationMinutes": t.time_limit_minutes,
                }
                for t in sorted(data.config.alarm_thresholds, key=lambda x: x.level)
            ],
        },
        "history": {
            "activationTimestamp": data.history.activation_timestamp,
            "reportCreationTimestamp": data.history.report_creation_timestamp,
            "recordCount": len(data.history.records),
            "records": [
                {
                    "day": r.day_index,
                    "date": r.date,
                    "temperature": {
                        "min": clean_num(r.min_temp),
                        "minTime": r.min_temp_time,
                        "max": clean_num(r.max_temp),
                        "maxTime": r.max_temp_time,
                        "avg": clean_num(r.avg_temp),
                    },
                    "alarms": [
                        {
                            "level": a.level,
                            "type": "cold" if a.level == 0 else "hot",
                            "accumulatedMinutes": a.accumulated_minutes,
                            "triggerTime": a.timestamp if a.timestamp != "00:00" else None,
                            "eventCount": a.count,
                        }
                        for a in sorted(r.alarms, key=lambda x: x.level)
                    ],
                    "sensorTimeoutMinutes": r.sensor_timeout_minutes,
                    "events": r.events,
                    "verified": {
                        "am": r.checked.am if r.checked else None,
                        "pm": r.checked.pm if r.checked else None,
                    }
                    if r.checked
                    else None,
                }
                for r in data.history.records
            ],
        },
        "certificate": {
            "version": clean_version(data.certificate.version),
            "lot": data.certificate.lot,
            "issuer": data.certificate.issuer,
            "validFrom": data.certificate.valid_from,
            "owner": data.certificate.owner,
            "publicKey": data.certificate.public_key[:32] + "..." if data.certificate.public_key else None,
        }
        if data.certificate.issuer
        else None,
        "signatures": {
            "certificate": data.signature_cert[:32] + "..." if data.signature_cert else None,
            "data": data.signature[:32] + "..." if data.signature else None,
        }
        if data.signature_cert or data.signature
        else None,
    }


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        description="Parse Berlinger Fridge-tag export files and output JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    arg_parser.add_argument("file", type=Path, help="FridgeTag export file to parse")
    arg_parser.add_argument("-o", "--output", type=Path, help="Output file (default: stdout)")
    arg_parser.add_argument("--compact", action="store_true", help="Compact JSON output")

    args = arg_parser.parse_args()

    if not args.file.exists():
        print(json.dumps({"error": f"File not found: {args.file}"}), file=sys.stderr)
        sys.exit(1)

    # Parse
    parser = FridgeTagParser()
    data = parser.parse_file(args.file)
    output = to_json(data)

    # Format
    indent = None if args.compact else 2
    json_output = json.dumps(output, indent=indent, ensure_ascii=False)

    # Output
    if args.output:
        args.output.write_text(json_output)
    else:
        print(json_output)


if __name__ == "__main__":
    main()
