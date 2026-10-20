#!/usr/bin/env python3
"""Sincronización y verificación bidireccional entre especificación y artefactos.

Garantiza que data/iom_spec.json, los CSV generados, la ontología y los conteos
de pruebas permanecen coherentes. Con --check solo verifica; con --fix regenera
vía generate_ontology.py y vuelve a verificar.

Uso:
    python scripts/sync_spec_artifacts.py --check
    python scripts/sync_spec_artifacts.py --fix
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "data" / "iom_spec.json"


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def count_csv(name: str) -> int:
    path = ROOT / "datasets" / name
    if not path.is_file():
        return -1
    with path.open(encoding="utf-8", newline="") as fh:
        return len(list(csv.DictReader(fh)))


def expected_counts(spec: dict) -> dict:
    n_triads = len(spec["triads"]["adv"])
    n_positions = len(spec["positions"]["indices"])
    n_vectors = len(spec["vectors"])
    steps_per_vector = len(spec["vectors"][0]["labels"]) if spec["vectors"] else 5
    # 6 nodos por tríada (2 fases × 3 pos), 5 destinos no reflexivos → 6*5=30 pares/tríada
    pairs_per_triad = (2 * n_positions) * (2 * n_positions - 1)
    # creates: 4 rules × product of position lists × n_triads
    creates = 0
    for rule in spec["creation_rules"]:
        creates += len(rule["source_positions"]) * len(rule["target_positions"]) * n_triads
    # mirrorOf: 3 posiciones × 2 direcciones × n_triads = 6 * n_triads
    mirrors = n_positions * 2 * n_triads
    nodes = n_triads * 2 * n_positions
    pairs = n_triads * pairs_per_triad
    none = pairs - mirrors - creates
    return {
        "n_triads": n_triads,
        "nodes": nodes,
        "vector_steps": n_vectors * steps_per_vector,
        "relation_candidates": pairs,
        "mirrorOf": mirrors,
        "creates": creates,
        "none": none,
    }


def check(spec: dict) -> list[str]:
    errors = []
    exp = expected_counts(spec)

    # Versión
    if not spec.get("spec_version"):
        errors.append("Falta spec_version")
    migrations = spec.get("migrations") or []
    if migrations and migrations[-1].get("to_version") != spec.get("spec_version"):
        errors.append(
            f"spec_version={spec.get('spec_version')} != último to_version={migrations[-1].get('to_version')}"
        )

    # Conteos CSV
    actual_nodes = count_csv("triad_nodes.csv")
    actual_vecs = count_csv("vector_steps.csv")
    actual_rels = count_csv("relation_candidates.csv")

    if actual_nodes != exp["nodes"]:
        errors.append(f"triad_nodes.csv: {actual_nodes} filas, esperado {exp['nodes']}")
    if actual_vecs != exp["vector_steps"]:
        errors.append(f"vector_steps.csv: {actual_vecs} filas, esperado {exp['vector_steps']}")
    if actual_rels != exp["relation_candidates"]:
        errors.append(
            f"relation_candidates.csv: {actual_rels} filas, esperado {exp['relation_candidates']}"
        )

    # Conteos de relaciones
    if actual_rels > 0:
        with (ROOT / "datasets" / "relation_candidates.csv").open(encoding="utf-8", newline="") as fh:
            from collections import Counter
            c = Counter(r["relation"] for r in csv.DictReader(fh))
        for key in ("mirrorOf", "creates", "none"):
            if c.get(key, 0) != exp[key]:
                errors.append(f"relación {key}: {c.get(key, 0)}, esperado {exp[key]}")

    # Ontología existe y menciona version-ish content
    ttl = ROOT / "ontology" / "io_ontology.ttl"
    if not ttl.is_file():
        errors.append("Falta ontology/io_ontology.ttl")
    else:
        text = ttl.read_text(encoding="utf-8")
        if "mirrorOf" not in text or "creates" not in text:
            errors.append("io_ontology.ttl no contiene mirrorOf/creates")

    # Schema
    schema = ROOT / "data" / "iom_spec.schema.json"
    if not schema.is_file():
        errors.append("Falta data/iom_spec.schema.json")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Solo verificar sincronización")
    parser.add_argument("--fix", action="store_true", help="Regenerar artefactos y verificar")
    args = parser.parse_args()

    if not args.check and not args.fix:
        args.check = True

    if args.fix:
        print("Regenerando ontología y datasets…")
        r = subprocess.run(
            [sys.executable, "scripts/generate_ontology.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            print(r.stdout)
            print(r.stderr, file=sys.stderr)
            return 1
        print(r.stdout.strip())

    spec = load_spec()
    errors = check(spec)
    exp = expected_counts(spec)

    print(f"spec_version={spec.get('spec_version')}  schema_version={spec.get('schema_version')}")
    print(f"Esperado: nodos={exp['nodes']} vectores={exp['vector_steps']} "
          f"pares={exp['relation_candidates']} "
          f"(mirror={exp['mirrorOf']} creates={exp['creates']} none={exp['none']})")

    if errors:
        print("INCONSISTENCIAS:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: especificación, CSV y ontología sincronizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
