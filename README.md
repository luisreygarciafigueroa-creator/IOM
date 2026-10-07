# IOM — Realidad I.O

Marco ontológico-formal en desarrollo, con Lean 4 y una ontología RDF validada mediante SHACL.

El repositorio contiene actualmente una implementación Lean acotada (`IOM/Core.lean`, `IOM/Operators.lean`) y scripts para generar y validar el grafo RDF. La validación cubre las restricciones definidas en `ontology/io_shapes.ttl`; no implica una verificación automática de todas las tesis del artículo.

## Requisitos

- Lean 4.9.0 (según `lean-toolchain`) para `lake build`.
- Python 3.9+ para la ontología RDF.

## Verificación

Desde la raíz del repositorio:

```bash
lake build
python -m pip install -r requirements.txt
python scripts/generate_ontology.py
python scripts/validate_shacl.py
```

Consulta [la guía de reproducción](REPRODUCCION.md) para más detalles y [el artículo](paper.md) para la propuesta teórica.
