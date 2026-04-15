# Generated from NoSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NoSQLParser import NoSQLParser
else:
    from NoSQLParser import NoSQLParser

# This class defines a complete listener for a parse tree produced by NoSQLParser.
class NoSQLListener(ParseTreeListener):

    # Enter a parse tree produced by NoSQLParser#programa.
    def enterPrograma(self, ctx:NoSQLParser.ProgramaContext):
        pass

    # Exit a parse tree produced by NoSQLParser#programa.
    def exitPrograma(self, ctx:NoSQLParser.ProgramaContext):
        pass


    # Enter a parse tree produced by NoSQLParser#sentencia.
    def enterSentencia(self, ctx:NoSQLParser.SentenciaContext):
        pass

    # Exit a parse tree produced by NoSQLParser#sentencia.
    def exitSentencia(self, ctx:NoSQLParser.SentenciaContext):
        pass


    # Enter a parse tree produced by NoSQLParser#create_stmt.
    def enterCreate_stmt(self, ctx:NoSQLParser.Create_stmtContext):
        pass

    # Exit a parse tree produced by NoSQLParser#create_stmt.
    def exitCreate_stmt(self, ctx:NoSQLParser.Create_stmtContext):
        pass


    # Enter a parse tree produced by NoSQLParser#read_stmt.
    def enterRead_stmt(self, ctx:NoSQLParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by NoSQLParser#read_stmt.
    def exitRead_stmt(self, ctx:NoSQLParser.Read_stmtContext):
        pass


    # Enter a parse tree produced by NoSQLParser#update_stmt.
    def enterUpdate_stmt(self, ctx:NoSQLParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by NoSQLParser#update_stmt.
    def exitUpdate_stmt(self, ctx:NoSQLParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by NoSQLParser#delete_stmt.
    def enterDelete_stmt(self, ctx:NoSQLParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by NoSQLParser#delete_stmt.
    def exitDelete_stmt(self, ctx:NoSQLParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by NoSQLParser#col_lista.
    def enterCol_lista(self, ctx:NoSQLParser.Col_listaContext):
        pass

    # Exit a parse tree produced by NoSQLParser#col_lista.
    def exitCol_lista(self, ctx:NoSQLParser.Col_listaContext):
        pass


    # Enter a parse tree produced by NoSQLParser#campo_lista.
    def enterCampo_lista(self, ctx:NoSQLParser.Campo_listaContext):
        pass

    # Exit a parse tree produced by NoSQLParser#campo_lista.
    def exitCampo_lista(self, ctx:NoSQLParser.Campo_listaContext):
        pass


    # Enter a parse tree produced by NoSQLParser#campo.
    def enterCampo(self, ctx:NoSQLParser.CampoContext):
        pass

    # Exit a parse tree produced by NoSQLParser#campo.
    def exitCampo(self, ctx:NoSQLParser.CampoContext):
        pass


    # Enter a parse tree produced by NoSQLParser#valor.
    def enterValor(self, ctx:NoSQLParser.ValorContext):
        pass

    # Exit a parse tree produced by NoSQLParser#valor.
    def exitValor(self, ctx:NoSQLParser.ValorContext):
        pass


    # Enter a parse tree produced by NoSQLParser#lista_valor.
    def enterLista_valor(self, ctx:NoSQLParser.Lista_valorContext):
        pass

    # Exit a parse tree produced by NoSQLParser#lista_valor.
    def exitLista_valor(self, ctx:NoSQLParser.Lista_valorContext):
        pass


    # Enter a parse tree produced by NoSQLParser#doc_anidado.
    def enterDoc_anidado(self, ctx:NoSQLParser.Doc_anidadoContext):
        pass

    # Exit a parse tree produced by NoSQLParser#doc_anidado.
    def exitDoc_anidado(self, ctx:NoSQLParser.Doc_anidadoContext):
        pass



del NoSQLParser