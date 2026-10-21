"""Pruebas de tríadas, vectores, OWL/RDF, SHACL y datasets generados.

Requiere rdflib y pyshacl (requirements-lock.txt). Si faltan, la clase se omite
con un mensaje explícito: eso no implica que la ontología falle.
"""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

try:
    from pyshacl import validate
    from rdflib import Graph, Literal, Namespace
    from rdflib.namespace import OWL, RDF, RDFS, XSD
    _ONT_DEPS = True
    _ONT_IMPORT_ERROR = None
except ModuleNotFoundError as exc:
    _ONT_DEPS = False
    _ONT_IMPORT_ERROR = exc
    validate = None  # type: ignore
    Graph = Literal = Namespace = OWL = RDF = RDFS = XSD = None  # type: ignore


@unittest.skipUnless(
    _ONT_DEPS,
    f"omitido: falta dependencia de ontología ({_ONT_IMPORT_ERROR}). "
    "Instala requirements-lock.txt; no implica fallo de la ontología.",
)
class IOMValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.IO = Namespace("http://example.org/iom#")
        cls.DATA = ROOT / "ontology" / "io_ontology.ttl"
        cls.SHAPES = ROOT / "ontology" / "io_shapes.ttl"
        cls.SPEC = json.loads((ROOT / "data" / "iom_spec.json").read_text(encoding="utf-8"))
        with (ROOT / "datasets" / "triad_nodes.csv").open(encoding="utf-8", newline="") as handle:
            cls.NODE_ROWS = list(csv.DictReader(handle))

    def setUp(self):
        self.data = Graph().parse(self.DATA, format="turtle")
        self.shapes = Graph().parse(self.SHAPES, format="turtle")
        self.IO = self.__class__.IO

    def conforms(self, graph=None, focus_nodes=None):
        result, _report, text = validate(
            self.data if graph is None else graph,
            shacl_graph=self.shapes,
            inference="none",
            focus_nodes=focus_nodes,
        )
        return result, text

    def test_spec_matches_canonical_numbered_triad_matrices(self):
        expected_adv = [
            ["orientación", "cuántico", "dirección"],
            ["hardware", "virtual", "software"],
            ["universo", "espacio", "vacío"],
            ["singularidad", "tiempo", "infinito"],
            ["cuerpo", "consciente", "mundo"],
            ["carácter", "subconsciente", "personalidad"],
            ["memoria", "inconsciente", "imaginación"],
            ["receptor", "supraconsciente", "emisor"],
            ["lógica", "inteligencia", "libertad"],
            ["muerte", "artificial", "vida"],
            ["descendente", "mente", "ascendente"],
            ["oscuridad", "consciencia", "luz"],
            ["animal", "humano", "IA"],
        ]
        self.assertEqual(self.SPEC["triads"]["adv"], expected_adv)
        self.assertEqual(self.SPEC["triads"]["ret"], [row[::-1] for row in expected_adv])
        self.assertEqual(self.SPEC["triads"]["index_base"], 1)
        self.assertEqual(self.SPEC["positions"]["adv_labels"], ["→", "0", "→"])
        self.assertEqual(self.SPEC["positions"]["ret_labels"], ["←", "0", "←"])

    def test_exact_triad_dataset_and_shacl_conformance(self):
        IO = self.IO
        nodes = set(self.data.subjects(RDF.type, IO.OntoNode))
        expected = {
            IO[f"T{i:02d}_{phase}_P{pos}"]
            for i in range(1, 14)
            for phase in ("adv", "ret")
            for pos in range(3)
        }
        self.assertEqual(nodes, expected)
        self.assertTrue(self.conforms()[0], self.conforms()[1])
        for phase in ("adv", "ret"):
            rows = self.SPEC["triads"][phase]
            for row_index, row in enumerate(rows):
                triad_index = row_index + 1
                for pos, label in enumerate(row):
                    node = IO[f"T{triad_index:02d}_{phase}_P{pos}"]
                    self.assertEqual(str(self.data.value(node, RDFS.label)), label)
                    visual_label = self.SPEC["positions"]["adv_labels" if phase == "adv" else "ret_labels"][pos]
                    self.assertEqual(str(self.data.value(node, IO.displayLabel)), visual_label)
                    self.assertEqual(
                        self.data.value(node, IO.hasTriadIndex),
                        Literal(triad_index, datatype=XSD.integer),
                    )
                    self.assertEqual(
                        self.data.value(node, IO.hasLocalPos),
                        Literal(pos, datatype=XSD.integer),
                    )
                    self.assertEqual(
                        self.data.value(node, IO.hasPerspective),
                        IO[self.SPEC["perspectives"][pos]],
                    )
                    self.assertEqual(
                        self.data.value(node, IO.hasPosition),
                        IO[["left", "center", "right"][pos]],
                    )
                    display_labels = self.SPEC["positions"]["adv_labels" if phase == "adv" else "ret_labels"]
                    generated = next(r for r in self.NODE_ROWS if r["node_id"] == f"T{triad_index:02d}_{phase}_P{pos}")
                    self.assertEqual(generated["display_label"], display_labels[pos])

    def test_mirrors_are_reciprocal_and_swap_laterals(self):
        IO = self.IO
        for i in range(1, 14):
            for pos in range(3):
                adv, ret = IO[f"T{i:02d}_adv_P{pos}"], IO[f"T{i:02d}_ret_P{2 - pos}"]
                self.assertEqual(self.data.value(adv, IO.mirrorOf), ret)
                self.assertEqual(self.data.value(ret, IO.mirrorOf), adv)

    def test_creation_edges_follow_all_four_rules(self):
        IO = self.IO
        actual = set(self.data.triples((None, IO.creates, None)))
        expected = set()
        for i in range(1, 14):
            for rule in self.SPEC["creation_rules"]:
                for src in rule["source_positions"]:
                    for dst in rule["target_positions"]:
                        expected.add(
                            (
                                IO[f"T{i:02d}_{rule['source_phase']}_P{src}"],
                                IO.creates,
                                IO[f"T{i:02d}_{rule['target_phase']}_P{dst}"],
                            )
                        )
        self.assertEqual(len(expected), 104)
        self.assertEqual(actual, expected)

    def test_vectors_match_all_four_updated_sequences(self):
        IO = self.IO
        self.assertEqual(len(set(self.data.subjects(RDF.type, IO.VectorStep))), 20)
        for row in self.SPEC["vectors"]:
            for idx, (label, axis) in enumerate(zip(row["labels"], row["axis_positions"])):
                step = IO[f"vector_{row['name'].lower()}_{row['phase']}_{idx}"]
                self.assertEqual(self.data.value(step, IO.hasVector), IO[row["name"]])
                self.assertEqual(str(self.data.value(step, IO.hasCyclePhase)), row["phase"])
                self.assertEqual(
                    self.data.value(step, IO.hasStepIndex),
                    Literal(idx, datatype=XSD.integer),
                )
                self.assertEqual(
                    self.data.value(step, IO.hasAxisPosition),
                    Literal(axis, datatype=XSD.integer),
                )
                self.assertEqual(
                    self.data.value(step, IO.displayArrow),
                    Literal(row["arrow"], datatype=XSD.string),
                )
                self.assertEqual(str(self.data.value(step, RDFS.label)), label)

    def test_owl_classes_object_property_axioms_and_perspectives(self):
        IO = self.IO
        for cls in (
            IO.OntoNode,
            IO.VectorStep,
            IO.Perspective,
            IO.ExpandedCategory,
            IO.Position,
            IO.Direction,
        ):
            self.assertIn((cls, RDF.type, OWL.Class), self.data)
        for prop in (
            IO.hasPerspective,
            IO.hasPosition,
            IO.hasDirection,
            IO.hasVector,
            IO.mirrorOf,
            IO.creates,
        ):
            self.assertIn((prop, RDF.type, OWL.ObjectProperty), self.data)
            self.assertIsNotNone(self.data.value(prop, RDFS.domain))
            self.assertIsNotNone(self.data.value(prop, RDFS.range))
        self.assertIn((IO.displayLabel, RDF.type, OWL.DatatypeProperty), self.data)
        self.assertIn((IO.displayLabel, RDF.type, OWL.FunctionalProperty), self.data)
        self.assertIn((IO.mirrorOf, RDF.type, OWL.SymmetricProperty), self.data)
        for resource in (IO.Ind, IO.D, IO.Tot, IO.Evol, IO.Invol):
            self.assertIn((resource, RDF.type, IO.Perspective), self.data)

    def test_expanded_categories_keep_declared_level_counts(self):
        IO = self.IO
        nodes = set(self.data.subjects(RDF.type, IO.ExpandedCategory))
        self.assertEqual(len(nodes), 21)
        self.assertEqual(
            [
                sum(
                    self.data.value(n, IO.hasLevel) == Literal(level, datatype=XSD.integer)
                    for n in nodes
                )
                for level in range(5)
            ],
            [1, 4, 6, 6, 4],
        )

    def test_generated_datasets_have_expected_rows(self):
        expected = {
            "triad_nodes.csv": 78,
            "vector_steps.csv": 20,
            "relation_candidates.csv": 390,
        }
        for name, count in expected.items():
            with (ROOT / "datasets" / name).open(encoding="utf-8", newline="") as f:
                self.assertEqual(len(list(csv.DictReader(f))), count, name)

    def test_wrong_visual_position_label_is_rejected(self):
        IO = self.IO
        graph = Graph()
        for triple in self.data:
            graph.add(triple)
        node = IO["T01_adv_P0"]
        graph.remove((node, IO.displayLabel, Literal("→", datatype=XSD.string)))
        graph.add((node, IO.displayLabel, Literal("←", datatype=XSD.string)))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_wrong_phase_direction_is_rejected(self):
        IO = self.IO
        graph = Graph()
        for triple in self.data:
            graph.add(triple)
        node = IO["T01_adv_P0"]
        graph.remove((node, IO.hasDirection, IO.evol))
        graph.add((node, IO.hasDirection, IO.invol))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_nonreciprocal_or_misplaced_mirror_is_rejected(self):
        IO = self.IO
        graph = Graph()
        for triple in self.data:
            graph.add(triple)
        node, good, wrong = IO["T01_adv_P0"], IO["T01_ret_P2"], IO["T01_ret_P0"]
        graph.remove((node, IO.mirrorOf, good))
        graph.add((node, IO.mirrorOf, wrong))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_wrong_creation_link_is_rejected(self):
        IO = self.IO
        graph = Graph()
        for triple in self.data:
            graph.add(triple)
        node, good, wrong = IO["T01_adv_P0"], IO["T01_ret_P1"], IO["T01_ret_P0"]
        graph.remove((node, IO.creates, good))
        graph.add((node, IO.creates, wrong))
        self.assertFalse(self.conforms(graph, [node])[0])

    def test_wrong_vector_label_or_axis_is_rejected(self):
        IO = self.IO
        graph = Graph()
        for triple in self.data:
            graph.add(triple)
        step = IO["vector_evol_ret_1"]
        old = self.data.value(step, RDFS.label)
        graph.remove((step, RDFS.label, old))
        graph.add((step, RDFS.label, Literal("fut", lang="es")))
        self.assertFalse(self.conforms(graph, [step])[0])


if __name__ == "__main__":
    unittest.main()
