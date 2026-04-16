# Generated from izqNormal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .izqNormalParser import izqNormalParser
else:
    from izqNormalParser import izqNormalParser

# This class defines a complete generic visitor for a parse tree produced by izqNormalParser.

class izqNormalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by izqNormalParser#programa.
    def visitPrograma(self, ctx:izqNormalParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqNormalParser#expresion.
    def visitExpresion(self, ctx:izqNormalParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqNormalParser#factor.
    def visitFactor(self, ctx:izqNormalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by izqNormalParser#term.
    def visitTerm(self, ctx:izqNormalParser.TermContext):
        return self.visitChildren(ctx)



del izqNormalParser