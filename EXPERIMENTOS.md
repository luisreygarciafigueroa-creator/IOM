# Experimentos computacionales PI-HGAT-T

## Definición operacional

En este repositorio, **PI-HGAT-T** significa *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Es una implementación operacional del nombre solicitado, definida aquí porque la petición no proporcionó una especificación de arquitectura externa. No se presenta como reproducción de un artículo o arquitectura canónica ajena.

El modelo codifica cada nodo con vectores one-hot de fase (`adv`/`ret`) y posición (`left`/`center`/`right`); aplica dos capas de atención multi-cabeza sobre los seis nodos de cada pareja de tríadas; y clasifica cada par dirigido como `none`, `mirrorOf` o `creates`. Se implementa en PyTorch puro, sin PyTorch Geometric. Se excluyen etiquetas léxicas y el índice de tríada para reducir memorización y permitir validación por tríada completa.

La suite compara tres variantes con la misma partición y semilla: modelo completo, ablación sin fase y ablación sin posición. Cada variante se entrena desde cero en cada fold.

## Datos y partición

- Fuente estructurada: [`data/iom_spec.json`](data/iom_spec.json), transcripción de las tablas proporcionadas por el usuario; no es un conjunto de mediciones empíricas.
- `datasets/triad_nodes.csv`: 78 nodos (13 tríadas × 2 fases × 3 posiciones).
- `datasets/relation_candidates.csv`: 390 pares dirigidos no reflexivos (13 × 6 × 5), etiquetados desde las reglas declaradas: 78 `mirrorOf`, 104 `creates`, 208 `none`.
- `datasets/vector_steps.csv`: 20 pasos, cuatro secuencias de cinco posiciones.
- Validación **leave-one-triad-out** en 13 pliegues: ninguna pareja de una tríada de prueba aparece en entrenamiento.

Son datos pequeños, construidos a partir de una especificación formal dada por el usuario. Los experimentos miden reconstrucción computacional de esa especificación; no prueban una teoría de conciencia, física o neurociencia.

## Correspondencia de métricas y propiedades

| Métrica | Propiedad formal evaluada | Referencia semántica |
|---|---|---|
| `mirrorOf` precision/recall/F1 | `io:mirrorOf` | SHACL: misma tríada, fase opuesta, enlace recíproco, `pos_ret = 2 - pos_adv` |
| `creates` precision/recall/F1 | `io:creates` y cuatro reglas `creation_rules` | SHACL: misma tríada, fase opuesta; lateral→centro o centro→lateral |
| Exactitud y macro-F1 de relación | Etiqueta triclase derivada de `io:mirrorOf`, `io:creates` y ausencia de enlace | Conteos y matriz de confusión, sin filtrado de casos |
| Conformidad de aristas predichas | Condiciones posicionales de `io:mirrorOf` / `io:creates` | Proporción observada de aristas no nulas que respetan las reglas SHACL codificadas |
| Comprobación estructural externa al modelo | `io:hasPhase`, `io:hasDirection`, posición, perspectiva y vectores | SHACL valida cada nodo/paso frente a sus reglas y secuencias literales |

**No se inventa un umbral estadístico de éxito.** La referencia formal de comparación es 1.0 porque la ontología define reglas deterministas y una lista extensional cerrada. Ese 1.0 describe la especificación de referencia, no un resultado prometido al modelo. Las métricas se publican como observaciones; SHACL decide la validez lógica de los datos, no el desempeño estadístico.

## Reproducción y artefactos

Desde la raíz, `python experiments/pi_hgat_t.py` lee los CSV y [`experiments/config.json`](experiments/config.json), fija semilla, ejecuta 39 entrenamientos deterministas en CPU (3 variantes × 13 pliegues) y escribe:

- `experiments/results/pi_hgat_t_metrics.json`: métricas, folds, matriz de confusión, configuración y versiones;
- `experiments/logs/pi_hgat_t.log`: resumen de ejecución.

El script de generación [`scripts/generate_ontology.py`](scripts/generate_ontology.py) recrea Turtle y CSV a partir del JSON canónico. La CI reproduce el experimento después de Lean, generación, pruebas y OWL RL/SHACL.

## Resultado registrado

El modelo completo obtuvo exactitud, macro-F1, F1 de `mirrorOf`, F1 de `creates` y conformidad de reglas de **1.0**. La ablación sin fase obtuvo exactitud **0.6000**; la ablación sin posición, **0.6359**. La puntuación perfecta es coherente con etiquetas definidas determinísticamente por fase/posición y reglas: demuestra reconstrucción del conjunto de especificación, no evidencia independiente ni validación empírica. Los valores completos por fold y matrices están en `experiments/results/pi_hgat_t_metrics.json`.
