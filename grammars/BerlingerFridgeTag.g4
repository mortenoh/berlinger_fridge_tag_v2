// BerlingerFridgeTag.g4 - Line-based parser for Berlinger Fridge-tag files
//
// This grammar parses individual lines without handling indentation.
// The hierarchy (based on indentation) is built by the visitor/listener.
//
// Design for multi-language targets (Java, JS, Python):
//   - Grammar handles line-level syntax only
//   - Each target implements hierarchy building
//   - Shared type definitions in each language
//
// Terminology aligned with open-msupply (https://github.com/msupply-foundation/open-msupply)
//
// Generate:
//   antlr4 -Dlanguage=Python3 -visitor BerlingerFridgeTag.g4
//   antlr4 -Dlanguage=Java -visitor BerlingerFridgeTag.g4
//   antlr4 -Dlanguage=JavaScript -visitor BerlingerFridgeTag.g4

grammar BerlingerFridgeTag;

// =============================================================================
// PARSER RULES
// =============================================================================

// Parse a single line (called per-line by host language)
line
    : entry (COMMA entry)* EOF
    ;

// An entry is key with optional value
entry
    : key COLON value?      # KeyValue
    ;

// Key types
key
    : knownKey              # KnownKeyRef
    | INT                   # IndexKey       // Numbered entries: 0, 1, 2...
    | ID+                   # GenericKey     // Unknown keys
    ;

// Known keys (enables type-safe visitor methods)
// Names follow open-msupply terminology where applicable
knownKey
    // Header
    : DEVICE | VERSION | FW_VERSION | SENSOR_COUNT
    // Sections
    | CONFIG | HISTORY | CERTIFICATE | ERRORS
    // Config - Device Info
    | SERIAL | PCB | CID | LOT | ZONE
    | MEASUREMENT_DELAY | MOVING_AVERAGE
    | USER_ALARM_CONFIG | USER_CLOCK_CONFIG
    | ALARM_INDICATION | TEMP_UNIT
    | ALARM | INTERNAL_SENSOR | TIMEOUT | OFFSET
    | REPORT_HISTORY_LENGTH | DETAILED_REPORT | USE_EXTERNAL_DEVICES
    | TEST_RESULT | TEST_TIMESTAMP
    // History - Timestamps
    | ACTIVATION_TIMESTAMP | REPORT_CREATION_TIMESTAMP
    // History - Daily Record
    | DATE_KEY | MIN_TEMP | MAX_TEMP | AVG_TEMP
    | MIN_TEMP_TIMESTAMP | MAX_TEMP_TIMESTAMP
    | SENSOR_TIMEOUT | EVENTS | CHECKED
    | AM_TIMESTAMP | PM_TIMESTAMP
    // Breach/Alarm Configuration (per open-msupply terminology)
    | TEMP_THRESHOLD | DURATION_THRESHOLD
    // Breach/Alarm Accumulators
    | ACCUMULATED_TIME | ALARM_TIMESTAMP | ALARM_COUNT
    | ACCUMULATED_SENSOR_TIMEOUT
    // Errors
    | ERROR_COUNT | ERROR_TIMESTAMP
    // Certificate
    | ISSUER | VALID_FROM | OWNER | PUBLIC_KEY
    | SIGNATURE_CERT | SIGNATURE
    ;

// Value types
value
    : temperature           # TempVal
    | DATETIME              # DateTimeVal
    | DATE                  # DateVal
    | TIME                  # TimeVal
    | INT                   # IntVal
    | HEX                   # HexVal
    | textValue             # TextVal
    ;

// Temperature: signed float or missing
temperature
    : SIGN? INT DOT INT     # TempNumber
    | SIGN INT              # TempSigned
    | MISSING               # TempMissing
    ;

// Text value (preserves structure for reconstruction)
textValue
    : textPart+
    ;

textPart
    : ID | INT | DOT | SIGN | AMPERSAND
    ;

// =============================================================================
// LEXER RULES - Keywords
// =============================================================================

// Header
DEVICE              : 'Device' ;
VERSION             : 'Vers' ;
FW_VERSION          : 'Fw Vers' ;
SENSOR_COUNT        : 'Sensor' ;

// Sections
CONFIG              : 'Conf' ;
HISTORY             : 'Hist' ;
CERTIFICATE         : 'Cert' ;
ERRORS              : 'Errors' ;

// Config - Device Info
SERIAL              : 'Serial' ;
PCB                 : 'PCB' ;
CID                 : 'CID' ;
LOT                 : 'Lot' ;
ZONE                : 'Zone' ;
MEASUREMENT_DELAY   : 'Measurement delay' ;
MOVING_AVERAGE      : 'Moving Avrg' ;
USER_ALARM_CONFIG   : 'User Alarm Config' ;
USER_CLOCK_CONFIG   : 'User Clock Config' ;
ALARM_INDICATION    : 'Alarm Indication' ;
TEMP_UNIT           : 'Temp unit' ;
ALARM               : 'Alarm' ;
INTERNAL_SENSOR     : 'Int Sensor' ;
TIMEOUT             : 'Timeout' ;
OFFSET              : 'Offset' ;
REPORT_HISTORY_LENGTH : 'Report history length' ;
DETAILED_REPORT     : 'Det Report' ;
USE_EXTERNAL_DEVICES : 'Use ext devices' ;
TEST_RESULT         : 'Test Res' ;
TEST_TIMESTAMP      : 'Test TS' ;

// History - Timestamps
ACTIVATION_TIMESTAMP    : 'TS Actv' ;
REPORT_CREATION_TIMESTAMP : 'TS Report Creation' ;

// History - Daily Record
DATE_KEY            : 'Date' ;
MIN_TEMP            : 'Min T' ;
MAX_TEMP            : 'Max T' ;
AVG_TEMP            : 'Avrg T' ;
MIN_TEMP_TIMESTAMP  : 'TS Min T' ;
MAX_TEMP_TIMESTAMP  : 'TS Max T' ;
SENSOR_TIMEOUT      : 'Int Sensor timeout' ;
EVENTS              : 'Events' ;
CHECKED             : 'Checked' ;
AM_TIMESTAMP        : 'TS AM' ;
PM_TIMESTAMP        : 'TS PM' ;

// Breach/Alarm Configuration
// T AL = Temperature Alarm Limit (threshold in °C)
// t AL = time Alarm Limit (duration threshold in minutes)
TEMP_THRESHOLD      : 'T AL' ;
DURATION_THRESHOLD  : 't AL' ;

// Breach/Alarm Accumulators
// t Acc = time Accumulated (cumulative breach minutes)
// TS A = Timestamp Alarm (when breach was triggered)
// C A = Count Alarm (number of breach events)
// t AccST = time Accumulated Sensor Timeout
ACCUMULATED_TIME    : 't Acc' ;
ALARM_TIMESTAMP     : 'TS A' ;
ALARM_COUNT         : 'C A' ;
ACCUMULATED_SENSOR_TIMEOUT : 't AccST' ;

// Errors
ERROR_COUNT         : 'Err Count' ;
ERROR_TIMESTAMP     : 'Err TS' ;

// Certificate
ISSUER              : 'Issuer' ;
VALID_FROM          : 'Valid from' ;
OWNER               : 'Owner' ;
PUBLIC_KEY          : 'Public Key' ;
SIGNATURE_CERT      : 'Sig Cert' ;
SIGNATURE           : 'Sig' ;

// =============================================================================
// LEXER RULES - Values
// =============================================================================

MISSING             : '---' ;
AMPERSAND           : '&' ;
COLON               : ':' ;
COMMA               : ',' ;
DOT                 : '.' ;
SIGN                : [+-] ;

// Date/Time (must precede INT)
DATETIME            : DATE_FRAG ' ' TIME_FRAG ;
DATE                : DATE_FRAG ;
TIME                : TIME_FRAG ;

fragment DATE_FRAG  : [0-9][0-9][0-9][0-9] '-' [0-9][0-9] '-' [0-9][0-9] ;
fragment TIME_FRAG  : [0-9][0-9] ':' [0-9][0-9] ;

// Hex (64+ chars)
HEX                 : [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]
                      [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]+
                    ;

INT                 : [0-9]+ ;
ID                  : [a-zA-Z_][a-zA-Z0-9_\-]* ;

// Skip whitespace
WS                  : [ \t]+ -> skip ;
