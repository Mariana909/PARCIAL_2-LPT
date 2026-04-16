import re
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


TOKEN_SPEC = [
    ("IF",      r"\bif\b"),
    ("THEN",    r"\bthen\b"),
    ("ELSE",    r"\belse\b"),
    ("OTRAS",   r"\botras\b"),
    ("EQ",      r"=="),
    ("NEQ",     r"!="),
    ("LEQ",     r"<="),
    ("GEQ",     r">="),
    ("LT",      r"<"),
    ("GT",      r">"),
    ("ASIG",    r"="),
    ("NUMBER",  r"\b\d+(\.\d+)?\b"),
    ("IDENT",   r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("WS",      r"[ \t]+"),
]

TOKEN_RE = re.compile("|".join(f"(?P<{name}>{pat})" for name, pat in TOKEN_SPEC))


def tokenizar(texto):
    tokens = []
    for m in TOKEN_RE.finditer(texto):
        tipo = m.lastgroup
        valor = m.group()
        if tipo not in ("WS", "NUMBER") or tipo == "NUMBER":
            if tipo != "WS":
                tokens.append((tipo, valor))
    return tokens


class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.hijos = []

    def agregar(self, hijo):
        self.hijos.append(hijo)
        return hijo


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return (None, None)

    def consumir(self, tipo):
        tok = self.actual()
        if tok[0] == tipo:
            self.pos += 1
            return tok
        return None

    # programa → sentencia+
    def parse_programa(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("programa"))
        pos_respaldo = self.pos
        encontro = False

        while self.actual()[0] is not None:
            if not self.parse_sentencia(nodo):
                break
            encontro = True

        if not encontro:
            self.pos = pos_respaldo
            nodo_padre.hijos.remove(nodo)
            return False
        return True

    # sentencia → prop | asignacion
    def parse_sentencia(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("sentencia"))
        pos_respaldo = self.pos

        if self.parse_prop(nodo):
            return True

        self.pos = pos_respaldo
        nodo.hijos.clear()
        if self.parse_asignacion(nodo):
            return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # asignacion → IDENT = expr
    def parse_asignacion(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("asignacion"))
        pos_respaldo = self.pos

        tok = self.consumir("IDENT")
        if tok:
            nodo.agregar(Nodo(tok[1]))
            tok_asig = self.consumir("ASIG")
            if tok_asig:
                nodo.agregar(Nodo("="))
                if self.parse_expr(nodo):
                    return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # prop → prop_emparejada | prop_no_emparejada
    def parse_prop(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("prop"))
        pos_respaldo = self.pos

        if self.parse_prop_emparejada(nodo):
            return True

        self.pos = pos_respaldo
        nodo.hijos.clear()
        if self.parse_prop_no_emparejada(nodo):
            return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # prop_emparejada → if condicion then prop_emparejada else prop_emparejada
    #                 | otras
    def parse_prop_emparejada(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("prop_emparejada"))
        pos_respaldo = self.pos

        if self.consumir("IF"):
            nodo.agregar(Nodo("if"))
            if self.parse_condicion(nodo):
                if self.consumir("THEN"):
                    nodo.agregar(Nodo("then"))
                    if self.parse_prop_emparejada(nodo):
                        if self.consumir("ELSE"):
                            nodo.agregar(Nodo("else"))
                            if self.parse_prop_emparejada(nodo):
                                return True

        self.pos = pos_respaldo
        nodo.hijos.clear()
        if self.consumir("OTRAS"):
            nodo.agregar(Nodo("otras"))
            return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # prop_no_emparejada → if condicion then prop
    #                    | if condicion then prop_emparejada else prop_no_emparejada
    def parse_prop_no_emparejada(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("prop_no_emparejada"))
        pos_respaldo = self.pos

        if self.consumir("IF"):
            nodo.agregar(Nodo("if"))
            if self.parse_condicion(nodo):
                if self.consumir("THEN"):
                    nodo.agregar(Nodo("then"))
                    pos_inner = self.pos
                    nodo_inner = list(nodo.hijos)

                    if self.parse_prop_emparejada(nodo):
                        if self.consumir("ELSE"):
                            nodo.agregar(Nodo("else"))
                            if self.parse_prop_no_emparejada(nodo):
                                return True

                    self.pos = pos_inner
                    nodo.hijos = list(nodo_inner)
                    if self.parse_prop(nodo):
                        return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # condicion → expr op expr
    def parse_condicion(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("condicion"))
        pos_respaldo = self.pos

        if self.parse_expr(nodo):
            if self.parse_op(nodo):
                if self.parse_expr(nodo):
                    return True

        self.pos = pos_respaldo
        nodo_padre.hijos.remove(nodo)
        return False

    # expr → NUMBER | IDENT
    def parse_expr(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("expr"))

        tok = self.consumir("NUMBER")
        if tok:
            nodo.agregar(Nodo(tok[1]))
            return True

        tok = self.consumir("IDENT")
        if tok:
            nodo.agregar(Nodo(tok[1]))
            return True

        nodo_padre.hijos.remove(nodo)
        return False

    # op → == | != | < | > | <= | >=
    def parse_op(self, nodo_padre):
        nodo = nodo_padre.agregar(Nodo("op"))

        for tipo in ("EQ", "NEQ", "LEQ", "GEQ", "LT", "GT"):
            tok = self.consumir(tipo)
            if tok:
                nodo.agregar(Nodo(tok[1]))
                return True

        nodo_padre.hijos.remove(nodo)
        return False

    def parsear(self):
        raiz = Nodo("programa")
        try:
            exito = self.parse_programa(raiz) and self.actual()[0] is None
        except SyntaxError as e:
            print(f"  Error de sintaxis: {e}")
            exito = False
        return exito, raiz


def calcular_posiciones(nodo, profundidad=0, contador=[0]):
    if not nodo.hijos:
        x = contador[0]
        contador[0] += 1
        nodo._x = x
        nodo._y = -profundidad
        return
    for hijo in nodo.hijos:
        calcular_posiciones(hijo, profundidad + 1, contador)
    nodo._x = sum(h._x for h in nodo.hijos) / len(nodo.hijos)
    nodo._y = -profundidad


def dibujar_arbol(nodo, ax):
    es_eps = nodo.etiqueta == "ε"
    es_hoja = not nodo.hijos
    color = "#E499DD" if es_eps else ("#7EC5C8" if es_hoja else "#AC4AD9")

    for hijo in nodo.hijos:
        ax.plot([nodo._x, hijo._x], [nodo._y, hijo._y],
                color="#888888", linewidth=1, zorder=1)
        dibujar_arbol(hijo, ax)

    circulo = plt.Circle((nodo._x, nodo._y), 0.35,
                          color=color, zorder=2, ec="white", linewidth=1.5)
    ax.add_patch(circulo)
    fontsize = 7 if len(nodo.etiqueta) > 6 else 8
    ax.text(nodo._x, nodo._y, nodo.etiqueta,
            ha="center", va="center", fontsize=fontsize,
            color="white", fontweight="bold", zorder=3)


def mostrar_arbol(raiz, expresion, aceptada):
    calcular_posiciones(raiz, contador=[0])

    todas = []
    def recoger(n):
        todas.append(n)
        for h in n.hijos:
            recoger(h)
    recoger(raiz)

    xs = [n._x for n in todas]
    ys = [n._y for n in todas]

    fig, ax = plt.subplots(figsize=(max(10, (max(xs) - min(xs) + 2) * 0.6),
                                    max(6,  (max(ys) - min(ys) + 2) * 1.1)))
    ax.set_aspect("equal")
    ax.axis("off")
    dibujar_arbol(raiz, ax)

    estado = "ACEPTADA" if aceptada else "RECHAZADA"
    color_titulo = "#2ecc50" if aceptada else "#e74c3c"
    ax.set_title(f'"{expresion}"  ->  {estado}',
                 fontsize=12, fontweight="bold", color=color_titulo, pad=14)

    leyenda = [
        mpatches.Patch(color="#AC4AD9", label="No terminal"),
        mpatches.Patch(color="#7EC5C8", label="Terminal"),
        mpatches.Patch(color="#E499DD", label="epsilon (vacío)"),
    ]
    ax.legend(handles=leyenda, loc="upper right", fontsize=8, framealpha=0.8)
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, 1.5)
    plt.tight_layout()
    nombre = re.sub(r'[^a-zA-Z0-9]', '_', expresion)[:40]
    plt.savefig(f"arbol_{nombre + str(time.time())[-2:]}.png", dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 parser.py <archivo>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        lineas = f.read().splitlines()

    for linea in lineas:
        if not linea.strip():
            continue
        tokens = tokenizar(linea)
        parser = Parser(tokens)
        aceptada, arbol = parser.parsear()
        print(f'{"ACEPTADA" if aceptada else "RECHAZADA"}  "{linea}"')
        mostrar_arbol(arbol, linea, aceptada)