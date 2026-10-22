#!/usr/bin/env python3
"""Punto fijo del repositorio: auto-creación desde la especificación.

Regenera artefactos derivados exclusivamente desde data/iom_spec.json
(+ axiomas embebidos en generate_ontology) y verifica identidad con lo
versionado. Encarnación técnica de:

  Orden Definitivo ⟹ ¬∃ Contenedor Exterior

El repositorio es un punto fijo de su propio generador: no necesita un
oráculo externo para reconstruirse.

Uso:
  python scripts/self_bootstrap.py
  python scripts/self_bootstrap.py --with-manifest
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DERIVED = [
    "datasets/triad_nodes.csv",
    "datasets/vector_steps.csv",
    "datasets/relation_candidates.csv",
]


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Punto fijo: regenerar desde spec y verificar identidad"
    )
    parser.add_argument(
        "--with-manifest",
        action="store_true",
        help="Incluir MANIFEST.sha256 (auto-certificación de identidad)",
    )
    args = parser.parse_args()

    print("=== self_bootstrap: punto fijo del repositorio ===")
    print("Fuente: data/iom_spec.json (+ reglas en generate_ontology.py)")
    print()

    print(">>> generate_ontology.py")
    r = run([sys.executable, "scripts/generate_ontology.py"])
    print(r.stdout, end="")
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        return 1

    paths = list(DERIVED)
    if args.with_manifest:
        print(">>> create_manifest.py")
        r = run([sys.executable, "scripts/create_manifest.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1
        paths.append("MANIFEST.sha256")

    print(">>> verificar identidad (git diff --exit-code)")
    r = run(["git", "diff", "--ignore-space-at-eol", "--exit-code", "--", *paths])
    if r.returncode != 0:
        print(
            "FALLO: el generador no es punto fijo — artefactos ≠ versionados.",
            file=sys.stderr,
        )
        print(r.stdout or r.stderr, file=sys.stderr)
        return 1

    print()
    print("OK: punto fijo alcanzado.")
    print("  El sistema regenera sus CSV desde la spec sin residuo exterior.")
    print("  Autonomía medible: el todo es reconstruible desde iom_spec.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
