from antlr4 import *
from GRAMATICA.NoSQLParser import NoSQLParser
from GRAMATICA.NoSQLVisitor import NoSQLVisitor
import json


class VisitorNoSQL(NoSQLVisitor):

    def __init__(self):
        self.db = {}

    def visitPrograma(self, ctx: NoSQLParser.ProgramaContext):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)

    def visitSentencia(self, ctx: NoSQLParser.SentenciaContext):
        return self.visit(ctx.getChild(0))

    def visitCreate_stmt(self, ctx: NoSQLParser.Create_stmtContext):
        nombre = ctx.IDENT().getText()
        campos = self.visit(ctx.campo_lista())

        if nombre not in self.db:
            self.db[nombre] = []

        self.db[nombre].append(campos)
        print(f"[CREATE] Documento agregado a la colección '{nombre}'")

    def visitRead_stmt(self, ctx: NoSQLParser.Read_stmtContext):
        col_lista = self.visit(ctx.col_lista())

        if col_lista == "ALL":
            colecciones = list(self.db.keys())
        else:
            colecciones = col_lista

        for nombre in colecciones:
            if nombre not in self.db:
                print(f"[READ] La colección '{nombre}' no existe")
            else:
                print(f"\n[READ] Colección '{nombre}':")
                for i, doc in enumerate(self.db[nombre]):
                    print(f"  Documento {i + 1}:")
                    print(json.dumps(doc, indent=4, ensure_ascii=False))

    def visitUpdate_stmt(self, ctx: NoSQLParser.Update_stmtContext):
        nombre = ctx.IDENT().getText()
        campos = self.visit(ctx.campo_lista())

        if nombre not in self.db:
            print(f"[UPDATE] La colección '{nombre}' no existe")
            return

        for doc in self.db[nombre]:
            for clave, valor in campos.items():
                doc[clave] = valor

        print(f"[UPDATE] Colección '{nombre}' actualizada")

    def visitDelete_stmt(self, ctx: NoSQLParser.Delete_stmtContext):
        col_lista = self.visit(ctx.col_lista())

        if col_lista == "ALL":
            self.db.clear()
            print("[DELETE] Todas las colecciones eliminadas")
        else:
            for nombre in col_lista:
                if nombre not in self.db:
                    print(f"[DELETE] La colección '{nombre}' no existe")
                else:
                    del self.db[nombre]
                    print(f"[DELETE] Colección '{nombre}' eliminada")

    def visitCol_lista(self, ctx: NoSQLParser.Col_listaContext):
        if ctx.ALL():
            return "ALL"
        return [ident.getText() for ident in ctx.IDENT()]

    def visitCampo_lista(self, ctx: NoSQLParser.Campo_listaContext):
        resultado = {}
        for campo in ctx.campo():
            clave, valor = self.visit(campo)
            resultado[clave] = valor
        return resultado

    def visitCampo(self, ctx: NoSQLParser.CampoContext):
        clave = ctx.IDENT().getText()
        valor = self.visit(ctx.valor())
        return clave, valor

    def visitValor(self, ctx: NoSQLParser.ValorContext):
        if ctx.NUMBER():
            texto = ctx.NUMBER().getText()
            return float(texto) if '.' in texto else int(texto)
        elif ctx.STRING():
            texto = ctx.STRING().getText()
            return texto[1:-1]
        elif ctx.IDENT():
            return ctx.IDENT().getText()
        elif ctx.lista_valor():
            return self.visit(ctx.lista_valor())
        elif ctx.doc_anidado():
            return self.visit(ctx.doc_anidado())

    def visitLista_valor(self, ctx: NoSQLParser.Lista_valorContext):
        return [self.visit(v) for v in ctx.valor()]

    def visitDoc_anidado(self, ctx: NoSQLParser.Doc_anidadoContext):
        return self.visit(ctx.campo_lista())