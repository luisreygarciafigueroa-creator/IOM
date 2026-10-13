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
  - Solo se incluyen en Fleiss' kappa los ítems con ≥ min_annotators
    respuestas no nulas.
  - "unsure" es una respuesta legítima del anotador, no un relleno.

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
    """Formato oficial: annotators=[ids], items=[{id, annotations: {A: label|null}}].

    Devuelve (annotator_ids, {pair_id: {annotator_id: label|None}}).
    """
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
                pair_map[aid] = None  # ausente
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
    """Formatos alternativos (compatibilidad)."""
    by_pair: dict[str, dict[str, str | None]] = defaultdict(dict)
    annotator_ids: list[str] = []

    if isinstance(data, dict) and "annotators" in data:
        anns = data["annotators"]
        # Lista de objetos {id, labels: {pair: label}}
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
        "Usa el formato de annotations_template.json "
        "(annotators: [ids], items: [{id, annotations: {A: label|null}}])."
    )


def load_annotations(path: Path) -> tuple[list[str], dict[str, dict[str, str | None]], dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    meta = {
        "status": data.get("status") if isinstance(data, dict) else None,
        "description": data.get("description") if isinstance(data, dict) else None,
    }
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        # Formato oficial de la plantilla
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
        # {id: {rule_label, notes}} o {id: label}
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
        help="Mínimo de respuestas no nulas por ítem para incluirlo en kappa (default 3)",
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

    # Separar presentes vs ausentes
    complete_pairs: dict[str, list[str]] = {}
    incomplete_pairs: dict[str, dict] = {}
    unsure_counts: Counter = Counter()
    present_counts: Counter = Counter()

    for pid, ann_map in by_pair.items():
        present = []
        missing = []
        for aid in annotator_ids:
            lab = ann_map.get(aid)
            if lab is None:
                missing.append(aid)
            else:
                present.append(lab)
                present_counts[lab] += 1
                if lab == "unsure":
                    unsure_counts[pid] += 1
        if len(present) >= args.min_annotators:
            # Para kappa necesitamos exactamente k respuestas; si hay más anotadores
            # de los requeridos, usamos solo los que respondieron (mismo k por ítem
            # solo si todos los ítems completos tienen el mismo número).
            complete_pairs[pid] = present
        else:
            incomplete_pairs[pid] = {
                "n_present": len(present),
                "n_missing": len(missing),
                "missing_annotators": missing,
                "present_labels": present,
            }

    status = meta.get("status") or "unknown"
    n_total = len(by_pair)
    n_complete = len(complete_pairs)
    n_incomplete = len(incomplete_pairs)

    if n_complete == 0:
        report = {
            "status": status,
            "n_pairs_total": n_total,
            "n_pairs_complete": 0,
            "n_pairs_incomplete": n_incomplete,
            "min_annotators_required": args.min_annotators,
            "fleiss_kappa": None,
            "majority_labels": {},
            "posthoc_agreement_with_rule_reference": None,
            "incomplete_detail": incomplete_pairs,
            "note": (
                "Sin ítems con ≥{0} anotaciones no nulas. "
                "Protocolo listo; esperando recolección humana. "
                "null/ausente ≠ 'unsure'."
            ).format(args.min_annotators),
        }
        out = ROOT / "experiments" / "results" / "independent_eval_scores.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        print(f"Escrito: {out}")
        return 0

    # Verificar que todos los ítems completos tienen el mismo número de respuestas
    lengths = {len(v) for v in complete_pairs.values()}
    if len(lengths) > 1:
        print(
            "ADVERTENCIA: los ítems completos tienen distinto número de anotadores. "
            "Fleiss' kappa requiere k fijo; se usará el mínimo común truncando.",
            file=sys.stderr,
        )
        k = min(lengths)
        ratings_map = {pid: labs[:k] for pid, labs in complete_pairs.items()}
    else:
        k = lengths.pop()
        ratings_map = complete_pairs

    categories = ["none", "mirrorOf", "creates", "unsure"]
    ordered_ids = sorted(ratings_map)
    ratings = [ratings_map[pid] for pid in ordered_ids]

    kappa = fleiss_kappa(ratings, categories)

    majority: dict[str, str] = {}
    unanimous = 0
    for pid, labs in ratings_map.items():
        cnt = Counter(labs)
        maj_lab, maj_n = cnt.most_common(1)[0]
        majority[pid] = maj_lab
        if maj_n == len(labs):
            unanimous += 1

    rule_ref = load_rule_reference()
    # Post-hoc solo sobre ítems con rule_label definido (no "unspecified")
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
        "n_pairs_total": n_total,
        "n_pairs_complete": n_complete,
        "n_pairs_incomplete": n_incomplete,
        "min_annotators_required": args.min_annotators,
        "n_annotators_per_complete_item": k,
        "fleiss_kappa": None if (isinstance(kappa, float) and kappa != kappa) else round(kappa, 4),
        "unanimous_fraction": round(unanimous / n_complete, 4) if n_complete else None,
        "majority_labels": majority,
        "label_distribution_present": dict(present_counts),
        "unsure_count_by_pair": dict(unsure_counts),
        "posthoc_agreement_with_rule_reference": agreement_with_rules,
        "n_posthoc_comparable": len(comparable),
        "incomplete_detail": incomplete_pairs if incomplete_pairs else {},
        "note": (
            "Fleiss' kappa y mayoría son el objetivo primario. "
            "posthoc_agreement_with_rule_reference excluye rule_label=unspecified "
            "y es solo post-hoc (no valida el marco empíricamente). "
            "null/ausente no se sustituye por 'unsure'."
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
