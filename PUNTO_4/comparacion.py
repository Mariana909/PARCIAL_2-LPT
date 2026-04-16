import sys
import os
import time
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "ANTLR"))

from ANTLR.main import evaluar
from cyk import analizar_cyk

longitudes = []
t_antlr = []
t_cyk = []
R_antlr = []
R_cyk = []

try:
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        with open(entrada, "r") as archivo:
            lineas = archivo.read().splitlines()

        primer_antlr = True
        for linea in lineas:
            if linea.strip() == "":
                continue
            tokens = linea.strip().split()

            t_0a = time.time()
            resultado_antlr = evaluar(linea)
            t_1a = time.time()

            t_0c = time.time()
            resultado_cyk = analizar_cyk(tokens)
            t_1c = time.time()

            if primer_antlr:
                primer_antlr = False
                continue

            longitudes.append(len(tokens))
            t_antlr.append(t_1a - t_0a)
            t_cyk.append(t_1c - t_0c)
            R_antlr.append(resultado_antlr)
            R_cyk.append(resultado_cyk)

        diferencias = [(i, lineas[i]) for i in range(len(R_antlr)) if R_antlr[i] != R_cyk[i]]
        if diferencias:
            print("Diferencias detectadas:")
            for i, linea in diferencias:
                print(f"  línea {i}: ANTLR={'ACEPTADA' if R_antlr[i] else 'RECHAZADA'} | CYK={'ACEPTADA' if R_cyk[i] else 'RECHAZADA'} | {linea}")
        else:
            print("Ambos parsers coinciden en todas las entradas.")

        plt.figure(figsize=(10, 6))
        plt.plot(longitudes, t_antlr, 'bo-', markersize=3, label='ANTLR')
        plt.plot(longitudes, t_cyk, 'gs-', markersize=3, label='CYK')
        plt.xlabel('Longitud de la entrada (tokens)')
        plt.ylabel('Tiempo de ejecución (s)')
        plt.title('Comparación de rendimiento: ANTLR vs CYK')
        plt.legend()
        plt.grid(True)
        plt.savefig('comparacion.png', dpi=150, bbox_inches='tight')
        plt.show()
        print("Gráfica guardada en comparacion.png")

    else:
        print("No se detectó archivo de entrada")

except FileNotFoundError:
    print("No se encontró el archivo")