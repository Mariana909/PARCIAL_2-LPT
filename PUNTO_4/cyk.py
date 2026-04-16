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
    tokens = tokens_originales
    pos = [0]  # usar lista para mutabilidad en funciones anidadas

    def parse_num():
        tok = tokens[pos[0]]
        pos[0] += 1
        return float(tok) if '.' in tok else int(tok)

    def parse_term():
        # maneja número negativo como token "-" seguido de NUM
        if tokens[pos[0]] == '-':
            pos[0] += 1
            val = parse_num()
            return -val
        return parse_num()

    def parse_factor():
        izq = parse_term()
        while pos[0] < len(tokens) and tokens[pos[0]] in ('*', '/'):
            op = tokens[pos[0]]
            pos[0] += 1
            der = parse_term()
            if op == '*':
                izq = izq * der
            else:
                if der == 0:
                    raise ZeroDivisionError("División por cero")
                resultado = izq / der
                izq = int(resultado) if resultado == int(resultado) else resultado
        return izq

    def parse_expresion():
        izq = parse_factor()
        while pos[0] < len(tokens) and tokens[pos[0]] in ('+', '-'):
            op = tokens[pos[0]]
            pos[0] += 1
            der = parse_factor()
            if op == '+':
                izq = izq + der
            else:
                izq = izq - der
        return izq

    return parse_expresion()


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