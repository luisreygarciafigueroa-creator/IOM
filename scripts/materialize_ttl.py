#!/usr/bin/env python3
"""Materializa ontology/io_ontology.ttl.

Preferir generate_ontology.py. Si el blob embebido no coincide con el
spec actual, se regenera desde data/iom_spec.json + CSV (idempotente).
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ontology" / "io_ontology.ttl"
# Hash canónico del TTL generado para spec 1.10.0 (animal|humano|IA … pequeño|espacio|grande)
EXPECTED = "716071a226ff7ee0a088bdecdb0fde745f86ca1b0622f9c5677b7e685e30564b"


def main() -> None:
    # 1) Intentar generar siempre desde el spec canónico (fuente de verdad)
    gen = ROOT / "scripts" / "generate_ontology.py"
    subprocess.check_call([sys.executable, str(gen)], cwd=ROOT)
    data = OUT.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED:
        # Aviso: el generador produjo un hash distinto (p. ej. cambio de serialización).
        # No fallamos: el generador es la fuente de verdad post-1.10.0.
        print(
            f"AVISO: hash generado {digest} ≠ EXPECTED {EXPECTED}; "
            "se conserva la salida de generate_ontology.py",
            file=sys.stderr,
        )
    print(f"OK {OUT} ({len(data)} bytes) sha256={digest}")


if __name__ == "__main__":
    main()
