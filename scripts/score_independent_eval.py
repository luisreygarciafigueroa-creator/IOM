#!/usr/bin/env python3
"""Scoring post-hoc de evaluación independiente (capa C).

Compara anotaciones humanas (annotations_template rellenado) con:
  - acuerdo inter-anotador (mayoría, Fleiss' kappa simplificado)
  - rule_reference (solo post-hoc; no es el objetivo primario)

Uso:
    python scripts/score_independent_eval.py
    python scripts/score_independent_eval.py --annotations path/to/filled.json
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "datasets" / "independent_eval"


def fleiss_kappa(ratings: list[list[str]], categories: list[str]) -> float:
    """Fleiss' kappa para N ítems, k anotadores, c categorías.
    ratings[i] = lista de etiquetas de los anotadores para el ítem i.
    """
    n_items = len(ratings)
    if n_items == 0:
        return 0.0
    n_raters = len(ratings[0])
    if n_raters < 2:
        return 0.0
    # tabla N_ij
    cat_idx = {c: i for i, c in enumerate(categories)}
    table = []
    for row in ratings:
        counts = [0] * len(categories)
        for lab in row:
            if lab in cat_idx:
                counts[cat_idx[lab]] += 1
        table.append(counts)
    # P_i
    P = []
    for counts in table:
        s = sum(c * (c - 1) for c in counts)
        P.append(s / (n_raters * (n_raters - 1)))
    P_bar = sum(P) / n_items
    # p_j
    totals = [sum(table[i][j] for i in range(n_items)) for j in range(len(categories))]
    p = [t / (n_items * n_raters) for t in totals]
    P_e = sum(pj ** 2 for pj in p)
    if abs(1 - P_e) < 1e-12:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--annotations",
        type=Path,
        default=EVAL_DIR / "annotations_template.json",
        help="JSON de anotaciones (plantilla o rellenado)",
    )
    args = parser.parse_args()

    if not args.annotations.is_file():
        print(f"No se encontró {args.annotations}")
        print("Rellena annotations_template.json con ≥3 anotadores y vuelve a ejecutar.")
        return 1

    data = json.loads(args.annotations.read_text(encoding="utf-8"))
    rule_ref = {}
    ref_path = EVAL_DIR / "rule_reference.json"
    if ref_path.is_file():
        raw = json.loads(ref_path.read_text(encoding="utf-8"))
        # soporta lista de {id, rule_label} o dict
        if isinstance(raw, list):
            rule_ref = {item["id"]: item.get("rule_label") for item in raw if "id" in item}
        elif isinstance(raw, dict):
            rule_ref = raw.get("labels") or raw

    # Normalizar anotaciones: esperamos {"annotators": [{"id": ..., "labels": {pair_id: label}}]}
    # o lista de {pair_id, annotator, label}
    by_pair: dict[str, list[str]] = defaultdict(list)

    if isinstance(data, dict) and "annotators" in data:
        for ann in data["annotators"]:
            for pair_id, label in (ann.get("labels") or {}).items():
                by_pair[pair_id].append(label)
    elif isinstance(data, list):
        for item in data:
            pid = item.get("id") or item.get("pair_id")
            lab = item.get("label") or item.get("annotation")
            if pid and lab:
                by_pair[pid].append(lab)
    else:
        print("Formato de anotaciones no reconocido. Usa annotations_template.json.")
        return 1

    if not by_pair:
        print("Sin anotaciones rellenadas (plantilla vacía). Protocolo listo; esperando anotadores.")
        print(f"Protocolo: {EVAL_DIR / 'PROTOCOL.json'}")
        return 0

    categories = ["none", "mirrorOf", "creates", "unsure"]
    ratings = [by_pair[pid] for pid in sorted(by_pair)]
    # homogeneizar longitud (padding con unsure si falta)
    max_r = max(len(r) for r in ratings)
    ratings = [r + ["unsure"] * (max_r - len(r)) for r in ratings]

    kappa = fleiss_kappa(ratings, categories)
    majority = {}
    for pid, labs in by_pair.items():
        majority[pid] = Counter(labs).most_common(1)[0][0]

    agreement_with_rules = None
    if rule_ref:
        matched = sum(1 for pid, maj in majority.items() if rule_ref.get(pid) == maj)
        agreement_with_rules = matched / len(majority) if majority else 0.0

    report = {
        "n_pairs_annotated": len(by_pair),
        "n_annotators_max": max_r,
        "fleiss_kappa": round(kappa, 4),
        "majority_labels": majority,
        "posthoc_agreement_with_rule_reference": agreement_with_rules,
        "note": (
            "Fleiss' kappa y mayoría son el objetivo primario. "
            "agreement_with_rule_reference es post-hoc y no valida el marco empíricamente."
        ),
    }

    out = ROOT / "experiments" / "results" / "independent_eval_scores.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"Escrito: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
