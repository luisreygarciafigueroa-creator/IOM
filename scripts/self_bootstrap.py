#!/usr/bin/env python3
"""Punto fijo del repositorio: auto-creación estable bajo iteración.

  python scripts/self_bootstrap.py --passes 2
  python scripts/self_bootstrap.py --with-manifest --passes 2

Con --with-manifest:
  1. Regenera CSV + MANIFEST.sha256
  2. Exige identidad con HEAD (git diff vacío)
  3. **Cobertura dura:** archivos críticos del árbol deben aparecer en el
     manifiesto regenerado; si faltan, falla (no es decorativo).
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

# Deben estar en MANIFEST si existen en disco (runners y protocolo de sentido).
CRITICAL_IF_PRESENT = [
    "scripts/self_bootstrap.py",
    "scripts/measure_invariance.py",
    "scripts/create_manifest.py",
    "scripts/generate_ontology.py",
    "IOM/SelfGenesis.lean",
    "IOM/FormalRules.lean",
    "MANIFIESTO.md",
    "docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md",
    "datasets/independent_eval/instrument/INSTRUCTIONS.md",
    "datasets/independent_eval/instrument/pairs.csv",
    "datasets/independent_eval/instrument/ACCESS_LOG.template.json",
]


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def git_diff_paths(paths: list[str]) -> subprocess.CompletedProcess:
    return run(["git", "diff", "--ignore-space-at-eol", "--exit-code", "--", *paths])


def porcelain(paths: list[str]) -> str:
    return run(["git", "status", "--porcelain", "--", *paths]).stdout


def manifest_paths(manifest_file: Path) -> set[str]:
    out: set[str] = set()
    for line in manifest_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        # "<hash>  <path>"
        parts = line.split("  ", 1)
        if len(parts) == 2:
            out.add(parts[1])
    return out


def check_manifest_coverage() -> list[str]:
    """Devuelve lista de críticos presentes en disco pero ausentes del manifiesto."""
    mf = ROOT / "MANIFEST.sha256"
    if not mf.is_file():
        return ["MANIFEST.sha256 (archivo inexistente)"]
    listed = manifest_paths(mf)
    missing = []
    for rel in CRITICAL_IF_PRESENT:
        p = ROOT / rel
        if p.is_file() and rel not in listed:
            missing.append(rel)
    return missing


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

            missing = check_manifest_coverage()
            if missing:
                print(
                    "FALLO de cobertura del manifiesto — archivos críticos en disco "
                    "pero ausentes de MANIFEST.sha256:",
                    file=sys.stderr,
                )
                for m in missing:
                    print(f"  - {m}", file=sys.stderr)
                print(
                    "\nEsto no es un warning: el punto fijo con --with-manifest "
                    "exige cobertura. Revisa create_manifest.py INCLUDE_* / exclusiones.",
                    file=sys.stderr,
                )
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
                    "\nVersiona el manifiesto actualizado:\n"
                    "  python scripts/create_manifest.py\n"
                    "  git add MANIFEST.sha256 && git commit -m 'chore: refresh MANIFEST'\n"
                    "  python scripts/self_bootstrap.py --with-manifest --passes 2",
                    file=sys.stderr,
                )
            return 1

        dirty = porcelain(paths).strip()
        if dirty:
            print(f"FALLO: porcelain no limpio:\n{dirty}", file=sys.stderr)
            return 1
        print(f"OK pasada {i}: diff vacío, porcelain limpio"
              + (", cobertura crítica OK" if args.with_manifest else ""))

    print()
    print("OK: punto fijo estable (S_{n+1} = S_n).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
