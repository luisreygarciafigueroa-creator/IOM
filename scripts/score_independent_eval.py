#!/usr/bin/env python3
"""Scoring post-hoc de evaluación independiente (capa C).

Formato oficial de anotaciones (annotations_template.json):

    {
      "annotators": ["A1", "A2", "A3"],
      "status": "pending_human_collection" | "complete",
      "items": [
        {
          "id": "NR01",
          "annotations": {"A1": "none" | null, ...},
          "free_text": {"A1": "...", ...}
        },
        ...
      ]
    }

Reglas estadísticas:
  - null / ausente ≠ etiqueta "unsure".
  - Fleiss' kappa exige el **mismo conjunto de anotadores** con respuesta
    no nula en **todos** los ítems incluidos (k fijo). No se trunca.
  - Si un ítem tiene un subconjunto distinto de respondentes, se excluye
    del kappa y se reporta en incomplete/heterogeneous.
  - "unsure" es una respuesta legítima, no un relleno.

Uso:
    python scripts/score_independent_eval.py
    python scripts/score_independent_eval.py --annotations path/to/filled.json
    python scripts/score_independent_eval.py --min-annotators 3
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "datasets" / "independent_eval"
VALID_LABELS = frozenset({"none", "mirrorOf", "creates", "unsure"})


def fleiss_kappa(ratings: list[list[str]], categories: list[str]) -> float:
    """Fleiss' kappa. ratings[i] = etiquetas de los k anotadores para el ítem i.
    Todas las filas deben tener la misma longitud k ≥ 2.
    """
    n_items = len(ratings)
    if n_items == 0:
        return float("nan")
    n_raters = len(ratings[0])
    if n_raters < 2:
        return float("nan")
    if any(len(r) != n_raters for r in ratings):
        raise ValueError("Todas las filas de ratings deben tener la misma longitud")

    cat_idx = {c: i for i, c in enumerate(categories)}
    table = []
    for row in ratings:
        counts = [0] * len(categories)
        for lab in row:
            if lab not in cat_idx:
                raise ValueError(f"Etiqueta fuera de categorías: {lab!r}")
            counts[cat_idx[lab]] += 1
        table.append(counts)

    P = []
    for counts in table:
        s = sum(c * (c - 1) for c in counts)
        P.append(s / (n_raters * (n_raters - 1)))
    P_bar = sum(P) / n_items

    totals = [sum(table[i][j] for i in range(n_items)) for j in range(len(categories))]
    p = [t / (n_items * n_raters) for t in totals]
    P_e = sum(pj ** 2 for pj in p)
    if abs(1 - P_e) < 1e-12:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def parse_template_format(data: dict) -> tuple[list[str], dict[str, dict[str, str | None]]]:
    """Formato oficial: annotators=[ids], items=[{id, annotations: {A: label|null}}]."""
    annotator_ids = list(data.get("annotators") or [])
    if not annotator_ids:
        raise ValueError("Campo 'annotators' vacío o ausente")

    by_pair: dict[str, dict[str, str | None]] = {}
    items = data.get("items")
    if not isinstance(items, list):
        raise ValueError("Campo 'items' debe ser una lista")

    for item in items:
        pid = item.get("id")
        if not pid:
            raise ValueError(f"Ítem sin id: {item!r}")
        anns = item.get("annotations") or {}
        if not isinstance(anns, dict):
            raise ValueError(f"annotations de {pid} debe ser un objeto")
        pair_map: dict[str, str | None] = {}
        for aid in annotator_ids:
            raw = anns.get(aid)
            if raw is None:
                pair_map[aid] = None
            elif isinstance(raw, str) and raw.strip() == "":
                pair_map[aid] = None
            elif raw in VALID_LABELS:
                pair_map[aid] = raw
            else:
                raise ValueError(
                    f"Etiqueta inválida en {pid}/{aid}: {raw!r}. "
                    f"Permitidas: {sorted(VALID_LABELS)} o null"
                )
        by_pair[pid] = pair_map
    return annotator_ids, by_pair


def parse_legacy_formats(data: Any) -> tuple[list[str], dict[str, dict[str, str | None]]]:
    by_pair: dict[str, dict[str, str | None]] = defaultdict(dict)
    annotator_ids: list[str] = []

    if isinstance(data, dict) and "annotators" in data:
        anns = data["annotators"]
        if isinstance(anns, list) and anns and isinstance(anns[0], dict) and "labels" in anns[0]:
            for ann in anns:
                aid = str(ann.get("id") or ann.get("name") or f"A{len(annotator_ids)+1}")
                annotator_ids.append(aid)
                for pair_id, label in (ann.get("labels") or {}).items():
                    by_pair[pair_id][aid] = label if label in VALID_LABELS else None
            return annotator_ids, dict(by_pair)

    if isinstance(data, list):
        aids_set: set[str] = set()
        for item in data:
            pid = item.get("id") or item.get("pair_id")
            aid = str(item.get("annotator") or "A1")
            lab = item.get("label") or item.get("annotation")
            if not pid:
                continue
            aids_set.add(aid)
            by_pair[pid][aid] = lab if lab in VALID_LABELS else None
        return sorted(aids_set), dict(by_pair)

    raise ValueError(
        "Formato de anotaciones no reconocido. "
        "Usa el formato de annotations_template.json."
    )


def load_annotations(path: Path) -> tuple[list[str], dict[str, dict[str, str | None]], dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    meta = {
        "status": data.get("status") if isinstance(data, dict) else None,
        "description": data.get("description") if isinstance(data, dict) else None,
        "evaluation_mode": data.get("evaluation_mode") if isinstance(data, dict) else None,
    }
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        annotator_ids, by_pair = parse_template_format(data)
    else:
        annotator_ids, by_pair = parse_legacy_formats(data)
    return annotator_ids, by_pair, meta


def load_rule_reference() -> dict[str, str]:
    ref_path = EVAL_DIR / "rule_reference.json"
    if not ref_path.is_file():
        return {}
    raw = json.loads(ref_path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return {item["id"]: item.get("rule_label") for item in raw if "id" in item}
    if isinstance(raw, dict):
        out = {}
        for k, v in raw.items():
            if k in ("labels",):
                continue
            if isinstance(v, dict):
                out[k] = v.get("rule_label")
            elif isinstance(v, str):
                out[k] = v
        if "labels" in raw and isinstance(raw["labels"], dict):
            out.update(raw["labels"])
        return out
    return {}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scoring de evaluación independiente (capa C)"
    )
    parser.add_argument(
        "--annotations",
        type=Path,
        default=EVAL_DIR / "annotations_template.json",
        help="JSON de anotaciones (plantilla o rellenado)",
    )
    parser.add_argument(
        "--min-annotators",
        type=int,
        default=3,
        help="Número exacto de anotadores con respuesta no nula requerido por ítem (default 3)",
    )
    args = parser.parse_args()

    if not args.annotations.is_file():
        print(f"ERROR: no se encontró {args.annotations}", file=sys.stderr)
        return 1

    try:
        annotator_ids, by_pair, meta = load_annotations(args.annotations)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR de formato: {exc}", file=sys.stderr)
        return 1

    k_required = args.min_annotators
    if k_required < 2:
        print("ERROR: --min-annotators debe ser ≥ 2", file=sys.stderr)
        return 1

    # Por ítem: quién respondió y con qué etiqueta (orden fijo de annotator_ids)
    incomplete_pairs: dict[str, dict] = {}
    respondent_sets: dict[str, tuple[str, ...]] = {}
    labels_by_pair_ordered: dict[str, list[str]] = {}
    unsure_counts: Counter = Counter()
    present_counts: Counter = Counter()

    for pid, ann_map in by_pair.items():
        respondents = []
        labels_ordered = []
        missing = []
        for aid in annotator_ids:
            lab = ann_map.get(aid)
            if lab is None:
                missing.append(aid)
            else:
                respondents.append(aid)
                labels_ordered.append(lab)
                present_counts[lab] += 1
                if lab == "unsure":
                    unsure_counts[pid] += 1

        if len(respondents) == k_required:
            respondent_sets[pid] = tuple(respondents)
            labels_by_pair_ordered[pid] = labels_ordered
        else:
            incomplete_pairs[pid] = {
                "n_present": len(respondents),
                "n_missing": len(missing),
                "missing_annotators": missing,
                "present_annotators": respondents,
                "present_labels": labels_ordered,
                "reason": (
                    f"se requieren exactamente {k_required} respuestas no nulas; "
                    f"hay {len(respondents)}"
                ),
            }

    status = meta.get("status") or "unknown"
    n_total = len(by_pair)

    # Agrupar ítems por el conjunto exacto de respondentes
    by_respondent_set: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for pid, rset in respondent_sets.items():
        by_respondent_set[rset].append(pid)

    # Elegir el conjunto de respondentes más frecuente con tamaño k_required
    # Solo se calcula kappa sobre ítems que comparten EXACTAMENTE el mismo conjunto.
    kappa_eligible_ids: list[str] = []
    kappa_annotators: tuple[str, ...] | None = None
    heterogeneous: dict[str, dict] = {}

    if by_respondent_set:
        # Preferir el set con más ítems; en empate, el primero en orden lexicográfico del tuple
        best_set = max(
            by_respondent_set.keys(),
            key=lambda s: (len(by_respondent_set[s]), s),
        )
        kappa_eligible_ids = sorted(by_respondent_set[best_set])
        kappa_annotators = best_set

        for rset, pids in by_respondent_set.items():
            if rset == best_set:
                continue
            for pid in pids:
                heterogeneous[pid] = {
                    "respondents": list(rset),
                    "n_present": len(rset),
                    "reason": (
                        "conjunto de anotadores distinto al usado para kappa "
                        f"({list(best_set)}); no se trunca ni se mezcla"
                    ),
                    "present_labels": labels_by_pair_ordered[pid],
                }

    n_kappa = len(kappa_eligible_ids)
    n_incomplete = len(incomplete_pairs)
    n_heterogeneous = len(heterogeneous)

    if n_kappa == 0:
        report = {
            "status": status,
            "evaluation_mode": meta.get("evaluation_mode"),
            "n_pairs_total": n_total,
            "n_pairs_in_kappa": 0,
            "n_pairs_incomplete": n_incomplete,
            "n_pairs_heterogeneous_respondent_set": n_heterogeneous,
            "min_annotators_required": k_required,
            "kappa_annotators": None,
            "fleiss_kappa": None,
            "majority_labels": {},
            "posthoc_agreement_with_rule_reference": None,
            "incomplete_detail": incomplete_pairs,
            "heterogeneous_detail": heterogeneous,
            "note": (
                f"Sin ítems con exactamente {k_required} respuestas no nulas "
                "del mismo conjunto de anotadores. No se trunca. "
                "null/ausente ≠ 'unsure'. Protocolo listo; esperando recolección."
            ),
        }
        out = ROOT / "experiments" / "results" / "independent_eval_scores.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        print(f"Escrito: {out}")
        return 0

    assert kappa_annotators is not None
    k = len(kappa_annotators)
    categories = ["none", "mirrorOf", "creates", "unsure"]
    ratings = [labels_by_pair_ordered[pid] for pid in kappa_eligible_ids]

    # Garantía: mismo k y mismo orden de anotadores
    if any(len(r) != k for r in ratings):
        print(
            "ERROR interno: longitudes inconsistentes tras filtrado; no se calcula kappa.",
            file=sys.stderr,
        )
        return 1

    kappa = fleiss_kappa(ratings, categories)

    majority: dict[str, str] = {}
    unanimous = 0
    for pid in kappa_eligible_ids:
        labs = labels_by_pair_ordered[pid]
        cnt = Counter(labs)
        maj_lab, maj_n = cnt.most_common(1)[0]
        majority[pid] = maj_lab
        if maj_n == len(labs):
            unanimous += 1

    # Mayoría también para ítems fuera de kappa (informativo, no entra en kappa)
    majority_all = dict(majority)
    for pid, labs in labels_by_pair_ordered.items():
        if pid not in majority_all and labs:
            majority_all[pid] = Counter(labs).most_common(1)[0][0]

    rule_ref = load_rule_reference()
    comparable = {
        pid: maj
        for pid, maj in majority.items()
        if rule_ref.get(pid) and rule_ref[pid] not in (None, "unspecified")
    }
    agreement_with_rules = None
    if comparable:
        matched = sum(1 for pid, maj in comparable.items() if rule_ref[pid] == maj)
        agreement_with_rules = round(matched / len(comparable), 4)

    report = {
        "status": status,
        "evaluation_mode": meta.get("evaluation_mode"),
        "n_pairs_total": n_total,
        "n_pairs_in_kappa": n_kappa,
        "n_pairs_incomplete": n_incomplete,
        "n_pairs_heterogeneous_respondent_set": n_heterogeneous,
        "min_annotators_required": k_required,
        "kappa_annotators": list(kappa_annotators),
        "n_annotators_per_kappa_item": k,
        "fleiss_kappa": None if (isinstance(kappa, float) and kappa != kappa) else round(kappa, 4),
        "unanimous_fraction": round(unanimous / n_kappa, 4) if n_kappa else None,
        "majority_labels_in_kappa": majority,
        "majority_labels_all_with_any_response": majority_all,
        "label_distribution_present": dict(present_counts),
        "unsure_count_by_pair": dict(unsure_counts),
        "posthoc_agreement_with_rule_reference": agreement_with_rules,
        "n_posthoc_comparable": len(comparable),
        "incomplete_detail": incomplete_pairs if incomplete_pairs else {},
        "heterogeneous_detail": heterogeneous if heterogeneous else {},
        "policy": (
            "Fleiss' kappa solo sobre ítems con exactamente k anotadores no nulos "
            "y el mismo conjunto de respondentes. No se trunca ni se rellena. "
            "null ≠ unsure."
        ),
        "note": (
            "Fleiss' kappa y mayoría (sobre el panel kappa) son el objetivo primario. "
            "posthoc_agreement_with_rule_reference excluye unspecified y es solo post-hoc."
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
