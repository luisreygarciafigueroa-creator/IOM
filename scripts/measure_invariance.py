#!/usr/bin/env python3
"""Invariancia interna no trivial (con control negativo).

Mide autonomía *y* distingue el grafo canónico de uno corrompido:

1. Auto-regeneración: etiqueta ≡ regla (fase, pos) aplicada al par.
2. Invariancia bajo índice de tríada.
3. Reconstrucción desde subconjunto (LOO feature lookup sin etiquetas del held-out).
4. **Control negativo:** al corromper una arista del grafo, (1) o (3) debe fallar.

Sin el control negativo, un 1.0 podría ser tautología.
"""
from __future__ import annotations

import copy
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_node(node_id: str) -> tuple[str, int]:
    parts = node_id.split("_")
    return parts[1], int(parts[2][1:])


def rule_label(src: str, tgt: str) -> str:
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    if sp == tp:
        return "none"
    if tpos == 2 - spos:
        return "mirrorOf"
    if (spos in (0, 2) and tpos == 1) or (spos == 1 and tpos in (0, 2)):
        return "creates"
    return "none"


def feature_key(src: str, tgt: str) -> tuple:
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    return (sp, spos, tp, tpos)


def self_regen_rate(rows: list[dict]) -> float:
    mism = sum(1 for r in rows if rule_label(r["source"], r["target"]) != r["relation"])
    return 1.0 - mism / max(len(rows), 1)


def triad_invariant(rows: list[dict]) -> bool:
    by_feat: dict[tuple, set[str]] = defaultdict(set)
    for r in rows:
        by_feat[feature_key(r["source"], r["target"])].add(r["relation"])
    return all(len(v) == 1 for v in by_feat.values())


def subset_reconstruction(rows: list[dict]) -> bool:
    for held in range(1, 14):
        train: dict[tuple, str] = {}
        test: list[tuple[tuple, str]] = []
        for r in rows:
            key = feature_key(r["source"], r["target"])
            tid = int(r["triad_index"])
            if tid == held:
                test.append((key, r["relation"]))
            else:
                train[key] = r["relation"]
        if any(train.get(k) != lab for k, lab in test):
            return False
    return True


def corrupt_one_edge(rows: list[dict]) -> list[dict]:
    """Cambia la etiqueta de la primera arista mirrorOf a none (grafo inválido)."""
    out = copy.deepcopy(rows)
    for r in out:
        if r["relation"] == "mirrorOf":
            r["relation"] = "none"
            break
    return out


def main() -> int:
    rows = list(
        csv.DictReader(
            (ROOT / "datasets" / "relation_candidates.csv").open(
                encoding="utf-8", newline=""
            )
        )
    )

    regen = self_regen_rate(rows)
    inv = triad_invariant(rows)
    subset = subset_reconstruction(rows)

    corrupted = corrupt_one_edge(rows)
    # Tras corrupción: o bien auto-regeneración cae, o el grafo ya no coincide con la regla
    corrupted_regen = self_regen_rate(corrupted)
    negative_control_detects = corrupted_regen < 1.0

    autonomy = regen == 1.0 and inv and subset
    non_trivial = autonomy and negative_control_detects

    report = {
        "framing": (
            "Invariancia no trivial: el canónico regenera 1.0; un grafo con una "
            "arista corrupta debe fallar el control negativo."
        ),
        "canonical": {
            "self_regeneration_rate": round(regen, 6),
            "triad_index_invariance": inv,
            "subset_reconstruction": subset,
            "autonomy_measurable": autonomy,
        },
        "negative_control": {
            "description": "primera arista mirrorOf relabelada a none",
            "corrupted_self_regeneration_rate": round(corrupted_regen, 6),
            "detects_corruption": negative_control_detects,
            "interpretation": (
                "si detects_corruption es false, la métrica no distingue "
                "grafo correcto de corrompido (tautología)"
            ),
        },
        "invariance_non_trivial": non_trivial,
    }

    out = ROOT / "experiments" / "results" / "invariance_metrics.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("Invariancia interna (con control negativo)")
    print(f"  Auto-regeneración canónica: {regen}")
    print(f"  Invariancia bajo índice de tríada: {inv}")
    print(f"  Reconstrucción desde subconjunto: {subset}")
    print(f"  Control negativo detecta corrupción: {negative_control_detects} (rate={corrupted_regen:.6f})")
    print(f"  Invariancia no trivial: {non_trivial}")
    print(f"  Informe: {out}")
    return 0 if non_trivial else 1


if __name__ == "__main__":
    raise SystemExit(main())
