#!/usr/bin/env python3
"""Pruebas del lector de anotaciones y de la política null ≠ unsure."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

# Importar funciones del script
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
                {"id": "CT01", "annotations": {"A1": None, "A2": None, "A3": None}},
            ],
        }
        aids, by_pair = mod.parse_template_format(data)
        self.assertEqual(aids, ["A1", "A2", "A3"])
        self.assertEqual(by_pair["NR01"]["A1"], None)
        self.assertEqual(by_pair["CT01"]["A2"], None)

    def test_parse_filled_template(self):
        data = {
            "annotators": ["A1", "A2", "A3"],
            "items": [
                {
                    "id": "NR01",
                    "annotations": {"A1": "none", "A2": "none", "A3": "unsure"},
                },
                {
                    "id": "CT01",
                    "annotations": {"A1": "mirrorOf", "A2": "mirrorOf", "A3": None},
                },
            ],
        }
        aids, by_pair = mod.parse_template_format(data)
        self.assertEqual(by_pair["NR01"]["A3"], "unsure")
        self.assertIsNone(by_pair["CT01"]["A3"])  # ausente, no unsure

    def test_invalid_label_rejected(self):
        data = {
            "annotators": ["A1"],
            "items": [{"id": "X", "annotations": {"A1": "maybe"}}],
        }
        with self.assertRaises(ValueError):
            mod.parse_template_format(data)

    def test_null_not_confused_with_unsure_in_scoring(self):
        """Ítems con null no deben entrar en kappa como si fueran unsure."""
        payload = {
            "annotators": ["A1", "A2", "A3"],
            "status": "partial",
            "items": [
                {
                    "id": "NR01",
                    "annotations": {"A1": "none", "A2": "none", "A3": "none"},
                },
                {
                    "id": "CT01",
                    "annotations": {"A1": "mirrorOf", "A2": None, "A3": None},
                },
            ],
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as fh:
            json.dump(payload, fh)
            path = Path(fh.name)
        try:
            aids, by_pair, meta = mod.load_annotations(path)
            # CT01 tiene solo 1 presente → incompleto con min=3
            present_ct01 = [v for v in by_pair["CT01"].values() if v is not None]
            self.assertEqual(len(present_ct01), 1)
            present_nr01 = [v for v in by_pair["NR01"].values() if v is not None]
            self.assertEqual(len(present_nr01), 3)
            self.assertNotIn(None, present_nr01)
        finally:
            path.unlink(missing_ok=True)


class FleissTests(unittest.TestCase):
    def test_perfect_agreement(self):
        ratings = [["none", "none", "none"], ["mirrorOf", "mirrorOf", "mirrorOf"]]
        k = mod.fleiss_kappa(ratings, ["none", "mirrorOf", "creates", "unsure"])
        self.assertAlmostEqual(k, 1.0)

    def test_empty_returns_nan(self):
        k = mod.fleiss_kappa([], ["none"])
        self.assertTrue(k != k)  # NaN


if __name__ == "__main__":
    unittest.main()
