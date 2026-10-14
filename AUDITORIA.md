# Auditoría IOM — enfoque de validación independiente

**Eje metodológico:** [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md)

## 1. Validación independiente (capa primaria)

**Estado: Completado.**

| Métrica | Valor |
|---|---:|
| Fleiss' κ | 0.6871 |
| Unánime | 10/14 |
| Mayoría (≥2) | 13/14 |
| Controles unánimes | sí |
| Fuera de reglas unánimes | sí |
| Acuerdo post-hoc con reglas (informativo) | 0.9394 |

Desacuerdos publicados: NC01, NC02, AM01, AM03.  
Artefactos: `datasets/independent_eval/`, `scripts/score_independent_eval.py`.

## 2. Consistencia formal (prerrequisito)

Lean 4.9.0: operadores, `isMirror` / `isCreates`, conteos; sin `sorry`.  
Premisas vs teoremas: [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md).

## 3. Conformidad estructural (prerrequisito)

SHACL, CSV canónicos, puentes `tests/test_formal_rules_bridge.py` y property links.

## 4. Diagnóstico sintético (no es validación independiente)

Recuperación de relaciones **generadas por reglas** bajo leave-one-triad-out:

| Método | Accuracy | Macro-F1 |
|---|---:|---:|
| PI-HGAT-T (fase + posición) | 1.0000 | 1.0000 |
| Ablación sin fase | 0.6000 | 0.6056 |
| Ablación sin posición | 0.6359 | 0.5771 |
| Oracle de reglas | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 |

Estas cifras **no** se reportan como validación independiente del marco. Véase [`docs/AUDITORIA_METRICAS.md`](docs/AUDITORIA_METRICAS.md).
