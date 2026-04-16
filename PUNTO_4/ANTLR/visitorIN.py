from antlr4 import *
from GRAMATICA.izqNormalParser import izqNormalParser
from GRAMATICA.izqNormalVisitor import izqNormalVisitor

class VisitorIN(izqNormalVisitor):
    def visitPrograma(self, ctx:izqNormalParser.ProgramaContext):
        return self.visit(ctx.expresion())

    def visitExpresion(self, ctx:izqNormalParser.ExpresionContext):
        if ctx.getChildCount() ==1:
            return self.visit(ctx.factor())
        left = self.visit(ctx.expresion())
        right = self.visit(ctx.factor())
        
        if ctx.SUM():
            return left + right
        else:
            return left - right

    def visitFactor(self, ctx:izqNormalParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        
        left = self.visit(ctx.factor())
        right = self.visit(ctx.term())
        
        if ctx.MUL():
            return left * right
        else:
            if right == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            result = left / right
    
            if result.is_integer():
                return int(result)
            
            return result

    def visitTerm(self, ctx):
        text = ctx.NUM().getText()
        
        if '.' in text:
            value = float(text)
        else:
            value = int(text)
        
        if ctx.RES():
            return -value
        else:
            return value