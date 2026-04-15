import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from antlr4 import *
from PUNTOS_1_2.visitor_NoSQL import VisitorNoSQL
from GRAMATICA.NoSQLLexer import NoSQLLexer
from GRAMATICA.NoSQLParser import NoSQLParser


def evaluar(programa):
    input_stream = InputStream(programa)
    lexer = NoSQLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = NoSQLParser(tokens)

    tree = parser.programa()

    visitor = VisitorNoSQL()
    visitor.visit(tree)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            with open(entrada, 'r', encoding='utf-8') as en:
                datos = en.read()
                evaluar(datos)
        else:
            print("No se detectó archivo de entrada")
    except FileNotFoundError:
        print("No se encontró el archivo")