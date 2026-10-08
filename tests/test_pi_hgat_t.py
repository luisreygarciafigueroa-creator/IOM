"""Pruebas rápidas de la implementación PI-HGAT-T y su vínculo ontológico."""
import unittest
import torch

from experiments.pi_hgat_t import PIHGATT, admissible_relation, features_for_node


class PIHGATTTests(unittest.TestCase):
    def test_feature_vector_uses_only_phase_and_position(self):
        self.assertEqual(features_for_node("T12_adv_P0"), [1.0, 0.0, 1.0, 0.0, 0.0])
        self.assertEqual(features_for_node("T00_ret_P2"), [0.0, 1.0, 0.0, 0.0, 1.0])

    def test_attention_model_returns_three_relation_logits_per_candidate(self):
        model = PIHGATT(dim=16, heads=4)
        graph = torch.eye(5)[:5].unsqueeze(0)
        pairs = torch.tensor([[0, 1], [1, 0]], dtype=torch.long)
        self.assertEqual(tuple(model(graph, pairs).shape), (1, 2, 3))

    def test_admissibility_uses_mirror_and_creation_properties(self):
        # Índices locales 0..2=avance; 3..5=retroceso.
        self.assertTrue(admissible_relation("mirrorOf", 0, 5))
        self.assertFalse(admissible_relation("mirrorOf", 0, 3))
        self.assertTrue(admissible_relation("creates", 0, 4))
        self.assertTrue(admissible_relation("creates", 4, 0))
        self.assertFalse(admissible_relation("creates", 0, 3))


if __name__ == "__main__":
    unittest.main()
