#!/usr/bin/env python3
"""Invariancia interna (EXP-D bajo autonomía).

En lugar de reportar «accuracy contra un oracle externo», mide:

1. **Auto-regeneración de etiquetas**: cada par (source, target) recibe la
   misma etiqueta que produce la regla formal aplicada al par (fase, pos).
2. **Invariancia bajo permutación de índice de tríada**: la etiqueta no
   depende del número de tríada, solo de (fase, posición).
3. **Reconstrucción desde subconjunto**: leave-one-triad-out recoverable
   por lookup de features — el sistema regenera relaciones desde cualquier
   subconjunto propio de 12 tríadas.

Las métricas 1.0 se reportan como **invariancia**, no como «acierto vs juez».
"""
from __future__ import annotations

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


def main() -> int:
    rows = list(
        csv.DictReader(
            (ROOT / "datasets" / "relation_candidates.csv").open(
                encoding="utf-8", newline=""
            )
        )
    )

    # 1. Auto-regeneración: gold ≡ regla aplicada al par
    mismatches = [
        r for r in rows if rule_label(r["source"], r["target"]) != r["relation"]
    ]
    self_regen_rate = 1.0 - len(mismatches) / max(len(rows), 1)

    # 2. Invariancia bajo índice de tríada
    by_feat: dict[tuple, set[str]] = defaultdict(set)
    for r in rows:
        by_feat[feature_key(r["source"], r["target"])].add(r["relation"])
    ambiguous = {str(k): list(v) for k, v in by_feat.items() if len(v) > 1}
    triad_invariant = len(ambiguous) == 0

    # 3. Reconstrucción desde subconjunto (LOO feature lookup)
    fold_ok = {}
    for held in range(1, 14):
        train = {}
        test = []
        for r in rows:
            key = feature_key(r["source"], r["target"])
            tid = int(r["triad_index"])
            if tid == held:
                test.append((key, r["relation"]))
            else:
                train[key] = r["relation"]
        recoverable = sum(1 for k, lab in test if train.get(k) == lab)
        fold_ok[held] = recoverable / max(len(test), 1)
    all_folds_invariant = all(v == 1.0 for v in fold_ok.values())

    report = {
        "framing": (
            "Métricas de INVARIANCIA (autonomía), no de accuracy contra "
            "oracle externo. El sistema regenera sus relaciones desde sí mismo."
        ),
        "self_regeneration": {
            "rate": round(self_regen_rate, 6),
            "mismatches": len(mismatches),
            "interpretation": "fracción de pares cuya etiqueta es reconstruible solo desde (fase, pos)",
        },
        "triad_index_invariance": {
            "holds": triad_invariant,
            "ambiguous_feature_keys": ambiguous,
            "interpretation": "la etiqueta no depende del índice de tríada",
        },
        "reconstruction_from_proper_subset": {
            "per_fold_recoverable_fraction": fold_ok,
            "all_folds_full_reconstruction": all_folds_invariant,
            "interpretation": (
                "desde cualquier subconjunto de 12 tríadas se regeneran "
                "las relaciones de la 13ª (punto fijo parcial)"
            ),
        },
        "invariance_summary": {
            "self_regeneration": self_regen_rate == 1.0,
            "triad_index_invariance": triad_invariant,
            "subset_reconstruction": all_folds_invariant,
            "autonomy_measurable": (
                self_regen_rate == 1.0 and triad_invariant and all_folds_invariant
            ),
        },
    }

    out = ROOT / "experiments" / "results" / "invariance_metrics.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    inv = report["invariance_summary"]
    print("Invariancia interna (autonomía medible)")
    print(f"  Auto-regeneración de etiquetas: {report['self_regeneration']['rate']}")
    print(f"  Invariancia bajo índice de tríada: {inv['triad_index_invariance']}")
    print(f"  Reconstrucción desde subconjunto: {inv['subset_reconstruction']}")
    print(f"  Autonomía medible (las tres): {inv['autonomy_measurable']}")
    print(f"  Informe: {out}")
    return 0 if inv["autonomy_measurable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
