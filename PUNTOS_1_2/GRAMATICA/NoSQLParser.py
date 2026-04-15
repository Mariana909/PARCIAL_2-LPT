# Generated from NoSQL.g4 by ANTLR 4.13.2
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
        4,1,17,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,5,6,60,8,6,10,6,12,6,63,9,6,3,6,65,8,6,1,7,1,7,1,7,5,7,70,8,
        7,10,7,12,7,73,9,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,84,8,
        9,1,10,1,10,1,10,1,10,5,10,90,8,10,10,10,12,10,93,9,10,1,10,1,10,
        1,10,1,10,3,10,99,8,10,1,11,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,
        10,12,14,16,18,20,22,0,0,105,0,25,1,0,0,0,2,35,1,0,0,0,4,37,1,0,
        0,0,6,42,1,0,0,0,8,46,1,0,0,0,10,51,1,0,0,0,12,64,1,0,0,0,14,66,
        1,0,0,0,16,74,1,0,0,0,18,83,1,0,0,0,20,98,1,0,0,0,22,100,1,0,0,0,
        24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,36,3,4,2,0,32,
        36,3,6,3,0,33,36,3,8,4,0,34,36,3,10,5,0,35,31,1,0,0,0,35,32,1,0,
        0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,8,0,0,38,39,
        5,16,0,0,39,40,3,14,7,0,40,41,5,12,0,0,41,5,1,0,0,0,42,43,5,9,0,
        0,43,44,3,12,6,0,44,45,5,12,0,0,45,7,1,0,0,0,46,47,5,10,0,0,47,48,
        5,16,0,0,48,49,3,14,7,0,49,50,5,12,0,0,50,9,1,0,0,0,51,52,5,11,0,
        0,52,53,3,12,6,0,53,54,5,12,0,0,54,11,1,0,0,0,55,65,5,13,0,0,56,
        61,5,16,0,0,57,58,5,1,0,0,58,60,5,16,0,0,59,57,1,0,0,0,60,63,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,64,55,
        1,0,0,0,64,56,1,0,0,0,65,13,1,0,0,0,66,71,3,16,8,0,67,68,5,2,0,0,
        68,70,3,16,8,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,
        0,0,0,72,15,1,0,0,0,73,71,1,0,0,0,74,75,5,16,0,0,75,76,5,3,0,0,76,
        77,3,18,9,0,77,17,1,0,0,0,78,84,5,14,0,0,79,84,5,15,0,0,80,84,5,
        16,0,0,81,84,3,20,10,0,82,84,3,22,11,0,83,78,1,0,0,0,83,79,1,0,0,
        0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,19,1,0,0,0,85,86,
        5,4,0,0,86,91,3,18,9,0,87,88,5,1,0,0,88,90,3,18,9,0,89,87,1,0,0,
        0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,
        1,0,0,0,94,95,5,5,0,0,95,99,1,0,0,0,96,97,5,4,0,0,97,99,5,5,0,0,
        98,85,1,0,0,0,98,96,1,0,0,0,99,21,1,0,0,0,100,101,5,6,0,0,101,102,
        3,14,7,0,102,103,5,7,0,0,103,23,1,0,0,0,8,27,35,61,64,71,83,91,98
    ]

class NoSQLParser ( Parser ):

    grammarFileName = "NoSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "':'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CREATE", "READ", "UPDATE", "DELETE", "END", "ALL", 
                      "NUMBER", "STRING", "IDENT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_create_stmt = 2
    RULE_read_stmt = 3
    RULE_update_stmt = 4
    RULE_delete_stmt = 5
    RULE_col_lista = 6
    RULE_campo_lista = 7
    RULE_campo = 8
    RULE_valor = 9
    RULE_lista_valor = 10
    RULE_doc_anidado = 11

    ruleNames =  [ "programa", "sentencia", "create_stmt", "read_stmt", 
                   "update_stmt", "delete_stmt", "col_lista", "campo_lista", 
                   "campo", "valor", "lista_valor", "doc_anidado" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    CREATE=8
    READ=9
    UPDATE=10
    DELETE=11
    END=12
    ALL=13
    NUMBER=14
    STRING=15
    IDENT=16
    WS=17

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

        def EOF(self):
            return self.getToken(NoSQLParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSQLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(NoSQLParser.SentenciaContext,i)


        def getRuleIndex(self):
            return NoSQLParser.RULE_programa

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

        localctx = NoSQLParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.sentencia()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                    break

            self.state = 29
            self.match(NoSQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_stmt(self):
            return self.getTypedRuleContext(NoSQLParser.Create_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(NoSQLParser.Read_stmtContext,0)


        def update_stmt(self):
            return self.getTypedRuleContext(NoSQLParser.Update_stmtContext,0)


        def delete_stmt(self):
            return self.getTypedRuleContext(NoSQLParser.Delete_stmtContext,0)


        def getRuleIndex(self):
            return NoSQLParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = NoSQLParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.create_stmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.read_stmt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.update_stmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.delete_stmt()
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


    class Create_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(NoSQLParser.CREATE, 0)

        def IDENT(self):
            return self.getToken(NoSQLParser.IDENT, 0)

        def campo_lista(self):
            return self.getTypedRuleContext(NoSQLParser.Campo_listaContext,0)


        def END(self):
            return self.getToken(NoSQLParser.END, 0)

        def getRuleIndex(self):
            return NoSQLParser.RULE_create_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_stmt" ):
                listener.enterCreate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_stmt" ):
                listener.exitCreate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_stmt" ):
                return visitor.visitCreate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def create_stmt(self):

        localctx = NoSQLParser.Create_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(NoSQLParser.CREATE)
            self.state = 38
            self.match(NoSQLParser.IDENT)
            self.state = 39
            self.campo_lista()
            self.state = 40
            self.match(NoSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(NoSQLParser.READ, 0)

        def col_lista(self):
            return self.getTypedRuleContext(NoSQLParser.Col_listaContext,0)


        def END(self):
            return self.getToken(NoSQLParser.END, 0)

        def getRuleIndex(self):
            return NoSQLParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_stmt" ):
                return visitor.visitRead_stmt(self)
            else:
                return visitor.visitChildren(self)




    def read_stmt(self):

        localctx = NoSQLParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(NoSQLParser.READ)
            self.state = 43
            self.col_lista()
            self.state = 44
            self.match(NoSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(NoSQLParser.UPDATE, 0)

        def IDENT(self):
            return self.getToken(NoSQLParser.IDENT, 0)

        def campo_lista(self):
            return self.getTypedRuleContext(NoSQLParser.Campo_listaContext,0)


        def END(self):
            return self.getToken(NoSQLParser.END, 0)

        def getRuleIndex(self):
            return NoSQLParser.RULE_update_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_stmt" ):
                listener.enterUpdate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_stmt" ):
                listener.exitUpdate_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_stmt" ):
                return visitor.visitUpdate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def update_stmt(self):

        localctx = NoSQLParser.Update_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_update_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(NoSQLParser.UPDATE)
            self.state = 47
            self.match(NoSQLParser.IDENT)
            self.state = 48
            self.campo_lista()
            self.state = 49
            self.match(NoSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delete_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(NoSQLParser.DELETE, 0)

        def col_lista(self):
            return self.getTypedRuleContext(NoSQLParser.Col_listaContext,0)


        def END(self):
            return self.getToken(NoSQLParser.END, 0)

        def getRuleIndex(self):
            return NoSQLParser.RULE_delete_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_stmt" ):
                listener.enterDelete_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_stmt" ):
                listener.exitDelete_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_stmt" ):
                return visitor.visitDelete_stmt(self)
            else:
                return visitor.visitChildren(self)




    def delete_stmt(self):

        localctx = NoSQLParser.Delete_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delete_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(NoSQLParser.DELETE)
            self.state = 52
            self.col_lista()
            self.state = 53
            self.match(NoSQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_listaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALL(self):
            return self.getToken(NoSQLParser.ALL, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(NoSQLParser.IDENT)
            else:
                return self.getToken(NoSQLParser.IDENT, i)

        def getRuleIndex(self):
            return NoSQLParser.RULE_col_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_lista" ):
                listener.enterCol_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_lista" ):
                listener.exitCol_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCol_lista" ):
                return visitor.visitCol_lista(self)
            else:
                return visitor.visitChildren(self)




    def col_lista(self):

        localctx = NoSQLParser.Col_listaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_col_lista)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(NoSQLParser.ALL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(NoSQLParser.IDENT)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 57
                    self.match(NoSQLParser.T__0)
                    self.state = 58
                    self.match(NoSQLParser.IDENT)
                    self.state = 63
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


    class Campo_listaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSQLParser.CampoContext)
            else:
                return self.getTypedRuleContext(NoSQLParser.CampoContext,i)


        def getRuleIndex(self):
            return NoSQLParser.RULE_campo_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo_lista" ):
                listener.enterCampo_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo_lista" ):
                listener.exitCampo_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampo_lista" ):
                return visitor.visitCampo_lista(self)
            else:
                return visitor.visitChildren(self)




    def campo_lista(self):

        localctx = NoSQLParser.Campo_listaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_campo_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.campo()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 67
                self.match(NoSQLParser.T__1)
                self.state = 68
                self.campo()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(NoSQLParser.IDENT, 0)

        def valor(self):
            return self.getTypedRuleContext(NoSQLParser.ValorContext,0)


        def getRuleIndex(self):
            return NoSQLParser.RULE_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo" ):
                listener.enterCampo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo" ):
                listener.exitCampo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampo" ):
                return visitor.visitCampo(self)
            else:
                return visitor.visitChildren(self)




    def campo(self):

        localctx = NoSQLParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_campo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(NoSQLParser.IDENT)
            self.state = 75
            self.match(NoSQLParser.T__2)
            self.state = 76
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(NoSQLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(NoSQLParser.STRING, 0)

        def IDENT(self):
            return self.getToken(NoSQLParser.IDENT, 0)

        def lista_valor(self):
            return self.getTypedRuleContext(NoSQLParser.Lista_valorContext,0)


        def doc_anidado(self):
            return self.getTypedRuleContext(NoSQLParser.Doc_anidadoContext,0)


        def getRuleIndex(self):
            return NoSQLParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = NoSQLParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_valor)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(NoSQLParser.NUMBER)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(NoSQLParser.STRING)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(NoSQLParser.IDENT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.lista_valor()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.doc_anidado()
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


    class Lista_valorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NoSQLParser.ValorContext)
            else:
                return self.getTypedRuleContext(NoSQLParser.ValorContext,i)


        def getRuleIndex(self):
            return NoSQLParser.RULE_lista_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_valor" ):
                listener.enterLista_valor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_valor" ):
                listener.exitLista_valor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_valor" ):
                return visitor.visitLista_valor(self)
            else:
                return visitor.visitChildren(self)




    def lista_valor(self):

        localctx = NoSQLParser.Lista_valorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lista_valor)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(NoSQLParser.T__3)
                self.state = 86
                self.valor()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 87
                    self.match(NoSQLParser.T__0)
                    self.state = 88
                    self.valor()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(NoSQLParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(NoSQLParser.T__3)
                self.state = 97
                self.match(NoSQLParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Doc_anidadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def campo_lista(self):
            return self.getTypedRuleContext(NoSQLParser.Campo_listaContext,0)


        def getRuleIndex(self):
            return NoSQLParser.RULE_doc_anidado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoc_anidado" ):
                listener.enterDoc_anidado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoc_anidado" ):
                listener.exitDoc_anidado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc_anidado" ):
                return visitor.visitDoc_anidado(self)
            else:
                return visitor.visitChildren(self)




    def doc_anidado(self):

        localctx = NoSQLParser.Doc_anidadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doc_anidado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(NoSQLParser.T__5)
            self.state = 101
            self.campo_lista()
            self.state = 102
            self.match(NoSQLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





