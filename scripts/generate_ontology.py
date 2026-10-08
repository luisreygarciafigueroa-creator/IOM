#!/usr/bin/env python3
"""Genera el grafo RDF a partir de los datos enumerados en MARCOI.O.txt.

Los índices T00..T12 son identificadores estructurales internos; el documento
no proporciona los nombres ni el orden de las 13 tríadas. Por ello no se les
asignan etiquetas inventadas ni perspectivas calculadas.
"""
from pathlib import Path
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
g = Graph()
g.bind("io", IO)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

# 13 tríadas estructurales × 2 fases × 3 posiciones locales = 78 nodos.
PHASES = ("adv", "ret")
POSITIONS = (0, 1, 2)
for triad_idx in range(13):
    for phase in PHASES:
        for pos in POSITIONS:
            node = IO[f"T{triad_idx:02d}_{phase}_P{pos}"]
            g.add((node, RDF.type, IO.OntoNode))
            g.add((node, IO.hasTriadIndex, Literal(triad_idx, datatype=XSD.integer)))
            g.add((node, IO.hasPhase, Literal(phase)))
            g.add((node, IO.hasLocalPos, Literal(pos, datatype=XSD.integer)))
            g.add((node, IO.hasDirection, IO.evol if phase == "adv" else IO.invol))

# Ejemplos nombrados en la fuente, sin asociarlos a índices no especificados.
for i, label in enumerate(("Oscuridad-Consciencia-Luz", "Hardware-Virtual-Software"), 1):
    example = IO[f"sourceTriadExample{i}"]
    g.add((example, RDF.type, IO.SourceTriadExample))
    g.add((example, RDFS.label, Literal(label, lang="es")))

# Extensión enumerada expresamente: 1 + 4 + 6 + 6 + 4 = 21 categorías.
levels = {
    0: ("Vacío Generativo (V)",),
    1: ("Potencia", "Acto", "Percepción", "Acción"),
    2: ("Sujeto-Objeto", "Causa-Efecto", "Presencia-Ausencia",
        "Símbolo-Significado", "Límite-Transgresión", "Mediación"),
    3: ("Sistema", "Entorno", "Red", "Holismo", "Emergencia", "Colapso"),
    4: ("E", "S_fwd", "Ivo", "S_rev"),
}
for level, labels in levels.items():
    for index, label in enumerate(labels, 1):
        category = IO[f"expanded_L{level}_{index:02d}"]
        g.add((category, RDF.type, IO.ExpandedCategory))
        g.add((category, IO.hasLevel, Literal(level, datatype=XSD.integer)))
        g.add((category, RDFS.label, Literal(label, lang="es")))

# Conteos globales declarados; no se asignan a instancias Txx.
model = IO.SourceModel
for predicate, value in (
    (IO.declaredTriadCount, 13),
    (IO.declaredPerspectiveCount, 5),
    (IO.declaredOperatorCount, 4),
    (IO.declaredExpandedCategoryCount, 21),
):
    g.add((model, predicate, Literal(value, datatype=XSD.integer)))

# Inversión de fase: el mismo índice y posición local se espejan.
for triad_idx in range(13):
    for pos in POSITIONS:
        adv = IO[f"T{triad_idx:02d}_adv_P{pos}"]
        ret = IO[f"T{triad_idx:02d}_ret_P{pos}"]
        g.add((adv, IO.mirrorOf, ret))
        g.add((ret, IO.mirrorOf, adv))

node_count = len(set(g.subjects(RDF.type, IO.OntoNode)))
category_count = len(set(g.subjects(RDF.type, IO.ExpandedCategory)))
assert node_count == 78, f"Deben ser 78 nodos estructurales; se generaron {node_count}"
assert category_count == 21, f"Deben ser 21 categorías explícitas; se generaron {category_count}"
out = ROOT / "ontology" / "io_ontology.ttl"
out.parent.mkdir(parents=True, exist_ok=True)
g.serialize(destination=str(out), format="turtle")
print(f"Nodos estructurales: {node_count}; categorías de la extensión: {category_count}")
print(f"✓ Ontología serializada en {out}")
