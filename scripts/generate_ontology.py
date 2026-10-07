#!/usr/bin/env python3
"""Genera ontology/io_ontology.ttl con 78 nodos (13 tríadas × 3 posiciones × 2 fases)."""
from rdflib import Graph, Namespace, Literal
from pathlib import Path

from rdflib.namespace import RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]

IO = Namespace("http://example.org/iom#")
g = Graph()
g.bind("io", IO)
g.bind("rdfs", RDFS)

PERSPECTIVES = ["Ind", "D", "Tot", "Evol", "Invol"]
PHASES = ["adv", "ret"]
POSITIONS = [0, 1, 2]

for triad_idx in range(13):
    for phase in PHASES:
        for pos in POSITIONS:
            node_id = f"T{triad_idx:02d}_{phase}_P{pos}"
            node = IO[node_id]
            g.add((node, RDF.type, IO.OntoNode))
            g.add((node, IO.hasTriadIndex, Literal(triad_idx, datatype=XSD.integer)))
            g.add((node, IO.hasPhase, Literal(phase)))
            g.add((node, IO.hasLocalPos, Literal(pos, datatype=XSD.integer)))
            direction = "evol" if phase == "adv" else "invol"
            g.add((node, IO.hasDirection, IO[direction]))
            persp_idx = (triad_idx + pos) % 5
            g.add((node, IO.hasPerspective, IO[PERSPECTIVES[persp_idx]]))
            g.add((node, IO.restoresVacuum, Literal(True, datatype=XSD.boolean)))

# Inversión lateral perfecta: espejo adv <-> ret
for triad_idx in range(13):
    for pos in POSITIONS:
        adv = IO[f"T{triad_idx:02d}_adv_P{pos}"]
        ret = IO[f"T{triad_idx:02d}_ret_P{pos}"]
        g.add((adv, IO.mirrorOf, ret))
        g.add((ret, IO.mirrorOf, adv))

g.serialize(str(ROOT / "ontology" / "io_ontology.ttl"), format="turtle")
node_count = len(list(g.subjects(RDF.type, IO.OntoNode)))
print(f"Nodos generados: {node_count}")
assert node_count == 78, f"Deben ser exactamente 78 nodos, se generaron {node_count}"
print(f"✓ Ontología serializada en {ROOT / 'ontology' / 'io_ontology.ttl'}")
