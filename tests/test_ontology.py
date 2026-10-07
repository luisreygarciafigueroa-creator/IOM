"""Pruebas de regresión para generación y validación de la ontología."""
import unittest
from pathlib import Path

from pyshacl import validate
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, XSD

ROOT = Path(__file__).resolve().parents[1]
IO = Namespace("http://example.org/iom#")
DATA = ROOT / "ontology" / "io_ontology.ttl"
SHAPES = ROOT / "ontology" / "io_shapes.ttl"
PERSPECTIVES = (IO.Ind, IO.D, IO.Tot, IO.Evol, IO.Invol)


class OntologyValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = Graph().parse(DATA, format="turtle")
        self.shapes = Graph().parse(SHAPES, format="turtle")

    def conforms(self, graph=None, focus_nodes=None):
        conforms, _report, report_text = validate(
            self.data if graph is None else graph,
            shacl_graph=self.shapes,
            inference="none",
            focus_nodes=focus_nodes,
        )
        return conforms, report_text

    def test_generated_node_count_and_conformance(self):
        nodes = set(self.data.subjects(RDF.type, IO.OntoNode))
        expected_nodes = {
            IO[f"T{triad:02d}_{phase}_P{position}"]
            for triad in range(13)
            for phase in ("adv", "ret")
            for position in range(3)
        }
        self.assertEqual(len(nodes), 78)
        self.assertEqual(nodes, expected_nodes)
        conforms, report_text = self.conforms()
        self.assertTrue(conforms, report_text)

    def test_generated_mirrors_are_reciprocal_and_aligned(self):
        for node in self.data.subjects(RDF.type, IO.OntoNode):
            mirror = self.data.value(node, IO.mirrorOf)
            self.assertIsNotNone(mirror)
            self.assertNotEqual(node, mirror)
            self.assertIn((mirror, RDF.type, IO.OntoNode), self.data)
            self.assertEqual(self.data.value(mirror, IO.mirrorOf), node)
            self.assertEqual(
                self.data.value(node, IO.hasTriadIndex),
                self.data.value(mirror, IO.hasTriadIndex),
            )
            self.assertEqual(
                self.data.value(node, IO.hasLocalPos),
                self.data.value(mirror, IO.hasLocalPos),
            )
            phases = {
                self.data.value(node, IO.hasPhase),
                self.data.value(mirror, IO.hasPhase),
            }
            self.assertEqual(phases, {Literal("adv"), Literal("ret")})

    def test_generated_direction_and_perspective_match_definitions(self):
        for node in self.data.subjects(RDF.type, IO.OntoNode):
            phase = self.data.value(node, IO.hasPhase)
            triad = int(self.data.value(node, IO.hasTriadIndex))
            position = int(self.data.value(node, IO.hasLocalPos))
            expected_direction = IO.evol if phase == Literal("adv") else IO.invol
            self.assertEqual(self.data.value(node, IO.hasDirection), expected_direction)
            self.assertEqual(
                self.data.value(node, IO.hasPerspective),
                PERSPECTIVES[(triad + position) % len(PERSPECTIVES)],
            )

    def test_invalid_triad_index_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        self.data.remove((node, IO.hasTriadIndex, None))
        self.data.add((node, IO.hasTriadIndex, Literal(13, datatype=XSD.integer)))
        conforms, report_text = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report_text)

    def test_mismatched_mirror_is_rejected(self):
        node = next(
            subject for subject in self.data.subjects(IO.hasPhase, Literal("adv"))
        )
        old_mirror = self.data.value(node, IO.mirrorOf)
        wrong_mirror = next(
            subject
            for subject in self.data.subjects(IO.hasPhase, Literal("adv"))
            if subject != node
        )
        self.data.remove((node, IO.mirrorOf, old_mirror))
        self.data.add((node, IO.mirrorOf, wrong_mirror))
        conforms, report_text = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report_text)

    def test_phase_direction_mismatch_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        direction = self.data.value(node, IO.hasDirection)
        self.data.remove((node, IO.hasDirection, direction))
        self.data.add((node, IO.hasDirection, IO.invol if direction == IO.evol else IO.evol))
        conforms, report_text = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report_text)

    def test_perspective_formula_mismatch_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        perspective = self.data.value(node, IO.hasPerspective)
        replacement = IO.D if perspective != IO.D else IO.Ind
        self.data.remove((node, IO.hasPerspective, perspective))
        self.data.add((node, IO.hasPerspective, replacement))
        conforms, report_text = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report_text)


if __name__ == "__main__":
    unittest.main()
