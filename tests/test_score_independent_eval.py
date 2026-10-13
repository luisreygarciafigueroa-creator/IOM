#!/usr/bin/env python3
"""Pruebas del lector de anotaciones, null≠unsure y política de kappa sin truncar."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "scripts" / "score_independent_eval.py"

spec = importlib.util.spec_from_file_location("score_independent_eval", SPEC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TemplateFormatTests(unittest.TestCase):
    def test_parse_empty_template(self):
        data = {
            "annotators": ["A1", "A2", "A3"],
            "status": "pending_human_collection",
            "items": [
                {"id": "NR01", "annotations": {"A1": None, "A2": None, "A3": None}},
            ],
        }
        aids, by_pair = mod.parse_template_format(data)
        self.assertEqual(aids, ["A1", "A2", "A3"])
        self.assertIsNone(by_pair["NR01"]["A1"])

    def test_null_not_unsure(self):
        data = {
            "annotators": ["A1", "A2", "A3"],
            "items": [
                {
                    "id": "CT01",
                    "annotations": {"A1": "mirrorOf", "A2": "mirrorOf", "A3": None},
                },
            ],
        }
        _, by_pair = mod.parse_template_format(data)
        self.assertIsNone(by_pair["CT01"]["A3"])

    def test_invalid_label_rejected(self):
        data = {
            "annotators": ["A1"],
            "items": [{"id": "X", "annotations": {"A1": "maybe"}}],
        }
        with self.assertRaises(ValueError):
            mod.parse_template_format(data)


class NoTruncatePolicyTests(unittest.TestCase):
    """Kappa no debe truncar; solo ítems con el mismo conjunto de respondentes."""

    def test_heterogeneous_respondent_sets_excluded(self):
        payload = {
            "annotators": ["A1", "A2", "A3", "A4"],
            "status": "partial",
            "items": [
                {
                    "id": "P1",
                    "annotations": {
                        "A1": "none",
                        "A2": "none",
                        "A3": "none",
                        "A4": None,
                    },
                },
                {
                    "id": "P2",
                    "annotations": {
                        "A1": "none",
                        "A2": "none",
                        "A3": "none",
                        "A4": None,
                    },
                },
                {
                    "id": "P3",
                    "annotations": {
                        "A1": "mirrorOf",
                        "A2": "mirrorOf",
                        "A3": None,
                        "A4": "mirrorOf",
                    },
                },
            ],
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as fh:
            json.dump(payload, fh)
            path = Path(fh.name)
        try:
            aids, by_pair, _meta = mod.load_annotations(path)
            # Simular la lógica de agrupación del main
            k_required = 3
            respondent_sets = {}
            for pid, ann_map in by_pair.items():
                respondents = tuple(
                    aid for aid in aids if ann_map.get(aid) is not None
                )
                if len(respondents) == k_required:
                    respondent_sets[pid] = respondents
            # P1 y P2: (A1,A2,A3); P3: (A1,A2,A4) — conjuntos distintos
            self.assertEqual(respondent_sets["P1"], ("A1", "A2", "A3"))
            self.assertEqual(respondent_sets["P3"], ("A1", "A2", "A4"))
            self.assertNotEqual(respondent_sets["P1"], respondent_sets["P3"])
        finally:
            path.unlink(missing_ok=True)


class FleissTests(unittest.TestCase):
    def test_perfect_agreement(self):
        ratings = [["none", "none", "none"], ["mirrorOf", "mirrorOf", "mirrorOf"]]
        k = mod.fleiss_kappa(ratings, ["none", "mirrorOf", "creates", "unsure"])
        self.assertAlmostEqual(k, 1.0)

    def test_mismatched_lengths_raise(self):
        with self.assertRaises(ValueError):
            mod.fleiss_kappa(
                [["none", "none"], ["none", "none", "none"]],
                ["none", "mirrorOf"],
            )


class AnnotatorPairsBlindTests(unittest.TestCase):
    def test_default_pairs_have_no_structural_hints(self):
        path = ROOT / "datasets" / "independent_eval" / "annotator_pairs.csv"
        text = path.read_text(encoding="utf-8").lower()
        forbidden = [
            "fase",
            "posición",
            "posicion",
            "lateral",
            "centro",
            "espejo",
            "creates",
            "mirror",
            "avance",
            "retroceso",
            "canónico",
            "canonico",
        ]
        for word in forbidden:
            self.assertNotIn(
                word,
                text,
                f"annotator_pairs.csv no debe contener la pista estructural {word!r}",
            )


if __name__ == "__main__":
    unittest.main()
