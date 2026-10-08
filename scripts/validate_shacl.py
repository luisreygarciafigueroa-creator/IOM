#!/usr/bin/env python3
"""Comprueba declaraciones OWL, inferencias de dominio/rango y restricciones SHACL."""
from pathlib import Path
import sys

from owlrl import DeductiveClosure, OWLRL_Semantics
from pyshacl import validate
from rdflib import Graph, Namespace
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).resolve().parents[1]
DATA_GRAPH = ROOT / "ontology" / "io_ontology.ttl"
SHAPES_GRAPH = ROOT / "ontology" / "io_shapes.ttl"
IO = Namespace("http://example.org/iom#")
REQUIRED_CLASSES = (IO.OntoNode, IO.VectorStep, IO.Perspective, IO.ExpandedCategory, IO.Position, IO.Direction, IO.SourceModel)
REQUIRED_PROPERTIES = (IO.hasPerspective, IO.hasPosition, IO.hasDirection, IO.hasVector, IO.mirrorOf, IO.creates)


def main() -> int:
    data = Graph().parse(DATA_GRAPH, format="turtle")
    for cls in REQUIRED_CLASSES:
        if (cls, RDF.type, OWL.Class) not in data:
            print(f"Falta declaración OWL de clase {cls}", file=sys.stderr)
            return 1
    for prop in REQUIRED_PROPERTIES:
        if (prop, RDF.type, OWL.ObjectProperty) not in data or (prop, RDFS.domain, None) not in data or (prop, RDFS.range, None) not in data:
            print(f"Falta axioma OWL de dominio/rango para {prop}", file=sys.stderr)
            return 1

    # OWL RL expande los axiomas de dominio y rango; se verifican las tipificaciones inferidas.
    closure = Graph()
    for triple in data:
        closure.add(triple)
    DeductiveClosure(OWLRL_Semantics).expand(closure)
    nodes = set(data.subjects(RDF.type, IO.OntoNode))
    vectors = set(data.subjects(RDF.type, IO.VectorStep))
    inferred_positions = {obj for node in nodes for obj in data.objects(node, IO.hasPosition)
                          if (obj, RDF.type, IO.Position) in closure}
    inferred_perspectives = {obj for node in nodes for obj in data.objects(node, IO.hasPerspective)
                             if (obj, RDF.type, IO.Perspective) in closure}
    if len(nodes) != 78 or len(vectors) != 20 or len(inferred_positions) != 3 or len(inferred_perspectives) != 3:
        print("Falló la comprobación OWL de cardinalidades/inferencias esperadas.", file=sys.stderr)
        return 1
    print(f"✓ OWL RL: clases y dominios/rangos declarados; inferidos posición/perspectiva para {len(nodes)} nodos.")

    conforms, _results_graph, results_text = validate(
        data_graph=data, shacl_graph=str(SHAPES_GRAPH), inference="none", abort_on_first=False,
    )
    if results_text:
        print(results_text)
    if conforms:
        print("✓ RDF satisface las restricciones SHACL cargadas.")
        return 0
    print("✗ RDF no satisface todas las restricciones SHACL.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
