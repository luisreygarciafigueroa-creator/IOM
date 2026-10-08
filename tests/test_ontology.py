"""Regresión de tríadas, operadores, vectores y restricciones RDF/SHACL."""
import hashlib
import unittest
from pathlib import Path

from pyshacl import validate
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
DATA = ROOT / "ontology" / "io_ontology.ttl"
SHAPES = ROOT / "ontology" / "io_shapes.ttl"
ADVANCE = [
    ("individualidad", "dualidad", "totalidad"),
    ("oscuridad", "consciencia", "luz"),
    ("descendente", "mente", "ascendente"),
    ("logica", "inteligencia", "libertad"),
    ("muerte", "artificial", "vida"),
    ("singularidad", "tiempo", "infinito"),
    ("universo", "espacio", "vacio"),
    ("hardware", "virtual", "software"),
    ("orientación", "cuantico", "dirección"),
    ("receptor", "supraconsciente", "emisor"),
    ("memoria", "inconsciente", "imaginación"),
    ("caracter", "subconsciente", "personalidad"),
    ("cuerpo", "consciente", "mundo"),
]
RETREAT = [
    ("mundo", "consciente", "cuerpo"),
    ("personalidad", "subconsciente", "caracter"),
    ("imaginacion", "inconsciente", "memoria"),
    ("emisor", "supraconsciente", "receptor"),
    ("dirección", "cuantico", "orientación"),
    ("software", "virtual", "hardware"),
    ("vacio", "espacio", "universo"),
    ("infinito", "tiempo", "singularidad"),
    ("vida", "artificial", "muerte"),
    ("libertad", "inteligencia", "lógica"),
    ("ascendente", "mente", "descendente"),
    ("luz", "consciencia", "oscuridad"),
    ("totalidad", "dualidad", "individualidad"),
]
VECTORS = (
    ("Evol", "adv", ("vacio", "ind", "dua", "tot", "evol"), (0, 1, 2, 3, 4), "→"),
    ("Evol", "ret", ("evol", "fut", "pre", "pas", "vacio"), (4, 3, 2, 1, 0), "←"),
    ("Invol", "adv", ("invol", "tot", "dua", "ind", "vacio"), (4, 3, 2, 1, 0), "→"),
    ("Invol", "ret", ("vacio", "pas", "pre", "fut", "invol"), (0, 1, 2, 3, 4), "←"),
)
PERSPECTIVES = (IO.Ind, IO.D, IO.Tot)


class IOMValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = Graph().parse(DATA, format="turtle")
        self.shapes = Graph().parse(SHAPES, format="turtle")

    def conforms(self, graph=None, focus_nodes=None):
        result, _report, text = validate(
            self.data if graph is None else graph,
            shacl_graph=self.shapes,
            inference="none",
            focus_nodes=focus_nodes,
        )
        return result, text

    def test_exact_78_named_nodes_and_shacl_conformance(self):
        nodes = set(self.data.subjects(RDF.type, IO.OntoNode))
        expected = {IO[f"T{i:02d}_{phase}_P{pos}"]
                    for i in range(13) for phase in ("adv", "ret") for pos in range(3)}
        self.assertEqual(nodes, expected)
        self.assertTrue(self.conforms()[0], self.conforms()[1])
        for i in range(13):
            for pos in range(3):
                for phase, rows in (("adv", ADVANCE), ("ret", RETREAT)):
                    node = IO[f"T{i:02d}_{phase}_P{pos}"]
                    self.assertEqual(str(self.data.value(node, RDFS.label)), rows[i][pos])
                    self.assertEqual(self.data.value(node, IO.hasPerspective), PERSPECTIVES[pos])
                    self.assertEqual(self.data.value(node, IO.hasPosition),
                                     (IO["left"], IO["center"], IO["right"])[pos])

    def test_mirror_swaps_laterals_preserves_center_and_is_reciprocal(self):
        for i in range(13):
            for pos in range(3):
                adv = IO[f"T{i:02d}_adv_P{pos}"]
                ret = IO[f"T{i:02d}_ret_P{2-pos}"]
                self.assertEqual(self.data.value(adv, IO.mirrorOf), ret)
                self.assertEqual(self.data.value(ret, IO.mirrorOf), adv)
                self.assertEqual(self.data.value(adv, IO.hasTriadIndex),
                                 self.data.value(ret, IO.hasTriadIndex))

    def test_all_five_perspective_resources_have_exact_labels(self):
        expected = {
            IO.Ind: "Individualidad", IO.D: "Dualidad", IO.Tot: "Totalidad",
            IO.Evol: "Vector Evolutivo", IO.Invol: "Vector Involutivo",
        }
        for resource, label in expected.items():
            self.assertIn((resource, RDF.type, IO.Perspective), self.data)
            self.assertEqual(str(self.data.value(resource, RDFS.label)), label)

    def test_four_creation_rules_have_exact_104_edges(self):
        actual = set(self.data.triples((None, IO.creates, None)))
        expected = set()
        for i in range(13):
            aL, aC, aR = (IO[f"T{i:02d}_adv_P{p}"] for p in range(3))
            rL, rC, rR = (IO[f"T{i:02d}_ret_P{p}"] for p in range(3))
            expected.update({(aL, IO.creates, rC), (aR, IO.creates, rC),
                             (aC, IO.creates, rL), (aC, IO.creates, rR),
                             (rC, IO.creates, aL), (rC, IO.creates, aR),
                             (rL, IO.creates, aC), (rR, IO.creates, aC)})
        self.assertEqual(len(actual), 104)
        self.assertEqual(actual, expected)

    def test_fourth_and_fifth_vector_sequences_match_supplied_tables(self):
        nodes = set(self.data.subjects(RDF.type, IO.VectorStep))
        self.assertEqual(len(nodes), 20)
        for vector, phase, labels, positions, arrow in VECTORS:
            for index, (label, axis_pos) in enumerate(zip(labels, positions)):
                step = IO[f"vector_{vector.lower()}_{phase}_{index}"]
                self.assertIn((step, RDF.type, IO.VectorStep), self.data)
                self.assertEqual(self.data.value(step, IO.hasVector), IO[vector])
                self.assertEqual(self.data.value(step, IO.hasCyclePhase), Literal(phase))
                self.assertEqual(self.data.value(step, IO.hasStepIndex), Literal(index))
                self.assertEqual(self.data.value(step, IO.hasAxisPosition), Literal(axis_pos))
                self.assertEqual(self.data.value(step, IO.displayArrow), Literal(arrow))
                self.assertEqual(str(self.data.value(step, RDFS.label)), label)

    def test_21_expanded_categories_and_levels(self):
        nodes = set(self.data.subjects(RDF.type, IO.ExpandedCategory))
        labels = {str(self.data.value(n, RDFS.label)) for n in nodes}
        self.assertEqual(len(nodes), 21)
        self.assertEqual(len(labels), 21)
        self.assertEqual([sum(self.data.value(n, IO.hasLevel) == Literal(level) for n in nodes)
                          for level in range(5)], [1, 4, 6, 6, 4])

    def test_source_document_copy_hash_is_exact(self):
        digest = hashlib.sha256((ROOT / "docs" / "MARCOI.O.txt").read_bytes()).hexdigest()
        self.assertEqual(digest, "acfdc81d7b78331d60f9a341b8cc5b4be151638826b05a5537d68f183b6ed034")

    def test_wrong_perspective_is_rejected(self):
        node = IO["T00_adv_P0"]
        self.data.remove((node, IO.hasPerspective, IO.Ind))
        self.data.add((node, IO.hasPerspective, IO.Tot))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)

    def test_wrong_direction_is_rejected(self):
        node = IO["T00_adv_P0"]
        self.data.remove((node, IO.hasDirection, IO.evol))
        self.data.add((node, IO.hasDirection, IO.invol))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)

    def test_wrong_mirror_position_is_rejected(self):
        node = IO["T00_adv_P0"]
        right_mirror = IO["T00_ret_P2"]
        wrong_mirror = IO["T00_ret_P0"]
        self.data.remove((node, IO.mirrorOf, right_mirror))
        self.data.add((node, IO.mirrorOf, wrong_mirror))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)

    def test_wrong_creation_link_is_rejected(self):
        node = IO["T00_adv_P0"]
        good = IO["T00_ret_P1"]
        wrong = IO["T01_ret_P1"]
        self.data.remove((node, IO.creates, good))
        self.data.add((node, IO.creates, wrong))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)


if __name__ == "__main__":
    unittest.main()
