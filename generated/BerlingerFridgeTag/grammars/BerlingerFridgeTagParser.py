# Generated from BerlingerFridgeTag.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,68,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,4,2,35,8,2,11,2,12,2,36,3,2,39,8,2,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,5,3,5,53,8,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,61,8,5,1,6,4,6,64,8,6,11,6,12,6,65,1,7,
        1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,1,55,3,0,57,57,60,61,66,
        67,76,0,16,1,0,0,0,2,26,1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,49,1,
        0,0,0,10,60,1,0,0,0,12,63,1,0,0,0,14,67,1,0,0,0,16,21,3,2,1,0,17,
        18,5,59,0,0,18,20,3,2,1,0,19,17,1,0,0,0,20,23,1,0,0,0,21,19,1,0,
        0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,
        1,0,0,0,26,27,3,4,2,0,27,29,5,58,0,0,28,30,3,8,4,0,29,28,1,0,0,0,
        29,30,1,0,0,0,30,3,1,0,0,0,31,39,3,6,3,0,32,39,5,66,0,0,33,35,5,
        67,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,
        39,1,0,0,0,38,31,1,0,0,0,38,32,1,0,0,0,38,34,1,0,0,0,39,5,1,0,0,
        0,40,41,7,0,0,0,41,7,1,0,0,0,42,50,3,10,5,0,43,50,5,62,0,0,44,50,
        5,63,0,0,45,50,5,64,0,0,46,50,5,66,0,0,47,50,5,65,0,0,48,50,3,12,
        6,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,
        1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,9,1,0,0,0,51,53,5,61,0,0,
        52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,66,0,0,55,56,5,
        60,0,0,56,61,5,66,0,0,57,58,5,61,0,0,58,61,5,66,0,0,59,61,5,56,0,
        0,60,52,1,0,0,0,60,57,1,0,0,0,60,59,1,0,0,0,61,11,1,0,0,0,62,64,
        3,14,7,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,
        66,13,1,0,0,0,67,68,7,1,0,0,68,15,1,0,0,0,8,21,29,36,38,49,52,60,
        65
    ]

class BerlingerFridgeTagParser ( Parser ):

    grammarFileName = "BerlingerFridgeTag.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Device'", "'Vers'", "'Fw Vers'", "'Sensor'", 
                     "'Conf'", "'Hist'", "'Cert'", "'Errors'", "'Serial'", 
                     "'PCB'", "'CID'", "'Lot'", "'Zone'", "'Measurement delay'", 
                     "'Moving Avrg'", "'User Alarm Config'", "'User Clock Config'", 
                     "'Alarm Indication'", "'Temp unit'", "'Alarm'", "'Int Sensor'", 
                     "'Timeout'", "'Offset'", "'Report history length'", 
                     "'Det Report'", "'Use ext devices'", "'Test Res'", 
                     "'Test TS'", "'TS Actv'", "'TS Report Creation'", "'Date'", 
                     "'Min T'", "'Max T'", "'Avrg T'", "'TS Min T'", "'TS Max T'", 
                     "'Int Sensor timeout'", "'Events'", "'Checked'", "'TS AM'", 
                     "'TS PM'", "'T AL'", "'t AL'", "'t Acc'", "'TS A'", 
                     "'C A'", "'t AccST'", "'Err Count'", "'Err TS'", "'Issuer'", 
                     "'Valid from'", "'Owner'", "'Public Key'", "'Sig Cert'", 
                     "'Sig'", "'---'", "'&'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "DEVICE", "VERSION", "FW_VERSION", "SENSOR_COUNT", 
                      "CONFIG", "HISTORY", "CERTIFICATE", "ERRORS", "SERIAL", 
                      "PCB", "CID", "LOT", "ZONE", "MEASUREMENT_DELAY", 
                      "MOVING_AVERAGE", "USER_ALARM_CONFIG", "USER_CLOCK_CONFIG", 
                      "ALARM_INDICATION", "TEMP_UNIT", "ALARM", "INTERNAL_SENSOR", 
                      "TIMEOUT", "OFFSET", "REPORT_HISTORY_LENGTH", "DETAILED_REPORT", 
                      "USE_EXTERNAL_DEVICES", "TEST_RESULT", "TEST_TIMESTAMP", 
                      "ACTIVATION_TIMESTAMP", "REPORT_CREATION_TIMESTAMP", 
                      "DATE_KEY", "MIN_TEMP", "MAX_TEMP", "AVG_TEMP", "MIN_TEMP_TIMESTAMP", 
                      "MAX_TEMP_TIMESTAMP", "SENSOR_TIMEOUT", "EVENTS", 
                      "CHECKED", "AM_TIMESTAMP", "PM_TIMESTAMP", "TEMP_THRESHOLD", 
                      "DURATION_THRESHOLD", "ACCUMULATED_TIME", "ALARM_TIMESTAMP", 
                      "ALARM_COUNT", "ACCUMULATED_SENSOR_TIMEOUT", "ERROR_COUNT", 
                      "ERROR_TIMESTAMP", "ISSUER", "VALID_FROM", "OWNER", 
                      "PUBLIC_KEY", "SIGNATURE_CERT", "SIGNATURE", "MISSING", 
                      "AMPERSAND", "COLON", "COMMA", "DOT", "SIGN", "DATETIME", 
                      "DATE", "TIME", "HEX", "INT", "ID", "WS" ]

    RULE_line = 0
    RULE_entry = 1
    RULE_key = 2
    RULE_knownKey = 3
    RULE_value = 4
    RULE_temperature = 5
    RULE_textValue = 6
    RULE_textPart = 7

    ruleNames =  [ "line", "entry", "key", "knownKey", "value", "temperature", 
                   "textValue", "textPart" ]

    EOF = Token.EOF
    DEVICE=1
    VERSION=2
    FW_VERSION=3
    SENSOR_COUNT=4
    CONFIG=5
    HISTORY=6
    CERTIFICATE=7
    ERRORS=8
    SERIAL=9
    PCB=10
    CID=11
    LOT=12
    ZONE=13
    MEASUREMENT_DELAY=14
    MOVING_AVERAGE=15
    USER_ALARM_CONFIG=16
    USER_CLOCK_CONFIG=17
    ALARM_INDICATION=18
    TEMP_UNIT=19
    ALARM=20
    INTERNAL_SENSOR=21
    TIMEOUT=22
    OFFSET=23
    REPORT_HISTORY_LENGTH=24
    DETAILED_REPORT=25
    USE_EXTERNAL_DEVICES=26
    TEST_RESULT=27
    TEST_TIMESTAMP=28
    ACTIVATION_TIMESTAMP=29
    REPORT_CREATION_TIMESTAMP=30
    DATE_KEY=31
    MIN_TEMP=32
    MAX_TEMP=33
    AVG_TEMP=34
    MIN_TEMP_TIMESTAMP=35
    MAX_TEMP_TIMESTAMP=36
    SENSOR_TIMEOUT=37
    EVENTS=38
    CHECKED=39
    AM_TIMESTAMP=40
    PM_TIMESTAMP=41
    TEMP_THRESHOLD=42
    DURATION_THRESHOLD=43
    ACCUMULATED_TIME=44
    ALARM_TIMESTAMP=45
    ALARM_COUNT=46
    ACCUMULATED_SENSOR_TIMEOUT=47
    ERROR_COUNT=48
    ERROR_TIMESTAMP=49
    ISSUER=50
    VALID_FROM=51
    OWNER=52
    PUBLIC_KEY=53
    SIGNATURE_CERT=54
    SIGNATURE=55
    MISSING=56
    AMPERSAND=57
    COLON=58
    COMMA=59
    DOT=60
    SIGN=61
    DATETIME=62
    DATE=63
    TIME=64
    HEX=65
    INT=66
    ID=67
    WS=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BerlingerFridgeTagParser.EntryContext)
            else:
                return self.getTypedRuleContext(BerlingerFridgeTagParser.EntryContext,i)


        def EOF(self):
            return self.getToken(BerlingerFridgeTagParser.EOF, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BerlingerFridgeTagParser.COMMA)
            else:
                return self.getToken(BerlingerFridgeTagParser.COMMA, i)

        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = BerlingerFridgeTagParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.entry()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 17
                self.match(BerlingerFridgeTagParser.COMMA)
                self.state = 18
                self.entry()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(BerlingerFridgeTagParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_entry

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class KeyValueContext(EntryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.EntryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def key(self):
            return self.getTypedRuleContext(BerlingerFridgeTagParser.KeyContext,0)

        def COLON(self):
            return self.getToken(BerlingerFridgeTagParser.COLON, 0)
        def value(self):
            return self.getTypedRuleContext(BerlingerFridgeTagParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValue" ):
                listener.enterKeyValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValue" ):
                listener.exitKeyValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValue" ):
                return visitor.visitKeyValue(self)
            else:
                return visitor.visitChildren(self)



    def entry(self):

        localctx = BerlingerFridgeTagParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entry)
        self._la = 0 # Token type
        try:
            localctx = BerlingerFridgeTagParser.KeyValueContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.key()
            self.state = 27
            self.match(BerlingerFridgeTagParser.COLON)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & 4083) != 0):
                self.state = 28
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_key

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class KnownKeyRefContext(KeyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.KeyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def knownKey(self):
            return self.getTypedRuleContext(BerlingerFridgeTagParser.KnownKeyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnownKeyRef" ):
                listener.enterKnownKeyRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnownKeyRef" ):
                listener.exitKnownKeyRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKnownKeyRef" ):
                return visitor.visitKnownKeyRef(self)
            else:
                return visitor.visitChildren(self)


    class IndexKeyContext(KeyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.KeyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BerlingerFridgeTagParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexKey" ):
                listener.enterIndexKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexKey" ):
                listener.exitIndexKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexKey" ):
                return visitor.visitIndexKey(self)
            else:
                return visitor.visitChildren(self)


    class GenericKeyContext(KeyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.KeyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BerlingerFridgeTagParser.ID)
            else:
                return self.getToken(BerlingerFridgeTagParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericKey" ):
                listener.enterGenericKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericKey" ):
                listener.exitGenericKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericKey" ):
                return visitor.visitGenericKey(self)
            else:
                return visitor.visitChildren(self)



    def key(self):

        localctx = BerlingerFridgeTagParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]:
                localctx = BerlingerFridgeTagParser.KnownKeyRefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.knownKey()
                pass
            elif token in [66]:
                localctx = BerlingerFridgeTagParser.IndexKeyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(BerlingerFridgeTagParser.INT)
                pass
            elif token in [67]:
                localctx = BerlingerFridgeTagParser.GenericKeyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 33
                    self.match(BerlingerFridgeTagParser.ID)
                    self.state = 36 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==67):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KnownKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEVICE(self):
            return self.getToken(BerlingerFridgeTagParser.DEVICE, 0)

        def VERSION(self):
            return self.getToken(BerlingerFridgeTagParser.VERSION, 0)

        def FW_VERSION(self):
            return self.getToken(BerlingerFridgeTagParser.FW_VERSION, 0)

        def SENSOR_COUNT(self):
            return self.getToken(BerlingerFridgeTagParser.SENSOR_COUNT, 0)

        def CONFIG(self):
            return self.getToken(BerlingerFridgeTagParser.CONFIG, 0)

        def HISTORY(self):
            return self.getToken(BerlingerFridgeTagParser.HISTORY, 0)

        def CERTIFICATE(self):
            return self.getToken(BerlingerFridgeTagParser.CERTIFICATE, 0)

        def ERRORS(self):
            return self.getToken(BerlingerFridgeTagParser.ERRORS, 0)

        def SERIAL(self):
            return self.getToken(BerlingerFridgeTagParser.SERIAL, 0)

        def PCB(self):
            return self.getToken(BerlingerFridgeTagParser.PCB, 0)

        def CID(self):
            return self.getToken(BerlingerFridgeTagParser.CID, 0)

        def LOT(self):
            return self.getToken(BerlingerFridgeTagParser.LOT, 0)

        def ZONE(self):
            return self.getToken(BerlingerFridgeTagParser.ZONE, 0)

        def MEASUREMENT_DELAY(self):
            return self.getToken(BerlingerFridgeTagParser.MEASUREMENT_DELAY, 0)

        def MOVING_AVERAGE(self):
            return self.getToken(BerlingerFridgeTagParser.MOVING_AVERAGE, 0)

        def USER_ALARM_CONFIG(self):
            return self.getToken(BerlingerFridgeTagParser.USER_ALARM_CONFIG, 0)

        def USER_CLOCK_CONFIG(self):
            return self.getToken(BerlingerFridgeTagParser.USER_CLOCK_CONFIG, 0)

        def ALARM_INDICATION(self):
            return self.getToken(BerlingerFridgeTagParser.ALARM_INDICATION, 0)

        def TEMP_UNIT(self):
            return self.getToken(BerlingerFridgeTagParser.TEMP_UNIT, 0)

        def ALARM(self):
            return self.getToken(BerlingerFridgeTagParser.ALARM, 0)

        def INTERNAL_SENSOR(self):
            return self.getToken(BerlingerFridgeTagParser.INTERNAL_SENSOR, 0)

        def TIMEOUT(self):
            return self.getToken(BerlingerFridgeTagParser.TIMEOUT, 0)

        def OFFSET(self):
            return self.getToken(BerlingerFridgeTagParser.OFFSET, 0)

        def REPORT_HISTORY_LENGTH(self):
            return self.getToken(BerlingerFridgeTagParser.REPORT_HISTORY_LENGTH, 0)

        def DETAILED_REPORT(self):
            return self.getToken(BerlingerFridgeTagParser.DETAILED_REPORT, 0)

        def USE_EXTERNAL_DEVICES(self):
            return self.getToken(BerlingerFridgeTagParser.USE_EXTERNAL_DEVICES, 0)

        def TEST_RESULT(self):
            return self.getToken(BerlingerFridgeTagParser.TEST_RESULT, 0)

        def TEST_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.TEST_TIMESTAMP, 0)

        def ACTIVATION_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.ACTIVATION_TIMESTAMP, 0)

        def REPORT_CREATION_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.REPORT_CREATION_TIMESTAMP, 0)

        def DATE_KEY(self):
            return self.getToken(BerlingerFridgeTagParser.DATE_KEY, 0)

        def MIN_TEMP(self):
            return self.getToken(BerlingerFridgeTagParser.MIN_TEMP, 0)

        def MAX_TEMP(self):
            return self.getToken(BerlingerFridgeTagParser.MAX_TEMP, 0)

        def AVG_TEMP(self):
            return self.getToken(BerlingerFridgeTagParser.AVG_TEMP, 0)

        def MIN_TEMP_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.MIN_TEMP_TIMESTAMP, 0)

        def MAX_TEMP_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.MAX_TEMP_TIMESTAMP, 0)

        def SENSOR_TIMEOUT(self):
            return self.getToken(BerlingerFridgeTagParser.SENSOR_TIMEOUT, 0)

        def EVENTS(self):
            return self.getToken(BerlingerFridgeTagParser.EVENTS, 0)

        def CHECKED(self):
            return self.getToken(BerlingerFridgeTagParser.CHECKED, 0)

        def AM_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.AM_TIMESTAMP, 0)

        def PM_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.PM_TIMESTAMP, 0)

        def TEMP_THRESHOLD(self):
            return self.getToken(BerlingerFridgeTagParser.TEMP_THRESHOLD, 0)

        def DURATION_THRESHOLD(self):
            return self.getToken(BerlingerFridgeTagParser.DURATION_THRESHOLD, 0)

        def ACCUMULATED_TIME(self):
            return self.getToken(BerlingerFridgeTagParser.ACCUMULATED_TIME, 0)

        def ALARM_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.ALARM_TIMESTAMP, 0)

        def ALARM_COUNT(self):
            return self.getToken(BerlingerFridgeTagParser.ALARM_COUNT, 0)

        def ACCUMULATED_SENSOR_TIMEOUT(self):
            return self.getToken(BerlingerFridgeTagParser.ACCUMULATED_SENSOR_TIMEOUT, 0)

        def ERROR_COUNT(self):
            return self.getToken(BerlingerFridgeTagParser.ERROR_COUNT, 0)

        def ERROR_TIMESTAMP(self):
            return self.getToken(BerlingerFridgeTagParser.ERROR_TIMESTAMP, 0)

        def ISSUER(self):
            return self.getToken(BerlingerFridgeTagParser.ISSUER, 0)

        def VALID_FROM(self):
            return self.getToken(BerlingerFridgeTagParser.VALID_FROM, 0)

        def OWNER(self):
            return self.getToken(BerlingerFridgeTagParser.OWNER, 0)

        def PUBLIC_KEY(self):
            return self.getToken(BerlingerFridgeTagParser.PUBLIC_KEY, 0)

        def SIGNATURE_CERT(self):
            return self.getToken(BerlingerFridgeTagParser.SIGNATURE_CERT, 0)

        def SIGNATURE(self):
            return self.getToken(BerlingerFridgeTagParser.SIGNATURE, 0)

        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_knownKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnownKey" ):
                listener.enterKnownKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnownKey" ):
                listener.exitKnownKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKnownKey" ):
                return visitor.visitKnownKey(self)
            else:
                return visitor.visitChildren(self)




    def knownKey(self):

        localctx = BerlingerFridgeTagParser.KnownKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_knownKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594037927934) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TextValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def textValue(self):
            return self.getTypedRuleContext(BerlingerFridgeTagParser.TextValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextVal" ):
                listener.enterTextVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextVal" ):
                listener.exitTextVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextVal" ):
                return visitor.visitTextVal(self)
            else:
                return visitor.visitChildren(self)


    class HexValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX(self):
            return self.getToken(BerlingerFridgeTagParser.HEX, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexVal" ):
                listener.enterHexVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexVal" ):
                listener.exitHexVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexVal" ):
                return visitor.visitHexVal(self)
            else:
                return visitor.visitChildren(self)


    class TimeValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(BerlingerFridgeTagParser.TIME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeVal" ):
                listener.enterTimeVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeVal" ):
                listener.exitTimeVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeVal" ):
                return visitor.visitTimeVal(self)
            else:
                return visitor.visitChildren(self)


    class TempValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def temperature(self):
            return self.getTypedRuleContext(BerlingerFridgeTagParser.TemperatureContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempVal" ):
                listener.enterTempVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempVal" ):
                listener.exitTempVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempVal" ):
                return visitor.visitTempVal(self)
            else:
                return visitor.visitChildren(self)


    class DateTimeValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(BerlingerFridgeTagParser.DATETIME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateTimeVal" ):
                listener.enterDateTimeVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateTimeVal" ):
                listener.exitDateTimeVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateTimeVal" ):
                return visitor.visitDateTimeVal(self)
            else:
                return visitor.visitChildren(self)


    class IntValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BerlingerFridgeTagParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntVal" ):
                listener.enterIntVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntVal" ):
                listener.exitIntVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntVal" ):
                return visitor.visitIntVal(self)
            else:
                return visitor.visitChildren(self)


    class DateValContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(BerlingerFridgeTagParser.DATE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateVal" ):
                listener.enterDateVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateVal" ):
                listener.exitDateVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateVal" ):
                return visitor.visitDateVal(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = BerlingerFridgeTagParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = BerlingerFridgeTagParser.TempValContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.temperature()
                pass

            elif la_ == 2:
                localctx = BerlingerFridgeTagParser.DateTimeValContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(BerlingerFridgeTagParser.DATETIME)
                pass

            elif la_ == 3:
                localctx = BerlingerFridgeTagParser.DateValContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(BerlingerFridgeTagParser.DATE)
                pass

            elif la_ == 4:
                localctx = BerlingerFridgeTagParser.TimeValContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(BerlingerFridgeTagParser.TIME)
                pass

            elif la_ == 5:
                localctx = BerlingerFridgeTagParser.IntValContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(BerlingerFridgeTagParser.INT)
                pass

            elif la_ == 6:
                localctx = BerlingerFridgeTagParser.HexValContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(BerlingerFridgeTagParser.HEX)
                pass

            elif la_ == 7:
                localctx = BerlingerFridgeTagParser.TextValContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.textValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_temperature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TempMissingContext(TemperatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.TemperatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MISSING(self):
            return self.getToken(BerlingerFridgeTagParser.MISSING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempMissing" ):
                listener.enterTempMissing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempMissing" ):
                listener.exitTempMissing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempMissing" ):
                return visitor.visitTempMissing(self)
            else:
                return visitor.visitChildren(self)


    class TempNumberContext(TemperatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.TemperatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(BerlingerFridgeTagParser.INT)
            else:
                return self.getToken(BerlingerFridgeTagParser.INT, i)
        def DOT(self):
            return self.getToken(BerlingerFridgeTagParser.DOT, 0)
        def SIGN(self):
            return self.getToken(BerlingerFridgeTagParser.SIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempNumber" ):
                listener.enterTempNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempNumber" ):
                listener.exitTempNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempNumber" ):
                return visitor.visitTempNumber(self)
            else:
                return visitor.visitChildren(self)


    class TempSignedContext(TemperatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BerlingerFridgeTagParser.TemperatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIGN(self):
            return self.getToken(BerlingerFridgeTagParser.SIGN, 0)
        def INT(self):
            return self.getToken(BerlingerFridgeTagParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempSigned" ):
                listener.enterTempSigned(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempSigned" ):
                listener.exitTempSigned(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTempSigned" ):
                return visitor.visitTempSigned(self)
            else:
                return visitor.visitChildren(self)



    def temperature(self):

        localctx = BerlingerFridgeTagParser.TemperatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_temperature)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = BerlingerFridgeTagParser.TempNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==61:
                    self.state = 51
                    self.match(BerlingerFridgeTagParser.SIGN)


                self.state = 54
                self.match(BerlingerFridgeTagParser.INT)
                self.state = 55
                self.match(BerlingerFridgeTagParser.DOT)
                self.state = 56
                self.match(BerlingerFridgeTagParser.INT)
                pass

            elif la_ == 2:
                localctx = BerlingerFridgeTagParser.TempSignedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(BerlingerFridgeTagParser.SIGN)
                self.state = 58
                self.match(BerlingerFridgeTagParser.INT)
                pass

            elif la_ == 3:
                localctx = BerlingerFridgeTagParser.TempMissingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(BerlingerFridgeTagParser.MISSING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def textPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BerlingerFridgeTagParser.TextPartContext)
            else:
                return self.getTypedRuleContext(BerlingerFridgeTagParser.TextPartContext,i)


        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_textValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextValue" ):
                listener.enterTextValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextValue" ):
                listener.exitTextValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextValue" ):
                return visitor.visitTextValue(self)
            else:
                return visitor.visitChildren(self)




    def textValue(self):

        localctx = BerlingerFridgeTagParser.TextValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_textValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.textPart()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & 1561) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BerlingerFridgeTagParser.ID, 0)

        def INT(self):
            return self.getToken(BerlingerFridgeTagParser.INT, 0)

        def DOT(self):
            return self.getToken(BerlingerFridgeTagParser.DOT, 0)

        def SIGN(self):
            return self.getToken(BerlingerFridgeTagParser.SIGN, 0)

        def AMPERSAND(self):
            return self.getToken(BerlingerFridgeTagParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return BerlingerFridgeTagParser.RULE_textPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextPart" ):
                listener.enterTextPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextPart" ):
                listener.exitTextPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextPart" ):
                return visitor.visitTextPart(self)
            else:
                return visitor.visitChildren(self)




    def textPart(self):

        localctx = BerlingerFridgeTagParser.TextPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_textPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & 1561) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





