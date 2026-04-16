# Generated from izqNormal.g4 by ANTLR 4.13.2
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
        4,1,8,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,3,
        3,3,43,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,45,0,8,1,0,0,0,2,11,1,0,0,0,
        4,25,1,0,0,0,6,42,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,
        11,12,6,1,-1,0,12,13,3,4,2,0,13,22,1,0,0,0,14,15,10,3,0,0,15,16,
        5,1,0,0,16,21,3,4,2,0,17,18,10,2,0,0,18,19,5,2,0,0,19,21,3,4,2,0,
        20,14,1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,
        0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,26,6,2,-1,0,26,27,3,6,3,0,27,
        36,1,0,0,0,28,29,10,3,0,0,29,30,5,3,0,0,30,35,3,6,3,0,31,32,10,2,
        0,0,32,33,5,4,0,0,33,35,3,6,3,0,34,28,1,0,0,0,34,31,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,39,
        43,5,5,0,0,40,41,5,2,0,0,41,43,5,5,0,0,42,39,1,0,0,0,42,40,1,0,0,
        0,43,7,1,0,0,0,5,20,22,34,36,42
    ]

class izqNormalParser ( Parser ):

    grammarFileName = "izqNormal.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "SUM", "RES", "MUL", "DIV", "NUM", "DECIMAL", 
                      "ENTERO", "WS" ]

    RULE_programa = 0
    RULE_expresion = 1
    RULE_factor = 2
    RULE_term = 3

    ruleNames =  [ "programa", "expresion", "factor", "term" ]

    EOF = Token.EOF
    SUM=1
    RES=2
    MUL=3
    DIV=4
    NUM=5
    DECIMAL=6
    ENTERO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(izqNormalParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(izqNormalParser.EOF, 0)

        def getRuleIndex(self):
            return izqNormalParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = izqNormalParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expresion(0)
            self.state = 9
            self.match(izqNormalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(izqNormalParser.FactorContext,0)


        def expresion(self):
            return self.getTypedRuleContext(izqNormalParser.ExpresionContext,0)


        def SUM(self):
            return self.getToken(izqNormalParser.SUM, 0)

        def RES(self):
            return self.getToken(izqNormalParser.RES, 0)

        def getRuleIndex(self):
            return izqNormalParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = izqNormalParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = izqNormalParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.match(izqNormalParser.SUM)
                        self.state = 16
                        self.factor(0)
                        pass

                    elif la_ == 2:
                        localctx = izqNormalParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        self.match(izqNormalParser.RES)
                        self.state = 19
                        self.factor(0)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(izqNormalParser.TermContext,0)


        def factor(self):
            return self.getTypedRuleContext(izqNormalParser.FactorContext,0)


        def MUL(self):
            return self.getToken(izqNormalParser.MUL, 0)

        def DIV(self):
            return self.getToken(izqNormalParser.DIV, 0)

        def getRuleIndex(self):
            return izqNormalParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = izqNormalParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = izqNormalParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(izqNormalParser.MUL)
                        self.state = 30
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = izqNormalParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(izqNormalParser.DIV)
                        self.state = 33
                        self.term()
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(izqNormalParser.NUM, 0)

        def RES(self):
            return self.getToken(izqNormalParser.RES, 0)

        def getRuleIndex(self):
            return izqNormalParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = izqNormalParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(izqNormalParser.NUM)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(izqNormalParser.RES)
                self.state = 41
                self.match(izqNormalParser.NUM)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expresion_sempred
        self._predicates[2] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




