#!/usr/bin/env python3
"""Verifica que las etiquetas del dataset son exactamente las relaciones RDF.

La ontología (reglas derivadas de data/iom_spec.json) se trata como fuente formal;
se comparan todos los pares dirigidos de cada tríada, incluidos los negativos.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

from rdflib import Graph, Namespace

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
CSV_PATH = ROOT / "datasets" / "relation_candidates.csv"
RDF_PATH = ROOT / "ontology" / "io_ontology.ttl"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Guardar informe JSON (por defecto solo consola)")
    args = parser.parse_args()
    graph = Graph().parse(RDF_PATH, format="turtle")
    expected: dict[tuple[str, str], str] = {}
    for relation in ("mirrorOf", "creates"):
        for src, _, tgt in graph.triples((None, IO[relation], None)):
            expected[(str(src).split("#")[-1], str(tgt).split("#")[-1])] = relation
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8", newline="")))
    actual = {(r["source"], r["target"]): r["relation"] for r in rows}
    errors: list[str] = []
    if len(actual) != len(rows):
        errors.append("El CSV contiene pares dirigidos duplicados.")
    keys = set(actual) | set(expected)
    mismatches = [{"source": s, "target": t, "csv": actual.get((s, t), "<missing>"),
                   "rdf": expected.get((s, t), "none")} for s, t in sorted(keys)
                  if actual.get((s, t), "none") != expected.get((s, t), "none")]
    if mismatches:
        errors.append(f"{len(mismatches)} pares difieren entre CSV y RDF.")
    report = {
        "status": "pass" if not errors else "fail",
        "rule_source": "data/iom_spec.json -> ontology/io_ontology.ttl",
        "dataset": "datasets/relation_candidates.csv",
        "sha256": {"iom_spec.json": sha256(ROOT / "data/iom_spec.json"),
                   "io_ontology.ttl": sha256(RDF_PATH), "relation_candidates.csv": sha256(CSV_PATH)},
        "counts": {"csv_pairs": len(rows), "rdf_labeled_pairs": len(expected),
                   "csv_labels": {label: sum(r["relation"] == label for r in rows)
                                  for label in ("none", "mirrorOf", "creates")}},
        "mismatch_count": len(mismatches), "mismatches": mismatches[:25], "errors": errors,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
