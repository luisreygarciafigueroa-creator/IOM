#!/usr/bin/env python3
"""Punto fijo del repositorio: auto-creación estable bajo iteración.

Requisitos de autonomía medible:
  1. Regenerar CSV (y opcionalmente MANIFEST) desde data/iom_spec.json.
  2. Verificar identidad con lo versionado (git diff vacío).
  3. Segunda pasada idéntica (S_{n+1} = S_n): sin timestamps ni orden inestable.

Con --with-manifest:
  - Lee el MANIFEST.sha256 versionado (si existe).
  - Regenera el manifiesto.
  - Comprueba que el nuevo manifiesto coincide con el versionado *antes*
    de cualquier commit; si el working tree ya tenía el manifiesto correcto,
    la segunda corrida no lo altera.

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

DERIVED_CSV = [
    "datasets/triad_nodes.csv",
    "datasets/vector_steps.csv",
    "datasets/relation_candidates.csv",
]


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def git_diff_paths(paths: list[str]) -> subprocess.CompletedProcess:
    return run(["git", "diff", "--ignore-space-at-eol", "--exit-code", "--", *paths])


def porcelain() -> str:
    return run(["git", "status", "--porcelain", "--", *DERIVED_CSV, "MANIFEST.sha256"]).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description="Punto fijo idempotente del repositorio")
    parser.add_argument(
        "--with-manifest",
        action="store_true",
        help="Incluir MANIFEST.sha256 en el punto fijo",
    )
    parser.add_argument(
        "--passes",
        type=int,
        default=2,
        help="Número de regeneraciones consecutivas (default 2 = prueba de estabilidad)",
    )
    args = parser.parse_args()

    print("=== self_bootstrap: punto fijo idempotente ===")
    print(f"Pasadas: {args.passes}  |  manifiesto: {args.with_manifest}")
    print()

    paths = list(DERIVED_CSV)
    if args.with_manifest:
        paths.append("MANIFEST.sha256")

    for i in range(1, args.passes + 1):
        print(f"--- pasada {i}/{args.passes} ---")
        r = run([sys.executable, "scripts/generate_ontology.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1

        if args.with_manifest:
            # Comparar manifiesto *versionado* (HEAD) con el que se acaba de regenerar
            # tras create_manifest: primero regenerar, luego diff contra HEAD.
            r = run([sys.executable, "scripts/create_manifest.py"])
            print(r.stdout, end="")
            if r.returncode != 0:
                print(r.stderr, file=sys.stderr)
                return 1

        r = git_diff_paths(paths)
        if r.returncode != 0:
            print(
                f"FALLO en pasada {i}: artefactos regenerados ≠ versionados (HEAD).",
                file=sys.stderr,
            )
            print(r.stdout or r.stderr, file=sys.stderr)
            print(
                "\nSi es la primera vez que regeneras tras un cambio de spec:\n"
                "  git add datasets/ MANIFEST.sha256 && git commit\n"
                "Luego vuelve a ejecutar self_bootstrap para confirmar S_n = S_{n+1}.",
                file=sys.stderr,
            )
            return 1

        dirty = porcelain().strip()
        if dirty:
            print(f"FALLO: working tree no limpio tras pasada {i}:\n{dirty}", file=sys.stderr)
            return 1
        print(f"OK pasada {i}: diff vacío, porcelain limpio")

    print()
    print("OK: punto fijo estable bajo iteración (S_{n+1} = S_n).")
    print("  Autonomía medible: regeneración idempotente desde iom_spec.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
