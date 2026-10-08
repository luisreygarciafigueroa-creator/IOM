# Experimentos computacionales PI-HGAT-T

## Definición operacional

En este repositorio, **PI-HGAT-T** significa *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Es la implementación de referencia del clasificador estructural de relaciones entre nodos de tríada del marco I.O.

El modelo codifica cada nodo con vectores one-hot de fase (`adv`/`ret`) y posición (`left`/`center`/`right`); aplica dos capas de atención multi-cabeza sobre los seis nodos de cada pareja de tríadas; y clasifica cada par dirigido como `none`, `mirrorOf` o `creates`. Se implementa en PyTorch puro, sin PyTorch Geometric. Se excluyen etiquetas léxicas y el índice de tríada para forzar generalización estructural y permitir validación por tríada completa.

La suite compara tres variantes con la misma partición y semilla: modelo completo, ablación sin fase y ablación sin posición. Cada variante se entrena desde cero en cada fold.

## Datos y partición

- Fuente estructurada: [`data/iom_spec.json`](data/iom_spec.json), operacionalización canónica de las tríadas, fases, vectores y reglas de relación del marco.
- `datasets/triad_nodes.csv`: 78 nodos (13 tríadas × 2 fases × 3 posiciones).
- `datasets/relation_candidates.csv`: 390 pares dirigidos no reflexivos (13 × 6 × 5), etiquetados desde las reglas declaradas: 78 `mirrorOf`, 104 `creates`, 208 `none`.
- `datasets/vector_steps.csv`: 20 pasos, cuatro secuencias de cinco posiciones.
- Validación **leave-one-triad-out** en 13 pliegues: ninguna pareja de una tríada de prueba aparece en entrenamiento.

Los datos constituyen el corpus empírico de evaluación estructural del marco. Los experimentos miden, de forma reproducible, la capacidad del modelo y de los baselines para recuperar las relaciones predichas por la ontología bajo partición rigurosa.

## Correspondencia de métricas y propiedades

| Métrica | Propiedad formal evaluada | Referencia semántica |
|---|---|---|
| `mirrorOf` precision/recall/F1 | `io:mirrorOf` | SHACL: misma tríada, fase opuesta, enlace recíproco, `pos_ret = 2 - pos_adv` |
| `creates` precision/recall/F1 | `io:creates` y cuatro reglas `creation_rules` | SHACL: misma tríada, fase opuesta; lateral→centro o centro→lateral |
| Exactitud y macro-F1 de relación | Etiqueta triclase derivada de `io:mirrorOf`, `io:creates` y ausencia de enlace | Conteos y matriz de confusión, sin filtrado de casos |
| Conformidad de aristas predichas | Condiciones posicionales de `io:mirrorOf` / `io:creates` | Proporción observada de aristas no nulas que respetan las reglas SHACL codificadas |
| Comprobación estructural externa al modelo | `io:hasPhase`, `io:hasDirection`, posición, perspectiva y vectores | SHACL valida cada nodo/paso frente a sus reglas y secuencias literales |

El criterio de referencia es la reconstrucción exacta de las relaciones ontológicas (score 1.0). Las métricas se publican completas por fold, clase y ablación, con matrices de confusión e intervalos de variabilidad (media ± desviación estándar sobre los 13 folds). SHACL y Lean aportan verificación formal independiente del desempeño estadístico del modelo.

## Reproducción y artefactos

Desde la raíz, `python experiments/pi_hgat_t.py` lee los CSV y [`experiments/config.json`](experiments/config.json), fija semilla, ejecuta 39 entrenamientos deterministas en CPU (3 variantes × 13 pliegues) y escribe:

- `experiments/results/pi_hgat_t_metrics.json`: métricas, folds, matriz de confusión, configuración y versiones;
- `experiments/logs/pi_hgat_t.log`: resumen de ejecución.

El script de generación [`scripts/generate_ontology.py`](scripts/generate_ontology.py) recrea Turtle y CSV a partir del JSON canónico. La CI reproduce el experimento después de Lean, generación, pruebas y OWL RL/SHACL.

## Resultado registrado

El modelo completo obtuvo exactitud, macro-F1, F1 de `mirrorOf`, F1 de `creates` y conformidad de reglas de **1.0**. La ablación sin fase obtuvo exactitud **0.6000**; la ablación sin posición, **0.6359**. La puntuación perfecta del modelo completo confirma que las relaciones son recuperables de forma determinista a partir de fase y posición; las ablaciones cuantifican la contribución empírica de cada factor. Los valores completos por fold y matrices están en `experiments/results/pi_hgat_t_metrics.json`.

## Baselines y evaluación externa (v1.1)

Ejecutar:

```bash
python experiments/baselines.py
```

Produce `experiments/results/baselines_comparison.json` con:

- reglas deterministas (oracle SHACL);
- regresión logística sobre features fase+posición;
- MLP sin estructura de grafo.

El conjunto de evaluación externa está en `datasets/external_eval/` (60 pares + protocolo de anotación por evaluadores independientes). Ver `docs/RELACIONES_OPERATIVAS.md` para la semántica exacta de `mirrorOf` y `creates`.

## Resultados por partición y variabilidad

Las matrices de confusión y métricas por fold se publican en `experiments/results/pi_hgat_t_metrics.json`. Los intervalos de variabilidad (media ± std de los 13 folds) aparecen en los reportes de baselines y en la auditoría automática.
