#!/usr/bin/env python3
"""Pruebas que formalizan las conclusiones de la auditoría de métricas 100%."""
from __future__ import annotations

import csv
import unittest
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_node(node_id: str):
    parts = node_id.split("_")
    return parts[1], int(parts[2][1:])


def feature_key(src, tgt):
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    return (sp, spos, tp, tpos)


def deterministic_label(src, tgt):
    sp, spos = parse_node(src)
    tp, tpos = parse_node(tgt)
    if sp == tp:
        return "none"
    if tpos == 2 - spos:
        return "mirrorOf"
    if (spos in (0, 2) and tpos == 1) or (spos == 1 and tpos in (0, 2)):
        return "creates"
    return "none"


class PerfectMetricsAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT / "datasets" / "relation_candidates.csv").open(encoding="utf-8", newline="") as fh:
            cls.rows = list(csv.DictReader(fh))

    def test_gold_matches_deterministic_rule(self):
        for row in self.rows:
            self.assertEqual(
                deterministic_label(row["source"], row["target"]),
                row["relation"],
                msg=row,
            )

    def test_label_is_function_of_phase_position_only(self):
        by_feat = defaultdict(set)
        for row in self.rows:
            by_feat[feature_key(row["source"], row["target"])].add(row["relation"])
        for key, labels in by_feat.items():
            self.assertEqual(len(labels), 1, f"clave {key} tiene etiquetas {labels}")

    def test_loo_features_fully_recoverable_from_train(self):
        """En cada fold LOO, todo par de test es recuperable por lookup de features."""
        for held in range(13):
            train = {}
            test = []
            for row in self.rows:
                key = feature_key(row["source"], row["target"])
                if int(row["triad_index"]) == held:
                    test.append((key, row["relation"]))
                else:
                    train[key] = row["relation"]
            for key, lab in test:
                self.assertEqual(train.get(key), lab)

    def test_model_does_not_use_triad_index_in_features(self):
        """Sanity: features_for_node en pi_hgat_t no incluye índice de tríada."""
        src = (ROOT / "experiments" / "pi_hgat_t.py").read_text(encoding="utf-8")
        self.assertIn("sin etiqueta léxica ni número de tríada", src)
        # La función features_for_node solo usa phase y position
        self.assertIn("phase == \"adv\"", src)
        self.assertIn("position == 0", src)


if __name__ == "__main__":
    unittest.main()
