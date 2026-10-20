#!/usr/bin/env python3
"""Puente: las relaciones del CSV deben satisfacer los predicados formales
codificados en IOM/FormalRules.lean (isMirrorRel / isCreatesRel / sameTriad).

Equivalencia de capas:
  Lean isMirrorRel  ↔  Python is_mirror ∧ same_triad
  Lean isCreatesRel ↔  Python is_creates ∧ same_triad
  Lean isMirror (posicional)  ↔  Python is_mirror  (sin exigir tríada)
"""
from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_relations():
    with (ROOT / "datasets" / "relation_candidates.csv").open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def parse_node(node_id: str) -> tuple[int, str, int]:
    """Devuelve (triad_id, phase, position)."""
    m = re.fullmatch(r"T(\d{2})_(adv|ret)_P([0-2])", node_id)
    assert m, node_id
    return int(m.group(1)), m.group(2), int(m.group(3))


def same_triad(src: str, tgt: str) -> bool:
    return parse_node(src)[0] == parse_node(tgt)[0]


def is_mirror_positional(src: str, tgt: str) -> bool:
    """Equivale a Lean isMirror / isMirrorPositional."""
    _sid, sp, spos = parse_node(src)
    _tid, tp, tpos = parse_node(tgt)
    return sp != tp and tpos == 2 - spos


def is_creates_positional(src: str, tgt: str) -> bool:
    """Equivale a Lean isCreates / isCreatesPositional."""
    _sid, sp, spos = parse_node(src)
    _tid, tp, tpos = parse_node(tgt)
    if sp == tp:
        return False
    lateral_s = spos in (0, 2)
    lateral_t = tpos in (0, 2)
    return (lateral_s and tpos == 1) or (spos == 1 and lateral_t)


def is_mirror_rel(src: str, tgt: str) -> bool:
    """Equivale a Lean isMirrorRel: sameTriad ∧ isMirrorPositional."""
    return same_triad(src, tgt) and is_mirror_positional(src, tgt)


def is_creates_rel(src: str, tgt: str) -> bool:
    """Equivale a Lean isCreatesRel: sameTriad ∧ isCreatesPositional."""
    return same_triad(src, tgt) and is_creates_positional(src, tgt)


class FormalRulesBridgeTests(unittest.TestCase):
    """Comprueba que el JSON/CSV regenerado cumple los predicados Lean."""

    @classmethod
    def setUpClass(cls):
        cls.rows = load_relations()
        cls.lean = (ROOT / "IOM" / "FormalRules.lean").read_text(encoding="utf-8")

    def test_lean_defines_same_triad_and_rel_predicates(self):
        self.assertIn("def sameTriad", self.lean)
        self.assertIn("def isMirrorRel", self.lean)
        self.assertIn("def isCreatesRel", self.lean)
        self.assertIn("def isMirrorPositional", self.lean)
        self.assertIn("def isCreatesPositional", self.lean)
        self.assertIn("triadId", self.lean)
        self.assertIn("expectedMirrorDirected", self.lean)
        self.assertIn("expectedCreatesDirected", self.lean)

    def test_every_mirrorOf_satisfies_isMirrorRel(self):
        for row in self.rows:
            if row["relation"] != "mirrorOf":
                continue
            self.assertTrue(
                is_mirror_rel(row["source"], row["target"]),
                f"mirrorOf viola isMirrorRel: {row['source']} -> {row['target']}",
            )
            self.assertFalse(
                is_creates_rel(row["source"], row["target"]),
                f"mirrorOf no debe ser createsRel: {row}",
            )

    def test_every_creates_satisfies_isCreatesRel(self):
        for row in self.rows:
            if row["relation"] != "creates":
                continue
            self.assertTrue(
                is_creates_rel(row["source"], row["target"]),
                f"creates viola isCreatesRel: {row['source']} -> {row['target']}",
            )
            self.assertFalse(
                is_mirror_rel(row["source"], row["target"]),
                f"creates no debe ser mirrorRel: {row}",
            )

    def test_none_satisfies_neither_rel(self):
        for row in self.rows:
            if row["relation"] != "none":
                continue
            self.assertFalse(
                is_mirror_rel(row["source"], row["target"]), row
            )
            self.assertFalse(
                is_creates_rel(row["source"], row["target"]), row
            )

    def test_cross_triad_positional_mirror_is_not_rel(self):
        """Un par cross-tríada puede cumplir la condición posicional pero no isMirrorRel."""
        # T07_adv_P0 y T01_ret_P2: posicional mirror, distinta tríada
        self.assertTrue(is_mirror_positional("T07_adv_P0", "T01_ret_P2"))
        self.assertFalse(same_triad("T07_adv_P0", "T01_ret_P2"))
        self.assertFalse(is_mirror_rel("T07_adv_P0", "T01_ret_P2"))

    def test_counts_match_lean_constants(self):
        from collections import Counter
        c = Counter(r["relation"] for r in self.rows)
        self.assertEqual(c["mirrorOf"], 78)
        self.assertEqual(c["creates"], 104)
        self.assertEqual(c["none"], 208)
        self.assertIn("78", self.lean)
        self.assertIn("104", self.lean)
        self.assertIn("208", self.lean)

    def test_partition_complete_with_rel(self):
        for row in self.rows:
            m = is_mirror_rel(row["source"], row["target"])
            c = is_creates_rel(row["source"], row["target"])
            self.assertFalse(m and c, row)
            if row["relation"] == "mirrorOf":
                self.assertTrue(m)
            elif row["relation"] == "creates":
                self.assertTrue(c)
            else:
                self.assertFalse(m or c)


if __name__ == "__main__":
    unittest.main()
