# Evaluación independiente (capa C)

**Estado:** protocolo v1.3.0 listo; anotaciones humanas **pendientes**. No hay resultados de acuerdo inter-anotador.

## Dos modos (no confundir)

| Modo | Archivo de pares | Qué se entrega al anotador | Pregunta |
|---|---|---|---|
| **interpretation_independent** (por defecto) | `annotator_pairs.csv` | Solo conceptos + contexto neutral; **sin** definiciones de reglas ni fase/posición | ¿Hay interpretación compartida *sin* enseñar IOM? |
| **rule_application** | `annotator_pairs_rule_application.csv` | Definiciones de `RELACIONES_OPERATIVAS.md` + contexto con fase/posición (sin etiqueta gold) | ¿Se aplican las reglas de forma consistente *una vez enseñadas*? |

Ambos modos usan la misma hoja de respuestas (`annotations_template.json`). Indica el modo en el campo opcional `evaluation_mode` del JSON rellenado.

## Materiales

| Archivo | Audiencia |
|---|---|
| `annotator_pairs.csv` | Anotadores (modo interpretación) |
| `annotator_pairs_rule_application.csv` | Anotadores (modo aplicación de reglas) |
| `annotations_template.json` | Respuestas |
| `PROTOCOL.json` | Instrucciones |
| `independent_pairs.csv` / `rule_reference.json` | **Solo análisis** |

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
