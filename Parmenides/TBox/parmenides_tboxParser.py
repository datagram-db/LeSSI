# Generated from Parmenides/TBox/parmenides_tbox.g4 by ANTLR 4.13.1
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
        4,1,33,172,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,1,4,1,30,8,1,11,1,12,1,31,3,1,34,8,1,1,1,5,1,37,8,1,10,1,12,
        1,40,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,50,8,1,11,1,12,1,51,
        3,1,54,8,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,3,1,62,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,74,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,99,8,2,10,2,12,2,102,9,2,1,2,1,2,1,2,1,2,1,2,4,2,
        109,8,2,11,2,12,2,110,1,2,1,2,1,2,4,2,116,8,2,11,2,12,2,117,1,2,
        1,2,3,2,122,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,132,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,143,8,4,10,4,12,4,146,9,4,1,
        4,3,4,149,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,160,8,6,10,
        6,12,6,163,9,6,1,6,1,6,1,6,1,7,1,7,3,7,170,8,7,1,7,0,0,8,0,2,4,6,
        8,10,12,14,0,0,190,0,19,1,0,0,0,2,61,1,0,0,0,4,121,1,0,0,0,6,131,
        1,0,0,0,8,148,1,0,0,0,10,150,1,0,0,0,12,154,1,0,0,0,14,169,1,0,0,
        0,16,17,3,2,1,0,17,18,5,1,0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,
        1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,24,5,2,0,0,24,
        25,3,4,2,0,25,26,5,3,0,0,26,33,3,8,4,0,27,29,5,4,0,0,28,30,3,10,
        5,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,
        1,0,0,0,33,27,1,0,0,0,33,34,1,0,0,0,34,38,1,0,0,0,35,37,3,6,3,0,
        36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,62,1,
        0,0,0,40,38,1,0,0,0,41,42,5,5,0,0,42,43,3,4,2,0,43,44,5,6,0,0,44,
        45,3,4,2,0,45,46,5,3,0,0,46,53,3,8,4,0,47,49,5,4,0,0,48,50,3,10,
        5,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,
        1,0,0,0,53,47,1,0,0,0,53,54,1,0,0,0,54,58,1,0,0,0,55,57,3,6,3,0,
        56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,62,1,
        0,0,0,60,58,1,0,0,0,61,23,1,0,0,0,61,41,1,0,0,0,62,3,1,0,0,0,63,
        64,5,7,0,0,64,65,3,4,2,0,65,66,5,8,0,0,66,122,1,0,0,0,67,68,5,27,
        0,0,68,122,5,9,0,0,69,70,3,14,7,0,70,71,3,14,7,0,71,73,3,14,7,0,
        72,74,3,4,2,0,73,72,1,0,0,0,73,74,1,0,0,0,74,122,1,0,0,0,75,76,3,
        14,7,0,76,77,5,7,0,0,77,78,3,4,2,0,78,79,5,8,0,0,79,80,5,29,0,0,
        80,84,5,10,0,0,81,83,3,12,6,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,
        1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,5,11,0,0,
        88,122,1,0,0,0,89,90,3,14,7,0,90,91,5,7,0,0,91,92,3,4,2,0,92,93,
        5,12,0,0,93,94,3,4,2,0,94,95,5,8,0,0,95,96,5,29,0,0,96,100,5,10,
        0,0,97,99,3,12,6,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,
        101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,11,0,0,104,
        122,1,0,0,0,105,106,5,13,0,0,106,108,3,4,2,0,107,109,3,4,2,0,108,
        107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,
        122,1,0,0,0,112,113,5,14,0,0,113,115,3,4,2,0,114,116,3,4,2,0,115,
        114,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,
        122,1,0,0,0,119,120,5,15,0,0,120,122,3,4,2,0,121,63,1,0,0,0,121,
        67,1,0,0,0,121,69,1,0,0,0,121,75,1,0,0,0,121,89,1,0,0,0,121,105,
        1,0,0,0,121,112,1,0,0,0,121,119,1,0,0,0,122,5,1,0,0,0,123,124,5,
        16,0,0,124,132,5,27,0,0,125,126,5,17,0,0,126,127,3,4,2,0,127,128,
        5,18,0,0,128,129,5,27,0,0,129,132,1,0,0,0,130,132,5,19,0,0,131,123,
        1,0,0,0,131,125,1,0,0,0,131,130,1,0,0,0,132,7,1,0,0,0,133,134,5,
        27,0,0,134,135,5,27,0,0,135,149,5,27,0,0,136,137,5,20,0,0,137,138,
        5,27,0,0,138,149,5,27,0,0,139,140,5,21,0,0,140,144,5,22,0,0,141,
        143,3,8,4,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,
        145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,149,5,23,0,0,148,
        133,1,0,0,0,148,136,1,0,0,0,148,139,1,0,0,0,149,9,1,0,0,0,150,151,
        5,27,0,0,151,152,5,24,0,0,152,153,5,27,0,0,153,11,1,0,0,0,154,155,
        5,27,0,0,155,161,5,25,0,0,156,157,3,4,2,0,157,158,5,12,0,0,158,160,
        1,0,0,0,159,156,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,165,3,4,2,0,165,166,
        5,26,0,0,166,13,1,0,0,0,167,170,5,27,0,0,168,170,5,28,0,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,15,1,0,0,0,19,21,31,33,38,51,53,58,61,
        73,84,100,110,117,121,131,144,148,161,169
    ]

class parmenides_tboxParser ( Parser ):

    grammarFileName = "parmenides_tbox.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'UPDATE'", "'over'", "'replace'", 
                     "'INVENT'", "'from'", "'('", "')'", "'?'", "'{'", "'}'", 
                     "','", "'AND'", "'OR'", "'NOT'", "'rem'", "'add'", 
                     "'to'", "'with-properties'", "'isa'", "'all'", "'['", 
                     "']'", "'->'", "':'", "'.'", "<INVALID>", "'none'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NULL", 
                      "NUMBER", "INTEGER", "SPACE", "COMMENT", "LINE_COMMENT" ]

    RULE_parmenides_tbox = 0
    RULE_rule = 1
    RULE_formula = 2
    RULE_operations = 3
    RULE_ontology_query = 4
    RULE_replacement_pair = 5
    RULE_key_values = 6
    RULE_opt_string = 7

    ruleNames =  [ "parmenides_tbox", "rule", "formula", "operations", "ontology_query", 
                   "replacement_pair", "key_values", "opt_string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    STRING=27
    NULL=28
    NUMBER=29
    INTEGER=30
    SPACE=31
    COMMENT=32
    LINE_COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Parmenides_tboxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.RuleContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.RuleContext,i)


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_parmenides_tbox

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParmenides_tbox" ):
                listener.enterParmenides_tbox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParmenides_tbox" ):
                listener.exitParmenides_tbox(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParmenides_tbox" ):
                return visitor.visitParmenides_tbox(self)
            else:
                return visitor.visitChildren(self)




    def parmenides_tbox(self):

        localctx = parmenides_tboxParser.Parmenides_tboxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parmenides_tbox)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.rule_()
                self.state = 17
                self.match(parmenides_tboxParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_rule

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubstitutionsContext(RuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.RuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)

        def ontology_query(self):
            return self.getTypedRuleContext(parmenides_tboxParser.Ontology_queryContext,0)

        def operations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.OperationsContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.OperationsContext,i)

        def replacement_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Replacement_pairContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Replacement_pairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstitutions" ):
                listener.enterSubstitutions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstitutions" ):
                listener.exitSubstitutions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstitutions" ):
                return visitor.visitSubstitutions(self)
            else:
                return visitor.visitChildren(self)


    class InventionContext(RuleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.RuleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.FormulaContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,i)

        def ontology_query(self):
            return self.getTypedRuleContext(parmenides_tboxParser.Ontology_queryContext,0)

        def operations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.OperationsContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.OperationsContext,i)

        def replacement_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Replacement_pairContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Replacement_pairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvention" ):
                listener.enterInvention(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvention" ):
                listener.exitInvention(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvention" ):
                return visitor.visitInvention(self)
            else:
                return visitor.visitChildren(self)



    def rule_(self):

        localctx = parmenides_tboxParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = parmenides_tboxParser.SubstitutionsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(parmenides_tboxParser.T__1)
                self.state = 24
                self.formula()
                self.state = 25
                self.match(parmenides_tboxParser.T__2)
                self.state = 26
                self.ontology_query()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 27
                    self.match(parmenides_tboxParser.T__3)
                    self.state = 29 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 28
                        self.replacement_pair()
                        self.state = 31 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==27):
                            break



                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 720896) != 0):
                    self.state = 35
                    self.operations()
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [5]:
                localctx = parmenides_tboxParser.InventionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(parmenides_tboxParser.T__4)
                self.state = 42
                self.formula()
                self.state = 43
                self.match(parmenides_tboxParser.T__5)
                self.state = 44
                self.formula()
                self.state = 45
                self.match(parmenides_tboxParser.T__2)
                self.state = 46
                self.ontology_query()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 47
                    self.match(parmenides_tboxParser.T__3)
                    self.state = 49 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 48
                        self.replacement_pair()
                        self.state = 51 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==27):
                            break



                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 720896) != 0):
                    self.state = 55
                    self.operations()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FparenContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFparen" ):
                listener.enterFparen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFparen" ):
                listener.exitFparen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFparen" ):
                return visitor.visitFparen(self)
            else:
                return visitor.visitChildren(self)


    class Unary_predicateContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.rel = None # Opt_stringContext
            self.arg = None # FormulaContext
            self.score = None # Token
            self.copyFrom(ctx)

        def opt_string(self):
            return self.getTypedRuleContext(parmenides_tboxParser.Opt_stringContext,0)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)

        def NUMBER(self):
            return self.getToken(parmenides_tboxParser.NUMBER, 0)
        def key_values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Key_valuesContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Key_valuesContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_predicate" ):
                listener.enterUnary_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_predicate" ):
                listener.exitUnary_predicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_predicate" ):
                return visitor.visitUnary_predicate(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class Rw_variableContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(parmenides_tboxParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRw_variable" ):
                listener.enterRw_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRw_variable" ):
                listener.exitRw_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRw_variable" ):
                return visitor.visitRw_variable(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.FormulaContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.FormulaContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.name = None # Opt_stringContext
            self.type_ = None # Opt_stringContext
            self.specification = None # Opt_stringContext
            self.cop = None # FormulaContext
            self.copyFrom(ctx)

        def opt_string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Opt_stringContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Opt_stringContext,i)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class Binary_predicateContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.FormulaContext
            super().__init__(parser)
            self.rel = None # Opt_stringContext
            self.src = None # FormulaContext
            self.dst = None # FormulaContext
            self.score = None # Token
            self.copyFrom(ctx)

        def opt_string(self):
            return self.getTypedRuleContext(parmenides_tboxParser.Opt_stringContext,0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.FormulaContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,i)

        def NUMBER(self):
            return self.getToken(parmenides_tboxParser.NUMBER, 0)
        def key_values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Key_valuesContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Key_valuesContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_predicate" ):
                listener.enterBinary_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_predicate" ):
                listener.exitBinary_predicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_predicate" ):
                return visitor.visitBinary_predicate(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = parmenides_tboxParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = parmenides_tboxParser.FparenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(parmenides_tboxParser.T__6)
                self.state = 64
                self.formula()
                self.state = 65
                self.match(parmenides_tboxParser.T__7)
                pass

            elif la_ == 2:
                localctx = parmenides_tboxParser.Rw_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(parmenides_tboxParser.STRING)
                self.state = 68
                self.match(parmenides_tboxParser.T__8)
                pass

            elif la_ == 3:
                localctx = parmenides_tboxParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                localctx.name = self.opt_string()
                self.state = 70
                localctx.type_ = self.opt_string()
                self.state = 71
                localctx.specification = self.opt_string()
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 72
                    localctx.cop = self.formula()


                pass

            elif la_ == 4:
                localctx = parmenides_tboxParser.Unary_predicateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                localctx.rel = self.opt_string()
                self.state = 76
                self.match(parmenides_tboxParser.T__6)
                self.state = 77
                localctx.arg = self.formula()
                self.state = 78
                self.match(parmenides_tboxParser.T__7)
                self.state = 79
                localctx.score = self.match(parmenides_tboxParser.NUMBER)
                self.state = 80
                self.match(parmenides_tboxParser.T__9)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 81
                    self.key_values()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(parmenides_tboxParser.T__10)
                pass

            elif la_ == 5:
                localctx = parmenides_tboxParser.Binary_predicateContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                localctx.rel = self.opt_string()
                self.state = 90
                self.match(parmenides_tboxParser.T__6)
                self.state = 91
                localctx.src = self.formula()
                self.state = 92
                self.match(parmenides_tboxParser.T__11)
                self.state = 93
                localctx.dst = self.formula()
                self.state = 94
                self.match(parmenides_tboxParser.T__7)
                self.state = 95
                localctx.score = self.match(parmenides_tboxParser.NUMBER)
                self.state = 96
                self.match(parmenides_tboxParser.T__9)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 97
                    self.key_values()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(parmenides_tboxParser.T__10)
                pass

            elif la_ == 6:
                localctx = parmenides_tboxParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.match(parmenides_tboxParser.T__12)
                self.state = 106
                self.formula()
                self.state = 108 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 107
                        self.formula()

                    else:
                        raise NoViableAltException(self)
                    self.state = 110 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass

            elif la_ == 7:
                localctx = parmenides_tboxParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 112
                self.match(parmenides_tboxParser.T__13)
                self.state = 113
                self.formula()
                self.state = 115 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 114
                        self.formula()

                    else:
                        raise NoViableAltException(self)
                    self.state = 117 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 8:
                localctx = parmenides_tboxParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 119
                self.match(parmenides_tboxParser.T__14)
                self.state = 120
                self.formula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_operations

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(OperationsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.OperationsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,0)

        def STRING(self):
            return self.getToken(parmenides_tboxParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class All_propertiesContext(OperationsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.OperationsContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_properties" ):
                listener.enterAll_properties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_properties" ):
                listener.exitAll_properties(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_properties" ):
                return visitor.visitAll_properties(self)
            else:
                return visitor.visitChildren(self)


    class RemoveContext(OperationsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.OperationsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(parmenides_tboxParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove" ):
                listener.enterRemove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove" ):
                listener.exitRemove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemove" ):
                return visitor.visitRemove(self)
            else:
                return visitor.visitChildren(self)



    def operations(self):

        localctx = parmenides_tboxParser.OperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operations)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = parmenides_tboxParser.RemoveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(parmenides_tboxParser.T__15)
                self.state = 124
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [17]:
                localctx = parmenides_tboxParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(parmenides_tboxParser.T__16)
                self.state = 126
                self.formula()
                self.state = 127
                self.match(parmenides_tboxParser.T__17)
                self.state = 128
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [19]:
                localctx = parmenides_tboxParser.All_propertiesContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(parmenides_tboxParser.T__18)
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


    class Ontology_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_ontology_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Isa_matchContext(Ontology_queryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.Ontology_queryContext
            super().__init__(parser)
            self.src = None # Token
            self.dst = None # Token
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsa_match" ):
                listener.enterIsa_match(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsa_match" ):
                listener.exitIsa_match(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsa_match" ):
                return visitor.visitIsa_match(self)
            else:
                return visitor.visitChildren(self)


    class All_queriesContext(Ontology_queryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.Ontology_queryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ontology_query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Ontology_queryContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Ontology_queryContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_queries" ):
                listener.enterAll_queries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_queries" ):
                listener.exitAll_queries(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_queries" ):
                return visitor.visitAll_queries(self)
            else:
                return visitor.visitChildren(self)


    class Edge_matchContext(Ontology_queryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.Ontology_queryContext
            super().__init__(parser)
            self.src = None # Token
            self.edge = None # Token
            self.dst = None # Token
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_match" ):
                listener.enterEdge_match(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_match" ):
                listener.exitEdge_match(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge_match" ):
                return visitor.visitEdge_match(self)
            else:
                return visitor.visitChildren(self)



    def ontology_query(self):

        localctx = parmenides_tboxParser.Ontology_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ontology_query)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = parmenides_tboxParser.Edge_matchContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                localctx.src = self.match(parmenides_tboxParser.STRING)
                self.state = 134
                localctx.edge = self.match(parmenides_tboxParser.STRING)
                self.state = 135
                localctx.dst = self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [20]:
                localctx = parmenides_tboxParser.Isa_matchContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(parmenides_tboxParser.T__19)
                self.state = 137
                localctx.src = self.match(parmenides_tboxParser.STRING)
                self.state = 138
                localctx.dst = self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [21]:
                localctx = parmenides_tboxParser.All_queriesContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(parmenides_tboxParser.T__20)
                self.state = 140
                self.match(parmenides_tboxParser.T__21)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137363456) != 0):
                    self.state = 141
                    self.ontology_query()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                self.match(parmenides_tboxParser.T__22)
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


    class Replacement_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.src = None # Token
            self.dst = None # Token

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_replacement_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplacement_pair" ):
                listener.enterReplacement_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplacement_pair" ):
                listener.exitReplacement_pair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplacement_pair" ):
                return visitor.visitReplacement_pair(self)
            else:
                return visitor.visitChildren(self)




    def replacement_pair(self):

        localctx = parmenides_tboxParser.Replacement_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_replacement_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx.src = self.match(parmenides_tboxParser.STRING)
            self.state = 151
            self.match(parmenides_tboxParser.T__23)
            self.state = 152
            localctx.dst = self.match(parmenides_tboxParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_valuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(parmenides_tboxParser.STRING, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.FormulaContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.FormulaContext,i)


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_key_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_values" ):
                listener.enterKey_values(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_values" ):
                listener.exitKey_values(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_values" ):
                return visitor.visitKey_values(self)
            else:
                return visitor.visitChildren(self)




    def key_values(self):

        localctx = parmenides_tboxParser.Key_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_key_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(parmenides_tboxParser.STRING)
            self.state = 155
            self.match(parmenides_tboxParser.T__24)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self.formula()
                    self.state = 157
                    self.match(parmenides_tboxParser.T__11) 
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 164
            self.formula()
            self.state = 165
            self.match(parmenides_tboxParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_opt_string

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NoneContext(Opt_stringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.Opt_stringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(parmenides_tboxParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNone" ):
                listener.enterNone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNone" ):
                listener.exitNone(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNone" ):
                return visitor.visitNone(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(Opt_stringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a parmenides_tboxParser.Opt_stringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(parmenides_tboxParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)



    def opt_string(self):

        localctx = parmenides_tboxParser.Opt_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opt_string)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = parmenides_tboxParser.ValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [28]:
                localctx = parmenides_tboxParser.NoneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(parmenides_tboxParser.NULL)
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





