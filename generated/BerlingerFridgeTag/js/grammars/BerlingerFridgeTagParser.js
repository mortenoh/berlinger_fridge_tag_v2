// Generated from BerlingerFridgeTag.g4 by ANTLR 4.13.2
// jshint ignore: start
import antlr4 from 'antlr4';
import BerlingerFridgeTagListener from './BerlingerFridgeTagListener.js';
import BerlingerFridgeTagVisitor from './BerlingerFridgeTagVisitor.js';

const serializedATN = [4,1,68,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,
2,5,7,5,2,6,7,6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,
1,1,1,1,1,1,3,1,30,8,1,1,2,1,2,1,2,4,2,35,8,2,11,2,12,2,36,3,2,39,8,2,1,
3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,5,3,5,53,8,5,1,5,1,5,1,5,
1,5,1,5,1,5,3,5,61,8,5,1,6,4,6,64,8,6,11,6,12,6,65,1,7,1,7,1,7,0,0,8,0,2,
4,6,8,10,12,14,0,2,1,0,1,55,3,0,57,57,60,61,66,67,76,0,16,1,0,0,0,2,26,1,
0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,49,1,0,0,0,10,60,1,0,0,0,12,63,1,0,0,0,
14,67,1,0,0,0,16,21,3,2,1,0,17,18,5,59,0,0,18,20,3,2,1,0,19,17,1,0,0,0,20,
23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,
5,0,0,1,25,1,1,0,0,0,26,27,3,4,2,0,27,29,5,58,0,0,28,30,3,8,4,0,29,28,1,
0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,39,3,6,3,0,32,39,5,66,0,0,33,35,5,67,
0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,
0,38,31,1,0,0,0,38,32,1,0,0,0,38,34,1,0,0,0,39,5,1,0,0,0,40,41,7,0,0,0,41,
7,1,0,0,0,42,50,3,10,5,0,43,50,5,62,0,0,44,50,5,63,0,0,45,50,5,64,0,0,46,
50,5,66,0,0,47,50,5,65,0,0,48,50,3,12,6,0,49,42,1,0,0,0,49,43,1,0,0,0,49,
44,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,9,
1,0,0,0,51,53,5,61,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,
66,0,0,55,56,5,60,0,0,56,61,5,66,0,0,57,58,5,61,0,0,58,61,5,66,0,0,59,61,
5,56,0,0,60,52,1,0,0,0,60,57,1,0,0,0,60,59,1,0,0,0,61,11,1,0,0,0,62,64,3,
14,7,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,13,1,0,
0,0,67,68,7,1,0,0,68,15,1,0,0,0,8,21,29,36,38,49,52,60,65];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class BerlingerFridgeTagParser extends antlr4.Parser {

    static grammarFileName = "BerlingerFridgeTag.g4";
    static literalNames = [ null, "'Device'", "'Vers'", "'Fw Vers'", "'Sensor'", 
                            "'Conf'", "'Hist'", "'Cert'", "'Errors'", "'Serial'", 
                            "'PCB'", "'CID'", "'Lot'", "'Zone'", "'Measurement delay'", 
                            "'Moving Avrg'", "'User Alarm Config'", "'User Clock Config'", 
                            "'Alarm Indication'", "'Temp unit'", "'Alarm'", 
                            "'Int Sensor'", "'Timeout'", "'Offset'", "'Report history length'", 
                            "'Det Report'", "'Use ext devices'", "'Test Res'", 
                            "'Test TS'", "'TS Actv'", "'TS Report Creation'", 
                            "'Date'", "'Min T'", "'Max T'", "'Avrg T'", 
                            "'TS Min T'", "'TS Max T'", "'Int Sensor timeout'", 
                            "'Events'", "'Checked'", "'TS AM'", "'TS PM'", 
                            "'T AL'", "'t AL'", "'t Acc'", "'TS A'", "'C A'", 
                            "'t AccST'", "'Err Count'", "'Err TS'", "'Issuer'", 
                            "'Valid from'", "'Owner'", "'Public Key'", "'Sig Cert'", 
                            "'Sig'", "'---'", "'&'", "':'", "','", "'.'" ];
    static symbolicNames = [ null, "DEVICE", "VERSION", "FW_VERSION", "SENSOR_COUNT", 
                             "CONFIG", "HISTORY", "CERTIFICATE", "ERRORS", 
                             "SERIAL", "PCB", "CID", "LOT", "ZONE", "MEASUREMENT_DELAY", 
                             "MOVING_AVERAGE", "USER_ALARM_CONFIG", "USER_CLOCK_CONFIG", 
                             "ALARM_INDICATION", "TEMP_UNIT", "ALARM", "INTERNAL_SENSOR", 
                             "TIMEOUT", "OFFSET", "REPORT_HISTORY_LENGTH", 
                             "DETAILED_REPORT", "USE_EXTERNAL_DEVICES", 
                             "TEST_RESULT", "TEST_TIMESTAMP", "ACTIVATION_TIMESTAMP", 
                             "REPORT_CREATION_TIMESTAMP", "DATE_KEY", "MIN_TEMP", 
                             "MAX_TEMP", "AVG_TEMP", "MIN_TEMP_TIMESTAMP", 
                             "MAX_TEMP_TIMESTAMP", "SENSOR_TIMEOUT", "EVENTS", 
                             "CHECKED", "AM_TIMESTAMP", "PM_TIMESTAMP", 
                             "TEMP_THRESHOLD", "DURATION_THRESHOLD", "ACCUMULATED_TIME", 
                             "ALARM_TIMESTAMP", "ALARM_COUNT", "ACCUMULATED_SENSOR_TIMEOUT", 
                             "ERROR_COUNT", "ERROR_TIMESTAMP", "ISSUER", 
                             "VALID_FROM", "OWNER", "PUBLIC_KEY", "SIGNATURE_CERT", 
                             "SIGNATURE", "MISSING", "AMPERSAND", "COLON", 
                             "COMMA", "DOT", "SIGN", "DATETIME", "DATE", 
                             "TIME", "HEX", "INT", "ID", "WS" ];
    static ruleNames = [ "line", "entry", "key", "knownKey", "value", "temperature", 
                         "textValue", "textPart" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = BerlingerFridgeTagParser.ruleNames;
        this.literalNames = BerlingerFridgeTagParser.literalNames;
        this.symbolicNames = BerlingerFridgeTagParser.symbolicNames;
    }



	line() {
	    let localctx = new LineContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, BerlingerFridgeTagParser.RULE_line);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 16;
	        this.entry();
	        this.state = 21;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===59) {
	            this.state = 17;
	            this.match(BerlingerFridgeTagParser.COMMA);
	            this.state = 18;
	            this.entry();
	            this.state = 23;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 24;
	        this.match(BerlingerFridgeTagParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	entry() {
	    let localctx = new EntryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, BerlingerFridgeTagParser.RULE_entry);
	    var _la = 0;
	    try {
	        localctx = new KeyValueContext(this, localctx);
	        this.enterOuterAlt(localctx, 1);
	        this.state = 26;
	        this.key();
	        this.state = 27;
	        this.match(BerlingerFridgeTagParser.COLON);
	        this.state = 29;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(((((_la - 56)) & ~0x1f) === 0 && ((1 << (_la - 56)) & 4083) !== 0)) {
	            this.state = 28;
	            this.value();
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	key() {
	    let localctx = new KeyContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, BerlingerFridgeTagParser.RULE_key);
	    var _la = 0;
	    try {
	        this.state = 38;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 1:
	        case 2:
	        case 3:
	        case 4:
	        case 5:
	        case 6:
	        case 7:
	        case 8:
	        case 9:
	        case 10:
	        case 11:
	        case 12:
	        case 13:
	        case 14:
	        case 15:
	        case 16:
	        case 17:
	        case 18:
	        case 19:
	        case 20:
	        case 21:
	        case 22:
	        case 23:
	        case 24:
	        case 25:
	        case 26:
	        case 27:
	        case 28:
	        case 29:
	        case 30:
	        case 31:
	        case 32:
	        case 33:
	        case 34:
	        case 35:
	        case 36:
	        case 37:
	        case 38:
	        case 39:
	        case 40:
	        case 41:
	        case 42:
	        case 43:
	        case 44:
	        case 45:
	        case 46:
	        case 47:
	        case 48:
	        case 49:
	        case 50:
	        case 51:
	        case 52:
	        case 53:
	        case 54:
	        case 55:
	            localctx = new KnownKeyRefContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 31;
	            this.knownKey();
	            break;
	        case 66:
	            localctx = new IndexKeyContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 32;
	            this.match(BerlingerFridgeTagParser.INT);
	            break;
	        case 67:
	            localctx = new GenericKeyContext(this, localctx);
	            this.enterOuterAlt(localctx, 3);
	            this.state = 34; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 33;
	                this.match(BerlingerFridgeTagParser.ID);
	                this.state = 36; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===67);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	knownKey() {
	    let localctx = new KnownKeyContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, BerlingerFridgeTagParser.RULE_knownKey);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 40;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) === 0 && ((1 << _la) & 4294967294) !== 0) || ((((_la - 32)) & ~0x1f) === 0 && ((1 << (_la - 32)) & 16777215) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	value() {
	    let localctx = new ValueContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, BerlingerFridgeTagParser.RULE_value);
	    try {
	        this.state = 49;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
	        switch(la_) {
	        case 1:
	            localctx = new TempValContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 42;
	            this.temperature();
	            break;

	        case 2:
	            localctx = new DateTimeValContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 43;
	            this.match(BerlingerFridgeTagParser.DATETIME);
	            break;

	        case 3:
	            localctx = new DateValContext(this, localctx);
	            this.enterOuterAlt(localctx, 3);
	            this.state = 44;
	            this.match(BerlingerFridgeTagParser.DATE);
	            break;

	        case 4:
	            localctx = new TimeValContext(this, localctx);
	            this.enterOuterAlt(localctx, 4);
	            this.state = 45;
	            this.match(BerlingerFridgeTagParser.TIME);
	            break;

	        case 5:
	            localctx = new IntValContext(this, localctx);
	            this.enterOuterAlt(localctx, 5);
	            this.state = 46;
	            this.match(BerlingerFridgeTagParser.INT);
	            break;

	        case 6:
	            localctx = new HexValContext(this, localctx);
	            this.enterOuterAlt(localctx, 6);
	            this.state = 47;
	            this.match(BerlingerFridgeTagParser.HEX);
	            break;

	        case 7:
	            localctx = new TextValContext(this, localctx);
	            this.enterOuterAlt(localctx, 7);
	            this.state = 48;
	            this.textValue();
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	temperature() {
	    let localctx = new TemperatureContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, BerlingerFridgeTagParser.RULE_temperature);
	    var _la = 0;
	    try {
	        this.state = 60;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,6,this._ctx);
	        switch(la_) {
	        case 1:
	            localctx = new TempNumberContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 52;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===61) {
	                this.state = 51;
	                this.match(BerlingerFridgeTagParser.SIGN);
	            }

	            this.state = 54;
	            this.match(BerlingerFridgeTagParser.INT);
	            this.state = 55;
	            this.match(BerlingerFridgeTagParser.DOT);
	            this.state = 56;
	            this.match(BerlingerFridgeTagParser.INT);
	            break;

	        case 2:
	            localctx = new TempSignedContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 57;
	            this.match(BerlingerFridgeTagParser.SIGN);
	            this.state = 58;
	            this.match(BerlingerFridgeTagParser.INT);
	            break;

	        case 3:
	            localctx = new TempMissingContext(this, localctx);
	            this.enterOuterAlt(localctx, 3);
	            this.state = 59;
	            this.match(BerlingerFridgeTagParser.MISSING);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	textValue() {
	    let localctx = new TextValueContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, BerlingerFridgeTagParser.RULE_textValue);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 63; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 62;
	            this.textPart();
	            this.state = 65; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while(((((_la - 57)) & ~0x1f) === 0 && ((1 << (_la - 57)) & 1561) !== 0));
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	textPart() {
	    let localctx = new TextPartContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, BerlingerFridgeTagParser.RULE_textPart);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 67;
	        _la = this._input.LA(1);
	        if(!(((((_la - 57)) & ~0x1f) === 0 && ((1 << (_la - 57)) & 1561) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

BerlingerFridgeTagParser.EOF = antlr4.Token.EOF;
BerlingerFridgeTagParser.DEVICE = 1;
BerlingerFridgeTagParser.VERSION = 2;
BerlingerFridgeTagParser.FW_VERSION = 3;
BerlingerFridgeTagParser.SENSOR_COUNT = 4;
BerlingerFridgeTagParser.CONFIG = 5;
BerlingerFridgeTagParser.HISTORY = 6;
BerlingerFridgeTagParser.CERTIFICATE = 7;
BerlingerFridgeTagParser.ERRORS = 8;
BerlingerFridgeTagParser.SERIAL = 9;
BerlingerFridgeTagParser.PCB = 10;
BerlingerFridgeTagParser.CID = 11;
BerlingerFridgeTagParser.LOT = 12;
BerlingerFridgeTagParser.ZONE = 13;
BerlingerFridgeTagParser.MEASUREMENT_DELAY = 14;
BerlingerFridgeTagParser.MOVING_AVERAGE = 15;
BerlingerFridgeTagParser.USER_ALARM_CONFIG = 16;
BerlingerFridgeTagParser.USER_CLOCK_CONFIG = 17;
BerlingerFridgeTagParser.ALARM_INDICATION = 18;
BerlingerFridgeTagParser.TEMP_UNIT = 19;
BerlingerFridgeTagParser.ALARM = 20;
BerlingerFridgeTagParser.INTERNAL_SENSOR = 21;
BerlingerFridgeTagParser.TIMEOUT = 22;
BerlingerFridgeTagParser.OFFSET = 23;
BerlingerFridgeTagParser.REPORT_HISTORY_LENGTH = 24;
BerlingerFridgeTagParser.DETAILED_REPORT = 25;
BerlingerFridgeTagParser.USE_EXTERNAL_DEVICES = 26;
BerlingerFridgeTagParser.TEST_RESULT = 27;
BerlingerFridgeTagParser.TEST_TIMESTAMP = 28;
BerlingerFridgeTagParser.ACTIVATION_TIMESTAMP = 29;
BerlingerFridgeTagParser.REPORT_CREATION_TIMESTAMP = 30;
BerlingerFridgeTagParser.DATE_KEY = 31;
BerlingerFridgeTagParser.MIN_TEMP = 32;
BerlingerFridgeTagParser.MAX_TEMP = 33;
BerlingerFridgeTagParser.AVG_TEMP = 34;
BerlingerFridgeTagParser.MIN_TEMP_TIMESTAMP = 35;
BerlingerFridgeTagParser.MAX_TEMP_TIMESTAMP = 36;
BerlingerFridgeTagParser.SENSOR_TIMEOUT = 37;
BerlingerFridgeTagParser.EVENTS = 38;
BerlingerFridgeTagParser.CHECKED = 39;
BerlingerFridgeTagParser.AM_TIMESTAMP = 40;
BerlingerFridgeTagParser.PM_TIMESTAMP = 41;
BerlingerFridgeTagParser.TEMP_THRESHOLD = 42;
BerlingerFridgeTagParser.DURATION_THRESHOLD = 43;
BerlingerFridgeTagParser.ACCUMULATED_TIME = 44;
BerlingerFridgeTagParser.ALARM_TIMESTAMP = 45;
BerlingerFridgeTagParser.ALARM_COUNT = 46;
BerlingerFridgeTagParser.ACCUMULATED_SENSOR_TIMEOUT = 47;
BerlingerFridgeTagParser.ERROR_COUNT = 48;
BerlingerFridgeTagParser.ERROR_TIMESTAMP = 49;
BerlingerFridgeTagParser.ISSUER = 50;
BerlingerFridgeTagParser.VALID_FROM = 51;
BerlingerFridgeTagParser.OWNER = 52;
BerlingerFridgeTagParser.PUBLIC_KEY = 53;
BerlingerFridgeTagParser.SIGNATURE_CERT = 54;
BerlingerFridgeTagParser.SIGNATURE = 55;
BerlingerFridgeTagParser.MISSING = 56;
BerlingerFridgeTagParser.AMPERSAND = 57;
BerlingerFridgeTagParser.COLON = 58;
BerlingerFridgeTagParser.COMMA = 59;
BerlingerFridgeTagParser.DOT = 60;
BerlingerFridgeTagParser.SIGN = 61;
BerlingerFridgeTagParser.DATETIME = 62;
BerlingerFridgeTagParser.DATE = 63;
BerlingerFridgeTagParser.TIME = 64;
BerlingerFridgeTagParser.HEX = 65;
BerlingerFridgeTagParser.INT = 66;
BerlingerFridgeTagParser.ID = 67;
BerlingerFridgeTagParser.WS = 68;

BerlingerFridgeTagParser.RULE_line = 0;
BerlingerFridgeTagParser.RULE_entry = 1;
BerlingerFridgeTagParser.RULE_key = 2;
BerlingerFridgeTagParser.RULE_knownKey = 3;
BerlingerFridgeTagParser.RULE_value = 4;
BerlingerFridgeTagParser.RULE_temperature = 5;
BerlingerFridgeTagParser.RULE_textValue = 6;
BerlingerFridgeTagParser.RULE_textPart = 7;

class LineContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_line;
    }

	entry = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(EntryContext);
	    } else {
	        return this.getTypedRuleContext(EntryContext,i);
	    }
	};

	EOF() {
	    return this.getToken(BerlingerFridgeTagParser.EOF, 0);
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(BerlingerFridgeTagParser.COMMA);
	    } else {
	        return this.getToken(BerlingerFridgeTagParser.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterLine(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitLine(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitLine(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class EntryContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_entry;
    }


	 
		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class KeyValueContext extends EntryContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	key() {
	    return this.getTypedRuleContext(KeyContext,0);
	};

	COLON() {
	    return this.getToken(BerlingerFridgeTagParser.COLON, 0);
	};

	value() {
	    return this.getTypedRuleContext(ValueContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterKeyValue(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitKeyValue(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitKeyValue(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.KeyValueContext = KeyValueContext;

class KeyContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_key;
    }


	 
		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class KnownKeyRefContext extends KeyContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	knownKey() {
	    return this.getTypedRuleContext(KnownKeyContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterKnownKeyRef(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitKnownKeyRef(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitKnownKeyRef(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.KnownKeyRefContext = KnownKeyRefContext;

class IndexKeyContext extends KeyContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	INT() {
	    return this.getToken(BerlingerFridgeTagParser.INT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterIndexKey(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitIndexKey(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitIndexKey(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.IndexKeyContext = IndexKeyContext;

class GenericKeyContext extends KeyContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	ID = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(BerlingerFridgeTagParser.ID);
	    } else {
	        return this.getToken(BerlingerFridgeTagParser.ID, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterGenericKey(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitGenericKey(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitGenericKey(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.GenericKeyContext = GenericKeyContext;

class KnownKeyContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_knownKey;
    }

	DEVICE() {
	    return this.getToken(BerlingerFridgeTagParser.DEVICE, 0);
	};

	VERSION() {
	    return this.getToken(BerlingerFridgeTagParser.VERSION, 0);
	};

	FW_VERSION() {
	    return this.getToken(BerlingerFridgeTagParser.FW_VERSION, 0);
	};

	SENSOR_COUNT() {
	    return this.getToken(BerlingerFridgeTagParser.SENSOR_COUNT, 0);
	};

	CONFIG() {
	    return this.getToken(BerlingerFridgeTagParser.CONFIG, 0);
	};

	HISTORY() {
	    return this.getToken(BerlingerFridgeTagParser.HISTORY, 0);
	};

	CERTIFICATE() {
	    return this.getToken(BerlingerFridgeTagParser.CERTIFICATE, 0);
	};

	ERRORS() {
	    return this.getToken(BerlingerFridgeTagParser.ERRORS, 0);
	};

	SERIAL() {
	    return this.getToken(BerlingerFridgeTagParser.SERIAL, 0);
	};

	PCB() {
	    return this.getToken(BerlingerFridgeTagParser.PCB, 0);
	};

	CID() {
	    return this.getToken(BerlingerFridgeTagParser.CID, 0);
	};

	LOT() {
	    return this.getToken(BerlingerFridgeTagParser.LOT, 0);
	};

	ZONE() {
	    return this.getToken(BerlingerFridgeTagParser.ZONE, 0);
	};

	MEASUREMENT_DELAY() {
	    return this.getToken(BerlingerFridgeTagParser.MEASUREMENT_DELAY, 0);
	};

	MOVING_AVERAGE() {
	    return this.getToken(BerlingerFridgeTagParser.MOVING_AVERAGE, 0);
	};

	USER_ALARM_CONFIG() {
	    return this.getToken(BerlingerFridgeTagParser.USER_ALARM_CONFIG, 0);
	};

	USER_CLOCK_CONFIG() {
	    return this.getToken(BerlingerFridgeTagParser.USER_CLOCK_CONFIG, 0);
	};

	ALARM_INDICATION() {
	    return this.getToken(BerlingerFridgeTagParser.ALARM_INDICATION, 0);
	};

	TEMP_UNIT() {
	    return this.getToken(BerlingerFridgeTagParser.TEMP_UNIT, 0);
	};

	ALARM() {
	    return this.getToken(BerlingerFridgeTagParser.ALARM, 0);
	};

	INTERNAL_SENSOR() {
	    return this.getToken(BerlingerFridgeTagParser.INTERNAL_SENSOR, 0);
	};

	TIMEOUT() {
	    return this.getToken(BerlingerFridgeTagParser.TIMEOUT, 0);
	};

	OFFSET() {
	    return this.getToken(BerlingerFridgeTagParser.OFFSET, 0);
	};

	REPORT_HISTORY_LENGTH() {
	    return this.getToken(BerlingerFridgeTagParser.REPORT_HISTORY_LENGTH, 0);
	};

	DETAILED_REPORT() {
	    return this.getToken(BerlingerFridgeTagParser.DETAILED_REPORT, 0);
	};

	USE_EXTERNAL_DEVICES() {
	    return this.getToken(BerlingerFridgeTagParser.USE_EXTERNAL_DEVICES, 0);
	};

	TEST_RESULT() {
	    return this.getToken(BerlingerFridgeTagParser.TEST_RESULT, 0);
	};

	TEST_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.TEST_TIMESTAMP, 0);
	};

	ACTIVATION_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.ACTIVATION_TIMESTAMP, 0);
	};

	REPORT_CREATION_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.REPORT_CREATION_TIMESTAMP, 0);
	};

	DATE_KEY() {
	    return this.getToken(BerlingerFridgeTagParser.DATE_KEY, 0);
	};

	MIN_TEMP() {
	    return this.getToken(BerlingerFridgeTagParser.MIN_TEMP, 0);
	};

	MAX_TEMP() {
	    return this.getToken(BerlingerFridgeTagParser.MAX_TEMP, 0);
	};

	AVG_TEMP() {
	    return this.getToken(BerlingerFridgeTagParser.AVG_TEMP, 0);
	};

	MIN_TEMP_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.MIN_TEMP_TIMESTAMP, 0);
	};

	MAX_TEMP_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.MAX_TEMP_TIMESTAMP, 0);
	};

	SENSOR_TIMEOUT() {
	    return this.getToken(BerlingerFridgeTagParser.SENSOR_TIMEOUT, 0);
	};

	EVENTS() {
	    return this.getToken(BerlingerFridgeTagParser.EVENTS, 0);
	};

	CHECKED() {
	    return this.getToken(BerlingerFridgeTagParser.CHECKED, 0);
	};

	AM_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.AM_TIMESTAMP, 0);
	};

	PM_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.PM_TIMESTAMP, 0);
	};

	TEMP_THRESHOLD() {
	    return this.getToken(BerlingerFridgeTagParser.TEMP_THRESHOLD, 0);
	};

	DURATION_THRESHOLD() {
	    return this.getToken(BerlingerFridgeTagParser.DURATION_THRESHOLD, 0);
	};

	ACCUMULATED_TIME() {
	    return this.getToken(BerlingerFridgeTagParser.ACCUMULATED_TIME, 0);
	};

	ALARM_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.ALARM_TIMESTAMP, 0);
	};

	ALARM_COUNT() {
	    return this.getToken(BerlingerFridgeTagParser.ALARM_COUNT, 0);
	};

	ACCUMULATED_SENSOR_TIMEOUT() {
	    return this.getToken(BerlingerFridgeTagParser.ACCUMULATED_SENSOR_TIMEOUT, 0);
	};

	ERROR_COUNT() {
	    return this.getToken(BerlingerFridgeTagParser.ERROR_COUNT, 0);
	};

	ERROR_TIMESTAMP() {
	    return this.getToken(BerlingerFridgeTagParser.ERROR_TIMESTAMP, 0);
	};

	ISSUER() {
	    return this.getToken(BerlingerFridgeTagParser.ISSUER, 0);
	};

	VALID_FROM() {
	    return this.getToken(BerlingerFridgeTagParser.VALID_FROM, 0);
	};

	OWNER() {
	    return this.getToken(BerlingerFridgeTagParser.OWNER, 0);
	};

	PUBLIC_KEY() {
	    return this.getToken(BerlingerFridgeTagParser.PUBLIC_KEY, 0);
	};

	SIGNATURE_CERT() {
	    return this.getToken(BerlingerFridgeTagParser.SIGNATURE_CERT, 0);
	};

	SIGNATURE() {
	    return this.getToken(BerlingerFridgeTagParser.SIGNATURE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterKnownKey(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitKnownKey(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitKnownKey(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ValueContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_value;
    }


	 
		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class TextValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	textValue() {
	    return this.getTypedRuleContext(TextValueContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTextVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTextVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTextVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TextValContext = TextValContext;

class HexValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	HEX() {
	    return this.getToken(BerlingerFridgeTagParser.HEX, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterHexVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitHexVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitHexVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.HexValContext = HexValContext;

class TimeValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	TIME() {
	    return this.getToken(BerlingerFridgeTagParser.TIME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTimeVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTimeVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTimeVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TimeValContext = TimeValContext;

class TempValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	temperature() {
	    return this.getTypedRuleContext(TemperatureContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTempVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTempVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTempVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TempValContext = TempValContext;

class DateTimeValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	DATETIME() {
	    return this.getToken(BerlingerFridgeTagParser.DATETIME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterDateTimeVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitDateTimeVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitDateTimeVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.DateTimeValContext = DateTimeValContext;

class IntValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	INT() {
	    return this.getToken(BerlingerFridgeTagParser.INT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterIntVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitIntVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitIntVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.IntValContext = IntValContext;

class DateValContext extends ValueContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	DATE() {
	    return this.getToken(BerlingerFridgeTagParser.DATE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterDateVal(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitDateVal(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitDateVal(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.DateValContext = DateValContext;

class TemperatureContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_temperature;
    }


	 
		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class TempMissingContext extends TemperatureContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	MISSING() {
	    return this.getToken(BerlingerFridgeTagParser.MISSING, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTempMissing(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTempMissing(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTempMissing(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TempMissingContext = TempMissingContext;

class TempNumberContext extends TemperatureContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	INT = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(BerlingerFridgeTagParser.INT);
	    } else {
	        return this.getToken(BerlingerFridgeTagParser.INT, i);
	    }
	};


	DOT() {
	    return this.getToken(BerlingerFridgeTagParser.DOT, 0);
	};

	SIGN() {
	    return this.getToken(BerlingerFridgeTagParser.SIGN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTempNumber(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTempNumber(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTempNumber(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TempNumberContext = TempNumberContext;

class TempSignedContext extends TemperatureContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	SIGN() {
	    return this.getToken(BerlingerFridgeTagParser.SIGN, 0);
	};

	INT() {
	    return this.getToken(BerlingerFridgeTagParser.INT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTempSigned(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTempSigned(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTempSigned(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

BerlingerFridgeTagParser.TempSignedContext = TempSignedContext;

class TextValueContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_textValue;
    }

	textPart = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(TextPartContext);
	    } else {
	        return this.getTypedRuleContext(TextPartContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTextValue(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTextValue(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTextValue(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TextPartContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = BerlingerFridgeTagParser.RULE_textPart;
    }

	ID() {
	    return this.getToken(BerlingerFridgeTagParser.ID, 0);
	};

	INT() {
	    return this.getToken(BerlingerFridgeTagParser.INT, 0);
	};

	DOT() {
	    return this.getToken(BerlingerFridgeTagParser.DOT, 0);
	};

	SIGN() {
	    return this.getToken(BerlingerFridgeTagParser.SIGN, 0);
	};

	AMPERSAND() {
	    return this.getToken(BerlingerFridgeTagParser.AMPERSAND, 0);
	};

	enterRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.enterTextPart(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof BerlingerFridgeTagListener ) {
	        listener.exitTextPart(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof BerlingerFridgeTagVisitor ) {
	        return visitor.visitTextPart(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




BerlingerFridgeTagParser.LineContext = LineContext; 
BerlingerFridgeTagParser.EntryContext = EntryContext; 
BerlingerFridgeTagParser.KeyContext = KeyContext; 
BerlingerFridgeTagParser.KnownKeyContext = KnownKeyContext; 
BerlingerFridgeTagParser.ValueContext = ValueContext; 
BerlingerFridgeTagParser.TemperatureContext = TemperatureContext; 
BerlingerFridgeTagParser.TextValueContext = TextValueContext; 
BerlingerFridgeTagParser.TextPartContext = TextPartContext; 
