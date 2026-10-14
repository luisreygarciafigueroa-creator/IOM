#!/usr/bin/env python3
"""Puntúa la evaluación independiente y publica métricas de acuerdo.

Entradas (datasets/independent_eval/):
  - independent_pairs.csv (14 filas NR01–AM03)
  - annotator_pairs.csv (42 filas)
  - annotator_pairs_rule_application.csv (42 filas)
  - rule_reference.json
  - annotations.json

Salidas:
  - experiments/results/independent_eval_metrics.json
  - datasets/independent_eval/SCORE_REPORT.md

Uso:
  python scripts/score_independent_eval.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "datasets" / "independent_eval"
OUT_JSON = ROOT / "experiments" / "results" / "independent_eval_metrics.json"
OUT_MD = EVAL / "SCORE_REPORT.md"
LABELS = ["none", "mirrorOf", "creates", "unsure"]
EXPECTED_IDS = [
    "NR01", "NR02", "NR03", "CT01", "CT02", "CT03",
    "XT01", "XT02", "NC01", "NC02", "NC03", "AM01", "AM02", "AM03",
]


def fleiss_kappa(item_labels: list[list[str]], categories: list[str]) -> float:
    N = len(item_labels)
    k = len(item_labels[0])
    c = len(categories)
    idx = {lab: i for i, lab in enumerate(categories)}
    table = []
    for labs in item_labels:
        row = [0] * c
        for lab in labs:
            if lab not in idx:
                raise ValueError(f"Etiqueta desconocida: {lab}")
            row[idx[lab]] += 1
        table.append(row)
    P = [(sum(x * x for x in row) - k) / (k * (k - 1)) for row in table]
    P_bar = sum(P) / N
    totals = [sum(table[i][j] for i in range(N)) for j in range(c)]
    p = [t / (N * k) for t in totals]
    P_e = sum(pj * pj for pj in p)
    if abs(1 - P_e) < 1e-12:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    pairs = load_csv(EVAL / "independent_pairs.csv")
    ann_rows = load_csv(EVAL / "annotator_pairs.csv")
    rule_rows = load_csv(EVAL / "annotator_pairs_rule_application.csv")
    rule_ref = json.loads((EVAL / "rule_reference.json").read_text(encoding="utf-8"))
    annotations = json.loads((EVAL / "annotations.json").read_text(encoding="utf-8"))

    pair_ids = [r["id"] for r in pairs]
    errors: list[str] = []
    if len(pairs) != 14:
        errors.append(f"independent_pairs.csv: se esperaban 14 filas, hay {len(pairs)}")
    if pair_ids != EXPECTED_IDS:
        errors.append(f"IDs desalineados: {pair_ids}")
    if set(rule_ref.keys()) != set(pair_ids):
        errors.append("rule_reference.json no coincide con independent_pairs.csv")
    if len(ann_rows) != 42:
        errors.append(f"annotator_pairs.csv: se esperaban 42 filas, hay {len(ann_rows)}")
    if len(rule_rows) != 42:
        errors.append(f"annotator_pairs_rule_application.csv: se esperaban 42 filas, hay {len(rule_rows)}")

    pair_meta = {
        r["id"]: (r["source"], r["target"], r["source_label"], r["target_label"], r["kind"])
        for r in pairs
    }
    for r in ann_rows:
        key = (r["source"], r["target"], r["source_label"], r["target_label"], r["kind"])
        if key != pair_meta.get(r["id"]):
            errors.append(f"Metadatos desalineados en annotator_pairs para {r['id']}")
    for r in rule_rows:
        key = (r["source"], r["target"], r["source_label"], r["target_label"], r["kind"])
        if key != pair_meta.get(r["id"]):
            errors.append(f"Metadatos desalineados en rule_application para {r['id']}")
        if r["rule_label"] != rule_ref[r["id"]]["rule_label"]:
            errors.append(f"rule_label inconsistente en {r['id']}")

    if errors:
        print("ERROR de integridad:")
        for e in errors:
            print(" -", e)
        return 1

    by_item: dict[str, dict[str, str]] = defaultdict(dict)
    for r in ann_rows:
        by_item[r["id"]][r["annotator"]] = r["label"]

    item_label_lists = [[by_item[pid][a] for a in ("A1", "A2", "A3")] for pid in pair_ids]
    kappa = fleiss_kappa(item_label_lists, LABELS)
    unanimous = sum(1 for labs in item_label_lists if len(set(labs)) == 1)
    majority = sum(1 for labs in item_label_lists if Counter(labs).most_common(1)[0][1] >= 2)

    unsure_by_kind: dict[str, list[float]] = defaultdict(list)
    for r in pairs:
        labs = item_label_lists[pair_ids.index(r["id"])]
        rate = sum(1 for x in labs if x == "unsure") / 3
        unsure_by_kind[r["kind"]].append(rate)
    unsure_rate_by_kind = {k: round(sum(v) / len(v), 4) for k, v in sorted(unsure_by_kind.items())}

    comparable_ids = [i for i in pair_ids if rule_ref[i]["rule_label"] != "unspecified"]
    hits = total = 0
    for pid in comparable_ids:
        rl = rule_ref[pid]["rule_label"]
        for a in ("A1", "A2", "A3"):
            total += 1
            if by_item[pid][a] == rl:
                hits += 1
    posthoc = round(hits / total, 4) if total else None

    disagreements = []
    for pid, labs in zip(pair_ids, item_label_lists):
        if len(set(labs)) > 1:
            c = Counter(labs)
            top = c.most_common()
            maj = "tie" if len(top) >= 2 and top[0][1] == top[1][1] else top[0][0]
            disagreements.append({
                "id": pid,
                "kind": pair_meta[pid][4],
                "labels": {"A1": labs[0], "A2": labs[1], "A3": labs[2]},
                "majority": maj,
                "rule_label": rule_ref[pid]["rule_label"],
            })

    metrics = {
        "status": "completed",
        "integrity": "ok",
        "n_items": 14,
        "n_annotators": 3,
        "n_judgments": 42,
        "fleiss_kappa": round(kappa, 4),
        "unanimous_fraction": round(unanimous / 14, 4),
        "majority_fraction": round(majority / 14, 4),
        "unanimous_count": unanimous,
        "majority_count": majority,
        "unsure_rate_by_kind": unsure_rate_by_kind,
        "posthoc_agreement_with_rules": posthoc,
        "posthoc_comparable_judgments": total,
        "disagreements": disagreements,
        "control_unanimous": all(
            len(set(by_item[i][a] for a in ("A1", "A2", "A3"))) == 1
            for i in ("CT01", "CT02", "CT03")
        ),
        "out_of_rules_unanimous": all(
            len(set(by_item[i][a] for a in ("A1", "A2", "A3"))) == 1
            for i in ("NR01", "NR02", "NR03")
        ),
        "source_annotations_status": annotations.get("status"),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Informe de puntuación — evaluación independiente IOM",
        "",
        f"**Estado:** `{metrics['status']}`",
        f"**Integridad:** `{metrics['integrity']}`",
        f"**Ítems:** {metrics['n_items']} (NR01–AM03)",
        f"**Anotadores:** {metrics['n_annotators']} | **Juicios:** {metrics['n_judgments']}",
        "",
        "## Métricas",
        "",
        "| Métrica | Valor |",
        "|---|---:|",
        f"| Fleiss' κ | **{metrics['fleiss_kappa']:.4f}** |",
        f"| Unánime | {metrics['unanimous_fraction']:.4f} ({metrics['unanimous_count']}/14) |",
        f"| Mayoría (≥2) | {metrics['majority_fraction']:.4f} ({metrics['majority_count']}/14) |",
        f"| Acuerdo post-hoc con reglas | {metrics['posthoc_agreement_with_rules']:.4f} ({hits}/{total}) |",
        f"| Controles unánimes | {metrics['control_unanimous']} |",
        f"| Fuera-de-reglas unánimes | {metrics['out_of_rules_unanimous']} |",
        "",
        "## Desacuerdos",
        "",
    ]
    if disagreements:
        lines.append("| id | kind | A1 | A2 | A3 | mayoría | rule_label |")
        lines.append("|---|---|---|---|---|---|---|")
        for d in disagreements:
            lines.append(
                f"| {d['id']} | {d['kind']} | {d['labels']['A1']} | {d['labels']['A2']} | "
                f"{d['labels']['A3']} | {d['majority']} | {d['rule_label']} |"
            )
    else:
        lines.append("_Ningún desacuerdo._")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("OK — evaluación independiente puntuada")
    print(f"  Fleiss κ = {metrics['fleiss_kappa']:.4f}")
    print(f"  unánime  = {metrics['unanimous_count']}/14")
    print(f"  post-hoc = {metrics['posthoc_agreement_with_rules']}")
    print(f"  → {OUT_JSON}")
    print(f"  → {OUT_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
