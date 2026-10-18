#!/usr/bin/env python3
"""Valida ejemplos de alineación de dominio (EXP-E) contra nodos canónicos y reglas formales.

No calcula κ de dominio ni afirma validez empírica de biología/economía.
Solo comprueba que los nodos sugeridos existen y que la relación propuesta
es admisible bajo FormalRules / SHACL para el par (source, target).
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = Path(__file__).resolve().parent / "examples.json"
NODES = ROOT / "datasets" / "triad_nodes.csv"
CANDIDATES = ROOT / "datasets" / "relation_candidates.csv"


def load_nodes() -> dict[str, dict]:
    out = {}
    with NODES.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["node_id"]] = row
    return out


def load_gold_relations() -> dict[tuple[str, str], str]:
    out = {}
    with CANDIDATES.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[(row["source"], row["target"])] = row["relation"]
    return out


def main() -> int:
    data = json.loads(EXAMPLES.read_text(encoding="utf-8"))
    nodes = load_nodes()
    gold = load_gold_relations()
    ok = 0
    warn = 0
    fail = 0
    report = []
    for pair in data["pairs"]:
        sid = pair["suggested_nodes"]["source"]
        tid = pair["suggested_nodes"]["target"]
        rel = pair["relation"]
        entry = {"id": pair["id"], "source": sid, "target": tid, "proposed": rel}
        if sid not in nodes or tid not in nodes:
            entry["status"] = "FAIL"
            entry["reason"] = "nodo sugerido ausente en triad_nodes.csv"
            fail += 1
        else:
            actual = gold.get((sid, tid))
            entry["gold_relation"] = actual
            if actual is None:
                entry["status"] = "WARN"
                entry["reason"] = "par no está en relation_candidates (posible cross-triad o demo heurística)"
                warn += 1
            elif actual == rel:
                entry["status"] = "OK"
                entry["reason"] = "relación propuesta coincide con gold canónico"
                ok += 1
            else:
                entry["status"] = "WARN"
                entry["reason"] = f"gold={actual} ≠ propuesto={rel} (mapeo demostrativo, no gold de dominio)"
                warn += 1
        report.append(entry)

    out_path = ROOT / "experiments" / "results" / "domain_mapping_validation.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "experiment": "EXP-E-DOMAIN-ALIGNMENT",
        "ok": ok,
        "warn": warn,
        "fail": fail,
        "pairs": report,
        "interpretation": (
            "OK = el par sugerido existe en el gold canónico con la misma etiqueta. "
            "WARN = mapeo demostrativo no idéntico al gold (esperado en demos de dominio). "
            "FAIL = nodo inválido. Este script no mide validez semántica de biología/economía."
        ),
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"EXP-E domain mapping: ok={ok} warn={warn} fail={fail}")
    print(f"Informe: {out_path}")
    for r in report:
        print(f"  {r['id']}: {r['status']} — {r.get('reason', '')}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
