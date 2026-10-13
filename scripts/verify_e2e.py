#!/usr/bin/env python3
"""Verificación integral de extremo a extremo (pipeline Python).

Ejecuta en secuencia, en un entorno limpio, los pasos de validación que no
requieren Lean (la compilación Lean se verifica por separado en CI o con
`lake build`). Confirma que no hay fallos ocultos de integración.

Uso:
    python scripts/verify_e2e.py
    python scripts/verify_e2e.py --skip-experiments   # solo validación formal
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    ("validate_spec", [sys.executable, "scripts/validate_spec.py"]),
    ("migrate_check", [sys.executable, "scripts/migrate_spec.py", "--check"]),
    ("sync_spec_artifacts", [sys.executable, "scripts/sync_spec_artifacts.py", "--check"]),
    ("generate_ontology", [sys.executable, "scripts/generate_ontology.py"]),
    ("unit_tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
    ("validate_shacl", [sys.executable, "scripts/validate_shacl.py"]),
]

EXPERIMENT_STEPS = [
    ("pi_hgat_t", [sys.executable, "experiments/pi_hgat_t.py"]),
    ("baselines", [sys.executable, "experiments/baselines.py"]),
    ("audit_report", [sys.executable, "scripts/generate_audit_report.py"]),
    ("metrics_audit", [sys.executable, "scripts/audit_perfect_metrics.py"]),
]


def run_step(name: str, cmd: list[str]) -> tuple[bool, float, str]:
    start = time.time()
    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=600,
        )
        elapsed = time.time() - start
        out = (result.stdout or "") + (result.stderr or "")
        ok = result.returncode == 0
        return ok, elapsed, out
    except subprocess.TimeoutExpired:
        return False, time.time() - start, f"TIMEOUT after 600s: {name}"
    except Exception as exc:
        return False, time.time() - start, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verificación e2e del pipeline IOM")
    parser.add_argument(
        "--skip-experiments",
        action="store_true",
        help="Omitir PI-HGAT-T, baselines y auditoría de métricas",
    )
    args = parser.parse_args()

    steps = list(STEPS)
    if not args.skip_experiments:
        steps.extend(EXPERIMENT_STEPS)

    print("=" * 60)
    print("IOM — verificación integral de extremo a extremo")
    print(f"Raíz: {ROOT}")
    print("=" * 60)

    failed = []
    for name, cmd in steps:
        print(f"\n>>> [{name}] {' '.join(cmd)}")
        ok, elapsed, out = run_step(name, cmd)
        status = "OK" if ok else "FAIL"
        print(f"    [{status}] {elapsed:.2f}s")
        if out.strip():
            # Mostrar últimas líneas para no inundar
            lines = out.strip().splitlines()
            for line in lines[-30:]:
                print(f"    | {line}")
        if not ok:
            failed.append(name)

    print("\n" + "=" * 60)
    if failed:
        print(f"RESULTADO: FALLÓ ({len(failed)} pasos): {', '.join(failed)}")
        return 1
    print(f"RESULTADO: TODOS LOS PASOS OK ({len(steps)} pasos)")
    print("Nota: la compilación Lean se verifica con `lake build` o el job CI 'lean'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
