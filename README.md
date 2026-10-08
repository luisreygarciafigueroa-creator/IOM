# IOM — formalización, ontología y experimentos reproducibles

Repositorio ejecutable del marco I.O. El documento original [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt) se conserva íntegro. La especificación más reciente de tríadas y vectores aportada por el usuario está centralizada en [`data/iom_spec.json`](data/iom_spec.json) y transcrita en [`docs/TRIADAS_CATEGORIALES.md`](docs/TRIADAS_CATEGORIALES.md) y [`docs/VECTORES_4_5.md`](docs/VECTORES_4_5.md).

> El código verifica propiedades formales de la especificación. Los experimentos estructurales son evidencia empírica de tesis filosóficas, físicas o neurocientíficas.

## Verificación completa

Requisitos: Elan/Lean 4.9.0, Python 3.12, `venv` e Internet para instalar dependencias.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python experiments/pi_hgat_t.py
```

La CI ejecuta la compilación Lean, genera los artefactos, corre pruebas, valida OWL RL/SHACL y reproduce PI-HGAT-T.

## Contenido verificado

- **Especificación canónica:** 13 tríadas de avance, 13 de retroceso; extremo inicial de avance `involución | vacio | evolución`, extremo final de retroceso `evolución | vacio | involución`; etiquetas con acentos y orden fiel a la última tabla recibida.
- **Perspectivas 4–5:** vectores evolutivo e involutivo con cuatro filas de cinco pasos; secuencias, posiciones y flechas actuales.
- **Lean 4.9.0:** operadores temporales, espejos de posición, cotas de índices vectoriales y teoremas formales; sin `sorry` ni `admit`.
- **RDF/OWL + SHACL:** axiomas de clases y propiedades, dominios/rangos, propiedades funcionales/simetría y restricciones SHACL de estructura, espejo, creación y secuencias vectoriales. El validador ejecuta expansión OWL RL y SHACL.
- **PI-HGAT-T:** clasificador de relaciones `none`/`mirrorOf`/`creates`, PyTorch, semilla fija, validación cruzada leave-one-triad-out y ablaciones sin fase/sin posición. Las métricas se vinculan directamente con las propiedades de la ontología; no se imponen umbrales arbitrarios. Los resultados y versiones quedan registrados.
- **Datasets reproducibles:** `datasets/triad_nodes.csv` (78 filas), `datasets/vector_steps.csv` (20) y `datasets/relation_candidates.csv` (390).

## Archivos importantes

| Ruta | Función |
|---|---|
| `data/iom_spec.json` | Fuente de verdad estructurada de etiquetas, secuencias y reglas |
| `IOM/` y `IOM.lean` | Especificación de estados, operadores y teoremas Lean |
| `ontology/io_ontology.ttl` | Instancias RDF y axiomas OWL generados |
| `ontology/io_shapes.ttl` | Validación SHACL estructural y semántica |
| `scripts/generate_ontology.py` | Generación de Turtle y CSV desde la fuente canónica |
| `scripts/validate_shacl.py` | Comprobación OWL RL y SHACL |
| `experiments/` | Configuración, PI-HGAT-T, métricas, versiones y logs |
| `datasets/` | CSV regenerables para análisis y entrenamiento |
| `requirements-lock.txt` | Lock completo de dependencias; `MANIFEST.sha256` identifica artefactos |
| `dist/IOM-reproducible.zip` | Paquete reproducible generado con `scripts/package_reproducible.py` |
| `EXPERIMENTOS.md`, `AUDITORIA.md`, `REPRODUCCION.md`, `paper.md` | Método, trazabilidad, alcance y reproducción |

Para la metodología y la correspondencia de métricas: [`EXPERIMENTOS.md`](EXPERIMENTOS.md). Para ejecutar paso a paso: [`REPRODUCCION.md`](REPRODUCCION.md).
