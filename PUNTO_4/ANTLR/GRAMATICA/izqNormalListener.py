# Generated from izqNormal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .izqNormalParser import izqNormalParser
else:
    from izqNormalParser import izqNormalParser

# This class defines a complete listener for a parse tree produced by izqNormalParser.
class izqNormalListener(ParseTreeListener):

    # Enter a parse tree produced by izqNormalParser#programa.
    def enterPrograma(self, ctx:izqNormalParser.ProgramaContext):
        pass

    # Exit a parse tree produced by izqNormalParser#programa.
    def exitPrograma(self, ctx:izqNormalParser.ProgramaContext):
        pass


    # Enter a parse tree produced by izqNormalParser#expresion.
    def enterExpresion(self, ctx:izqNormalParser.ExpresionContext):
        pass

    # Exit a parse tree produced by izqNormalParser#expresion.
    def exitExpresion(self, ctx:izqNormalParser.ExpresionContext):
        pass


    # Enter a parse tree produced by izqNormalParser#factor.
    def enterFactor(self, ctx:izqNormalParser.FactorContext):
        pass

    # Exit a parse tree produced by izqNormalParser#factor.
    def exitFactor(self, ctx:izqNormalParser.FactorContext):
        pass


    # Enter a parse tree produced by izqNormalParser#term.
    def enterTerm(self, ctx:izqNormalParser.TermContext):
        pass

    # Exit a parse tree produced by izqNormalParser#term.
    def exitTerm(self, ctx:izqNormalParser.TermContext):
        pass



del izqNormalParser