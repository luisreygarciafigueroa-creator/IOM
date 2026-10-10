#!/usr/bin/env python3
"""Valida data/iom_spec.json contra data/iom_spec.schema.json."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "data" / "iom_spec.json"
SCHEMA_PATH = ROOT / "data" / "iom_spec.schema.json"


def _minimal_validate() -> int:
    """Fallback sin jsonschema: comprueba campos obligatorios y conteos."""
    data = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    required = [
        "schema_version",
        "spec_version",
        "title",
        "source_date",
        "positions",
        "perspectives",
        "phases",
        "triads",
        "vectors",
        "creation_rules",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        print(f"ERROR: faltan campos {missing}", file=sys.stderr)
        print(f"  archivo: {SPEC_PATH}", file=sys.stderr)
        print(f"  claves presentes: {sorted(data.keys())}", file=sys.stderr)
        return 1
    if "adv" not in data.get("triads", {}) or "ret" not in data.get("triads", {}):
        print("ERROR: triads debe contener 'adv' y 'ret'", file=sys.stderr)
        return 1
    if len(data["triads"]["adv"]) != len(data["triads"]["ret"]):
        print("ERROR: triads.adv y triads.ret deben tener la misma longitud", file=sys.stderr)
        return 1
    if len(data["positions"]) != 3:
        print("ERROR: positions debe tener exactamente 3 elementos", file=sys.stderr)
        return 1
    print(f"OK (validación mínima): {SPEC_PATH.name}")
    print(f"  schema_version={data.get('schema_version')}  spec_version={data.get('spec_version')}")
    return 0


def main() -> int:
    require_jsonschema = os.environ.get("IOM_REQUIRE_JSONSCHEMA", "").lower() in {"1", "true", "yes"}
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        msg = (
            "jsonschema no instalado; se realiza validación estructural mínima.\n"
            "  Instalar: python -m pip install -r requirements-lock.txt"
        )
        print(msg, file=sys.stderr)
        if require_jsonschema:
            print("ERROR: IOM_REQUIRE_JSONSCHEMA=1 exige jsonschema en este entorno.", file=sys.stderr)
            return 1
        return _minimal_validate()

    if not SPEC_PATH.is_file():
        print(f"ERROR: no existe {SPEC_PATH}", file=sys.stderr)
        return 1
    if not SCHEMA_PATH.is_file():
        print(f"ERROR: no existe {SCHEMA_PATH}", file=sys.stderr)
        return 1

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    instance = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        for err in errors:
            path = ".".join(str(p) for p in err.path) or "<root>"
            print(f"ERROR {path}: {err.message}", file=sys.stderr)
        return 1
    print(f"OK: {SPEC_PATH.name} cumple el esquema {SCHEMA_PATH.name}")
    print(
        f"  schema_version={instance.get('schema_version')}  "
        f"spec_version={instance.get('spec_version')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
