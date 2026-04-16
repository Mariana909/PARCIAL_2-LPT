# Parcial 2 — Lenguajes de Programación y Transducción

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

### ANTLR4 tools
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

### Conclusión

La gramática BNF resultante es compacta y cubre los casos de uso fundamentales de un lenguaje NoSQL simplificado. La separación entre `campo_lista`, `lista_valor` y `doc_anidado` permite expresar estructuras de datos anidadas de forma natural, manteniendo la gramática libre de ambigüedades gracias a los delimitadores explícitos (`END`, `;`, `:`) que actúan como guías de parseo sin necesidad de lookahead extendido.

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

### Salida esperada

```
[CREATE] Documento agregado a la colección 'usuarios'
[CREATE] Documento agregado a la colección 'usuarios'
[CREATE] Documento agregado a la colección 'productos'

[READ] Colección 'usuarios':
  Documento 1:
    {
        "nombre": "Juan Pérez",
        "edad": 25,
        "activo": "true",
        "direccion": {
            "ciudad": "Bogotá",
            "pais": "Colombia"
        }
    }
  Documento 2:
    {
        "nombre": "María López",
        "edad": 30,
        "activo": "false",
        "direccion": {
            "ciudad": "Medellín",
            "pais": "Colombia"
        }
    }

[READ] Colección 'usuarios':
[READ] Colección 'productos':
  ...

[UPDATE] Colección 'usuarios' actualizada

[READ] Colección 'usuarios':
  Documento 1:
    { ..., "activo": "true", "edad": 31 }
  Documento 2:
    { ..., "activo": "true", "edad": 31 }

[DELETE] Colección 'productos' eliminada

[READ] Colección 'usuarios':
  ...
```

### Conclusión

El visitor demuestra que ANTLR4 permite separar limpiamente el análisis sintáctico de la semántica: el parser generado se encarga exclusivamente de verificar la estructura, mientras que el visitor implementa el comportamiento. La representación en memoria como diccionarios de Python resulta suficiente para simular las operaciones CRUD básicas; una extensión natural sería añadir filtros en `READ` y `UPDATE` para operar sobre documentos específicos en lugar de colecciones enteras.

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

Esta gramática **es ambigua**. La cadena que lo demuestra es:

```
if e1 then if e2 then otras else otras
```

Para esta misma cadena se pueden construir **dos árboles de derivación distintos**, dependiendo de con cuál `then` se empareja el `else`. Los árboles se graficaron con la herramienta online [https://mshang.ca/syntree/](https://mshang.ca/syntree/):

<img width="1114" height="326" alt="image" src="https://github.com/user-attachments/assets/2181428b-222b-40d6-9df2-a4953d19e133" />

<img width="649" height="326" alt="image" src="https://github.com/user-attachments/assets/0298242c-9c69-43ba-b611-885f756d51c7" />


### Solución

Se resolvió la ambigüedad aplicando la solución clásica descrita en el capítulo 4 de **Compiladores: Principios, técnicas y herramientas** (Aho, Sethi y Ullman): distinguir explícitamente entre proposiciones *emparejadas* y *no emparejadas*, de modo que cualquier proposición entre un `then` y un `else` deba estar completamente emparejada.

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

### Conclusión

La ambigüedad del `dangling else` es un problema clásico que afecta a prácticamente todo lenguaje con condicionales anidados. La solución de separar producciones emparejadas y no emparejadas elimina la ambigüedad de forma formal y sin alterar el lenguaje generado. La mayoría de lenguajes reales resuelven este problema de manera pragmática (asociando el `else` con el `if` más cercano), pero la corrección gramatical explícita es preferible cuando se requiere una especificación formal precisa.

---

## Punto 4 — CYK vs Parser predictivo (ANTLR4)

**Carpeta:** `PUNTO_4/`

### Gramática de la calculadora

Se reutilizó la gramática aritmética implementada en ANTLR4 en entregas anteriores [`ASOCIATIVIDAD_PRECEDENCIA/IZQ_NORMAL`](https://github.com/Mariana909/ASOCIATIVIDAD_PRECEDENCIA/tree/main/IZQ_NORMAL)(`PUNTO_4/ANTLR/GRAMATICA/izqNormal.g4`), que define expresiones con `+`, `-`, `*`, `/` y números con signo, también se usó como base las implementaciones (cyk.py y comparacion.py) del repositorio [COMPARACION_COMPLEJIDAD](https://github.com/Mariana909/COMPARACION_COMPLEJIDAD.git), ajustándolas a la gramática de izqNormal y modificando un poco la salida de comparacion.py.

### Transformación a Forma Normal de Chomsky (FNC)

CYK requiere que la gramática esté en FNC. La gramática original es recursiva a izquierda con producciones ternarias, por lo que la transformación requiere cuatro pasos.

**Gramática original**:
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

### Ejecución

```bash
# Comparación completa con gráfica
python3 PUNTO_4/comparacion.py PUNTO_4/entrada.txt

# Solo CYK
python3 PUNTO_4/cyk.py PUNTO_4/entrada.txt

# Solo ANTLR
python3 PUNTO_4/ANTLR/main.py PUNTO_4/entrada.txt
```

### Salida esperada

```
Expresión       ANTLR        CYK    Val ANTLR      Val CYK  Coinciden
--------------------------------------------------------------------------------
         1   ACEPTADA   ACEPTADA            3            3         SI
         2   ACEPTADA   ACEPTADA            6            6         SI
         3   ACEPTADA   ACEPTADA            4            4         SI
         4   ACEPTADA   ACEPTADA           20           20         SI
         5   ACEPTADA   ACEPTADA           14           14         SI
         ...
        29   ACEPTADA   ACEPTADA         2826         2826         SI

Gráfica guardada en comparacion.png
```

<img width="1281" height="818" alt="image" src="https://github.com/user-attachments/assets/9ef34da0-8890-4def-aecf-250b2866ef8e" />


Todas las expresiones son aceptadas por ambos parsers y los valores calculados coinciden, confirmando que la FNC implementada es equivalente a la gramática original y que el evaluador respeta la precedencia de operadores.

### Comparación de rendimiento

| Parser | Complejidad | Tiempo (~59 tokens) |
|--------|-------------|----------------------|
| ANTLR4 | O(n) | ≈ 0.002 s |
| CYK  | O(n³) | ≈ 0.9 s |

### Conclusión

La diferencia de rendimiento entre ambos enfoques es drástica y refleja directamente sus complejidades teóricas. ANTLR4 aprovecha la estructura determinista de la gramática LL para analizar en tiempo lineal, mientras que CYK paga el costo de ser un algoritmo de propósito general capaz de manejar cualquier gramática libre de contexto en FNC. Para gramáticas de expresiones aritméticas, donde la precedencia y asociatividad están bien definidas, un parser LL es siempre la opción práctica; CYK resulta útil cuando la gramática es ambigua o cuando se requiere un reconocedor general sin comprometerse con un estilo de parseo particular.

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

### Salida esperada

```
ACEPTADA  "x = 5"
ACEPTADA  "y = x"
ACEPTADA  "if x < 10 then otras"
ACEPTADA  "if x == y then otras else otras"
ACEPTADA  "if x > 0 then if y < 5 then otras else otras"
ACEPTADA  "if x != 0 then otras else if y == 1 then otras else otras"
```

Para cada línea aceptada se genera además una imagen PNG con el árbol sintáctico correspondiente.

<img width="1485" height="1033" alt="image" src="https://github.com/user-attachments/assets/bdac5eba-d648-41bf-9e80-9dfabe84992e" />


### Conclusión

El parser descendente recursivo con backtracking demuestra de forma práctica cómo la gramática no ambigua del punto 3 guía directamente la estructura del código: cada regla de producción se traduce en una función, y la distinción entre `prop_emparejada` y `prop_no_emparejada` en la gramática se refleja en funciones separadas que evitan la ambigüedad en tiempo de parseo. El backtracking permite manejar alternativas sin necesidad de calcular conjuntos FIRST/FOLLOW explícitamente, a costa de un peor caso exponencial en gramáticas muy ambiguas; para esta gramática en particular el backtracking es acotado y el rendimiento es aceptable.
