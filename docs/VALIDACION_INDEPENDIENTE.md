# Enfoque del repositorio: validación independiente

Este documento define el **eje metodológico del repositorio IOM**. Toda afirmación empírica o interpretativa sobre el marco se justifica por **validación independiente**. Las capas formal y sintética son prerrequisitos de consistencia, no sustitutos de esa validación.

---

## Principio rector

> Una relación, etiqueta o métrica **solo** se presenta como evidencia sobre el marco cuando procede de datos o juicios **no generados por las reglas canónicas** del propio repositorio, bajo protocolo ciego y métricas de acuerdo publicadas.

| Fuente de datos | Rol en el repositorio |
|---|---|
| `data/iom_spec.json` + CSV regenerados | Especificación y gold **sintético** (no validación independiente) |
| Lean / SHACL | Consistencia formal y estructural |
| PI-HGAT-T / baselines | Recuperabilidad de reglas en corpus sintético (diagnóstico interno) |
| `datasets/independent_eval/` | **Validación independiente** (capa primaria de interpretación) |
| `datasets/external_eval/` | Conjunto retenido / protocolo externo de apoyo |
| CSV de dominio vía ingesta | Alineación estructural; validación independiente solo tras etiquetas ciegas propias |

---

## Qué cuenta como independiente

1. **Origen:** pares o conceptos **no** tomados del generador de 390 candidatos, o tomados como control explícito y declarado.
2. **Cegado:** el anotador no ve `rule_label`, gold de entrenamiento ni métricas de modelos.
3. **Protocolo publicado:** `datasets/independent_eval/PROTOCOL.json`.
4. **Métricas primarias:** Fleiss' κ, acuerdo unánime/mayoría, tasa de `unsure`, tabla de desacuerdos.
5. **Post-hoc:** coincidencia con `rule_reference` es informativa, **no** el objetivo de la validación.

---

## Jerarquía de afirmaciones (obligatoria en docs y paper)

| Prioridad | Afirmación legítima | Artefacto |
|---:|---|---|
| **1** | Acuerdo inter-anotador / interpretabilidad bajo protocolo ciego | `independent_eval`, `score_independent_eval.py` |
| **2** | Corrección formal de operadores y predicados | Lean (`IOM/*.lean`) |
| **3** | Conformidad estructural de la especificación | SHACL, puentes CSV↔predicado |
| **4** | Recuperabilidad de relaciones *generadas por reglas* | PI-HGAT-T, baselines (diagnóstico) |

Las métricas de prioridad 4 **no** se promocionan a «validación del marco».

---

## Pipeline recomendado

```bash
# 1) Consistencia formal y estructural (prerrequisito)
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py

# 2) Validación independiente (eje empírico/interpretativo)
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json

# 3) Diagnóstico sintético (opcional, no sustituye 2)
python experiments/pi_hgat_t.py
python experiments/baselines.py
python scripts/audit_perfect_metrics.py
```

---

## Estado actual

| Componente | Estado |
|---|---|
| Protocolo ciego | Publicado (`PROTOCOL.json`) |
| Pares independientes (14, NR01–AM03) | Publicados |
| Anotaciones A1–A3 | Completadas en `annotations.json` |
| Fleiss' κ | 0.6871 (controles unánimes; desacuerdos en NEW/ambiguos) |
| CSV de presentación al anotador | Ciego (`annotator_pairs.csv` sin pistas estructurales) |
| Análisis post-hoc | `annotator_pairs_rule_application.csv`, `rule_reference.json` |

---

## Referencias

- Protocolo y datos: [`datasets/independent_eval/`](../datasets/independent_eval/)
- Delimitación de capas: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- Premisas vs teoremas: [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)
- Auditoría de métricas sintéticas 100 %: [`AUDITORIA_METRICAS.md`](AUDITORIA_METRICAS.md)
