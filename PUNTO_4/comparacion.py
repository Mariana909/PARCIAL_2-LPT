import sys
import os
import time
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "ANTLR"))

from ANTLR.main import parsear_antlr, evaluar_antlr
from cyk import parsear_cyk, evaluar_cyk, tokenizar_cyk

longitudes  = []
t_antlr     = []
t_cyk       = []
R_antlr     = []
R_cyk       = []
V_antlr     = []
V_cyk       = []

try:
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lineas = f.read().splitlines()

        primer = True
        for linea in lineas:
            if not linea.strip():
                continue

            tokens_orig = linea.strip().split()
            tokens_norm = tokenizar_cyk(linea)

            t_0a = time.time()
            aceptada_a, tree = parsear_antlr(linea)
            t_1a = time.time()

            t_0c = time.time()
            aceptada_c = parsear_cyk(tokens_norm)
            t_1c = time.time()

            if primer:
                primer = False
                continue

            val_a = evaluar_antlr(tree) if aceptada_a else None
            val_c = evaluar_cyk(tokens_orig) if aceptada_c else None

            longitudes.append(len(tokens_orig))
            t_antlr.append(t_1a - t_0a)
            t_cyk.append(t_1c - t_0c)
            R_antlr.append(aceptada_a)
            R_cyk.append(aceptada_c)
            V_antlr.append(val_a)
            V_cyk.append(val_c)

        print(f"\n{'Expresión':<10} {'ANTLR':>10} {'CYK':>10} {'Val ANTLR':>12} {'Val CYK':>12} {'Coinciden':>10}")
        print("-" * 80)
        idx = 0
        for linea in lineas:
            if not linea.strip():
                continue
            if idx == 0:
                idx += 1
                continue
            coincide = "SI" if R_antlr[idx-1] == R_cyk[idx-1] and V_antlr[idx-1] == V_cyk[idx-1] else "NO"
            estado_a = "ACEPTADA" if R_antlr[idx-1] else "RECHAZADA"
            estado_c = "ACEPTADA" if R_cyk[idx-1]   else "RECHAZADA"
            print(f"{idx:>10} {estado_a:>10} {estado_c:>10} {str(V_antlr[idx-1]):>12} {str(V_cyk[idx-1]):>12} {coincide:>10}")
            idx += 1

        plt.figure(figsize=(10, 6))
        plt.plot(longitudes, t_antlr, 'bo-', markersize=3, label='ANTLR')
        plt.plot(longitudes, t_cyk,   'gs-', markersize=3, label='CYK')
        plt.xlabel('Longitud de la entrada (tokens)')
        plt.ylabel('Tiempo de parseo (s)')
        plt.title('Comparación de rendimiento: ANTLR vs CYK')
        plt.legend()
        plt.grid(True)
        plt.savefig('comparacion.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("\nGráfica guardada en comparacion.png")
    else:
        print("No se detectó archivo de entrada")

except FileNotFoundError:
    print("No se encontró el archivo")