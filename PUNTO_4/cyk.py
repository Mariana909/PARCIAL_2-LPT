import sys
import re
import time


TOKEN_NUM = re.compile(r'^-?\d+(\.\d+)?$')


def tokenizar_cyk(linea):
    tokens = []
    for tok in linea.strip().split():
        if TOKEN_NUM.match(tok):
            tokens.append("NUM")
        else:
            tokens.append(tok)
    return tokens


gramatica = {
    "expresion": [["E1", "factor"], ["E2", "factor"],
                  ["F1", "term"],   ["F2", "term"],
                  ["T_RES", "NUM"], ["NUM"]],
    "factor":    [["F1", "term"],   ["F2", "term"],
                  ["T_RES", "NUM"], ["NUM"]],
    "term":      [["NUM"], ["T_RES", "NUM"]],
    "E1":        [["expresion", "T_SUM"]],
    "E2":        [["expresion", "T_RES"]],
    "F1":        [["factor", "T_MUL"]],
    "F2":        [["factor", "T_DIV"]],
    "T_SUM":     [["+"]],
    "T_RES":     [["-"]],
    "T_MUL":     [["*"]],
    "T_DIV":     [["/"]],
    "NUM":       [["NUM"]],
}
simbolo_inicio = "expresion"


def parsear_cyk(tokens):
    n = len(tokens)
    if n == 0:
        return False

    tabla = [[set() for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for no_terminal, producciones in gramatica.items():
            for lado_derecho in producciones:
                if len(lado_derecho) == 1 and lado_derecho[0] == tokens[j]:
                    tabla[j][j].add(no_terminal)

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for no_terminal, producciones in gramatica.items():
                    for lado_derecho in producciones:
                        if (len(lado_derecho) == 2
                                and lado_derecho[0] in tabla[i][k]
                                and lado_derecho[1] in tabla[k + 1][j]):
                            tabla[i][j].add(no_terminal)

    return simbolo_inicio in tabla[0][n - 1]


def evaluar_cyk(tokens_originales):
    operadores = {'+', '-', '*', '/'}
    pila = []
    i = 0
    tokens = tokens_originales

    def siguiente_expr(pos):
        izq = float(tokens[pos]) if '.' in tokens[pos] else int(tokens[pos])
        pos += 1
        while pos < len(tokens) and tokens[pos] in operadores:
            op = tokens[pos]
            der = float(tokens[pos+1]) if '.' in tokens[pos+1] else int(tokens[pos+1])
            if op == '+':
                izq = izq + der
            elif op == '-':
                izq = izq - der
            elif op == '*':
                izq = izq * der
            elif op == '/':
                if der == 0:
                    raise ZeroDivisionError("División por cero")
                resultado = izq / der
                izq = int(resultado) if resultado == int(resultado) else resultado
            pos += 2
        return izq

    return siguiente_expr(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 cyk.py <archivo>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        lineas = f.read().splitlines()

    for linea in lineas:
        if not linea.strip():
            continue
        tokens_norm = tokenizar_cyk(linea)
        tokens_orig = linea.strip().split()

        t_0 = time.time()
        aceptada = parsear_cyk(tokens_norm)
        t_1 = time.time()

        if aceptada:
            resultado = evaluar_cyk(tokens_orig)
            estado = f"ACEPTADA  resultado = {resultado}"
        else:
            estado = "RECHAZADA"

        print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")