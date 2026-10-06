#!/usr/bin/env python3
"""Valida ontology/io_ontology.ttl contra ontology/io_shapes.ttl."""
from pyshacl import validate

conforms, results_graph, results_text = validate(
    "ontology/io_ontology.ttl",
    shacl_graph="ontology/io_shapes.ttl",
    inference="none",
    abort_on_first=False,
)

print(results_text)
if conforms:
    print("✓ Las 4 restricciones SHACL fueron satisfechas.")
else:
    print("✗ La ontología NO satisface las restricciones SHACL")
    exit(1)
