"""Pruebas de regresión RDF/SHACL para los datos enumerados en MARCOI.O.txt."""
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
EXPECTED_LABELS = {
    "Vacío Generativo (V)", "Potencia", "Acto", "Percepción", "Acción",
    "Sujeto-Objeto", "Causa-Efecto", "Presencia-Ausencia",
    "Símbolo-Significado", "Límite-Transgresión", "Mediación",
    "Sistema", "Entorno", "Red", "Holismo", "Emergencia", "Colapso",
    "E", "S_fwd", "Ivo", "S_rev",
}


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

    def test_exactly_78_structural_nodes_and_shacl_conformance(self):
        nodes = set(self.data.subjects(RDF.type, IO.OntoNode))
        expected = {
            IO[f"T{i:02d}_{phase}_P{pos}"]
            for i in range(13) for phase in ("adv", "ret") for pos in range(3)
        }
        self.assertEqual(nodes, expected)
        self.assertTrue(self.conforms()[0], self.conforms()[1])

    def test_mirrors_are_reciprocal_aligned_and_phase_opposed(self):
        for node in self.data.subjects(RDF.type, IO.OntoNode):
            mirror = self.data.value(node, IO.mirrorOf)
            self.assertIsNotNone(mirror)
            self.assertEqual(self.data.value(mirror, IO.mirrorOf), node)
            for prop in (IO.hasTriadIndex, IO.hasLocalPos):
                self.assertEqual(self.data.value(node, prop), self.data.value(mirror, prop))
            self.assertNotEqual(self.data.value(node, IO.hasPhase), self.data.value(mirror, IO.hasPhase))

    def test_phase_direction_correspondence(self):
        for node in self.data.subjects(RDF.type, IO.OntoNode):
            phase = self.data.value(node, IO.hasPhase)
            expected = IO.evol if phase == Literal("adv") else IO.invol
            self.assertEqual(self.data.value(node, IO.hasDirection), expected)

    def test_exact_21_expanded_category_labels_and_level_counts(self):
        nodes = set(self.data.subjects(RDF.type, IO.ExpandedCategory))
        labels = {str(label) for label in self.data.objects(None, RDFS.label)
                  if (label, ) and (None, RDF.type, IO.ExpandedCategory) in self.data}
        labels = {str(self.data.value(node, RDFS.label)) for node in nodes}
        self.assertEqual(len(nodes), 21)
        self.assertEqual(labels, EXPECTED_LABELS)
        self.assertEqual([sum(1 for n in nodes if self.data.value(n, IO.hasLevel) == Literal(level))
                          for level in range(5)], [1, 4, 6, 6, 4])

    def test_source_examples_are_kept_without_inventing_the_other_eleven(self):
        labels = {str(self.data.value(n, RDFS.label))
                  for n in self.data.subjects(RDF.type, IO.SourceTriadExample)}
        self.assertEqual(labels, {"Oscuridad-Consciencia-Luz", "Hardware-Virtual-Software"})
        self.assertEqual(len(list(self.data.subjects(RDF.type, IO.SourceTriadExample))), 2)

    def test_source_document_matches_recorded_sha256(self):
        source = ROOT / "docs" / "MARCOI.O.txt"
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.assertEqual(digest, "acfdc81d7b78331d60f9a341b8cc5b4be151638826b05a5537d68f183b6ed034")

    def test_no_unsupported_perspective_or_vacuum_claim_per_structural_node(self):
        for node in self.data.subjects(RDF.type, IO.OntoNode):
            self.assertFalse(list(self.data.objects(node, IO.hasPerspective)))
            self.assertFalse(list(self.data.objects(node, IO.restoresVacuum)))

    def test_invalid_triad_index_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        self.data.remove((node, IO.hasTriadIndex, None))
        self.data.add((node, IO.hasTriadIndex, Literal(13, datatype=XSD.integer)))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)

    def test_wrong_phase_direction_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        direction = self.data.value(node, IO.hasDirection)
        self.data.remove((node, IO.hasDirection, direction))
        self.data.add((node, IO.hasDirection, IO.invol if direction == IO.evol else IO.evol))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)

    def test_mismatched_mirror_is_rejected(self):
        node = next(self.data.subjects(IO.hasPhase, Literal("adv")))
        old = self.data.value(node, IO.mirrorOf)
        wrong = next(n for n in self.data.subjects(IO.hasPhase, Literal("adv")) if n != node)
        self.data.remove((node, IO.mirrorOf, old))
        self.data.add((node, IO.mirrorOf, wrong))
        conforms, report = self.conforms(focus_nodes=[node])
        self.assertFalse(conforms, report)


if __name__ == "__main__":
    unittest.main()
