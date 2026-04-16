import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from antlr4 import *
from ANTLR.visitorIN import VisitorIN
from GRAMATICA.izqNormalLexer import izqNormalLexer
from GRAMATICA.izqNormalParser import izqNormalParser


def parsear_antlr(expresion):
    input_stream = InputStream(expresion)
    lexer = izqNormalLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = izqNormalParser(tokens)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    tree = parser.programa()

    if parser.getNumberOfSyntaxErrors() > 0:
        return False, None

    return True, tree


def evaluar_antlr(tree):
    visitor = VisitorIN()
    return visitor.visit(tree)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            with open(entrada, 'r') as en:
                lineas = en.read().splitlines()

            for linea in lineas:
                if linea.strip() == "":
                    continue

                t_0 = time.time()
                aceptada, tree = parsear_antlr(linea)
                t_1 = time.time()

                if aceptada:
                    resultado = evaluar_antlr(tree)
                    estado = f"ACEPTADA  resultado = {resultado}"
                else:
                    estado = "RECHAZADA"

                print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")
        else:
            print("No se detectó archivo de entrada")
    except FileNotFoundError:
        print("No se encontró el archivo")