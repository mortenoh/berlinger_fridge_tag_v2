/**
 * Berlinger FridgeTag Key Constants.
 *
 * Grammar token names mapped to file format strings.
 * Mirrors the Python keys.py for cross-language consistency.
 */

export const Key = {
  // ==========================================================================
  // Header - Top-level device identification
  // ==========================================================================
  DEVICE: "Device", // Device model name (e.g., "Fridge-tag 2")
  VERSION: "Vers", // File format version (string, e.g., "1.0")
  FW_VERSION: "Fw Vers", // Firmware version installed on device (string)
  SENSOR_COUNT: "Sensor", // Number of temperature sensors (int, typically 1)

  // ==========================================================================
  // Sections - Major data sections in the file
  // ==========================================================================
  CONFIG: "Conf", // Configuration section header (device settings)
  HISTORY: "Hist", // History section header (temperature records)
  CERTIFICATE: "Cert", // Certificate section header (digital signature info)
  ERRORS: "Errors", // Errors section header (device error log)

  // ==========================================================================
  // Config - Device identification and settings
  // ==========================================================================
  SERIAL: "Serial", // Device serial number (int, unique device ID)
  PCB: "PCB", // PCB revision/batch identifier (string)
  CID: "CID", // Customer ID / configuration ID (int)
  LOT: "Lot", // Manufacturing lot number (string)
  ZONE: "Zone", // Temperature zone setting (float, target storage temp in °C)
  MEASUREMENT_DELAY: "Measurement delay", // Delay between measurements (int, minutes)
  MOVING_AVERAGE: "Moving Avrg", // Moving average window size (int, samples)
  USER_ALARM_CONFIG: "User Alarm Config", // User-configurable alarm settings (hex flags)
  USER_CLOCK_CONFIG: "User Clock Config", // User-configurable clock settings (hex flags)
  ALARM_INDICATION: "Alarm Indication", // How alarms are indicated (int, mode code)
  TEMP_UNIT: "Temp unit", // Temperature unit display setting (string, "C" or "F")
  ALARM: "Alarm", // Alarm configuration subsection header
  INTERNAL_SENSOR: "Int Sensor", // Internal sensor subsection header
  TIMEOUT: "Timeout", // Sensor timeout subsection header
  OFFSET: "Offset", // Temperature sensor calibration offset (float, °C)
  REPORT_HISTORY_LENGTH: "Report history length", // Days of history to include in reports (int)
  DETAILED_REPORT: "Det Report", // Detailed report enabled flag (int, 0 or 1)
  USE_EXTERNAL_DEVICES: "Use ext devices", // External devices enabled (int, 0 or 1)
  TEST_RESULT: "Test Res", // Factory test result code (int)
  TEST_TIMESTAMP: "Test TS", // Factory test timestamp (datetime string)

  // ==========================================================================
  // History - Session timestamps
  // ==========================================================================
  ACTIVATION_TIMESTAMP: "TS Actv", // When monitoring was activated (datetime string)
  REPORT_CREATION_TIMESTAMP: "TS Report Creation", // When report was generated (datetime string)

  // ==========================================================================
  // History - Daily temperature records (one per day index)
  // ==========================================================================
  DATE: "Date", // Date for this record (date string, e.g., "2024-01-15")
  MIN_TEMP: "Min T", // Minimum temperature recorded that day (float, °C, or null)
  MAX_TEMP: "Max T", // Maximum temperature recorded that day (float, °C, or null)
  AVG_TEMP: "Avrg T", // Average temperature for the day (float, °C, or null)
  MIN_TEMP_TIMESTAMP: "TS Min T", // Time when minimum temp was recorded (time string)
  MAX_TEMP_TIMESTAMP: "TS Max T", // Time when maximum temp was recorded (time string)
  SENSOR_TIMEOUT: "Int Sensor timeout", // Internal sensor timeout subsection header
  EVENTS: "Events", // Number of measurement events for the day (int)
  CHECKED: "Checked", // Manual check-in timestamps subsection header
  AM_TIMESTAMP: "TS AM", // Morning manual check timestamp (datetime string, or null)
  PM_TIMESTAMP: "TS PM", // Afternoon manual check timestamp (datetime string, or null)

  // ==========================================================================
  // Breach/Alarm Configuration - Threshold settings per alarm level
  // ==========================================================================
  TEMP_THRESHOLD: "T AL", // Temperature Alarm Limit - threshold temp (float, °C)
  DURATION_THRESHOLD: "t AL", // time Alarm Limit - duration before alarm triggers (int, minutes)

  // ==========================================================================
  // Breach/Alarm Accumulators - Per day, per alarm level
  // ==========================================================================
  ACCUMULATED_TIME: "t Acc", // time Accumulated - total minutes in breach state (int)
  ALARM_TIMESTAMP: "TS A", // Timestamp Alarm - when breach was first triggered (datetime string)
  ALARM_COUNT: "C A", // Count Alarm - number of separate breach events (int)
  ACCUMULATED_SENSOR_TIMEOUT: "t AccST", // time Accumulated Sensor Timeout - sensor offline minutes (int)

  // ==========================================================================
  // Errors - Device error logging
  // ==========================================================================
  ERROR_COUNT: "Err Count", // Error Count - number of errors logged (int)
  ERROR_TIMESTAMP: "Err TS", // Error Timestamp - when error occurred (datetime string)

  // ==========================================================================
  // Certificate - Digital signature and authenticity verification
  // ==========================================================================
  ISSUER: "Issuer", // Certificate issuer name (string, e.g., "Berlinger AG")
  VALID_FROM: "Valid from", // Certificate validity start date (date string)
  OWNER: "Owner", // Certificate owner / subject name (string)
  PUBLIC_KEY: "Public Key", // Public key for signature verification (hex string)
  SIGNATURE_CERT: "Sig Cert", // Certificate signature (hex string, signs the cert data)
  SIGNATURE: "Sig", // Data signature (hex string, signs the entire file content)
};
