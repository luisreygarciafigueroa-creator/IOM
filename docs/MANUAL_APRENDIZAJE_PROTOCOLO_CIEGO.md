# Manual de aprendizaje: evaluación de validación semántica y concordancia mediante pruebas a ciegas

> Guía pedagógica del protocolo ciego (EXP-A) y de la distinción entre capas experimentales A–E.  
> Método: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md) · Suite: [`../experiments/domain_mapping/registry.json`](../experiments/domain_mapping/registry.json)

---

## 1. Propósito del protocolo ciego

El marco I.O. (cinco perspectivas: Individualidad, Dualidad, Totalidad, Evolución e Involución; relaciones `mirrorOf` y `creates`) se evalúa como **prueba de interpretabilidad en el mundo real**, no como producto de software ni verificación circular de reglas sintéticas.

Objetivos del protocolo:

1. Evitar sesgo de confirmación (recuperar reglas internas ≠ validez empírica).
2. Garantizar interpretabilidad externa con anotadores ciegos a las reglas.
3. Medir robustez ante conceptos nuevos y casos ambiguos.

### Objetivos de aprendizaje

1. Explicar Fleiss' κ como medida de acuerdo inter-anotador corregida por azar.
2. Distinguir validez semántica real (EXP-A) de diagnóstico sintético (EXP-D).
3. Interpretar desacuerdos (NC/AM) como señal de prueba real, no como fallo trivial.

## 2. Fleiss' κ y evidencia actual (EXP-A)

| Métrica | Valor | Lectura |
|---|---:|---|
| Pares evaluados | 14 | `datasets/independent_eval/` |
| Fleiss' κ | **0.6871** | Acuerdo moderado-sustancial |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Conceptos nuevos y casos ambiguos |

κ = 0.6871 es **demostración provisional** bajo protocolo ciego; **no** prueba universal del marco.

```bash
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

## 3. Valor pedagógico del desacuerdo

| Código | Tipo | Lectura |
|---|---|---|
| NC01, NC02 | Conceptos nuevos | Falta de consolidación léxica |
| AM01, AM03 | Casos ambiguos | Solapamiento de fronteras |

## 4. Capas experimentales A–E

| ID | Capa | Runner | Afirmación legítima |
|---|---|---|---|
| **EXP-A** | Validez semántica (mundo real) | `scripts/score_independent_eval.py` | Interpretabilidad sobre conceptos externos |
| EXP-B | Formal | `lake build` | Teoremas en Lean 4 |
| EXP-C | Estructural | `scripts/validate_shacl.py` | Conformidad OWL/SHACL |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperación de relaciones *generadas por reglas* (**no** validez real) |
| EXP-E | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | Alineación de 8 pares bio/econ |

## 5. Autoevaluación

Véase [`../experiments/learning/quiz_blind_protocol.json`](../experiments/learning/quiz_blind_protocol.json).

1. ¿Qué distingue EXP-A de EXP-D? → **b)** interpretabilidad externa vs recuperación de reglas internas.
2. ¿Qué significa κ = 0.6871? → **b)** acuerdo moderado-sustancial sobre 14 pares.
3. ¿Cómo se clasifican NC/AM? → **c)** conceptos nuevos y casos ambiguos.
