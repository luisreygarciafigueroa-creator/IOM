#!/usr/bin/env python3
"""Verificación de extremo a extremo (incluye capa opcional)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    ("self_bootstrap", [sys.executable, "scripts/self_bootstrap.py", "--passes", "2"]),
    ("validate_spec", [sys.executable, "scripts/validate_spec.py"]),
    ("validate_shacl", [sys.executable, "scripts/validate_shacl.py"]),
    ("measure_invariance", [sys.executable, "scripts/measure_invariance.py"]),
    ("pi_hgat_t", [sys.executable, "experiments/optional/pi_hgat_t.py"]),
    ("baselines", [sys.executable, "experiments/optional/baselines.py"]),
]


def main() -> int:
    for name, cmd in STEPS:
        print(f">>> {name}")
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode != 0:
            print(f"FAIL: {name}", file=sys.stderr)
            return r.returncode
    print("OK: e2e completo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
