# Informe de puntuación — evaluación independiente IOM

**Estado:** `completed`  
**Integridad de datos:** `ok`  
**Ítems:** 14 (NR01–AM03)  
**Anotadores:** 3 (A1, A2, A3)  
**Juicios totales:** 42

## Métricas de concordancia

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Fracción unánime | 0.7143 (10/14) |
| Fracción mayoría (≥2) | 0.9286 (13/14) |
| Acuerdo post-hoc con reglas | 0.9394 (31/33) |
| Controles unánimes | True |
| Fuera-de-reglas unánimes | True |

## Tasa de `unsure` por kind

| kind | tasa media |
|---|---:|
| `ambiguous` | 0.2222 |
| `control_creates` | 0.0000 |
| `control_mirror` | 0.0000 |
| `cross_triad` | 0.0000 |
| `new_concept` | 0.3333 |
| `out_of_rules` | 0.0000 |

## Desacuerdos ítem a ítem

| id | kind | A1 | A2 | A3 | mayoría | rule_label |
|---|---|---|---|---|---|---|
| NC01 | new_concept | mirrorOf | unsure | unsure | unsure | unspecified |
| NC02 | new_concept | creates | unsure | none | tie | unspecified |
| AM01 | ambiguous | mirrorOf | mirrorOf | unsure | mirrorOf | mirrorOf |
| AM03 | ambiguous | mirrorOf | mirrorOf | unsure | mirrorOf | mirrorOf |

## Interpretación

- Los **controles** y los casos **fuera de reglas / cross-tríada** son unánimes: el protocolo operativo es estable sobre el dominio formal.
- Los desacuerdos se concentran en **conceptos nuevos** y **ambiguos**, donde el protocolo permite `unsure` y la analogía estructural no es obligatoria.
- El acuerdo post-hoc con `rule_reference` (~94 %) confirma alineación en ítems con etiqueta de regla definida; no mide validación empírica del marco en el mundo real.
- Las cifras de PI-HGAT-T siguen siendo **recuperación de relaciones generadas por reglas**; este experimento mide **interpretabilidad / acuerdo inter-anotador** bajo el protocolo publicado.

## Artefactos

- `datasets/independent_eval/independent_pairs.csv`
- `datasets/independent_eval/annotator_pairs.csv`
- `datasets/independent_eval/annotator_pairs_rule_application.csv`
- `datasets/independent_eval/annotations.json`
- `datasets/independent_eval/rule_reference.json`
- `datasets/independent_eval/PROTOCOL.json`
- `experiments/results/independent_eval_metrics.json`
- `datasets/independent_eval/SCORE_REPORT.md`
