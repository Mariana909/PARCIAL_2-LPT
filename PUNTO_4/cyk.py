import sys
import time

gramatica = {
    "expresion": [["E1", "factor"], ["E2", "factor"], ["F1", "term"],
                  ["F2", "term"], ["T_RES", "NUM"], ["NUM"]],
    "factor":    [["F1", "term"], ["F2", "term"], ["T_RES", "NUM"], ["NUM"]],
    "term":      [["NUM"], ["T_RES", "NUM"]],
    "E1":        [["expresion", "T_SUM"]],
    "E2":        [["expresion", "T_RES"]],
    "F1":        [["factor", "T_MUL"]],
    "F2":        [["factor", "T_DIV"]],
    "T_SUM":     [["+"]],
    "T_RES":     [["-"]],
    "T_MUL":     [["*"]],
    "T_DIV":     [["/"]],
    "NUM":       [["<número>"]],  # cualquier token numérico
}
simbolo_inicio = "expresion"



def analizar_cyk(tokens):
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


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            with open(entrada, "r") as archivo:
                lineas = archivo.read().splitlines()

            for linea in lineas:
                if linea.strip() == "":
                    continue
                tokens = linea.strip().split()
                t_0 = time.time()
                resultado = analizar_cyk(tokens)
                t_1 = time.time()
                estado = "ACEPTADA" if resultado else "RECHAZADA"
                print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")
        else:
            print("No se detectó archivo de entrada")

    except FileNotFoundError:
        print("No se encontró el archivo")