# Generated from BerlingerFridgeTag.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BerlingerFridgeTagParser import BerlingerFridgeTagParser
else:
    from BerlingerFridgeTagParser import BerlingerFridgeTagParser

# This class defines a complete generic visitor for a parse tree produced by BerlingerFridgeTagParser.

class BerlingerFridgeTagVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BerlingerFridgeTagParser#line.
    def visitLine(self, ctx:BerlingerFridgeTagParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#KeyValue.
    def visitKeyValue(self, ctx:BerlingerFridgeTagParser.KeyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#KnownKeyRef.
    def visitKnownKeyRef(self, ctx:BerlingerFridgeTagParser.KnownKeyRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#IndexKey.
    def visitIndexKey(self, ctx:BerlingerFridgeTagParser.IndexKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#GenericKey.
    def visitGenericKey(self, ctx:BerlingerFridgeTagParser.GenericKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#knownKey.
    def visitKnownKey(self, ctx:BerlingerFridgeTagParser.KnownKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TempVal.
    def visitTempVal(self, ctx:BerlingerFridgeTagParser.TempValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#DateTimeVal.
    def visitDateTimeVal(self, ctx:BerlingerFridgeTagParser.DateTimeValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#DateVal.
    def visitDateVal(self, ctx:BerlingerFridgeTagParser.DateValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TimeVal.
    def visitTimeVal(self, ctx:BerlingerFridgeTagParser.TimeValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#IntVal.
    def visitIntVal(self, ctx:BerlingerFridgeTagParser.IntValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#HexVal.
    def visitHexVal(self, ctx:BerlingerFridgeTagParser.HexValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TextVal.
    def visitTextVal(self, ctx:BerlingerFridgeTagParser.TextValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TempNumber.
    def visitTempNumber(self, ctx:BerlingerFridgeTagParser.TempNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TempSigned.
    def visitTempSigned(self, ctx:BerlingerFridgeTagParser.TempSignedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#TempMissing.
    def visitTempMissing(self, ctx:BerlingerFridgeTagParser.TempMissingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#textValue.
    def visitTextValue(self, ctx:BerlingerFridgeTagParser.TextValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BerlingerFridgeTagParser#textPart.
    def visitTextPart(self, ctx:BerlingerFridgeTagParser.TextPartContext):
        return self.visitChildren(ctx)



del BerlingerFridgeTagParser