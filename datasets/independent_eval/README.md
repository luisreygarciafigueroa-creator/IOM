# Evaluación independiente (interpretación de relaciones)

Este conjunto **no** es una partición del generador de 390 candidatos. Incluye controles, casos fuera de reglas, cross-tríada, conceptos nuevos y casos ambiguos.

**Estado actual:** protocolo v1.2.0 listo; anotaciones humanas **pendientes** (`status: pending_human_collection`). No hay resultados de acuerdo inter-anotador todavía.

## Materiales (separación ciega)

| Archivo | Audiencia | Contenido |
|---|---|---|
| **`annotator_pairs.csv`** | Anotadores | id, etiquetas de conceptos, contexto **neutral** (sin pistas de clasificación) |
| **`annotations_template.json`** | Anotadores / recolector | Hoja de respuestas (`null` = no respondido) |
| **`PROTOCOL.json`** | Anotadores / recolector | Instrucciones, cegamiento, outcomes |
| `independent_pairs.csv` | **Solo análisis** | kind, node_ids, contexto técnico |
| `rule_reference.json` | **Solo análisis** | Etiquetas de regla (ocultas a anotadores) |

## Formato de respuestas (oficial)

```json
{
  "annotators": ["A1", "A2", "A3"],
  "status": "pending_human_collection",
  "items": [
    {
      "id": "NR01",
      "annotations": {"A1": null, "A2": null, "A3": null},
      "free_text": {"A1": "", "A2": "", "A3": ""}
    }
  ]
}
```

- `null` → el anotador **aún no** evaluó el caso (dato ausente).
- `"unsure"` → el anotador evaluó y **no puede decidir** con la definición.
- Etiquetas válidas: `none` | `mirrorOf` | `creates` | `unsure`.

## Scoring

```bash
python scripts/score_independent_eval.py
python scripts/score_independent_eval.py --min-annotators 3
```

El script:
1. Lee el formato de la plantilla (y formatos legacy).
2. **No** sustituye `null` por `unsure`.
3. Solo calcula Fleiss' kappa sobre ítems con ≥3 respuestas no nulas.
4. Reporta ítems incompletos por separado.
5. La coincidencia con `rule_reference` es **post-hoc** y excluye `unspecified`.

## Uso legítimo del lenguaje

| Legítimo | No legítimo |
|---|---|
| «Protocolo de anotación ciega preparado; recolección pendiente» | «El marco está validado por anotadores humanos» |
| «Acuerdo inter-anotador (kappa) sobre definiciones» | «Accuracy del modelo sobre independent_eval» |
| «Mapa de desacuerdos y tasa de unsure» | «Los anotadores confirman las reglas SHACL» |

Las cifras de accuracy de PI-HGAT-T en `experiments/results/` son **recuperación de relaciones generadas por reglas** (capa B), no evaluación de este protocolo (capa C).
