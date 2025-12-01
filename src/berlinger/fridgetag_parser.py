"""FridgeTag Parser Module.

This module provides parsing infrastructure for Berlinger Fridge-tag 2
export files using the BerlingerFridgeTag.g4 line-based grammar.

Components:
  - Data structures (FridgeTagData, HistorySection, etc.)
  - LineVisitor for ANTLR parse tree traversal
  - FridgeTagParser for building typed data from files
  - Utility functions (parse_line, get_indent, to_dict)
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from antlr4 import CommonTokenStream, InputStream
from pydantic import BaseModel, Field

# Add generated grammar to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "generated" / "BerlingerFridgeTag" / "grammars"))

from BerlingerFridgeTagLexer import BerlingerFridgeTagLexer
from BerlingerFridgeTagParser import BerlingerFridgeTagParser
from BerlingerFridgeTagVisitor import BerlingerFridgeTagVisitor

from berlinger.keys import Key

# =============================================================================
# DATA STRUCTURES
# =============================================================================


class AlarmThreshold(BaseModel):
    """Alarm threshold configuration."""

    level: int  # 0=low temp, 1=high temp
    temp_limit: float
    time_limit_minutes: int


class AlarmRecord(BaseModel):
    """Alarm accumulator in history record."""

    level: int  # 0=low temp, 1=high temp
    accumulated_minutes: int
    timestamp: str | None = None
    count: int = 0


class CheckedTimestamps(BaseModel):
    """AM/PM verification timestamps."""

    am: str | None = None
    pm: str | None = None


class HistoryRecord(BaseModel):
    """A single day's temperature record."""

    day_index: int  # 1-based (1-60)
    date: str
    min_temp: float | None = None
    min_temp_time: str | None = None
    max_temp: float | None = None
    max_temp_time: str | None = None
    avg_temp: float | None = None
    alarms: list[AlarmRecord] = Field(default_factory=list)
    sensor_timeout_minutes: int = 0
    events: int = 0
    checked: CheckedTimestamps | None = None


class HistorySection(BaseModel):
    """Complete history with metadata and records."""

    activation_timestamp: str | None = None
    report_creation_timestamp: str | None = None
    records: list[HistoryRecord] = Field(default_factory=list)


class DeviceConfig(BaseModel):
    """Device configuration."""

    serial: int | None = None
    pcb: str | None = None
    cid: int | None = None
    lot: str | None = None
    zone: float | None = None
    alarm_thresholds: list[AlarmThreshold] = Field(default_factory=list)


class Certificate(BaseModel):
    """Device certificate."""

    version: str | None = None
    lot: str | None = None
    issuer: str | None = None
    valid_from: str | None = None
    owner: str | None = None
    public_key: str | None = None


class FridgeTagData(BaseModel):
    """Complete parsed FridgeTag data."""

    device: str | None = None
    version: str | None = None
    fw_version: str | None = None
    sensor: int | None = None
    config: DeviceConfig = Field(default_factory=DeviceConfig)
    history: HistorySection = Field(default_factory=HistorySection)
    certificate: Certificate = Field(default_factory=Certificate)
    signature_cert: str | None = None
    signature: str | None = None


# =============================================================================
# LINE VISITOR
# =============================================================================


class ParsedEntry(BaseModel):
    """Result of parsing a single entry."""

    model_config = {"arbitrary_types_allowed": True}

    key: str | int
    value: Any
    is_section: bool
    is_index: bool
    raw_line: str


class LineVisitor(BerlingerFridgeTagVisitor):
    """Extract typed values from parse tree."""

    def __init__(self, raw_line: str = ""):
        self.raw_line = raw_line

    def visitKeyValue(self, ctx: BerlingerFridgeTagParser.KeyValueContext) -> ParsedEntry:
        key_ctx = ctx.key()
        is_section = ctx.value() is None
        is_index = False

        if hasattr(key_ctx, "knownKey") and key_ctx.knownKey():
            key = key_ctx.knownKey().getText()
        elif hasattr(key_ctx, "INT") and key_ctx.INT():
            key = int(key_ctx.INT().getText())
            is_index = True
        elif hasattr(key_ctx, "ID") and key_ctx.ID():
            key = " ".join([id_token.getText() for id_token in key_ctx.ID()])
        else:
            key = key_ctx.getText()

        value = None
        if ctx.value():
            value_ctx = ctx.value()
            if isinstance(value_ctx, BerlingerFridgeTagParser.TextValContext):
                value = self._extract_raw_value(ctx)
            else:
                value = self.visit(value_ctx)

        return ParsedEntry(key=key, value=value, is_section=is_section, is_index=is_index, raw_line=self.raw_line)

    def _extract_raw_value(self, ctx: BerlingerFridgeTagParser.KeyValueContext) -> str:
        """Extract raw value text preserving spaces."""
        colon_pos = self.raw_line.find(":", ctx.key().stop.stop)
        if colon_pos >= 0:
            rest = self.raw_line[colon_pos + 1 :]
            comma_pos = rest.find(",")
            if comma_pos >= 0:
                return rest[:comma_pos].strip()
            return rest.strip()
        return ctx.value().getText()

    def visitTempVal(self, ctx: BerlingerFridgeTagParser.TempValContext) -> float | None:
        return self.visit(ctx.temperature())

    def visitTempNumber(self, ctx: BerlingerFridgeTagParser.TempNumberContext) -> float:
        return float(ctx.getText())

    def visitTempSigned(self, ctx: BerlingerFridgeTagParser.TempSignedContext) -> float:
        return float(ctx.getText())

    def visitTempMissing(self, ctx: BerlingerFridgeTagParser.TempMissingContext) -> None:
        return None

    def visitDateTimeVal(self, ctx: BerlingerFridgeTagParser.DateTimeValContext) -> str:
        return ctx.DATETIME().getText()

    def visitDateVal(self, ctx: BerlingerFridgeTagParser.DateValContext) -> str:
        return ctx.DATE().getText()

    def visitTimeVal(self, ctx: BerlingerFridgeTagParser.TimeValContext) -> str:
        return ctx.TIME().getText()

    def visitIntVal(self, ctx: BerlingerFridgeTagParser.IntValContext) -> int:
        return int(ctx.INT().getText())

    def visitHexVal(self, ctx: BerlingerFridgeTagParser.HexValContext) -> str:
        return ctx.HEX().getText()

    def visitTextVal(self, ctx: BerlingerFridgeTagParser.TextValContext) -> str:
        return ctx.getText()


# =============================================================================
# LINE PARSING UTILITIES
# =============================================================================


def parse_line(line: str) -> list[ParsedEntry]:
    """Parse a single line and return list of entries."""
    stripped = line.lstrip(" ")
    if not stripped.strip():
        return []

    input_stream = InputStream(stripped)
    lexer = BerlingerFridgeTagLexer(input_stream)
    lexer.removeErrorListeners()

    token_stream = CommonTokenStream(lexer)
    parser = BerlingerFridgeTagParser(token_stream)
    parser.removeErrorListeners()

    tree = parser.line()

    if parser.getNumberOfSyntaxErrors() > 0:
        return []

    visitor = LineVisitor(stripped)
    entries = []
    for entry_ctx in tree.entry():
        entry = visitor.visit(entry_ctx)
        if entry:
            entries.append(entry)

    return entries


def get_indent(line: str) -> int:
    """Count leading spaces."""
    return len(line) - len(line.lstrip(" "))


# =============================================================================
# DOCUMENT PARSER
# =============================================================================


class FridgeTagParser:
    """Build typed FridgeTagData from file."""

    def __init__(self) -> None:
        self.data = FridgeTagData()
        self.context_stack: list[tuple[int, str, Any]] = []

    def parse_file(self, file_path: str | Path) -> FridgeTagData:
        """Parse a FridgeTag file."""
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        return self.parse_lines(lines)

    def parse_lines(self, lines: list[str]) -> FridgeTagData:
        """Parse lines into typed structure."""
        self.data = FridgeTagData()
        self.context_stack = [(-1, "root", self.data)]

        current_hist_record: HistoryRecord | None = None
        current_alarm_section: str | None = None

        for line in lines:
            line = line.rstrip("\r\n")
            indent = get_indent(line)
            entries = parse_line(line)

            if not entries:
                continue

            while self.context_stack and self.context_stack[-1][0] >= indent:
                self.context_stack.pop()

            parent_indent, parent_section, parent_obj = self.context_stack[-1]

            for entry in entries:
                key = entry.key
                value = entry.value

                if entry.is_section:
                    # Section headers
                    if key == Key.CONFIG:
                        self.context_stack.append((indent, Key.CONFIG, self.data.config))
                    elif key == Key.HISTORY:
                        self.context_stack.append((indent, Key.HISTORY, self.data.history))
                    elif key == Key.CERTIFICATE:
                        self.context_stack.append((indent, Key.CERTIFICATE, self.data.certificate))
                    elif key == Key.ALARM:
                        current_alarm_section = "config" if parent_section == Key.CONFIG else "history"
                        self.context_stack.append((indent, Key.ALARM, None))
                    elif key == Key.INTERNAL_SENSOR:
                        self.context_stack.append((indent, "IntSensor", None))
                    elif key == Key.SENSOR_TIMEOUT:
                        self.context_stack.append((indent, "IntSensorTimeout", None))
                    elif key == Key.CHECKED:
                        if current_hist_record:
                            current_hist_record.checked = CheckedTimestamps()
                        self.context_stack.append((indent, Key.CHECKED, None))
                    elif entry.is_index:
                        idx = int(key)
                        if parent_section == Key.HISTORY:
                            current_hist_record = HistoryRecord(day_index=idx, date="")
                            self.data.history.records.append(current_hist_record)
                            self.context_stack.append((indent, f"Day{idx}", current_hist_record))
                        elif parent_section == Key.ALARM:
                            self.context_stack.append((indent, f"AlarmLevel{idx}", idx))
                else:
                    self._set_value(parent_section, key, value, current_hist_record, current_alarm_section)

        return self.data

    def _set_value(
        self,
        section: str,
        key: str,
        value: Any,
        hist_record: HistoryRecord | None,
        alarm_section: str | None,
    ) -> None:
        """Set a value in the appropriate structure."""
        # Top-level
        if section == "root":
            if key == Key.DEVICE:
                self.data.device = value
            elif key == Key.VERSION:
                self.data.version = str(value)
            elif key == Key.FW_VERSION:
                self.data.fw_version = value
            elif key == Key.SENSOR_COUNT:
                self.data.sensor = value
            elif key == Key.SIGNATURE_CERT:
                self.data.signature_cert = value
            elif key == Key.SIGNATURE:
                self.data.signature = value

        # Config section
        elif section == Key.CONFIG:
            if key == Key.SERIAL:
                self.data.config.serial = value
            elif key == Key.PCB:
                self.data.config.pcb = value
            elif key == Key.CID:
                self.data.config.cid = value
            elif key == Key.LOT:
                self.data.config.lot = value
            elif key == Key.ZONE:
                self.data.config.zone = value

        # Config alarm thresholds
        elif section.startswith("AlarmLevel") and alarm_section == "config":
            level = int(section.replace("AlarmLevel", ""))
            threshold = next((t for t in self.data.config.alarm_thresholds if t.level == level), None)
            if not threshold:
                threshold = AlarmThreshold(level=level, temp_limit=0.0, time_limit_minutes=0)
                self.data.config.alarm_thresholds.append(threshold)
            if key == Key.TEMP_THRESHOLD:
                threshold.temp_limit = value
            elif key == Key.DURATION_THRESHOLD:
                threshold.time_limit_minutes = value

        # History metadata
        elif section == Key.HISTORY:
            if key == Key.ACTIVATION_TIMESTAMP:
                self.data.history.activation_timestamp = value
            elif key == Key.REPORT_CREATION_TIMESTAMP:
                self.data.history.report_creation_timestamp = value

        # History day record
        elif section.startswith("Day") and hist_record:
            if key == Key.DATE:
                hist_record.date = value
            elif key == Key.MIN_TEMP:
                hist_record.min_temp = value
            elif key == Key.MIN_TEMP_TIMESTAMP:
                hist_record.min_temp_time = value
            elif key == Key.MAX_TEMP:
                hist_record.max_temp = value
            elif key == Key.MAX_TEMP_TIMESTAMP:
                hist_record.max_temp_time = value
            elif key == Key.AVG_TEMP:
                hist_record.avg_temp = value
            elif key == Key.EVENTS:
                hist_record.events = value

        # History alarm accumulators
        elif section.startswith("AlarmLevel") and alarm_section == "history" and hist_record:
            level = int(section.replace("AlarmLevel", ""))
            alarm = next((a for a in hist_record.alarms if a.level == level), None)
            if not alarm:
                alarm = AlarmRecord(level=level, accumulated_minutes=0)
                hist_record.alarms.append(alarm)
            if key == Key.ACCUMULATED_TIME:
                alarm.accumulated_minutes = value
            elif key == Key.ALARM_TIMESTAMP:
                alarm.timestamp = value
            elif key == Key.ALARM_COUNT:
                alarm.count = value

        # Sensor timeout
        elif section == "IntSensorTimeout" and hist_record:
            if key == Key.ACCUMULATED_SENSOR_TIMEOUT:
                hist_record.sensor_timeout_minutes = value

        # Checked timestamps
        elif section == Key.CHECKED and hist_record and hist_record.checked:
            if key == Key.AM_TIMESTAMP:
                hist_record.checked.am = value
            elif key == Key.PM_TIMESTAMP:
                hist_record.checked.pm = value

        # Certificate
        elif section == Key.CERTIFICATE:
            if key == Key.VERSION:
                self.data.certificate.version = str(value)
            elif key == Key.LOT:
                self.data.certificate.lot = value
            elif key == Key.ISSUER:
                self.data.certificate.issuer = value
            elif key == Key.VALID_FROM:
                self.data.certificate.valid_from = value
            elif key == Key.OWNER:
                self.data.certificate.owner = value
            elif key == Key.PUBLIC_KEY:
                self.data.certificate.public_key = value


# =============================================================================
# OUTPUT SERIALIZATION
# =============================================================================


def to_dict(data: FridgeTagData, include_records: bool = True) -> dict[str, Any]:
    """Convert FridgeTagData to JSON-serializable dict with camelCase keys."""
    result: dict[str, Any] = {
        "device": data.device,
        "version": data.version,
    }

    if data.fw_version:
        result["fwVersion"] = data.fw_version
    if data.sensor:
        result["sensor"] = data.sensor

    # Config
    result["config"] = {
        "serial": data.config.serial,
        "pcb": data.config.pcb,
        "cid": data.config.cid,
        "lot": data.config.lot,
        "zone": data.config.zone,
        "alarmThresholds": [
            {
                "level": t.level,
                "tempLimit": t.temp_limit,
                "timeLimitMinutes": t.time_limit_minutes,
            }
            for t in sorted(data.config.alarm_thresholds, key=lambda x: x.level)
        ],
    }

    # History
    history_dict: dict[str, Any] = {
        "activationTimestamp": data.history.activation_timestamp,
        "reportCreationTimestamp": data.history.report_creation_timestamp,
        "recordCount": len(data.history.records),
    }

    if include_records:
        history_dict["records"] = [
            {
                "dayIndex": r.day_index,
                "date": r.date,
                "minTemp": r.min_temp,
                "minTempTime": r.min_temp_time,
                "maxTemp": r.max_temp,
                "maxTempTime": r.max_temp_time,
                "avgTemp": r.avg_temp,
                "alarms": [
                    {
                        "level": a.level,
                        "accumulatedMinutes": a.accumulated_minutes,
                        "timestamp": a.timestamp,
                        "count": a.count,
                    }
                    for a in sorted(r.alarms, key=lambda x: x.level)
                ],
                "sensorTimeoutMinutes": r.sensor_timeout_minutes,
                "events": r.events,
                "checked": {"am": r.checked.am, "pm": r.checked.pm} if r.checked else None,
            }
            for r in data.history.records
        ]

    result["history"] = history_dict

    # Certificate
    if data.certificate.issuer:
        result["certificate"] = {
            "version": data.certificate.version,
            "lot": data.certificate.lot,
            "issuer": data.certificate.issuer,
            "validFrom": data.certificate.valid_from,
            "owner": data.certificate.owner,
        }

    return result
