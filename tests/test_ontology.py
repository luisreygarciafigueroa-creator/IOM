"""Pruebas de tríadas, vectores, OWL/RDF, SHACL y datasets generados."""
import csv
import json
import unittest
from pathlib import Path

from pyshacl import validate
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import OWL, RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
DATA = ROOT / "ontology" / "io_ontology.ttl"
SHAPES = ROOT / "ontology" / "io_shapes.ttl"
SPEC = json.loads((ROOT / "data" / "iom_spec.json").read_text(encoding="utf-8"))


class IOMValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = Graph().parse(DATA, format="turtle")
        self.shapes = Graph().parse(SHAPES, format="turtle")

    def conforms(self, graph=None, focus_nodes=None):
        result, _report, text = validate(self.data if graph is None else graph,
                                         shacl_graph=self.shapes, inference="none",
                                         focus_nodes=focus_nodes)
        return result, text

    def test_exact_triad_dataset_and_shacl_conformance(self):
        nodes = set(self.data.subjects(RDF.type, IO.OntoNode))
        expected = {IO[f"T{i:02d}_{phase}_P{pos}"]
                    for i in range(13) for phase in ("adv", "ret") for pos in range(3)}
        self.assertEqual(nodes, expected)
        self.assertTrue(self.conforms()[0], self.conforms()[1])
        for phase, rows in SPEC["triads"].items():
            for i, row in enumerate(rows):
                for pos, label in enumerate(row):
                    node = IO[f"T{i:02d}_{phase}_P{pos}"]
                    self.assertEqual(str(self.data.value(node, RDFS.label)), label)
                    self.assertEqual(self.data.value(node, IO.hasTriadIndex), Literal(i, datatype=XSD.integer))
                    self.assertEqual(self.data.value(node, IO.hasLocalPos), Literal(pos, datatype=XSD.integer))
                    self.assertEqual(self.data.value(node, IO.hasPerspective), IO[SPEC["perspectives"][pos]])
                    self.assertEqual(self.data.value(node, IO.hasPosition), IO[SPEC["positions"][pos]])

    def test_mirrors_are_reciprocal_and_swap_laterals(self):
        for i in range(13):
            for pos in range(3):
                adv, ret = IO[f"T{i:02d}_adv_P{pos}"], IO[f"T{i:02d}_ret_P{2-pos}"]
                self.assertEqual(self.data.value(adv, IO.mirrorOf), ret)
                self.assertEqual(self.data.value(ret, IO.mirrorOf), adv)

    def test_creation_edges_follow_all_four_rules(self):
        actual = set(self.data.triples((None, IO.creates, None)))
        expected = set()
        for i in range(13):
            for rule in SPEC["creation_rules"]:
                for src in rule["source_positions"]:
                    for dst in rule["target_positions"]:
                        expected.add((IO[f"T{i:02d}_{rule['source_phase']}_P{src}"], IO.creates,
                                      IO[f"T{i:02d}_{rule['target_phase']}_P{dst}"]))
        self.assertEqual(len(expected), 104)
        self.assertEqual(actual, expected)

    def test_vectors_match_all_four_updated_sequences(self):
        self.assertEqual(len(set(self.data.subjects(RDF.type, IO.VectorStep))), 20)
        for row in SPEC["vectors"]:
            for idx, (label, axis) in enumerate(zip(row["labels"], row["axis_positions"])):
                step = IO[f"vector_{row['name'].lower()}_{row['phase']}_{idx}"]
                self.assertEqual(self.data.value(step, IO.hasVector), IO[row["name"]])
                self.assertEqual(str(self.data.value(step, IO.hasCyclePhase)), row["phase"])
                self.assertEqual(self.data.value(step, IO.hasStepIndex), Literal(idx, datatype=XSD.integer))
                self.assertEqual(self.data.value(step, IO.hasAxisPosition), Literal(axis, datatype=XSD.integer))
                self.assertEqual(self.data.value(step, IO.displayArrow), Literal(row["arrow"], datatype=XSD.string))
                self.assertEqual(str(self.data.value(step, RDFS.label)), label)

    def test_owl_classes_object_property_axioms_and_perspectives(self):
        for cls in (IO.OntoNode, IO.VectorStep, IO.Perspective, IO.ExpandedCategory, IO.Position, IO.Direction):
            self.assertIn((cls, RDF.type, OWL.Class), self.data)
        for prop in (IO.hasPerspective, IO.hasPosition, IO.hasDirection, IO.hasVector, IO.mirrorOf, IO.creates):
            self.assertIn((prop, RDF.type, OWL.ObjectProperty), self.data)
            self.assertIsNotNone(self.data.value(prop, RDFS.domain))
            self.assertIsNotNone(self.data.value(prop, RDFS.range))
        self.assertIn((IO.mirrorOf, RDF.type, OWL.SymmetricProperty), self.data)
        for resource in (IO.Ind, IO.D, IO.Tot, IO.Evol, IO.Invol):
            self.assertIn((resource, RDF.type, IO.Perspective), self.data)

    def test_expanded_categories_keep_declared_level_counts(self):
        nodes = set(self.data.subjects(RDF.type, IO.ExpandedCategory))
        self.assertEqual(len(nodes), 21)
        self.assertEqual([sum(self.data.value(n, IO.hasLevel) == Literal(level, datatype=XSD.integer) for n in nodes)
                          for level in range(5)], [1, 4, 6, 6, 4])

    def test_generated_datasets_have_expected_rows(self):
        expected = {"triad_nodes.csv": 78, "vector_steps.csv": 20, "relation_candidates.csv": 390}
        for name, count in expected.items():
            with (ROOT / "datasets" / name).open(encoding="utf-8", newline="") as f:
                self.assertEqual(len(list(csv.DictReader(f))), count, name)

    def test_wrong_phase_direction_is_rejected(self):
        graph = Graph()
        for triple in self.data: graph.add(triple)
        node = IO["T00_adv_P0"]
        graph.remove((node, IO.hasDirection, IO.evol))
        graph.add((node, IO.hasDirection, IO.invol))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_nonreciprocal_or_misplaced_mirror_is_rejected(self):
        graph = Graph()
        for triple in self.data: graph.add(triple)
        node, good, wrong = IO["T00_adv_P0"], IO["T00_ret_P2"], IO["T00_ret_P0"]
        graph.remove((node, IO.mirrorOf, good))
        graph.add((node, IO.mirrorOf, wrong))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_wrong_creation_link_is_rejected(self):
        graph = Graph()
        for triple in self.data: graph.add(triple)
        node, good, wrong = IO["T00_adv_P0"], IO["T00_ret_P1"], IO["T01_ret_P1"]
        graph.remove((node, IO.creates, good))
        graph.add((node, IO.creates, wrong))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_wrong_vector_label_or_axis_is_rejected(self):
        graph = Graph()
        for triple in self.data: graph.add(triple)
        step = IO["vector_evol_ret_1"]
        old = self.data.value(step, RDFS.label)
        graph.remove((step, RDFS.label, old))
        graph.add((step, RDFS.label, Literal("fut", lang="es")))
        self.assertFalse(self.conforms(graph, [step])[0])


if __name__ == "__main__":
    unittest.main()
