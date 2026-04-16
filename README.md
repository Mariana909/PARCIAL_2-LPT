# Parcial 2 — Lenguajes de Programación 2026-1

Repositorio con las soluciones a los cinco puntos del parcial. Cada punto tiene su propia carpeta con su gramática, implementación y archivo de prueba.

---

## Requisitos previos

### Java Runtime (requerido por ANTLR4)
```bash
sudo apt install -y default-jre
java -version   # openjdk 17.x
```

### Python 3.8+
```bash
sudo apt install -y python3-full python3-pip python3-venv
```

### Entorno virtual y dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ANTLR4 tools (para regenerar parsers si se modifica alguna gramática)
```bash
pip install antlr4-tools
```

---

## Punto 1 — Gramática NoSQL (BNF)

**Carpeta:** `PUNTOS_1_2/`

Se diseñó una gramática para un lenguaje de manipulación de datos orientado a bases de datos no relacionales. La gramática es intencionalmente simplificada respecto a un motor real (como MongoDB), pero cubre las cuatro operaciones CRUD con soporte para documentos anidados y listas.

La gramática completa en notación BNF se encuentra en [`PUNTOS_1_2/NoSQL_BNF.txt`](PUNTOS_1_2/NoSQL_BNF.txt). Las operaciones soportadas son:

- `CREATE <colección> <campo>:<valor>; ... END`
- `READ <colección, ...> END` / `READ ALL END`
- `UPDATE <colección> <campo>:<valor>; ... END`
- `DELETE <colección, ...> END` / `DELETE ALL END`

Los valores pueden ser números, strings, identificadores, listas (`[v1, v2]`) o documentos anidados (`{campo: valor}`).

---

## Punto 2 — Implementación en ANTLR4

**Carpeta:** `PUNTOS_1_2/`

La gramática del punto 1 se implementó en ANTLR4. Para regenerar el parser (solo si se modifica `NoSQL.g4`):

```bash
cd PUNTOS_1_2/GRAMATICA
antlr4 -Dlanguage=Python3 -visitor NoSQL.g4
cd ../..
```

El visitor implementado en [`PUNTOS_1_2/visitor_NoSQL.py`](PUNTOS_1_2/visitor_NoSQL.py) mantiene un diccionario de diccionarios en memoria para simular la base de datos. Cada colección es una lista de documentos; cada documento es un diccionario Python. Las operaciones del visitor:

- `visitCreate_stmt` — agrega un nuevo documento a la colección.
- `visitRead_stmt` — imprime todos los documentos de las colecciones indicadas (o todas si es `ALL`).
- `visitUpdate_stmt` — actualiza los campos especificados en todos los documentos de la colección.
- `visitDelete_stmt` — elimina la colección completa (o todas con `ALL`).

### Ejecución

```bash
python3 PUNTOS_1_2/main.py PUNTOS_1_2/entrada.txt
```

El archivo [`PUNTOS_1_2/entrada.txt`](PUNTOS_1_2/entrada.txt) contiene un ciclo completo de pruebas: dos `CREATE`, un `READ`, un `UPDATE`, otro `READ` y un `DELETE`.

---

## Punto 3 — Ambigüedad en la gramática if-then-else

**Carpeta:** `PUNTO_3/`

### Detección de la ambigüedad

La gramática propuesta en el enunciado era:

```
prop             → if expr then prop
                 | prop_emparejada

prop_emparejada  → if expr then prop_emparejada else prop
                 | otras
```

Esta gramática **sigue siendo ambigua**. La cadena que lo demuestra es:

```
if e1 then if e2 then otras else otras
```

Para esta misma cadena se pueden construir **dos árboles de derivación distintos**, dependiendo de con cuál `then` se empareja el `else`. Los árboles se generaron con la herramienta online [https://mshang.ca/syntree/](https://mshang.ca/syntree/):

> *(insertar aquí las imágenes de los dos árboles)*

### Solución

Se resolvió la ambigüedad aplicando la solución clásica descrita en **Compiladores: Principios, técnicas y herramientas** (Aho, Lam, Sethi, Ullman — 2.ª ed., cap. 4, pág. 180): distinguir explícitamente entre proposiciones *emparejadas* y *no emparejadas*, de modo que cualquier proposición entre un `then` y un `else` deba estar completamente emparejada.

La gramática no ambigua resultante (guardada en [`PUNTO_3/G_ARREGLADA.txt`](PUNTO_3/G_ARREGLADA.txt)) es:

```
prop               → prop_emparejada
                   | prop_no_emparejada

prop_emparejada    → if expr then prop_emparejada else prop_emparejada
                   | otras

prop_no_emparejada → if expr then prop
                   | if expr then prop_emparejada else prop_no_emparejada
```

Esta gramática genera exactamente el mismo lenguaje pero permite un único árbol de derivación para cada cadena válida.

---

## Punto 4 — CYK vs Parser predictivo (ANTLR4)

**Carpeta:** `PUNTO_4/`

### Gramática de la calculadora

Se reutilizó la gramática aritmética implementada en ANTLR4 en entregas anteriores (`PUNTO_4/ANTLR/GRAMATICA/izqNormal.g4`), que define expresiones con `+`, `-`, `*`, `/` y números con signo.

### Transformación a Forma Normal de Chomsky (FNC)

CYK requiere que la gramática esté en FNC. La gramática original es recursiva a izquierda con producciones ternarias, por lo que la transformación requiere cuatro pasos.

**Gramática original** (simplificada):
```
expresion → expresion + factor | expresion - factor | factor
factor    → factor * term | factor / term | term
term      → NUM | - NUM
```

**Paso 1 — Nuevo símbolo de inicio:** no necesario, `expresion` no aparece en lados derechos.

**Paso 2 — Eliminar producciones unitarias:** `expresion → factor` y `factor → term` se eliminan propagando sus alternativas hacia arriba.

**Paso 3 — Reemplazar terminales en producciones mixtas:**
```
T_SUM → +    T_RES → -    T_MUL → *    T_DIV → /
```

**Paso 4 — Descomponer producciones ternarias:**
```
E1   → expresion T_SUM       expresion → E1 factor
E2   → expresion T_RES       expresion → E2 factor
F1   → factor T_MUL          expresion → F1 term
F2   → factor T_DIV          expresion → F2 term
                              expresion → T_RES NUM
                              expresion → NUM

factor → F1 term
factor → F2 term
factor → T_RES NUM
factor → NUM

term → NUM
term → T_RES NUM

T_SUM → +  |  T_RES → -  |  T_MUL → *  |  T_DIV → /
```

Esta FNC está implementada en [`PUNTO_4/cyk.py`](PUNTO_4/cyk.py).

### Comparación de rendimiento

| Parser | Complejidad | Tiempo (~150 tokens) |
|--------|-------------|----------------------|
| ANTLR4 (LL\*) | O(n) | ≈ 0.01 s |
| CYK (prog. dinámica) | O(n³) | ≈ 1.6 s |

ANTLR4 usa estrategia LL(\*) con predicción adaptativa, lo que le permite analizar en tiempo lineal. CYK construye una tabla de n² celdas donde cada celda requiere hasta n comparaciones, resultando en complejidad cúbica inevitable.

### Ejecución

```bash
# Generar entradas de prueba
python3 PUNTO_4/genEntrada.py

# Comparación completa con gráfica
python3 PUNTO_4/comparacion.py PUNTO_4/entrada.txt

# Solo CYK
python3 PUNTO_4/cyk.py PUNTO_4/entrada.txt

# Solo ANTLR
python3 PUNTO_4/ANTLR/main.py PUNTO_4/entrada.txt
```

---

## Punto 5 — Parser descendente recursivo con emparejamiento

**Carpeta:** `PUNTO_5/`

### Gramática

Se extendió la gramática no ambigua del punto 3 añadiendo soporte para asignaciones, quedando en [`PUNTO_5/G3_ampliada.txt`](PUNTO_5/G3_ampliada.txt):

```
programa           → sentencia+
sentencia          → prop | asignacion
asignacion         → IDENT = expr
prop               → prop_emparejada | prop_no_emparejada
prop_emparejada    → if condicion then prop_emparejada else prop_emparejada | otras
prop_no_emparejada → if condicion then prop
                   | if condicion then prop_emparejada else prop_no_emparejada
condicion          → expr op expr
expr               → NUMBER | IDENT
op                 → == | != | < | > | <= | >=
```

### Implementación

Se reutilizó como base el parser descendente recursivo del repositorio [ARBOL_SINTACTICO](https://github.com/Mariana909/ARBOL_SINTACTICO.git), adaptando las funciones a las reglas de esta gramática.

El mecanismo de **emparejamiento** está en la función `consumir(tipo)`: verifica si el token actual coincide con el esperado y avanza el puntero; si no coincide, el parser hace *backtracking* restaurando la posición para intentar otra alternativa. Cada función `parse_X` sigue el patrón:

```python
def parse_X(self, nodo_padre):
    pos_respaldo = self.pos          # guardar posición
    if self.consumir("TOKEN_A"):     # intentar alternativa 1
        ...
        return True
    self.pos = pos_respaldo          # backtracking
    if self.parse_Y(nodo):           # intentar alternativa 2
        return True
    nodo_padre.hijos.remove(nodo)    # falló, limpiar árbol
    return False
```

Se conservó la visualización del árbol sintáctico (usando `matplotlib`) del proyecto original, ya que complementa bien la salida del parser.

### Ejecución

```bash
python3 PUNTO_5/parser_G3_ampliada.py PUNTO_5/entrada.txt
```

El archivo [`PUNTO_5/entrada.txt`](PUNTO_5/entrada.txt) incluye asignaciones simples, condicionales sin `else`, con `else`, y anidados, cubriendo los casos de ambas reglas de `prop`.
