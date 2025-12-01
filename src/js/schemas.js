/**
 * Zod schemas for FridgeTag data structures.
 *
 * These schemas mirror the Python Pydantic models in fridgetag_parser.py.
 */

import { z } from "zod";

// =============================================================================
// DATA STRUCTURE SCHEMAS
// =============================================================================

export const alarmThresholdSchema = z.object({
  level: z.number().int(),
  tempLimit: z.number(),
  timeLimitMinutes: z.number().int(),
});

export const alarmRecordSchema = z.object({
  level: z.number().int(),
  accumulatedMinutes: z.number().int(),
  timestamp: z.string().nullable().default(null),
  count: z.number().int().default(0),
});

export const checkedTimestampsSchema = z.object({
  am: z.string().nullable().default(null),
  pm: z.string().nullable().default(null),
});

export const historyRecordSchema = z.object({
  dayIndex: z.number().int(),
  date: z.string(),
  minTemp: z.number().nullable().default(null),
  minTempTime: z.string().nullable().default(null),
  maxTemp: z.number().nullable().default(null),
  maxTempTime: z.string().nullable().default(null),
  avgTemp: z.number().nullable().default(null),
  alarms: z.array(alarmRecordSchema).default([]),
  sensorTimeoutMinutes: z.number().int().default(0),
  events: z.number().int().default(0),
  checked: checkedTimestampsSchema.nullable().default(null),
});

export const historySectionSchema = z.object({
  activationTimestamp: z.string().nullable().default(null),
  reportCreationTimestamp: z.string().nullable().default(null),
  records: z.array(historyRecordSchema).default([]),
});

export const deviceConfigSchema = z.object({
  serial: z.number().int().nullable().default(null),
  pcb: z.string().nullable().default(null),
  cid: z.number().int().nullable().default(null),
  lot: z.string().nullable().default(null),
  zone: z.number().nullable().default(null),
  alarmThresholds: z.array(alarmThresholdSchema).default([]),
});

export const certificateSchema = z.object({
  version: z.string().nullable().default(null),
  lot: z.string().nullable().default(null),
  issuer: z.string().nullable().default(null),
  validFrom: z.string().nullable().default(null),
  owner: z.string().nullable().default(null),
  publicKey: z.string().nullable().default(null),
});

export const fridgeTagDataSchema = z.object({
  device: z.string().nullable().default(null),
  version: z.string().nullable().default(null),
  fwVersion: z.string().nullable().default(null),
  sensor: z.number().int().nullable().default(null),
  config: deviceConfigSchema.default({}),
  history: historySectionSchema.default({}),
  certificate: certificateSchema.default({}),
  signatureCert: z.string().nullable().default(null),
  signature: z.string().nullable().default(null),
});

// =============================================================================
// FACTORY FUNCTIONS
// =============================================================================

/**
 * Create a new FridgeTagData object with defaults.
 */
export function createFridgeTagData() {
  return fridgeTagDataSchema.parse({});
}

/**
 * Create a new HistoryRecord with the given day index.
 */
export function createHistoryRecord(dayIndex) {
  return historyRecordSchema.parse({ dayIndex, date: "" });
}

/**
 * Create a new AlarmThreshold.
 */
export function createAlarmThreshold(level, tempLimit = 0, timeLimitMinutes = 0) {
  return alarmThresholdSchema.parse({ level, tempLimit, timeLimitMinutes });
}

/**
 * Create a new AlarmRecord.
 */
export function createAlarmRecord(level, accumulatedMinutes = 0) {
  return alarmRecordSchema.parse({ level, accumulatedMinutes });
}

/**
 * Create a new CheckedTimestamps object.
 */
export function createCheckedTimestamps() {
  return checkedTimestampsSchema.parse({});
}
