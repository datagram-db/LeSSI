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
        4,1,48,253,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,
        3,1,42,8,1,1,1,1,1,1,1,1,1,4,1,48,8,1,11,1,12,1,49,3,1,52,8,1,1,
        1,5,1,55,8,1,10,1,12,1,58,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,67,
        8,1,10,1,12,1,70,9,1,1,1,3,1,73,8,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,
        81,8,1,11,1,12,1,82,3,1,85,8,1,1,1,5,1,88,8,1,10,1,12,1,91,9,1,3,
        1,93,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,105,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,114,8,2,10,2,12,2,117,9,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,130,8,2,10,2,12,2,133,9,2,
        1,2,1,2,1,2,1,2,1,2,4,2,140,8,2,11,2,12,2,141,1,2,1,2,1,2,4,2,147,
        8,2,11,2,12,2,148,1,2,1,2,3,2,153,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,162,8,3,10,3,12,3,165,9,3,1,3,1,3,1,3,3,3,170,8,3,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,3,4,180,8,4,1,4,1,4,3,4,184,8,4,1,4,1,4,
        3,4,188,8,4,1,4,1,4,3,4,192,8,4,1,5,1,5,4,5,196,8,5,11,5,12,5,197,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,208,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,221,8,7,10,7,12,7,224,9,7,1,7,3,7,227,
        8,7,1,7,3,7,230,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,241,
        8,9,10,9,12,9,244,9,9,1,9,1,9,1,9,1,10,1,10,3,10,251,8,10,1,10,0,
        0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,280,0,25,1,0,0,0,2,92,1,0,0,
        0,4,152,1,0,0,0,6,154,1,0,0,0,8,176,1,0,0,0,10,195,1,0,0,0,12,207,
        1,0,0,0,14,229,1,0,0,0,16,231,1,0,0,0,18,235,1,0,0,0,20,250,1,0,
        0,0,22,23,3,2,1,0,23,24,5,1,0,0,24,26,1,0,0,0,25,22,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,30,5,2,0,0,30,
        41,3,4,2,0,31,37,5,3,0,0,32,33,3,6,3,0,33,34,5,4,0,0,34,36,1,0,0,
        0,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,
        1,0,0,0,39,37,1,0,0,0,40,42,3,6,3,0,41,31,1,0,0,0,41,42,1,0,0,0,
        42,43,1,0,0,0,43,44,5,5,0,0,44,51,3,14,7,0,45,47,5,6,0,0,46,48,3,
        16,8,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,
        52,1,0,0,0,51,45,1,0,0,0,51,52,1,0,0,0,52,56,1,0,0,0,53,55,3,12,
        6,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,93,
        1,0,0,0,58,56,1,0,0,0,59,60,5,7,0,0,60,61,5,8,0,0,61,72,3,4,2,0,
        62,68,5,3,0,0,63,64,3,6,3,0,64,65,5,4,0,0,65,67,1,0,0,0,66,63,1,
        0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,
        68,1,0,0,0,71,73,3,6,3,0,72,62,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,
        0,74,75,5,9,0,0,75,76,3,4,2,0,76,77,5,5,0,0,77,84,3,14,7,0,78,80,
        5,6,0,0,79,81,3,16,8,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,
        82,83,1,0,0,0,83,85,1,0,0,0,84,78,1,0,0,0,84,85,1,0,0,0,85,89,1,
        0,0,0,86,88,3,12,6,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,
        90,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,92,29,1,0,0,0,92,59,1,0,0,
        0,93,3,1,0,0,0,94,95,5,10,0,0,95,96,3,4,2,0,96,97,5,11,0,0,97,153,
        1,0,0,0,98,99,5,38,0,0,99,153,5,12,0,0,100,101,3,20,10,0,101,102,
        3,20,10,0,102,104,3,20,10,0,103,105,3,4,2,0,104,103,1,0,0,0,104,
        105,1,0,0,0,105,153,1,0,0,0,106,107,3,20,10,0,107,108,5,10,0,0,108,
        109,3,4,2,0,109,110,5,11,0,0,110,111,5,41,0,0,111,115,5,13,0,0,112,
        114,3,18,9,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,5,14,0,0,119,
        153,1,0,0,0,120,121,3,20,10,0,121,122,5,10,0,0,122,123,3,4,2,0,123,
        124,5,15,0,0,124,125,3,4,2,0,125,126,5,11,0,0,126,127,5,41,0,0,127,
        131,5,13,0,0,128,130,3,18,9,0,129,128,1,0,0,0,130,133,1,0,0,0,131,
        129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,
        135,5,14,0,0,135,153,1,0,0,0,136,137,5,16,0,0,137,139,3,4,2,0,138,
        140,3,4,2,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,153,1,0,0,0,143,144,5,17,0,0,144,146,3,4,2,0,145,
        147,3,4,2,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,0,0,148,
        149,1,0,0,0,149,153,1,0,0,0,150,151,5,18,0,0,151,153,3,4,2,0,152,
        94,1,0,0,0,152,98,1,0,0,0,152,100,1,0,0,0,152,106,1,0,0,0,152,120,
        1,0,0,0,152,136,1,0,0,0,152,143,1,0,0,0,152,150,1,0,0,0,153,5,1,
        0,0,0,154,155,5,38,0,0,155,169,5,40,0,0,156,157,5,19,0,0,157,163,
        5,20,0,0,158,159,3,8,4,0,159,160,5,4,0,0,160,162,1,0,0,0,161,158,
        1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,
        1,0,0,0,165,163,1,0,0,0,166,167,3,8,4,0,167,168,5,21,0,0,168,170,
        1,0,0,0,169,156,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,
        5,9,0,0,172,173,5,38,0,0,173,174,5,22,0,0,174,175,5,40,0,0,175,7,
        1,0,0,0,176,177,5,40,0,0,177,179,5,23,0,0,178,180,3,10,5,0,179,178,
        1,0,0,0,179,180,1,0,0,0,180,183,1,0,0,0,181,182,5,24,0,0,182,184,
        5,38,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,187,1,0,0,0,185,186,
        5,25,0,0,186,188,5,38,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,191,
        1,0,0,0,189,190,5,26,0,0,190,192,5,38,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,9,1,0,0,0,193,194,5,27,0,0,194,196,5,38,0,0,195,193,
        1,0,0,0,196,197,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,11,1,
        0,0,0,199,200,5,28,0,0,200,208,5,38,0,0,201,202,5,29,0,0,202,203,
        3,4,2,0,203,204,5,30,0,0,204,205,5,38,0,0,205,208,1,0,0,0,206,208,
        5,31,0,0,207,199,1,0,0,0,207,201,1,0,0,0,207,206,1,0,0,0,208,13,
        1,0,0,0,209,210,5,38,0,0,210,211,5,38,0,0,211,230,5,38,0,0,212,213,
        5,32,0,0,213,214,5,38,0,0,214,230,5,38,0,0,215,216,5,33,0,0,216,
        222,5,34,0,0,217,218,3,14,7,0,218,219,5,15,0,0,219,221,1,0,0,0,220,
        217,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,
        226,1,0,0,0,224,222,1,0,0,0,225,227,3,14,7,0,226,225,1,0,0,0,226,
        227,1,0,0,0,227,228,1,0,0,0,228,230,5,35,0,0,229,209,1,0,0,0,229,
        212,1,0,0,0,229,215,1,0,0,0,230,15,1,0,0,0,231,232,5,38,0,0,232,
        233,5,36,0,0,233,234,5,38,0,0,234,17,1,0,0,0,235,236,5,38,0,0,236,
        242,5,23,0,0,237,238,3,4,2,0,238,239,5,15,0,0,239,241,1,0,0,0,240,
        237,1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,
        245,1,0,0,0,244,242,1,0,0,0,245,246,3,4,2,0,246,247,5,37,0,0,247,
        19,1,0,0,0,248,251,5,38,0,0,249,251,5,39,0,0,250,248,1,0,0,0,250,
        249,1,0,0,0,251,21,1,0,0,0,31,27,37,41,49,51,56,68,72,82,84,89,92,
        104,115,131,141,148,152,163,169,179,183,187,191,197,207,222,226,
        229,242,250
    ]

class parmenides_tboxParser ( Parser ):

    grammarFileName = "parmenides_tbox.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'UPDATE'", "'where'", "'and'", 
                     "'over'", "'replace'", "'INVENT'", "'from'", "'as'", 
                     "'('", "')'", "'?'", "'{'", "'}'", "','", "'AND'", 
                     "'OR'", "'NOT'", "'with'", "'<'", "'>'", "'withparents'", 
                     "':'", "'attr'", "'withval'", "'asname'", "'/'", "'rem'", 
                     "'add'", "'to'", "'with-properties'", "'isa'", "'all'", 
                     "'['", "']'", "'->'", "'.'", "<INVALID>", "'none'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NULL", "INTEGER", 
                      "NUMBER", "SPACE", "COMMENT", "LINE_COMMENT", "DecimalFloatingConstant", 
                      "FractionalConstant", "ExponentPart", "DIGIT" ]

    RULE_parmenides_tbox = 0
    RULE_rule = 1
    RULE_formula = 2
    RULE_sentence_match = 3
    RULE_field_match = 4
    RULE_data_match_path = 5
    RULE_operations = 6
    RULE_ontology_query = 7
    RULE_replacement_pair = 8
    RULE_key_values = 9
    RULE_opt_string = 10

    ruleNames =  [ "parmenides_tbox", "rule", "formula", "sentence_match", 
                   "field_match", "data_match_path", "operations", "ontology_query", 
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
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    STRING=38
    NULL=39
    INTEGER=40
    NUMBER=41
    SPACE=42
    COMMENT=43
    LINE_COMMENT=44
    DecimalFloatingConstant=45
    FractionalConstant=46
    ExponentPart=47
    DIGIT=48

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.rule_()
                self.state = 23
                self.match(parmenides_tboxParser.T__0)
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==7):
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

        def sentence_match(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Sentence_matchContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Sentence_matchContext,i)

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

        def sentence_match(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Sentence_matchContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Sentence_matchContext,i)

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
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = parmenides_tboxParser.SubstitutionsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(parmenides_tboxParser.T__1)
                self.state = 30
                self.formula()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 31
                    self.match(parmenides_tboxParser.T__2)
                    self.state = 37
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 32
                            self.sentence_match()
                            self.state = 33
                            self.match(parmenides_tboxParser.T__3) 
                        self.state = 39
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    self.state = 40
                    self.sentence_match()


                self.state = 43
                self.match(parmenides_tboxParser.T__4)
                self.state = 44
                self.ontology_query()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 45
                    self.match(parmenides_tboxParser.T__5)
                    self.state = 47 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 46
                        self.replacement_pair()
                        self.state = 49 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==38):
                            break



                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0):
                    self.state = 53
                    self.operations()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [7]:
                localctx = parmenides_tboxParser.InventionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(parmenides_tboxParser.T__6)
                self.state = 60
                self.match(parmenides_tboxParser.T__7)
                self.state = 61
                self.formula()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 62
                    self.match(parmenides_tboxParser.T__2)
                    self.state = 68
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 63
                            self.sentence_match()
                            self.state = 64
                            self.match(parmenides_tboxParser.T__3) 
                        self.state = 70
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    self.state = 71
                    self.sentence_match()


                self.state = 74
                self.match(parmenides_tboxParser.T__8)
                self.state = 75
                self.formula()
                self.state = 76
                self.match(parmenides_tboxParser.T__4)
                self.state = 77
                self.ontology_query()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 78
                    self.match(parmenides_tboxParser.T__5)
                    self.state = 80 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 79
                        self.replacement_pair()
                        self.state = 82 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==38):
                            break



                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0):
                    self.state = 86
                    self.operations()
                    self.state = 91
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = parmenides_tboxParser.FparenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(parmenides_tboxParser.T__9)
                self.state = 95
                self.formula()
                self.state = 96
                self.match(parmenides_tboxParser.T__10)
                pass

            elif la_ == 2:
                localctx = parmenides_tboxParser.Rw_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(parmenides_tboxParser.STRING)
                self.state = 99
                self.match(parmenides_tboxParser.T__11)
                pass

            elif la_ == 3:
                localctx = parmenides_tboxParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                localctx.name = self.opt_string()
                self.state = 101
                localctx.type_ = self.opt_string()
                self.state = 102
                localctx.specification = self.opt_string()
                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 103
                    localctx.cop = self.formula()


                pass

            elif la_ == 4:
                localctx = parmenides_tboxParser.Unary_predicateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                localctx.rel = self.opt_string()
                self.state = 107
                self.match(parmenides_tboxParser.T__9)
                self.state = 108
                localctx.arg = self.formula()
                self.state = 109
                self.match(parmenides_tboxParser.T__10)
                self.state = 110
                localctx.score = self.match(parmenides_tboxParser.NUMBER)
                self.state = 111
                self.match(parmenides_tboxParser.T__12)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 112
                    self.key_values()
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 118
                self.match(parmenides_tboxParser.T__13)
                pass

            elif la_ == 5:
                localctx = parmenides_tboxParser.Binary_predicateContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                localctx.rel = self.opt_string()
                self.state = 121
                self.match(parmenides_tboxParser.T__9)
                self.state = 122
                localctx.src = self.formula()
                self.state = 123
                self.match(parmenides_tboxParser.T__14)
                self.state = 124
                localctx.dst = self.formula()
                self.state = 125
                self.match(parmenides_tboxParser.T__10)
                self.state = 126
                localctx.score = self.match(parmenides_tboxParser.NUMBER)
                self.state = 127
                self.match(parmenides_tboxParser.T__12)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 128
                    self.key_values()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 134
                self.match(parmenides_tboxParser.T__13)
                pass

            elif la_ == 6:
                localctx = parmenides_tboxParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.match(parmenides_tboxParser.T__15)
                self.state = 137
                self.formula()
                self.state = 139 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 138
                        self.formula()

                    else:
                        raise NoViableAltException(self)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass

            elif la_ == 7:
                localctx = parmenides_tboxParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.match(parmenides_tboxParser.T__16)
                self.state = 144
                self.formula()
                self.state = 146 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 145
                        self.formula()

                    else:
                        raise NoViableAltException(self)
                    self.state = 148 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 8:
                localctx = parmenides_tboxParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.match(parmenides_tboxParser.T__17)
                self.state = 151
                self.formula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentence_matchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.relname = None # Token
            self.n = None # Token
            self.as_name = None # Token
            self.parents = None # Token

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.INTEGER)
            else:
                return self.getToken(parmenides_tboxParser.INTEGER, i)

        def field_match(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parmenides_tboxParser.Field_matchContext)
            else:
                return self.getTypedRuleContext(parmenides_tboxParser.Field_matchContext,i)


        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_sentence_match

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence_match" ):
                listener.enterSentence_match(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence_match" ):
                listener.exitSentence_match(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence_match" ):
                return visitor.visitSentence_match(self)
            else:
                return visitor.visitChildren(self)




    def sentence_match(self):

        localctx = parmenides_tboxParser.Sentence_matchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sentence_match)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            localctx.relname = self.match(parmenides_tboxParser.STRING)
            self.state = 155
            localctx.n = self.match(parmenides_tboxParser.INTEGER)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 156
                self.match(parmenides_tboxParser.T__18)
                self.state = 157
                self.match(parmenides_tboxParser.T__19)
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 158
                        self.field_match()
                        self.state = 159
                        self.match(parmenides_tboxParser.T__3) 
                    self.state = 165
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 166
                self.field_match()
                self.state = 167
                self.match(parmenides_tboxParser.T__20)


            self.state = 171
            self.match(parmenides_tboxParser.T__8)
            self.state = 172
            localctx.as_name = self.match(parmenides_tboxParser.STRING)
            self.state = 173
            self.match(parmenides_tboxParser.T__21)
            self.state = 174
            localctx.parents = self.match(parmenides_tboxParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_matchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.n = None # Token
            self.attr = None # Token
            self.withval = None # Token
            self.asname = None # Token

        def INTEGER(self):
            return self.getToken(parmenides_tboxParser.INTEGER, 0)

        def data_match_path(self):
            return self.getTypedRuleContext(parmenides_tboxParser.Data_match_pathContext,0)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_field_match

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_match" ):
                listener.enterField_match(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_match" ):
                listener.exitField_match(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_match" ):
                return visitor.visitField_match(self)
            else:
                return visitor.visitChildren(self)




    def field_match(self):

        localctx = parmenides_tboxParser.Field_matchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field_match)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            localctx.n = self.match(parmenides_tboxParser.INTEGER)
            self.state = 177
            self.match(parmenides_tboxParser.T__22)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 178
                self.data_match_path()


            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 181
                self.match(parmenides_tboxParser.T__23)
                self.state = 182
                localctx.attr = self.match(parmenides_tboxParser.STRING)


            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 185
                self.match(parmenides_tboxParser.T__24)
                self.state = 186
                localctx.withval = self.match(parmenides_tboxParser.STRING)


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 189
                self.match(parmenides_tboxParser.T__25)
                self.state = 190
                localctx.asname = self.match(parmenides_tboxParser.STRING)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_match_pathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(parmenides_tboxParser.STRING)
            else:
                return self.getToken(parmenides_tboxParser.STRING, i)

        def getRuleIndex(self):
            return parmenides_tboxParser.RULE_data_match_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_match_path" ):
                listener.enterData_match_path(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_match_path" ):
                listener.exitData_match_path(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_match_path" ):
                return visitor.visitData_match_path(self)
            else:
                return visitor.visitChildren(self)




    def data_match_path(self):

        localctx = parmenides_tboxParser.Data_match_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_match_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 193
                self.match(parmenides_tboxParser.T__26)
                self.state = 194
                self.match(parmenides_tboxParser.STRING)
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==27):
                    break

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
        self.enterRule(localctx, 12, self.RULE_operations)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = parmenides_tboxParser.RemoveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(parmenides_tboxParser.T__27)
                self.state = 200
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [29]:
                localctx = parmenides_tboxParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(parmenides_tboxParser.T__28)
                self.state = 202
                self.formula()
                self.state = 203
                self.match(parmenides_tboxParser.T__29)
                self.state = 204
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [31]:
                localctx = parmenides_tboxParser.All_propertiesContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(parmenides_tboxParser.T__30)
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
        self.enterRule(localctx, 14, self.RULE_ontology_query)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                localctx = parmenides_tboxParser.Edge_matchContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                localctx.src = self.match(parmenides_tboxParser.STRING)
                self.state = 210
                localctx.edge = self.match(parmenides_tboxParser.STRING)
                self.state = 211
                localctx.dst = self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [32]:
                localctx = parmenides_tboxParser.Isa_matchContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(parmenides_tboxParser.T__31)
                self.state = 213
                localctx.src = self.match(parmenides_tboxParser.STRING)
                self.state = 214
                localctx.dst = self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [33]:
                localctx = parmenides_tboxParser.All_queriesContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.match(parmenides_tboxParser.T__32)
                self.state = 216
                self.match(parmenides_tboxParser.T__33)
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 217
                        self.ontology_query()
                        self.state = 218
                        self.match(parmenides_tboxParser.T__14) 
                    self.state = 224
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 287762808832) != 0):
                    self.state = 225
                    self.ontology_query()


                self.state = 228
                self.match(parmenides_tboxParser.T__34)
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
        self.enterRule(localctx, 16, self.RULE_replacement_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            localctx.src = self.match(parmenides_tboxParser.STRING)
            self.state = 232
            self.match(parmenides_tboxParser.T__35)
            self.state = 233
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
        self.enterRule(localctx, 18, self.RULE_key_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(parmenides_tboxParser.STRING)
            self.state = 236
            self.match(parmenides_tboxParser.T__22)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.formula()
                    self.state = 238
                    self.match(parmenides_tboxParser.T__14) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 245
            self.formula()
            self.state = 246
            self.match(parmenides_tboxParser.T__36)
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
        self.enterRule(localctx, 20, self.RULE_opt_string)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                localctx = parmenides_tboxParser.ValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(parmenides_tboxParser.STRING)
                pass
            elif token in [39]:
                localctx = parmenides_tboxParser.NoneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 249
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





