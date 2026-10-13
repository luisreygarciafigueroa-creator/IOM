# IOM — reglas formales y evaluación reproducible

IOM es un marco estructural que conecta una especificación canónica con reglas verificadas en Lean/RDF y experimentos reproducibles. Las métricas miden recuperación de relaciones generadas por reglas, **no validación independiente de la teoría**.

[![CI](https://github.com/luisreygarciafigueroa-creator/IOM/actions/workflows/ci.yml/badge.svg)](https://github.com/luisreygarciafigueroa-creator/IOM/actions/workflows/ci.yml)

## Inicio rápido

Con Python **3.12** y Lean 4.9.0 instalados:

```bash
python -m pip install -r requirements-lock.txt
python scripts/validate_csv.py && python scripts/verify_bridge.py && lake build
```

## Documentación

- [Guía completa: marco, pipeline e ingesta](docs/GUIA.md)
- [Experimentos y resultados](EXPERIMENTOS.md)
- [Reproducción](REPRODUCCION.md)
- [Diccionario de datos y contratos CSV](docs/DATA_DICTIONARY.md)
- [Protocolo de evaluación independiente](datasets/independent_eval/README.md)
- [Notebook demo sin Lean](notebooks/demo_pipeline.ipynb)
- [Documentación navegable](docs/index.md)
- [Playbook de extensión y versionado](docs/EXTENSION_Y_VERSIONADO.md)
- [Cómo citar](CITATION.cff) · [Licencia MIT](LICENSE)

Fuente canónica: [`data/iom_spec.json`](data/iom_spec.json). La CI comprueba Lean, CSV, RDF↔etiquetas, SHACL y experimentos; publica métricas en el resumen de la ejecución y como artefactos descargables.
