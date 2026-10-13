#!/usr/bin/env python3
"""Comprueba que ontology/CSV versionados coinciden con generate_ontology.py.

Flujo:
  1. Ejecuta scripts/generate_ontology.py (reescribe artefactos).
  2. Compara los archivos generados con el árbol git (git diff --exit-code).
  3. Opcionalmente regenera MANIFEST.sha256 y lo compara.

Sale con código 1 si hay diferencias (artefactos desactualizados en el repo).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GENERATED = [
    "ontology/io_ontology.ttl",
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
    args = parser.parse_args()

    if not args.skip_generate:
        print(">>> generate_ontology.py")
        r = run([sys.executable, "scripts/generate_ontology.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1

    paths = list(GENERATED)
    if args.with_manifest:
        print(">>> create_manifest.py")
        r = run([sys.executable, "scripts/create_manifest.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1
        paths.append("MANIFEST.sha256")

    print(">>> git diff --exit-code (artefactos generados)")
    r = run(["git", "diff", "--exit-code", "--", *paths])
    if r.returncode != 0:
        print("ERROR: los artefactos generados no coinciden con lo versionado.", file=sys.stderr)
        print(r.stdout or r.stderr, file=sys.stderr)
        print(
            "\nEjecuta localmente:\n"
            "  python scripts/generate_ontology.py\n"
            "  python scripts/create_manifest.py   # si usas --with-manifest\n"
            "  git add ontology datasets MANIFEST.sha256 && git commit",
            file=sys.stderr,
        )
        return 1

    print("OK: artefactos generados idénticos a los versionados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
