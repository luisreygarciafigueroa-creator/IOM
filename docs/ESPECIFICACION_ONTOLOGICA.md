# Especificación Ontológica: Guía Metodológica para el Mapeo e Integración de Dominios Empíricos en el Marco I.O.

## 1. Fundamentos Ontológicos y Estructura Semántica

El marco I.O. constituye un sistema de representación formal diseñado para resolver el mapeo e integración de entidades y fenómenos del mundo real dentro de una arquitectura semántica rigurosa, computable y cuantitativamente medible. La arquitectura se fundamenta en un sistema de clasificación epistémica cerrado compuesto por **cinco perspectivas**:

| Perspectiva | Función |
|---|---|
| **Individualidad** | Parametrización de la entidad en su condición singular, discreta y diferenciada |
| **Dualidad** | Modelado de parejas relacionales, polaridades, oposiciones y complementariedades |
| **Totalidad** | Integración sistémica y holística en una unidad ontológica de rango superior |
| **Evolución** | Transiciones de estado, trayectorias de desarrollo y transformación funcional |
| **Involución** | Repliegue, degradación estructural, simplificación o contracción de estados |

La operatividad se articula mediante el álgebra de relaciones `creates` (dependencias causales/generativas), `mirrorOf` (simetría estructural e isomorfismo) y la parametrización de **fases**. A diferencia de entornos sintéticos autorreferenciales, el marco I.O. se define como una **demostración provisional de validez semántica en el mundo real bajo protocolo ciego**.

---

## 2. Arquitectura de Validación: Experimentos EXP-A a EXP-E

| ID | Capa | Runner | Objetivo |
|---|---|---|---|
| **EXP-A** | Validez semántica (ciego) | `scripts/score_independent_eval.py` | Acuerdo inter-anotador (Fleiss' κ) sobre pares reales/nuevos/ambiguos |
| **EXP-B** | Formal | `lake build` | Coherencia lógica y teoremas en Lean 4 |
| **EXP-C** | Estructural | `scripts/validate_shacl.py` | Restricciones de forma RDF/SHACL |
| **EXP-D** | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperabilidad de reglas *generadas por el sistema* (no validez real) |
| **EXP-E** | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | Alineación de cosmología náhuatl a las 13 tríadas |

### Evidencia EXP-A (validez semántica empírica)

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** (moderado-sustancial, n = 14) |
| Acuerdo unánime | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 (conceptos nuevos y ambiguos) |

La concentración del desacuerdo en NC/AM demuestra que la incertidumbre proviene de fronteras semánticas extremas, no de fallas estructurales del núcleo.

---

## 3. Reglas de Modelado y Mapeo a las 13 Tríadas

Protocolo de proyección sistemática:

1. **Identificación** de la entidad o par del mundo real y sus límites contextuales.
2. **Asignación de perspectiva** (Individualidad / Dualidad / Totalidad / Evolución / Involución).
3. **Relaciones y fases**: `creates` o `mirrorOf` + indexación de fase operacional.
4. **Verificación** de alineación sobre una de las 13 tríadas sin violar axiomas.

Ejemplos EXP-E:

- **Cosmología náhuatl** — Cinco Soles y camino al Mictlán bajo Evolución/Involución con `mirrorOf` y `creates`.

Guía operativa: [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · Catálogo: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md).

---

## 4. Pipeline de Ejecución y Verificación

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build                                                                    # EXP-B
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py                                    # EXP-C
.venv/bin/python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json                    # EXP-A
.venv/bin/python experiments/pi_hgat_t.py                                     # EXP-D
.venv/bin/python experiments/baselines.py
.venv/bin/python experiments/domain_mapping/validate_examples.py              # EXP-E
.venv/bin/python scripts/generate_audit_report.py
```

---

## 5. Gobernanza Semántica y Criterios de Aceptación

| Capa | Qué mide | Qué **no** mide |
|---|---|---|
| EXP-D (PI-HGAT-T) | Recuperabilidad de reglas sintéticas | Validez semántica en el mundo real |
| EXP-A (protocolo ciego) | Interpretabilidad humana independiente | Recuperación algorítmica de reglas |

El único criterio válido de validez semántica empírica es el acuerdo inter-anotador bajo protocolo ciego (EXP-A). El marco se presenta como **demostración provisional**, no como verdad universal.

Documentos de soporte: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) · [`MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md) · [`DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](DICTAMEN_TECNICO_EPISTEMOLOGICO.md) · [`AUDITORIA_EPISTEMOLOGICA.md`](AUDITORIA_EPISTEMOLOGICA.md).
