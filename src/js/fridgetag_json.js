#!/usr/bin/env node
/**
 * FridgeTag JSON Export - Parse and output clean JSON.
 *
 * Usage:
 *   node src/js/fridgetag_json.js FILE                    # Parse file, output to stdout
 *   node src/js/fridgetag_json.js FILE -o output.json     # Write to file
 *   node src/js/fridgetag_json.js FILE --compact          # Compact JSON
 */

import fs from "fs";
import { FridgeTagParser } from "./fridgetag_parser.js";

/**
 * Convert parsed data to clean JSON structure.
 */
function toJson(data) {
  return {
    device: {
      name: data.device,
      version: data.version,
      firmwareVersion: data.fwVersion,
      sensorCount: data.sensor,
    },
    config: {
      serial: data.config.serial,
      pcb: data.config.pcb,
      cid: data.config.cid,
      lot: data.config.lot,
      zone: data.config.zone,
      alarmThresholds: data.config.alarmThresholds
        .sort((a, b) => a.level - b.level)
        .map((t) => ({
          level: t.level,
          type: t.level === 0 ? "cold" : "hot",
          temperatureLimit: t.tempLimit,
          durationMinutes: t.timeLimitMinutes,
        })),
    },
    history: {
      activationTimestamp: data.history.activationTimestamp,
      reportCreationTimestamp: data.history.reportCreationTimestamp,
      recordCount: data.history.records.length,
      records: data.history.records.map((r) => ({
        day: r.dayIndex,
        date: r.date,
        temperature: {
          min: r.minTemp,
          minTime: r.minTempTime,
          max: r.maxTemp,
          maxTime: r.maxTempTime,
          avg: r.avgTemp,
        },
        alarms: r.alarms.sort((a, b) => a.level - b.level).map((a) => ({
          level: a.level,
          type: a.level === 0 ? "cold" : "hot",
          accumulatedMinutes: a.accumulatedMinutes,
          triggerTime: a.timestamp !== "00:00" ? a.timestamp : null,
          eventCount: a.count,
        })),
        sensorTimeoutMinutes: r.sensorTimeoutMinutes,
        events: r.events,
        verified: r.checked
          ? {
              am: r.checked.am,
              pm: r.checked.pm,
            }
          : null,
      })),
    },
    certificate: data.certificate.issuer
      ? {
          version: data.certificate.version,
          lot: data.certificate.lot,
          issuer: data.certificate.issuer,
          validFrom: data.certificate.validFrom,
          owner: data.certificate.owner,
          publicKey: data.certificate.publicKey
            ? data.certificate.publicKey.slice(0, 32) + "..."
            : null,
        }
      : null,
    signatures:
      data.signatureCert || data.signature
        ? {
            certificate: data.signatureCert
              ? data.signatureCert.slice(0, 32) + "..."
              : null,
            data: data.signature ? data.signature.slice(0, 32) + "..." : null,
          }
        : null,
  };
}

/**
 * Parse command line arguments.
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const result = { file: null, output: null, compact: false, help: false };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === "-h" || arg === "--help") {
      result.help = true;
    } else if (arg === "-o" || arg === "--output") {
      result.output = args[++i];
    } else if (arg === "--compact") {
      result.compact = true;
    } else if (!arg.startsWith("-")) {
      result.file = arg;
    }
  }

  return result;
}

/**
 * Print usage information.
 */
function printUsage() {
  console.log(`Usage: node 0505_fridgetag_json.js [options] FILE

Parse Berlinger Fridge-tag export files and output JSON.

Arguments:
  FILE                 FridgeTag export file to parse

Options:
  -o, --output FILE    Output file (default: stdout)
  --compact            Compact JSON output (no indentation)
  -h, --help           Show this help message`);
}

/**
 * Main entry point.
 */
function main() {
  const args = parseArgs();

  if (args.help || !args.file) {
    printUsage();
    process.exit(args.help ? 0 : 1);
  }

  // Check file exists
  if (!fs.existsSync(args.file)) {
    console.error(JSON.stringify({ error: `File not found: ${args.file}` }));
    process.exit(1);
  }

  // Parse
  const parser = new FridgeTagParser();
  const data = parser.parseFile(args.file);
  const output = toJson(data);

  // Format
  const indent = args.compact ? undefined : 2;
  const jsonOutput = JSON.stringify(output, null, indent);

  // Output
  if (args.output) {
    fs.writeFileSync(args.output, jsonOutput);
  } else {
    console.log(jsonOutput);
  }
}

main();
