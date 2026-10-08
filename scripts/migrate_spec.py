#!/usr/bin/env python3
"""Aplica migraciones declarativas a data/iom_spec.json.

Las migraciones se registran en el campo `migrations` del propio JSON.
Este script solo registra y valida; las transformaciones semánticas futuras
deben implementarse como funciones nombradas en MIGRATION_HANDLERS.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "data" / "iom_spec.json"

# Handlers de migración (from_version -> función). Vacío en 1.1.0 porque el
# cambio fue solo metadatos.
MIGRATION_HANDLERS: dict[str, callable] = {}


def load() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    SPEC_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def list_migrations(data: dict) -> None:
    migrations = data.get("migrations") or []
    if not migrations:
        print("No hay migraciones registradas.")
        return
    for m in migrations:
        print(f"  {m['from_version']} -> {m['to_version']}: {m['description']} ({m.get('date', '?')})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gestión de migraciones de iom_spec.json")
    parser.add_argument("--list", action="store_true", help="Listar migraciones registradas")
    parser.add_argument("--check", action="store_true", help="Verificar que spec_version es coherente")
    args = parser.parse_args()

    data = load()
    if args.list:
        print(f"spec_version actual: {data.get('spec_version')}")
        list_migrations(data)
        return
    if args.check:
        version = data.get("spec_version")
        migrations = data.get("migrations") or []
        if migrations:
            last = migrations[-1]["to_version"]
            if last != version:
                raise SystemExit(f"Inconsistencia: último to_version={last} pero spec_version={version}")
        print(f"OK: spec_version={version} coherente con historial de migraciones")
        return
    parser.print_help()


if __name__ == "__main__":
    main()
