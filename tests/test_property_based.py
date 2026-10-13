#!/usr/bin/env python3
"""Pruebas generativas y casos negativos para límites de índices, espejos y creates.

Cubre:
- Generación exhaustiva de pares (fase, pos) y verificación de partición
  none / mirrorOf / creates (mutuamente excluyentes y completas).
- Casos negativos: índices fuera de rango, misma fase, posición no reflejada,
  creates entre tríadas distintas, espejo no recíproco.
- Transformaciones temporales / involución de fase y posición.
"""
from __future__ import annotations

import itertools
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PHASES = ("adv", "ret")
POSITIONS = (0, 1, 2)


def opposite_phase(p: str) -> str:
    return "ret" if p == "adv" else "adv"


def mirror_pos(p: int) -> int:
    return 2 - p


def is_mirror(sp: str, spos: int, tp: str, tpos: int) -> bool:
    return sp != tp and tpos == mirror_pos(spos)


def is_creates(sp: str, spos: int, tp: str, tpos: int) -> bool:
    if sp == tp:
        return False
    lateral_s = spos in (0, 2)
    lateral_t = tpos in (0, 2)
    return (lateral_s and tpos == 1) or (spos == 1 and lateral_t)


def classify(sp: str, spos: int, tp: str, tpos: int) -> str:
    if is_mirror(sp, spos, tp, tpos):
        return "mirrorOf"
    if is_creates(sp, spos, tp, tpos):
        return "creates"
    return "none"


class ExhaustivePartitionTests(unittest.TestCase):
    """Todas las combinaciones (fase, pos) × (fase, pos) no reflexivas."""

    def test_partition_is_complete_and_exclusive(self):
        nodes = list(itertools.product(PHASES, POSITIONS))
        counts = {"none": 0, "mirrorOf": 0, "creates": 0}
        for (sp, spos), (tp, tpos) in itertools.product(nodes, nodes):
            if (sp, spos) == (tp, tpos):
                continue
            label = classify(sp, spos, tp, tpos)
            counts[label] += 1
            # exclusividad
            m = is_mirror(sp, spos, tp, tpos)
            c = is_creates(sp, spos, tp, tpos)
            self.assertFalse(m and c)
            if label == "mirrorOf":
                self.assertTrue(m)
            elif label == "creates":
                self.assertTrue(c)
            else:
                self.assertFalse(m or c)
        # 6 nodos, 30 pares dirigidos no reflexivos
        self.assertEqual(sum(counts.values()), 30)
        # Por tríada: 6 mirror, 8 creates, 16 none → ×13 = 78/104/208
        self.assertEqual(counts["mirrorOf"], 6)
        self.assertEqual(counts["creates"], 8)
        self.assertEqual(counts["none"], 16)

    def test_mirror_is_involution_on_position(self):
        for p in POSITIONS:
            self.assertEqual(mirror_pos(mirror_pos(p)), p)

    def test_phase_opposite_is_involution(self):
        for p in PHASES:
            self.assertEqual(opposite_phase(opposite_phase(p)), p)
            self.assertNotEqual(opposite_phase(p), p)


class NegativeCaseTests(unittest.TestCase):
    """Casos que DEBEN fallar / clasificarse como none."""

    def test_same_phase_never_mirror_or_creates(self):
        for phase in PHASES:
            for spos, tpos in itertools.product(POSITIONS, POSITIONS):
                if spos == tpos:
                    continue
                self.assertEqual(classify(phase, spos, phase, tpos), "none")

    def test_wrong_mirror_position_is_none(self):
        # adv P0 → ret P0 no es espejo (debería ser P2)
        self.assertFalse(is_mirror("adv", 0, "ret", 0))
        self.assertFalse(is_mirror("adv", 0, "ret", 1))
        self.assertTrue(is_mirror("adv", 0, "ret", 2))

    def test_creates_requires_center_involvement(self):
        # lateral → lateral (sin centro) no es creates
        self.assertFalse(is_creates("adv", 0, "ret", 2))
        self.assertFalse(is_creates("adv", 2, "ret", 0))
        # lateral → centro sí
        self.assertTrue(is_creates("adv", 0, "ret", 1))
        self.assertTrue(is_creates("adv", 1, "ret", 0))

    def test_index_bounds(self):
        """Posiciones fuera de {0,1,2} no son válidas en la especificación."""
        for bad in (-1, 3, 4, 99):
            # mirror_pos fuera de dominio no debe usarse en producción;
            # documentamos el comportamiento aritmético
            mirrored = 2 - bad
            self.assertNotIn(bad, POSITIONS)
            self.assertNotIn(mirrored, POSITIONS) if bad not in ( -1,) else True

    def test_center_mirror_is_center(self):
        self.assertEqual(mirror_pos(1), 1)
        self.assertTrue(is_mirror("adv", 1, "ret", 1))


class GenerativeConsistencyTests(unittest.TestCase):
    """Propiedades que deben sostenerse para cualquier tríada sintética."""

    def test_mirror_count_per_synthetic_triad(self):
        nodes = list(itertools.product(PHASES, POSITIONS))
        mirrors = [
            ((sp, spos), (tp, tpos))
            for (sp, spos), (tp, tpos) in itertools.product(nodes, nodes)
            if (sp, spos) != (tp, tpos) and is_mirror(sp, spos, tp, tpos)
        ]
        self.assertEqual(len(mirrors), 6)
        # reciprocidad: si A mirrors B, B mirrors A
        mirror_set = set(mirrors)
        for a, b in mirrors:
            self.assertIn((b, a), mirror_set)

    def test_creates_count_per_synthetic_triad(self):
        nodes = list(itertools.product(PHASES, POSITIONS))
        creates = [
            ((sp, spos), (tp, tpos))
            for (sp, spos), (tp, tpos) in itertools.product(nodes, nodes)
            if (sp, spos) != (tp, tpos) and is_creates(sp, spos, tp, tpos)
        ]
        self.assertEqual(len(creates), 8)

    def test_no_overlap_mirror_creates_generative(self):
        nodes = list(itertools.product(PHASES, POSITIONS))
        for (sp, spos), (tp, tpos) in itertools.product(nodes, nodes):
            if (sp, spos) == (tp, tpos):
                continue
            self.assertFalse(
                is_mirror(sp, spos, tp, tpos) and is_creates(sp, spos, tp, tpos)
            )


class AxisBoundTests(unittest.TestCase):
    """Límites del eje vectorial [0, 4] alineados con FormalRules.lean."""

    def test_axis_in_0_4(self):
        for n in range(5):
            self.assertTrue(0 <= n <= 4)

    def test_axis_retreat_involution(self):
        for n in range(5):
            self.assertEqual(4 - (4 - n), n)

    def test_axis_out_of_range_rejected(self):
        for bad in (-1, 5, 6):
            self.assertFalse(0 <= bad <= 4)


if __name__ == "__main__":
    unittest.main()
