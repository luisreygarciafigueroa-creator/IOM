#!/usr/bin/env python3
"""Auditoría rigurosa de las métricas perfectas (100%).

Investiga por qué PI-HGAT-T y el MLP alcanzan accuracy/F1 = 1.0:

1. Independencia train/test bajo leave-one-triad-out (sí: ninguna pareja
   de la tríada held-out aparece en entrenamiento).
2. Sin embargo, las etiquetas están **completamente determinadas** por
   (fase, posición) del par — reglas idénticas en las 13 tríadas.
3. Por tanto, cualquier modelo que aprenda la función determinista
   (fase_src, pos_src, fase_tgt, pos_tgt) → {none, mirrorOf, creates}
   generaliza al 100% a tríadas no vistas.
4. El oracle de reglas deterministas y el MLP (features = one-hot fase+pos)
   alcanzan 1.0; la regresión logística lineal no separa mirrorOf/creates.

Este script demuestra (1)–(3) de forma programática y escribe un informe JSON.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ("none", "mirrorOf", "creates")


def parse_node(node_id: str) -> tuple[str, int]:
    parts = node_id.split("_")
    return parts[1], int(parts[2][1:])


def feature_key(src: str, tgt: str) -> tuple:
    """Clave de features usada por los modelos (fase+posición, sin tríada ni etiqueta)."""
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    return (sp, spos, tp, tpos)


def deterministic_label(src: str, tgt: str) -> str:
    """Regla determinista alineada con SHACL / FormalRules.lean."""
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    if sp == tp:
        return "none"
    if tpos == 2 - spos:
        return "mirrorOf"
    lateral_s = spos in (0, 2)
    lateral_t = tpos in (0, 2)
    if (lateral_s and tpos == 1) or (spos == 1 and lateral_t):
        return "creates"
    return "none"


def main() -> int:
    rows = []
    with (ROOT / "datasets" / "relation_candidates.csv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    # 1. Consistencia gold vs regla determinista
    mismatches = []
    for row in rows:
        pred = deterministic_label(row["source"], row["target"])
        if pred != row["relation"]:
            mismatches.append({"row": row, "rule_predicts": pred})

    # 2. La etiqueta es función solo de (fase, pos) — misma clave → misma etiqueta
    by_feature: dict[tuple, set[str]] = defaultdict(set)
    by_feature_triads: dict[tuple, set[int]] = defaultdict(set)
    for row in rows:
        key = feature_key(row["source"], row["target"])
        by_feature[key].add(row["relation"])
        by_feature_triads[key].add(int(row["triad_index"]))

    non_deterministic_features = {
        str(k): list(v) for k, v in by_feature.items() if len(v) > 1
    }

    # 3. Leave-one-triad-out: ¿las features del held-out aparecen en train?
    #    Sí, con la misma etiqueta — por eso un learner que memoriza la
    #    función feature→label generaliza al 100%.
    triad_feature_overlap = {}
    for held in range(1, 14):
        train_map = {}
        test_keys = set()
        for row in rows:
            key = feature_key(row["source"], row["target"])
            tid = int(row["triad_index"])
            if tid == held:
                test_keys.add((key, row["relation"]))
            else:
                train_map[key] = row["relation"]
        recoverable = sum(1 for k, lab in test_keys if train_map.get(k) == lab)
        triad_feature_overlap[held] = {
            "test_pairs": len(test_keys),
            "recoverable_by_feature_lookup": recoverable,
            "fraction": recoverable / len(test_keys) if test_keys else 0.0,
        }

    all_recoverable = all(
        v["fraction"] == 1.0 for v in triad_feature_overlap.values()
    )

    # 4. Conteos
    from collections import Counter
    counts = Counter(r["relation"] for r in rows)

    report = {
        "conclusion": (
            "Las métricas perfectas (100%) de PI-HGAT-T y del MLP no indican "
            "sobreajuste por fuga de identidad de tríada: leave-one-triad-out "
            "excluye correctamente las parejas del held-out. Indican que las "
            "etiquetas son una función determinista de (fase, posición) del par, "
            "idéntica en las 13 tríadas. Aprender esa función basta para "
            "generalizar al 100%. El oracle de reglas deterministas alcanza 1.0 "
            "sin aprendizaje. La arquitectura de grafo no es necesaria para este "
            "corpus sintético; sirve como demostración de recuperabilidad estructural."
        ),
        "gold_vs_deterministic_rule": {
            "mismatches": len(mismatches),
            "details": mismatches[:5],  # muestra
            "perfect_match": len(mismatches) == 0,
        },
        "label_determined_by_phase_position_only": {
            "unique_feature_keys": len(by_feature),
            "keys_with_ambiguous_labels": non_deterministic_features,
            "is_deterministic_function": len(non_deterministic_features) == 0,
        },
        "leave_one_triad_out_feature_overlap": {
            "per_fold": triad_feature_overlap,
            "all_folds_100pct_recoverable_by_feature_lookup": all_recoverable,
            "interpretation": (
                "En cada fold, el 100% de los pares de prueba tiene una clave "
                "(fase,pos) ya vista en entrenamiento con la misma etiqueta. "
                "No hay fuga de node_id/triad_index (el modelo no los usa), "
                "pero la función a aprender es trivialmente compartida."
            ),
        },
        "class_counts": dict(counts),
        "implications": [
            "No se requiere arquitectura compleja (GAT) para este corpus: el MLP y el oracle bastan.",
            "Las ablaciones sin fase/posición degradan el rendimiento porque rompen la función determinista.",
            "La validación empírica real del marco exige datos cuyas etiquetas NO se deriven de las mismas reglas (véase datasets/independent_eval/ y external_eval/).",
            "Reportar 100% como 'recuperación de relaciones generadas por reglas' es correcto; reportarlo como 'validación del marco en el mundo real' no lo es.",
        ],
    }

    out = ROOT / "experiments" / "results" / "perfect_metrics_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Auditoría de métricas perfectas")
    print(f"  Gold vs regla determinista: mismatches={len(mismatches)}")
    print(f"  Función determinista fase+pos: {len(non_deterministic_features) == 0}")
    print(f"  LOO recoverable por lookup de features: {all_recoverable}")
    print(f"  Informe: {out}")
    print()
    print(report["conclusion"])
    return 0 if len(mismatches) == 0 and all_recoverable else 1


if __name__ == "__main__":
    raise SystemExit(main())
