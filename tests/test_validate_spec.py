#!/usr/bin/env python3
"""Validación del schema y de la spec canónica."""
from __future__ import annotations

import json
import unittest
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "data" / "iom_spec.schema.json").read_text(encoding="utf-8"))
SPEC = json.loads((ROOT / "data" / "iom_spec.json").read_text(encoding="utf-8"))


class SpecificationSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = Draft202012Validator(SCHEMA)

    def test_canonical_spec_conforms_to_schema(self):
        errors = list(self.validator.iter_errors(SPEC))
        self.assertEqual(errors, [])

    def test_canonical_position_metadata_and_triad_indexing_are_accepted(self):
        spec = deepcopy(SPEC)
        spec["positions"]["indices"] = [0, 1, 2]
        spec["positions"]["adv_labels"] = ["→", "0", "→"]
        spec["positions"]["ret_labels"] = ["←", "0", "←"]
        spec["positions"]["perspectives"] = ["Ind", "D", "Tot"]
        spec["triads"]["index_base"] = 1
        spec["triads"]["note"] = "Los arrays empiezan en cero; triad_index es 1-based."
        errors = list(self.validator.iter_errors(spec))
        self.assertEqual(errors, [])

    def test_invalid_position_metadata_is_rejected(self):
        invalid_spec = deepcopy(SPEC)
        invalid_spec["positions"]["indices"] = [0, 1]
        errors = list(self.validator.iter_errors(invalid_spec))
        self.assertTrue(any(list(error.absolute_path)[:1] == ["positions"] for error in errors))

    def test_unknown_triad_metadata_is_rejected(self):
        spec = deepcopy(SPEC)
        spec["triads"]["unexpected"] = True
        errors = list(self.validator.iter_errors(spec))
        self.assertTrue(any(list(error.absolute_path) == ["triads"] for error in errors))

    def test_missing_spec_version_is_rejected(self):
        invalid_spec = deepcopy(SPEC)
        del invalid_spec["spec_version"]
        errors = list(self.validator.iter_errors(invalid_spec))
        self.assertTrue(any("spec_version" in error.message for error in errors))

    def test_malformed_semantic_version_is_rejected(self):
        invalid_spec = deepcopy(SPEC)
        invalid_spec["spec_version"] = "1.1"
        errors = list(self.validator.iter_errors(invalid_spec))
        self.assertTrue(any(list(error.absolute_path) == ["spec_version"] for error in errors))

    def test_purpose_is_present_and_matches_schema(self):
        """La unidad informativa queda registrada en el spec canónico."""
        self.assertIn("purpose", SPEC)
        purpose = SPEC["purpose"]
        self.assertEqual(purpose["id"], "informational_unit_creation")
        self.assertIn("mínima estructura autocontenida", purpose["definition"])
        self.assertIn("criterion", purpose)
        errors = list(self.validator.iter_errors(SPEC))
        self.assertEqual(errors, [])

    def test_generated_from_records_purpose_id(self):
        stamp = json.loads((ROOT / "datasets" / "GENERATED_FROM.json").read_text(encoding="utf-8"))
        self.assertEqual(stamp.get("purpose_id"), "informational_unit_creation")
        self.assertEqual(stamp.get("spec_version"), SPEC["spec_version"])


if __name__ == "__main__":
    unittest.main()
