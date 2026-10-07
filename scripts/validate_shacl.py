#!/usr/bin/env python3
"""Valida la ontología IOM contra sus formas SHACL."""
from pathlib import Path
import sys

from pyshacl import validate

ROOT = Path(__file__).resolve().parents[1]
DATA_GRAPH = ROOT / "ontology" / "io_ontology.ttl"
SHAPES_GRAPH = ROOT / "ontology" / "io_shapes.ttl"


def main() -> int:
    conforms, _results_graph, results_text = validate(
        data_graph=str(DATA_GRAPH),
        shacl_graph=str(SHAPES_GRAPH),
        inference="none",
        abort_on_first=False,
    )
    if results_text:
        print(results_text)
    if conforms:
        print("✓ La ontología satisface todas las formas SHACL cargadas.")
        return 0
    print("✗ La ontología no satisface las formas SHACL; revisa los resultados anteriores.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
