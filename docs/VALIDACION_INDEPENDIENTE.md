# Prueba de validez semántica en el mundo real

Este documento define el **carácter del repositorio IOM**: una **prueba y demostración** de validez semántica del marco I.O. cuando se aplica a conceptos, pares y dominios **externos** a las reglas canónicas.

No es un motor de inferencia de producción ni una demostración de que el marco «describe la realidad». Es un aparato reproducible para **medir** si la semántica operativa (`mirrorOf`, `creates`, perspectivas, fases) es interpretable por anotadores independientes y alineable a fenómenos reales.

---

## Principio rector

> Una relación, etiqueta o métrica cuenta como evidencia de **validez semántica en el mundo real** solo cuando procede de datos o juicios **no generados por las reglas canónicas** del repositorio, bajo protocolo ciego y métricas de acuerdo publicadas.

| Fuente de datos | Rol |
|---|---|
| `data/iom_spec.json` + CSV regenerados | Estructura semántica **bajo prueba** (definición formal, no evidencia de mundo real) |
| Lean / SHACL | Consistencia de esa estructura |
| PI-HGAT-T / baselines | Recuperabilidad de reglas en corpus sintético (diagnóstico interno) |
| `datasets/independent_eval/` | **Prueba de validez semántica** (eje del repositorio) |
| `datasets/external_eval/` | Conjunto retenido / protocolo externo de apoyo |
| Catálogo de dominios + CSV de ingesta | **Demostración** de alineación a fenómenos reales; validez solo tras etiquetas ciegas propias |

---

## Qué se demuestra y qué no

| Se demuestra (con la evidencia actual) | No se demuestra |
|---|---|
| Acuerdo inter-anotador medible (κ ≈ 0.69) sobre un panel de 14 pares independientes | Verdad ontológica universal del marco |
| Controles estructurales estables bajo cegado | Que PI-HGAT-T = 1.0 valide el marco en el mundo |
| Desacuerdos localizados en conceptos nuevos/ambiguos | Cobertura de todos los dominios empíricos |
| Posibilidad de mapear dominios (biología, economía, …) a las 13 tríadas | Que esos mapeos estén validados empíricamente en campo |

---

## Qué cuenta como evidencia de mundo real

1. **Origen externo:** pares o conceptos no tomados del generador de 390 candidatos, o tomados como control explícito.
2. **Cegado:** el anotador no ve `rule_label`, gold de entrenamiento ni métricas de modelos.
3. **Protocolo publicado:** `datasets/independent_eval/PROTOCOL.json`.
4. **Métricas primarias:** Fleiss' κ, acuerdo unánime/mayoría, tasa de `unsure`, tabla de desacuerdos.
5. **Post-hoc:** coincidencia con `rule_reference` es informativa, **no** el objetivo de la prueba semántica.

---

## Jerarquía de afirmaciones

| Prioridad | Afirmación legítima | Artefacto |
|---:|---|---|
| **1** | Validez semántica / interpretabilidad en el mundo real (acuerdo inter-anotador) | `independent_eval`, `score_independent_eval.py` |
| **2** | Demostración de alineación a dominios reales | `CATALOGO_DOMINIOS.md`, `datasets/ingestion/` |
| **3** | Corrección formal de operadores | Lean (`IOM/*.lean`) |
| **4** | Conformidad estructural de la especificación | SHACL, puentes CSV↔predicado |
| **5** | Recuperabilidad de relaciones *generadas por reglas* | PI-HGAT-T, baselines (diagnóstico) |

Las métricas de prioridad 5 **no** se promocionan a «validez semántica en el mundo real».

---

## Pipeline recomendado

```bash
# 1) Consistencia de la estructura bajo prueba
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py

# 2) Prueba de validez semántica (eje)
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json

# 3) Diagnóstico sintético (opcional)
python experiments/pi_hgat_t.py
python experiments/baselines.py
python scripts/audit_perfect_metrics.py
```

---

## Estado actual de la demostración

| Componente | Estado |
|---|---|
| Protocolo ciego | Publicado (`PROTOCOL.json`) |
| Pares independientes (14, NR01–AM03) | Publicados |
| Anotaciones A1–A3 | Completadas en `annotations.json` |
| Fleiss' κ | 0.6871 (controles unánimes; desacuerdos en NEW/ambiguos) |
| CSV ciego al anotador | `annotator_pairs.csv` sin pistas estructurales |
| Catálogo de dominios | Biología, economía y plantilla genérica |

---

## Referencias

- Protocolo y datos: [`datasets/independent_eval/`](../datasets/independent_eval/)
- Dominios reales: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md)
- Delimitación de capas: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- Premisas vs teoremas: [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)
- Auditoría de métricas sintéticas 100 %: [`AUDITORIA_METRICAS.md`](AUDITORIA_METRICAS.md)
