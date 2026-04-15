# Generated from NoSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NoSQLParser import NoSQLParser
else:
    from NoSQLParser import NoSQLParser

# This class defines a complete generic visitor for a parse tree produced by NoSQLParser.

class NoSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NoSQLParser#programa.
    def visitPrograma(self, ctx:NoSQLParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#sentencia.
    def visitSentencia(self, ctx:NoSQLParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#create_stmt.
    def visitCreate_stmt(self, ctx:NoSQLParser.Create_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#read_stmt.
    def visitRead_stmt(self, ctx:NoSQLParser.Read_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#update_stmt.
    def visitUpdate_stmt(self, ctx:NoSQLParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#delete_stmt.
    def visitDelete_stmt(self, ctx:NoSQLParser.Delete_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#col_lista.
    def visitCol_lista(self, ctx:NoSQLParser.Col_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#campo_lista.
    def visitCampo_lista(self, ctx:NoSQLParser.Campo_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#campo.
    def visitCampo(self, ctx:NoSQLParser.CampoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#valor.
    def visitValor(self, ctx:NoSQLParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#lista_valor.
    def visitLista_valor(self, ctx:NoSQLParser.Lista_valorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NoSQLParser#doc_anidado.
    def visitDoc_anidado(self, ctx:NoSQLParser.Doc_anidadoContext):
        return self.visitChildren(ctx)



del NoSQLParser