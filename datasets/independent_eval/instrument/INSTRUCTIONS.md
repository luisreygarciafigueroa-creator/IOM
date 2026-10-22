# Instrucciones de anotación (instrumento autocontenido)

Este paquete es **autosuficiente**. No necesita ni debe acompañarse del
repositorio del proyecto, del README, del manifiesto conceptual ni de
documentos de experimentos.

## Tarea

Para cada fila del archivo `pairs.csv`, elija **una** etiqueta que describa
la relación entre `source_label` y `target_label`, usando solo el contexto
de esa fila y las definiciones de abajo.

## Etiquetas admitidas

| Etiqueta | Definición operativa (neutra) |
|----------|------------------------------|
| `none` | No hay relación estructural clara entre los dos términos en el sentido de las otras dos etiquetas. |
| `mirrorOf` | Los términos se comportan como **polos complementarios** de una misma oposición (uno refleja al otro; si uno es «un lado», el otro es el lado opuesto o el centro simétrico). |
| `creates` | Un término **genera, produce o da lugar** al otro en una transición (origen → resultado), no solo como oposición estática. |
| `unsure` | No puede decidir con la información dada. |

No se le pide que conozca un marco teórico externo. Aplique solo estas definiciones.

## Reglas de procedimiento

1. Anote de forma **independiente** (sin consultar a otros anotadores).
2. **No** busque el repositorio del proyecto, manifiestos ni informes de métricas antes de terminar.
3. Si ya conoce el proyecto, declárelo en la hoja de acceso (`ACCESS_LOG` que le entregue el coordinador); sus juicios pueden excluirse del κ principal.
4. Devuelva un archivo `annotations_<su_id>.json` con la forma:

```json
{
  "annotator_id": "A?",
  "labels": {
    "NR01": "none",
    "NR02": "creates"
  }
}
```

(un valor por cada `id` de `pairs.csv`)

## Qué **no** forma parte de este instrumento

- Manifiestos filosóficos o cosmologías
- Código, ontologías, resultados de modelos
- Etiquetas «correctas» de referencia
