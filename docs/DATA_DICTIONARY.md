# Diccionario de datos y contratos CSV

Los contratos máquina-legibles están en [`data/csv_schemas.json`](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/data/csv_schemas.json); se validan con `python scripts/validate_csv.py`. Las filas CSV se parsean como texto y el validador convierte explícitamente campos enteros.

## `datasets/triad_nodes.csv` (78 filas)

| Columna | Tipo/dominio | Semántica |
|---|---|---|
| `node_id` | cadena `TNN_{adv,ret}_P{0,1,2}` | Identificador estable, triada, fase y posición. |
| `triad_index` | entero ≥ 0 | Índice de triada dentro de la fase; no es feature del modelo. |
| `phase` | `adv` / `ret` | Fase de avance o retroceso. |
| `direction` | `evol` / `invol` | Dirección vectorial asignada por la especificación a esa fase. |
| `position_index` | entero 0–2 | Índice posicional: 0 izquierda, 1 centro, 2 derecha. |
| `position` | `left` / `center` / `right` | Nombre legible de posición; debe corresponder al índice. |
| `perspective` | `Ind` / `D` / `Tot` | Perspectiva posicional de la columna. |
| `label` | cadena no vacía | Rótulo de dominio de la fuente; el clasificador PI-HGAT-T lo excluye. |

## `datasets/vector_steps.csv` (20 filas)

| Columna | Tipo/dominio | Semántica |
|---|---|---|
| `step_id` | cadena | Identificador del paso vectorial. |
| `vector` | cadena | Nombre de la secuencia vectorial (Evol/Invol). |
| `phase` | `adv` / `ret` | Fase a la que pertenece la secuencia. |
| `step_index` | entero 0–4 | Índice ordinal del paso usado por RDF (`io:hasStepIndex`). |
| `axis_position` | entero 0–4 | Coordenada sobre el eje del vector. |
| `label` | cadena no vacía | Etiqueta textual de ese paso. |
| `arrow` | cadena no vacía | Notación direccional declarada. |

## `datasets/relation_candidates.csv` (390 filas)

| Columna | Tipo/dominio | Semántica |
|---|---|---|
| `triad_index` | entero ≥ 0 | Triada local a la que pertenece el par. |
| `source`, `target` | ID canónico de nodo | Par dirigido; no reflexivo. |
| `relation` | `none`, `mirrorOf`, `creates` | Etiqueta derivada de aristas RDF `io:mirrorOf` / `io:creates`; `none` significa ausencia de ambas reglas en el universo de candidatos. |

## Procedencia y validación

Se generan desde `data/iom_spec.json` por `scripts/generate_ontology.py`. `scripts/verify_bridge.py` compara etiquetas completas —incluidos negativos— con RDF y reporta hashes SHA-256; el test no sustituye Lean/SHACL ni la evaluación independiente.
