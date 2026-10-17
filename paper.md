# IOM — prueba de validez semántica en el mundo real

## Alcance y procedencia

Este informe presenta el repositorio IOM como una **prueba y demostración** de validez semántica del marco I.O. cuando se aplica a conceptos y pares **externos** a las reglas canónicas. El documento de referencia se conserva en [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt); la especificación operativa en [`data/iom_spec.json`](data/iom_spec.json). Metodología: [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md).

Las afirmaciones sobre **vacío**, **unidad informativa**, **infinito** y **transformación** (premisas vs teoremas) constan en [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md). Lean formaliza espejos, creates y vectores en `IOM/FormalRules.lean`.

## Delimitación epistemológica

Tres capas no intercambiables ([`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)):

| Capa | Artefactos | Afirmación legítima |
|---|---|---|
| **Validez semántica (mundo real)** | `independent_eval/`, protocolo ciego, κ, desacuerdos, catálogo de dominios | Interpretabilidad y acuerdo sobre conceptos externos (**eje del repositorio**) |
| **Formal** | Lean 4, teoremas sin `sorry` | Corrección *dentro del sistema formal* |
| **Sintética** | SHACL, CSV, PI-HGAT-T, baselines | Recuperabilidad de relaciones *generadas por reglas* (diagnóstico interno) |

Las métricas sintéticas **no** se interpretan como validez semántica en el mundo real.

## Prueba de validez semántica (eje empírico)

`datasets/independent_eval/` define pares fuera de las cuatro reglas, conceptos nuevos y casos ambiguos, con protocolo de anotación **ciega**. Las etiquetas de prueba **no** se derivan de `relation_candidates.csv`.

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Unánime | 10/14 |
| Controles unánimes | sí |
| Desacuerdos | NC01, NC02, AM01, AM03 |

Lectura: demostración **provisional** de interpretabilidad semántica bajo protocolo ciego, no prueba universal del marco.

Scoring: `python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`. La coincidencia post-hoc con `rule_reference` es informativa, no el objetivo primario.

Alineación a dominios reales (biología, economía, …): [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md).

## Especificación categorial

Trece tríadas por fase; cinco perspectivas (Individualidad, Dualidad, Totalidad, Evolución, Involución). 78 nodos; 104 aristas `io:creates`; espejos recíprocos. Spec y CSV canónicos definen la **estructura semántica bajo prueba**, no la evidencia de mundo real.

## Formalización Lean y ontología

`IOM/Core.lean`, `Operators.lean`, `Specification.lean`, `FormalRules.lean` (predicado `isMirror` / `isCreates`). OWL/SHACL y puentes de prueba garantizan conformidad estructural. Compilación Lean 4.9.0 sin `sorry`.

## Diagnóstico sintético: PI-HGAT-T (no es validez semántica real)

Mide si las relaciones **generadas por reglas** son recuperables bajo leave-one-triad-out a partir de fase y posición.

| Variante | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 |
|---|---:|---:|---:|---:|
| **PI-HGAT-T (fase + posición)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| Ablación sin fase | 0.6000 | 0.6056 | 0.7500 | 0.6667 |
| Ablación sin posición | 0.6359 | 0.5771 | 0.3871 | 0.4870 |
| Oracle de reglas | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 | 0.0000 | 0.0000 |

El 100 % demuestra recuperabilidad estructural del gold sintético, no validez semántica en el mundo real ([`docs/AUDITORIA_METRICAS.md`](docs/AUDITORIA_METRICAS.md)).

## Reproducción

```bash
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
python experiments/pi_hgat_t.py   # diagnóstico sintético
```

Véase [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) y [`REPRODUCCION.md`](REPRODUCCION.md).
