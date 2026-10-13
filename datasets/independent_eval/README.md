# Evaluación independiente (capa C)

**Estado:** protocolo v1.3.0 listo; anotaciones humanas **pendientes**. No hay resultados de acuerdo inter-anotador.

## Dos modos (no confundir)

| Modo | Archivo de pares | Qué se entrega al anotador | Pregunta |
|---|---|---|---|
| **interpretation_independent** (por defecto) | `annotator_pairs.csv` | Solo conceptos + contexto neutral; **sin** definiciones de reglas ni fase/posición | ¿Hay interpretación compartida *sin* enseñar IOM? |
| **rule_application** | `annotator_pairs_rule_application.csv` | Definiciones de `RELACIONES_OPERATIVAS.md` + contexto con fase/posición (sin etiqueta gold) | ¿Se aplican las reglas de forma consistente *una vez enseñadas*? |

Ambos modos usan la misma hoja de respuestas (`annotations_template.json`). Indica el modo en el campo opcional `evaluation_mode` del JSON rellenado.

## Separación estricta de materiales

| Archivo | ¿Se distribuye a anotadores? |
|---|---|
| `annotator_pairs.csv` | **Sí** (modo interpretación) |
| `annotator_pairs_rule_application.csv` | **Sí** (modo aplicación de reglas) |
| `annotations_template.json` | **Sí** |
| `PROTOCOL.json` (instrucciones del modo) | **Sí** |
| `independent_pairs.csv` | **No** — solo análisis (kind, node_ids, contexto técnico) |
| `rule_reference.json` | **No** — solo análisis (etiquetas de regla) |

La categoría `new_concept` (y el resto de `kind`) existe **únicamente** en `independent_pairs.csv` / análisis. Los materiales para anotadores no indican que un concepto sea ajeno al vocabulario de las 13 filas.

## Scoring (sin truncar)

```bash
python scripts/score_independent_eval.py
python scripts/score_independent_eval.py --min-annotators 3
```

- `null` ≠ `unsure`.
- Fleiss' kappa **solo** sobre ítems con exactamente *k* respuestas no nulas del **mismo conjunto** de anotadores.
- Si un ítem tiene otro subconjunto de respondentes, se excluye del kappa (no se recortan las primeras respuestas).

## Dependencias de la suite completa

`tests/test_ontology.py` requiere `pyshacl` (y `rdflib`). Instalar con:

```bash
python -m pip install -r requirements-lock.txt
```

Sin esas dependencias, esas pruebas se omiten con mensaje claro; **no** implica fallo de la ontología. Lean se verifica con `lake build`.

## Lenguaje legítimo

| Legítimo | No legítimo |
|---|---|
| «Protocolo listo; recolección pendiente» | «IOM validado por humanos» |
| «Kappa de acuerdo en modo X» | «Accuracy del modelo sobre independent_eval» |
| «Consistencia al aplicar reglas enseñadas» | «Validez universal del marco» |
