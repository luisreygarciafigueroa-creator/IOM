# Auditoría de correspondencia con la especificación IOM

**Fuentes:** [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt) y la especificación operativa normalizada en [`data/iom_spec.json`](data/iom_spec.json).

## Correspondencia y comprobación

| Especificación | Representación | Verificación |
|---|---|---|
| Estado temporal y vacío | `State(time, payload)`; `vacuum` | Lean 4.9.0 |
| Cuatro operadores temporales | `E`, `S_fwd`, `Ivo`, `S_rev` | Teoremas Lean compilados |
| Cinco perspectivas | Individualidad, Dualidad, Totalidad, Evolución, Involución | RDF `io:Perspective`, `five_perspectives` en JSON |
| Posiciones de tríada (persp. 1–3) | izquierda=0/`Ind`; centro=1/`D`; derecha=2/`Tot` | RDF/OWL, SHACL, pruebas y `TriadPosition` Lean |
| Espejos laterales | misma fila, fase opuesta, `pos_ret = 2 - pos_adv` | OWL `mirrorOf`, SHACL y Lean |
| Dinámicas `creates` | cuatro reglas, 104 aristas | Generador, SHACL y comparación exacta |
| Perspectivas 4–5 | cuatro secuencias de 5 pasos = 20 | RDF, SHACL y pruebas |
| PI-HGAT-T | recuperación de relaciones por reglas | JSON de métricas, CI |

## Premisas frente a teoremas

Véase [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md). Predicados `isMirror` / `isCreates` en `IOM/FormalRules.lean`; verificación CSV en `tests/test_formal_rules_bridge.py`.

## Métricas de recuperación estructural (reglas)

El criterio de referencia es la **recuperación exacta (1.0) de relaciones generadas por reglas**. No equivale a validación empírica del marco sobre datos independientes.

| Método | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 |
|---|---:|---:|---:|---:|
| PI-HGAT-T (fase + posición) | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Ablación sin fase | 0.6000 | 0.6056 | 0.7500 | 0.6667 |
| Ablación sin posición | 0.6359 | 0.5771 | 0.3871 | 0.4870 |
| Reglas deterministas (oracle) | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 | 0.0000 | 0.0000 |

## Evaluación independiente — cierre

**Estado: Completado.** Artefactos en `datasets/independent_eval/` y métricas en `experiments/results/independent_eval_metrics.json`.

| Métrica | Valor |
|---|---:|
| Fleiss' κ | 0.6871 |
| Unánime | 10/14 |
| Mayoría (≥2) | 13/14 |
| Acuerdo post-hoc con reglas | 0.9394 |
| Controles (CT01–CT03) unánimes | sí |
| Fuera de reglas (NR01–NR03) unánimes | sí |

Desacuerdos publicados (NC01, NC02, AM01, AM03). Puntuación: `python scripts/score_independent_eval.py`.

Este cierre valida la **interpretabilidad del protocolo de relaciones** bajo tres aplicaciones independientes del protocolo; no redefine las métricas de recuperación estructural de PI-HGAT-T.
