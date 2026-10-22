#!/usr/bin/env python3
"""Punto fijo del repositorio: auto-creación estable bajo iteración.

  python scripts/self_bootstrap.py --passes 2
  python scripts/self_bootstrap.py --with-manifest --passes 2

CSV siempre; MANIFEST solo con --with-manifest (versionar el manifiesto
tras cambios de árbol: create_manifest.py && git add MANIFEST.sha256).
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


def porcelain(paths: list[str]) -> str:
    return run(["git", "status", "--porcelain", "--", *paths]).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description="Punto fijo idempotente")
    parser.add_argument("--with-manifest", action="store_true")
    parser.add_argument("--passes", type=int, default=2)
    args = parser.parse_args()

    paths = list(DERIVED_CSV)
    if args.with_manifest:
        paths.append("MANIFEST.sha256")

    print("=== self_bootstrap: punto fijo idempotente ===")
    print(f"Pasadas: {args.passes}  |  manifiesto: {args.with_manifest}")
    print()

    for i in range(1, args.passes + 1):
        print(f"--- pasada {i}/{args.passes} ---")
        r = run([sys.executable, "scripts/generate_ontology.py"])
        print(r.stdout, end="")
        if r.returncode != 0:
            print(r.stderr, file=sys.stderr)
            return 1

        if args.with_manifest:
            r = run([sys.executable, "scripts/create_manifest.py"])
            print(r.stdout, end="")
            if r.returncode != 0:
                print(r.stderr, file=sys.stderr)
                return 1

        r = git_diff_paths(paths)
        if r.returncode != 0:
            print(
                f"FALLO en pasada {i}: regenerado ≠ HEAD en {paths}",
                file=sys.stderr,
            )
            print(r.stdout or r.stderr, file=sys.stderr)
            if args.with_manifest:
                print(
                    "\nSi el árbol cambió, versiona el manifiesto:\n"
                    "  python scripts/create_manifest.py\n"
                    "  git add MANIFEST.sha256 && git commit -m 'chore: refresh MANIFEST'\n"
                    "Luego: python scripts/self_bootstrap.py --with-manifest --passes 2",
                    file=sys.stderr,
                )
            return 1

        dirty = porcelain(paths).strip()
        if dirty:
            print(f"FALLO: porcelain no limpio:\n{dirty}", file=sys.stderr)
            return 1
        print(f"OK pasada {i}: diff vacío, porcelain limpio")

    print()
    print("OK: punto fijo estable (S_{n+1} = S_n).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
