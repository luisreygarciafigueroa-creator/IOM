# Evaluación independiente (interpretación de relaciones)

**Estado: Completado**

Este conjunto **no** es una partición del generador de 390 candidatos. Incluye controles canónicos, pares fuera de las cuatro reglas, pares entre tríadas, conceptos nuevos y casos ambiguos.

## Integridad de datos

| Archivo | Filas | Notas |
|---|---:|---|
| `independent_pairs.csv` | 14 (+ cabecera) | NR01–AM03, metadatos alineados |
| `annotator_pairs.csv` | 42 | 14 ítems × 3 anotadores |
| `annotator_pairs_rule_application.csv` | 42 | + `rule_label` y `matches_rule` |
| `rule_reference.json` | 14 claves | Oculto a anotadores durante el juicio |
| `annotations.json` | 14 ítems | Anotaciones cerradas + métricas |

Correspondencia verificada por `scripts/score_independent_eval.py`.

## Resultados (resumen)

| Métrica | Valor |
|---|---:|
| Fleiss' κ | 0.6871 |
| Unánime | 10/14 |
| Mayoría (≥2) | 13/14 |
| Acuerdo post-hoc con reglas | 0.9394 |
| Controles unánimes | sí |
| Fuera-de-reglas unánimes | sí |

Desacuerdos: NC01, NC02, AM01, AM03. Informe: `SCORE_REPORT.md`.

```bash
python scripts/score_independent_eval.py
```
