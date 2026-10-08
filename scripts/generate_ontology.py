#!/usr/bin/env python3
"""Genera RDF desde MARCOI.O.txt y sus dos especificaciones complementarias."""
from pathlib import Path
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
g = Graph()
g.bind("io", IO)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

for perspective, label in (
    (IO.Ind, "Individualidad"), (IO.D, "Dualidad"), (IO.Tot, "Totalidad"),
    (IO.Evol, "Vector Evolutivo"), (IO.Invol, "Vector Involutivo"),
):
    g.add((perspective, RDF.type, IO.Perspective))
    g.add((perspective, RDFS.label, Literal(label, lang="es")))

ADVANCE = [
    ("individualidad", "dualidad", "totalidad"),
    ("oscuridad", "consciencia", "luz"),
    ("descendente", "mente", "ascendente"),
    ("logica", "inteligencia", "libertad"),
    ("muerte", "artificial", "vida"),
    ("singularidad", "tiempo", "infinito"),
    ("universo", "espacio", "vacio"),
    ("hardware", "virtual", "software"),
    ("orientación", "cuantico", "dirección"),
    ("receptor", "supraconsciente", "emisor"),
    ("memoria", "inconsciente", "imaginación"),
    ("caracter", "subconsciente", "personalidad"),
    ("cuerpo", "consciente", "mundo"),
]
RETREAT = [
    ("mundo", "consciente", "cuerpo"),
    ("personalidad", "subconsciente", "caracter"),
    ("imaginacion", "inconsciente", "memoria"),
    ("emisor", "supraconsciente", "receptor"),
    ("dirección", "cuantico", "orientación"),
    ("software", "virtual", "hardware"),
    ("vacio", "espacio", "universo"),
    ("infinito", "tiempo", "singularidad"),
    ("vida", "artificial", "muerte"),
    ("libertad", "inteligencia", "lógica"),
    ("ascendente", "mente", "descendente"),
    ("luz", "consciencia", "oscuridad"),
    ("totalidad", "dualidad", "individualidad"),
]
POSITIONS = ("left", "center", "right")
PERSPECTIVES = (IO.Ind, IO.D, IO.Tot)
PHASES = {"adv": ADVANCE, "ret": RETREAT}

for phase, rows in PHASES.items():
    direction = IO.evol if phase == "adv" else IO.invol
    for triad_idx, labels in enumerate(rows):
        for pos_idx, label in enumerate(labels):
            node = IO[f"T{triad_idx:02d}_{phase}_P{pos_idx}"]
            g.add((node, RDF.type, IO.OntoNode))
            g.add((node, IO.hasTriadIndex, Literal(triad_idx, datatype=XSD.integer)))
            g.add((node, IO.hasPhase, Literal(phase)))
            g.add((node, IO.hasLocalPos, Literal(pos_idx, datatype=XSD.integer)))
            g.add((node, IO.hasPosition, IO[POSITIONS[pos_idx]]))
            g.add((node, IO.hasPerspective, PERSPECTIVES[pos_idx]))
            g.add((node, IO.hasDirection, direction))
            g.add((node, RDFS.label, Literal(label, lang="es")))

# Espejo lateral: izquierda ↔ derecha y centro ↔ centro en la otra fase.
for triad_idx in range(13):
    for pos_idx in range(3):
        opposite_pos = 2 - pos_idx
        adv = IO[f"T{triad_idx:02d}_adv_P{pos_idx}"]
        ret = IO[f"T{triad_idx:02d}_ret_P{opposite_pos}"]
        g.add((adv, IO.mirrorOf, ret))
        g.add((ret, IO.mirrorOf, adv))

# Cuatro dinámicas de generación cruzada aplicadas fila por fila.
for triad_idx in range(13):
    adv_left = IO[f"T{triad_idx:02d}_adv_P0"]
    adv_center = IO[f"T{triad_idx:02d}_adv_P1"]
    adv_right = IO[f"T{triad_idx:02d}_adv_P2"]
    ret_left = IO[f"T{triad_idx:02d}_ret_P0"]
    ret_center = IO[f"T{triad_idx:02d}_ret_P1"]
    ret_right = IO[f"T{triad_idx:02d}_ret_P2"]
    for source in (adv_left, adv_right):
        g.add((source, IO.creates, ret_center))
    for target in (ret_left, ret_right):
        g.add((adv_center, IO.creates, target))
    for source in (ret_left, ret_right):
        g.add((source, IO.creates, adv_center))
    for target in (adv_left, adv_right):
        g.add((ret_center, IO.creates, target))

# Posiciones de eje para las perspectivas cuarta y quinta (4 filas × 5 pasos).
VECTOR_ROWS = (
    ("Evol", "adv", ("vacio", "ind", "dua", "tot", "evol"), (0, 1, 2, 3, 4), "→"),
    ("Evol", "ret", ("evol", "fut", "pre", "pas", "vacio"), (4, 3, 2, 1, 0), "←"),
    ("Invol", "adv", ("invol", "tot", "dua", "ind", "vacio"), (4, 3, 2, 1, 0), "→"),
    ("Invol", "ret", ("vacio", "pas", "pre", "fut", "invol"), (0, 1, 2, 3, 4), "←"),
)
for vector_name, phase, labels, axis_positions, arrow in VECTOR_ROWS:
    for visual_index, (label, axis_pos) in enumerate(zip(labels, axis_positions)):
        step = IO[f"vector_{vector_name.lower()}_{phase}_{visual_index}"]
        g.add((step, RDF.type, IO.VectorStep))
        g.add((step, IO.hasVector, IO[vector_name]))
        g.add((step, IO.hasCyclePhase, Literal(phase)))
        g.add((step, IO.hasAxisPosition, Literal(axis_pos, datatype=XSD.integer)))
        g.add((step, IO.hasStepIndex, Literal(visual_index, datatype=XSD.integer)))
        g.add((step, IO.displayArrow, Literal(arrow)))
        g.add((step, RDFS.label, Literal(label, lang="es")))

# Las 21 categorías enumeradas en la extensión teórica del documento.
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

model = IO.SourceModel
for predicate, value in (
    (IO.declaredTriadCount, 13),
    (IO.declaredPerspectiveCount, 5),
    (IO.declaredOperatorCount, 4),
    (IO.declaredExpandedCategoryCount, 21),
):
    g.add((model, predicate, Literal(value, datatype=XSD.integer)))

node_count = len(set(g.subjects(RDF.type, IO.OntoNode)))
vector_count = len(set(g.subjects(RDF.type, IO.VectorStep)))
category_count = len(set(g.subjects(RDF.type, IO.ExpandedCategory)))
creates_count = len(set(g.triples((None, IO.creates, None))))
assert len(ADVANCE) == len(RETREAT) == 13
assert node_count == 78, f"Deben ser 78 nodos de fase y posición; se generaron {node_count}"
assert vector_count == 20, f"Deben ser 20 pasos vectoriales; se generaron {vector_count}"
assert category_count == 21, f"Deben ser 21 categorías de la extensión; se generaron {category_count}"
assert creates_count == 104, f"Deben ser 104 relaciones creates; se generaron {creates_count}"
out = ROOT / "ontology" / "io_ontology.ttl"
out.parent.mkdir(parents=True, exist_ok=True)
g.serialize(destination=str(out), format="turtle")
print(f"Tríadas: 13 por fase; nodos: {node_count}; relaciones creates: {creates_count}")
print(f"Pasos vectoriales: {vector_count}; categorías de la extensión: {category_count}")
print(f"✓ Ontología serializada en {out}")
