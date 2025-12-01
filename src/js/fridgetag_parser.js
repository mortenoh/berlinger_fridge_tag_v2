/**
 * FridgeTag Parser - JavaScript Implementation using ANTLR4
 *
 * Parses Berlinger Fridge-tag 2 export files using the BerlingerFridgeTag grammar.
 * Mirrors the Python fridgetag_parser.py for cross-language consistency.
 */

import fs from "fs";
import antlr4 from "antlr4";
import BerlingerFridgeTagLexer from "../../generated/BerlingerFridgeTag/js/grammars/BerlingerFridgeTagLexer.js";
import BerlingerFridgeTagParser from "../../generated/BerlingerFridgeTag/js/grammars/BerlingerFridgeTagParser.js";
import BerlingerFridgeTagVisitor from "../../generated/BerlingerFridgeTag/js/grammars/BerlingerFridgeTagVisitor.js";
import { Key } from "./keys.js";
import {
  createFridgeTagData,
  createHistoryRecord,
  createAlarmThreshold,
  createAlarmRecord,
  createCheckedTimestamps,
} from "./schemas.js";

// =============================================================================
// LINE VISITOR
// =============================================================================

class LineVisitor extends BerlingerFridgeTagVisitor {
  constructor(rawLine = "") {
    super();
    this.rawLine = rawLine;
  }

  visitKeyValue(ctx) {
    const keyCtx = ctx.key();
    const isSection = ctx.value() === null;
    let isIndex = false;
    let key;

    if (keyCtx.knownKey && keyCtx.knownKey()) {
      key = keyCtx.knownKey().getText();
    } else if (keyCtx.INT && keyCtx.INT()) {
      key = parseInt(keyCtx.INT().getText(), 10);
      isIndex = true;
    } else if (keyCtx.ID && keyCtx.ID()) {
      key = keyCtx.ID().map((t) => t.getText()).join(" ");
    } else {
      key = keyCtx.getText();
    }

    let value = null;
    if (ctx.value()) {
      const valueCtx = ctx.value();
      if (valueCtx.constructor.name === "TextValContext") {
        value = this._extractRawValue(ctx);
      } else {
        value = this.visit(valueCtx);
      }
    }

    return { key, value, isSection, isIndex, rawLine: this.rawLine };
  }

  _extractRawValue(ctx) {
    const colonPos = this.rawLine.indexOf(":", ctx.key().stop.stop);
    if (colonPos >= 0) {
      const rest = this.rawLine.slice(colonPos + 1);
      const commaPos = rest.indexOf(",");
      if (commaPos >= 0) {
        return rest.slice(0, commaPos).trim();
      }
      return rest.trim();
    }
    return ctx.value().getText();
  }

  visitTempVal(ctx) {
    return this.visit(ctx.temperature());
  }

  visitTempNumber(ctx) {
    return parseFloat(ctx.getText());
  }

  visitTempSigned(ctx) {
    return parseFloat(ctx.getText());
  }

  visitTempMissing(ctx) {
    return null;
  }

  visitDateTimeVal(ctx) {
    return ctx.DATETIME().getText();
  }

  visitDateVal(ctx) {
    return ctx.DATE().getText();
  }

  visitTimeVal(ctx) {
    return ctx.TIME().getText();
  }

  visitIntVal(ctx) {
    return parseInt(ctx.INT().getText(), 10);
  }

  visitHexVal(ctx) {
    return ctx.HEX().getText();
  }

  visitTextVal(ctx) {
    return ctx.getText();
  }
}

// =============================================================================
// LINE PARSING UTILITIES
// =============================================================================

function parseLine(line) {
  const stripped = line.trimStart();
  if (!stripped.trim()) return [];

  const inputStream = new antlr4.InputStream(stripped);
  const lexer = new BerlingerFridgeTagLexer(inputStream);
  lexer.removeErrorListeners();

  const tokenStream = new antlr4.CommonTokenStream(lexer);
  const parser = new BerlingerFridgeTagParser(tokenStream);
  parser.removeErrorListeners();

  const tree = parser.line();

  if (parser.syntaxErrors > 0) {
    return [];
  }

  const visitor = new LineVisitor(stripped);
  const entries = [];

  for (const entryCtx of tree.entry()) {
    const entry = visitor.visit(entryCtx);
    if (entry) {
      entries.push(entry);
    }
  }

  return entries;
}

function getIndent(line) {
  return line.length - line.trimStart().length;
}

// =============================================================================
// PARSER CLASS
// =============================================================================

export class FridgeTagParser {
  constructor() {
    this.data = null;
    this.contextStack = [];
  }

  parseFile(filePath) {
    const content = fs.readFileSync(filePath, "utf-8");
    return this.parseText(content);
  }

  parseText(text) {
    const lines = text.split(/\r?\n/);
    return this.parseLines(lines);
  }

  parseLines(lines) {
    this.data = createFridgeTagData();
    this.contextStack = [{ indent: -1, section: "root", obj: this.data }];

    let currentHistRecord = null;
    let currentAlarmSection = null;

    for (const line of lines) {
      const indent = getIndent(line);
      const entries = parseLine(line);

      if (entries.length === 0) continue;

      // Pop stack to find parent
      while (this.contextStack.length > 0 && this.contextStack[this.contextStack.length - 1].indent >= indent) {
        this.contextStack.pop();
      }

      const parent = this.contextStack[this.contextStack.length - 1];
      const parentSection = parent.section;

      for (const entry of entries) {
        const { key, value, isSection, isIndex } = entry;

        if (isSection) {
          if (key === Key.CONFIG) {
            this.contextStack.push({ indent, section: Key.CONFIG, obj: this.data.config });
          } else if (key === Key.HISTORY) {
            this.contextStack.push({ indent, section: Key.HISTORY, obj: this.data.history });
          } else if (key === Key.CERTIFICATE) {
            this.contextStack.push({ indent, section: Key.CERTIFICATE, obj: this.data.certificate });
          } else if (key === Key.ALARM) {
            currentAlarmSection = parentSection === Key.CONFIG ? "config" : "history";
            this.contextStack.push({ indent, section: Key.ALARM, obj: null });
          } else if (key === Key.INTERNAL_SENSOR) {
            this.contextStack.push({ indent, section: "IntSensor", obj: null });
          } else if (key === Key.SENSOR_TIMEOUT) {
            this.contextStack.push({ indent, section: "IntSensorTimeout", obj: null });
          } else if (key === Key.CHECKED) {
            if (currentHistRecord) {
              currentHistRecord.checked = createCheckedTimestamps();
            }
            this.contextStack.push({ indent, section: Key.CHECKED, obj: null });
          } else if (isIndex) {
            const idx = key;
            if (parentSection === Key.HISTORY) {
              currentHistRecord = createHistoryRecord(idx);
              this.data.history.records.push(currentHistRecord);
              this.contextStack.push({ indent, section: `Day${idx}`, obj: currentHistRecord });
            } else if (parentSection === Key.ALARM) {
              this.contextStack.push({ indent, section: `AlarmLevel${idx}`, obj: idx });
            }
          }
        } else {
          this._setValue(parentSection, key, value, currentHistRecord, currentAlarmSection);
        }
      }
    }

    return this.data;
  }

  _setValue(section, key, value, histRecord, alarmSection) {
    if (section === "root") {
      if (key === Key.DEVICE) this.data.device = value;
      else if (key === Key.VERSION) this.data.version = String(value);
      else if (key === Key.FW_VERSION) this.data.fwVersion = value;
      else if (key === Key.SENSOR_COUNT) this.data.sensor = value;
      else if (key === Key.SIGNATURE_CERT) this.data.signatureCert = value;
      else if (key === Key.SIGNATURE) this.data.signature = value;
    } else if (section === Key.CONFIG) {
      if (key === Key.SERIAL) this.data.config.serial = value;
      else if (key === Key.PCB) this.data.config.pcb = value;
      else if (key === Key.CID) this.data.config.cid = value;
      else if (key === Key.LOT) this.data.config.lot = value;
      else if (key === Key.ZONE) this.data.config.zone = value;
    } else if (section.startsWith("AlarmLevel") && alarmSection === "config") {
      const level = parseInt(section.replace("AlarmLevel", ""), 10);
      let threshold = this.data.config.alarmThresholds.find((t) => t.level === level);
      if (!threshold) {
        threshold = createAlarmThreshold(level);
        this.data.config.alarmThresholds.push(threshold);
      }
      if (key === Key.TEMP_THRESHOLD) threshold.tempLimit = value;
      else if (key === Key.DURATION_THRESHOLD) threshold.timeLimitMinutes = value;
    } else if (section === Key.HISTORY) {
      if (key === Key.ACTIVATION_TIMESTAMP) this.data.history.activationTimestamp = value;
      else if (key === Key.REPORT_CREATION_TIMESTAMP) this.data.history.reportCreationTimestamp = value;
    } else if (section.startsWith("Day") && histRecord) {
      if (key === Key.DATE) histRecord.date = value;
      else if (key === Key.MIN_TEMP) histRecord.minTemp = value;
      else if (key === Key.MIN_TEMP_TIMESTAMP) histRecord.minTempTime = value;
      else if (key === Key.MAX_TEMP) histRecord.maxTemp = value;
      else if (key === Key.MAX_TEMP_TIMESTAMP) histRecord.maxTempTime = value;
      else if (key === Key.AVG_TEMP) histRecord.avgTemp = value;
      else if (key === Key.EVENTS) histRecord.events = value;
    } else if (section.startsWith("AlarmLevel") && alarmSection === "history" && histRecord) {
      const level = parseInt(section.replace("AlarmLevel", ""), 10);
      let alarm = histRecord.alarms.find((a) => a.level === level);
      if (!alarm) {
        alarm = createAlarmRecord(level);
        histRecord.alarms.push(alarm);
      }
      if (key === Key.ACCUMULATED_TIME) alarm.accumulatedMinutes = value;
      else if (key === Key.ALARM_TIMESTAMP) alarm.timestamp = value;
      else if (key === Key.ALARM_COUNT) alarm.count = value;
    } else if (section === "IntSensorTimeout" && histRecord) {
      if (key === Key.ACCUMULATED_SENSOR_TIMEOUT) histRecord.sensorTimeoutMinutes = value;
    } else if (section === Key.CHECKED && histRecord && histRecord.checked) {
      if (key === Key.AM_TIMESTAMP) histRecord.checked.am = value;
      else if (key === Key.PM_TIMESTAMP) histRecord.checked.pm = value;
    } else if (section === Key.CERTIFICATE) {
      if (key === Key.VERSION) this.data.certificate.version = String(value);
      else if (key === Key.LOT) this.data.certificate.lot = value;
      else if (key === Key.ISSUER) this.data.certificate.issuer = value;
      else if (key === Key.VALID_FROM) this.data.certificate.validFrom = value;
      else if (key === Key.OWNER) this.data.certificate.owner = value;
      else if (key === Key.PUBLIC_KEY) this.data.certificate.publicKey = value;
    }
  }
}

export { Key };
