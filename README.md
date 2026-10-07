# IOM — Realidad I.O

Marco ontológico-formal en desarrollo, con Lean 4 y una ontología RDF validada mediante SHACL.

El repositorio contiene actualmente una implementación Lean acotada (`IOM/Core.lean`, `IOM/Operators.lean`) y scripts para generar y validar el grafo RDF. La validación cubre las restricciones definidas en `ontology/io_shapes.ttl`; no implica una verificación automática de todas las tesis del artículo.

## Requisitos

- Lean 4.9.0 (según `lean-toolchain`) para `lake build`.
- Python 3.9+ para la ontología RDF.

## Verificación

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

El entorno virtual evita modificar el Python del sistema, que algunas distribuciones (incluido Ubuntu reciente) protegen contra instalaciones globales con `pip`.

Consulta [la guía de reproducción](REPRODUCCION.md) para más detalles y [el artículo](paper.md) para la propuesta teórica.
