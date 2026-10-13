# Mapa verificable del pipeline

```mermaid
flowchart LR
  S[Especificación<br/>../data/iom_spec.json] --> L[Lean<br/>../IOM/FormalRules.lean]
  S --> G[Generador<br/>../scripts/generate_ontology.py]
  G --> R[RDF/SHACL<br/>../ontology/io_ontology.ttl<br/>../ontology/io_shapes.ttl]
  G --> C[CSV canónicos<br/>../datasets/*.csv]
  R --> V[Validación RDF↔CSV<br/>../scripts/verify_bridge.py]
  C --> V
  C --> M[Modelos y baselines<br/>../experiments/]
  V --> O[Resultados y hashes<br/>../experiments/results/]
  M --> O
```

Rutas fuente: [especificación](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/data/iom_spec.json), [reglas Lean](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/IOM/FormalRules.lean), [generador](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/scripts/generate_ontology.py), [ontología](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/ontology/io_ontology.ttl), [candidatos](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/datasets/relation_candidates.csv), [PI-HGAT-T](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/experiments/pi_hgat_t.py), [baselines](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/experiments/baselines.py).

Orden de ejecución: generar artefactos → validar contratos CSV → cotejar RDF y etiquetas → ejecutar pruebas/SHACL → modelos → publicar resultados.
