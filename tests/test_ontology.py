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


class OntologyValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = Graph().parse(DATA, format="turtle")
        self.shapes = Graph().parse(SHAPES, format="turtle")

    def test_generated_node_count_and_conformance(self):
        self.assertEqual(len(set(self.data.subjects(RDF.type, IO.OntoNode))), 78)
        conforms, _report, _text = validate(self.data, shacl_graph=self.shapes, inference="none")
        self.assertTrue(conforms)

    def test_invalid_triad_index_is_rejected(self):
        node = next(self.data.subjects(RDF.type, IO.OntoNode))
        self.data.remove((node, IO.hasTriadIndex, None))
        self.data.add((node, IO.hasTriadIndex, Literal(13, datatype=XSD.integer)))
        conforms, _report, report_text = validate(self.data, shacl_graph=self.shapes, inference="none")
        self.assertFalse(conforms, report_text)


if __name__ == "__main__":
    unittest.main()
