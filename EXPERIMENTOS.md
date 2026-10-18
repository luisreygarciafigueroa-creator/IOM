# Experimentos computacionales PI-HGAT-T

## Definición operativa

En este repositorio, **PI-HGAT-T** significa *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Es la implementación de referencia del clasificador estructural de relaciones entre nodos de tríada del marco I.O.

El modelo codifica cada nodo con vectores one-hot de fase (`adv`/`ret`) y posición (`left`/`center`/`right`); aplica dos capas de atención multi-cabeza sobre los seis nodos de cada pareja de tríadas; y clasifica cada par dirigido como `none`, `mirrorOf` o `creates`. Se implementa en PyTorch puro, sin PyTorch Geometric. Se excluyen etiquetas léxicas y el índice de tríada para forzar generalización estructural y permitir validación por tríada completa.

La suite compara tres variantes con la misma partición y semilla: modelo completo, ablación sin fase y ablación sin posición. Cada variante se entrena desde cero en cada fold.

## Justificación metodológica: por qué validar con aprendizaje automático

La Fase 1 del repositorio (Lean, RDF/OWL, SHACL, datasets regenerados de forma determinista) demuestra **corrección estructural** en un universo sin ruido: las relaciones `mirrorOf` y `creates` son deducibles de las reglas y verificables formalmente.

La Fase 2 responde a una pregunta distinta y complementaria:

> ¿Esas mismas relaciones siguen siendo **recuperables** cuando un modelo inductivo solo observa atributos parciales (fase, posición) bajo partición leave-one-triad-out?

Esta prueba de **recuperabilidad estructural** (no de validez semántica en el mundo real) es útil por cuatro razones. Las cifras siguientes **no** se interpretan como validación del marco sobre datos independientes:

1. **Aprendibilidad de la ontología.** La recuperación perfecta (accuracy = 1.0, F1 = 1.0) demuestra que la estructura no es un artefacto ad hoc: un modelo puede reconstruir las relaciones generadas por reglas a partir de rasgos mínimos.
2. **Robustez ante información incompleta.** Las ablaciones cuantifican la contribución de cada factor: sin fase la accuracy cae a 0.60; sin posición a ~0.64. Esto revela puntos de fragilidad estructural ante perturbaciones controladas.
3. **Puente explícito entre lo determinista y lo probabilístico.** Fase 1 produce el gold determinista; Fase 2 mide si un modelo generaliza ese gold. El mismo pipeline admite, en extensiones, CSV de dominios externos (biología, economía, etc.) alineados vía `scripts/importar_datos_personalizados.py`, permitiendo evaluar robustez frente al ruido del mundo real **sin modificar** la bóveda formal.
4. **Límite de interpretación.** Las métricas miden recuperabilidad de relaciones *generadas por reglas*, no la verdad del marco sobre datos independientes del generador. Para validación humana independiente véase `datasets/independent_eval/`; para evaluación externa de reglas, `datasets/external_eval/`.

En resumen: el ML no «prueba» la ontología; demuestra que es **aprendible y estructuralmente estable**, y prepara el terreno para evaluaciones empíricas con datos de dominios reales.

## Datos y partición

- Fuente estructurada: [`data/iom_spec.json`](data/iom_spec.json), operacionalización canónica de las tríadas, fases, vectores y reglas de relación del marco.
- `datasets/triad_nodes.csv`: 78 nodos (13 tríadas × 2 fases × 3 posiciones).
- `datasets/relation_candidates.csv`: 390 pares dirigidos no reflexivos (13 × 6 × 5), etiquetados desde las reglas declaradas: 78 `mirrorOf`, 104 `creates`, 208 `none`.
- `datasets/vector_steps.csv`: 20 pasos, cuatro secuencias de cinco posiciones.
- Validación **leave-one-triad-out** en 13 folds: ninguna pareja de una tríada de prueba aparece en entrenamiento.

## Resultados numéricos finales — PI-HGAT-T y ablaciones

Semilla fija `20261008`, 100 épocas, AdamW, leave-one-triad-out (13 folds), 390 candidatos por evaluación agregada.

### Tabla 1. Métricas agregadas por variante

| Variante | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 | Conformidad reglas | Aristas predichas |
|---|---:|---:|---:|---:|---:|---:|
| **PI-HGAT-T (fase + posición)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | 182 |
| Ablación sin fase | 0.6000 | 0.6056 | 0.7500 | 0.6667 | 0.5385 | 338 |
| Ablación sin posición | 0.6359 | 0.5771 | 0.3871 | 0.4870 | 0.3932 | 234 |

### Tabla 2. Precisión / recall / F1 por clase (modelo completo)

| Clase | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| none | 1.0000 | 1.0000 | 1.0000 | 208 |
| mirrorOf | 1.0000 | 1.0000 | 1.0000 | 78 |
| creates | 1.0000 | 1.0000 | 1.0000 | 104 |

Fuente: `experiments/results/pi_hgat_t_metrics.json`.

## Resultados numéricos finales — Baselines

| Método | Accuracy | Macro-F1 |
|---|---:|---:|
| **Reglas deterministas (oracle SHACL)** | **1.0000** | **1.0000** |
| **MLP sin grafo** | **1.0000** | **1.0000** |
| Regresión logística | 0.5333 | 0.2424 |
| PI-HGAT-T (referencia) | 1.0000 | 1.0000 |

## Suite experimental integrada (capas A–E)

Registro: [`experiments/domain_mapping/registry.json`](experiments/domain_mapping/registry.json).

| ID | Experimento | Capa | Runner | Afirmación legítima |
|---|---|---|---|---|
| **EXP-A** | Evaluación ciega inter-anotador | Validez semántica (mundo real) | `scripts/score_independent_eval.py` | κ = 0.6871 — interpretabilidad provisional (n=14) |
| EXP-B | Lean 4 | Formal | `lake build` | Solidez deductiva |
| EXP-C | SHACL / CSV | Estructural | `scripts/validate_shacl.py` | Conformidad de formas |
| EXP-D | PI-HGAT-T + baselines | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperación de relaciones *generadas por reglas* |
| **EXP-E** | Alineación de dominios (bio/econ) | Demostración de mapeo | `experiments/domain_mapping/validate_examples.py` | Cartografía a 13 tríadas sin romper reglas |

Protocolos metodológicos: [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) · [`docs/INTEGRACION_METODOLOGICA.md`](docs/INTEGRACION_METODOLOGICA.md) · [`docs/AUDITORIA_TECNICA.md`](docs/AUDITORIA_TECNICA.md).

```bash
python experiments/domain_mapping/validate_examples.py
# → experiments/results/domain_mapping_validation.json
```

Los resultados de EXP-E (4/4 OK) demuestran que los ejemplos de biología y economía del protocolo pueden anclarse a nodos canónicos con relaciones `mirrorOf`/`creates` admisibles. **No** constituyen κ de dominio ni validación de campo.
