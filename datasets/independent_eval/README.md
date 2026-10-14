# Evaluación independiente (eje de validación del repositorio)

**Estado: Completado** · Este directorio es el **centro de la validación independiente** del marco IOM. No es un anexo del generador de 390 candidatos.

## Principio

Los juicios se obtienen bajo protocolo **ciego**: sin `rule_label`, sin gold de entrenamiento y sin pistas estructurales en el material presentado al anotador (`annotator_pairs.csv`).

## Integridad

| Archivo | Rol |
|---|---|
| `annotator_pairs.csv` | Material **ciego** (id, etiquetas léxicas, contexto genérico) |
| `independent_pairs.csv` | Metadatos de análisis (kind, source/target estructurales) |
| `annotations.json` | Juicios A1–A3 + métricas |
| `rule_reference.json` | Solo post-hoc |
| `annotator_pairs_rule_application.csv` | Análisis post-hoc label vs regla |
| `PROTOCOL.json` | Protocolo publicado |
| `SCORE_REPORT.md` | Informe de puntuación |

## Resultados

| Métrica | Valor |
|---|---:|
| Fleiss' κ | 0.6871 |
| Unánime | 10/14 |
| Mayoría (≥2) | 13/14 |
| Controles unánimes | sí |
| Fuera-de-reglas unánimes | sí |

Desacuerdos: NC01, NC02, AM01, AM03.

```bash
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

## Lenguaje

Este conjunto autoriza afirmaciones de **validación independiente / interpretabilidad**.  
Las métricas de PI-HGAT-T **no** se interpretan como validación independiente del marco.
