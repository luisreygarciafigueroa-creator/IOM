# Auditoría IOM — prueba de validez semántica en el mundo real

**Carácter del repositorio:** [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md)

## 1. Validez semántica en el mundo real (capa primaria)

**Estado: demostración provisional completada** (panel de 14 pares; no generalización universal).

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

Alineación a dominios reales (demostración de mapeo, no validación de campo): [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md).

## 2. Consistencia formal (prerrequisito)

Lean 4.9.0: operadores, `isMirror` / `isCreates`, conteos; sin `sorry`.  
Premisas vs teoremas: [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md).

## 3. Conformidad estructural (prerrequisito)

SHACL, CSV canónicos, puentes `tests/test_formal_rules_bridge.py` y property links.

## 4. Diagnóstico sintético (no es validez semántica real)

Recuperación de relaciones **generadas por reglas** bajo leave-one-triad-out:

| Método | Accuracy | Macro-F1 |
|---|---:|---:|
| PI-HGAT-T (fase + posición) | 1.0000 | 1.0000 |
| Ablación sin fase | 0.6000 | 0.6056 |
| Ablación sin posición | 0.6359 | 0.5771 |
| Oracle de reglas | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 |

Estas cifras **no** se reportan como validez semántica en el mundo real. Véase [`docs/AUDITORIA_METRICAS.md`](docs/AUDITORIA_METRICAS.md).

## Documentos de evaluación técnica ampliados

- [`docs/AUDITORIA_TECNICA.md`](docs/AUDITORIA_TECNICA.md) — validez semántica, κ y dictamen
- [`docs/INTEGRACION_METODOLOGICA.md`](docs/INTEGRACION_METODOLOGICA.md) — mapeo de dominios empíricos
- [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) — protocolo de alineación y validación ciega
