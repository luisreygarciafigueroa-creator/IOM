#!/usr/bin/env python3
"""Comprueba que los CSV versionados coinciden con generate_ontology.py.

El Turtle (ontology/io_ontology.ttl) se regenera siempre en CI antes de SHACL;
la comparación byte-a-byte del TTL es frágil entre versiones de rdflib, por eso
solo se exige igualdad exacta de:

  - datasets/triad_nodes.csv
  - datasets/vector_steps.csv
  - datasets/relation_candidates.csv

Flujo:
  1. (opcional) generate_ontology.py
  2. git diff --exit-code sobre los CSV anteriores (ignorando fin de línea)
  3. (opcional) create_manifest.py + diff de MANIFEST.sha256

Uso:
  python scripts/check_generated_committed.py
  python scripts/check_generated_committed.py --with-manifest
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GENERATED_CSV = [
    "datasets/triad_nodes.csv",
    "datasets/vector_steps.csv",
    "datasets/relation_candidates.csv",
]


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--with-manifest",
        action="store_true",
        help="También regenerar MANIFEST.sha256 y exigir que coincida",
    )
    parser.add_argument(
        "--skip-generate",
        action="store_true",
        help="No regenerar; solo comparar el working tree actual con HEAD",
    )
    parser.add_argument(
        "--include-ttl",
        action="store_true",
        help="Incluir ontology/io_ontology.ttl en el diff (puede fallar por orden de serialización rdflib)",
    )
    args = parser.parse_args()

    if not args.skip_generate:
        print(">>> generate_ontology.py")
        r = run([sys.executable, "scripts/generate_ontology.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1

    paths = list(GENERATED_CSV)
    if args.include_ttl:
        paths.insert(0, "ontology/io_ontology.ttl")

    if args.with_manifest:
        print(">>> create_manifest.py")
        r = run([sys.executable, "scripts/create_manifest.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1
        paths.append("MANIFEST.sha256")

    print(">>> git diff --ignore-space-at-eol --exit-code", " ".join(paths))
    r = run(["git", "diff", "--ignore-space-at-eol", "--exit-code", "--", *paths])
    if r.returncode != 0:
        print(
            "ERROR: los artefactos generados no coinciden con lo versionado.",
            file=sys.stderr,
        )
        print(r.stdout or r.stderr, file=sys.stderr)
        print(
            "\nEjecuta localmente:\n"
            "  python scripts/generate_ontology.py\n"
            "  python scripts/create_manifest.py   # si usas --with-manifest\n"
            "  git add datasets ontology MANIFEST.sha256 && git commit",
            file=sys.stderr,
        )
        return 1

    print("OK: CSV generados coinciden con los versionados (sin diferencias de contenido)")
    if not args.include_ttl:
        print(
            "Nota: ontology/io_ontology.ttl no se compara byte-a-byte; "
            "CI lo regenera antes de SHACL. Para versionarlo: "
            "python scripts/generate_ontology.py && git add ontology/io_ontology.ttl"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
