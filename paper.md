# IOM — formalización, ontología y experimento computacional reproducible

## Alcance y procedencia

Este informe describe código verificable. El documento original se conserva en [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt); la versión más reciente de las tablas recibidas del usuario se registra en [`data/iom_spec.json`](data/iom_spec.json). Las afirmaciones filosóficas, neurocientíficas y físicas no se presentan como hechos empíricos demostrados.

## Especificación categorial actualizada

La fuente canónica define trece tríadas por fase. Avance comienza con `involución | vacio | evolución`; retroceso termina con `evolución | vacio | involución`. Las otras doce filas de cada fase conservan el orden y las etiquetas de la tabla del usuario. Cada concepto se representa como `io:OntoNode` con índices de fila, fase, posición, perspectiva posicional, dirección y etiqueta.

Las columnas corresponden a izquierda/centro/derecha y a metadatos `Ind`/`D`/`Tot`. Esos nombres de perspectiva no sustituyen las etiquetas de las filas categoriales.

Las cuatro reglas de creación generan 104 aristas `io:creates`; los espejos entre fases son recíprocos y cambian izquierda/derecha, preservando centro. Hay 78 nodos de tríada.

## Perspectivas vectoriales cuarta y quinta

Las secuencias vigentes son:

| Vector | Fase | Etiquetas (izquierda a derecha) | Eje | Flecha |
|---|---|---|---|---|
| Evolutivo | Avance | vacio · ind · dua · tot · evol | 0 · 1 · 2 · 3 · 4 | → |
| Evolutivo | Retroceso | evol · tot · dua · ind · vacio | 4 · 3 · 2 · 1 · 0 | ← |
| Involutivo | Avance | invol · tot · dua · ind · vacio | 4 · 3 · 2 · 1 · 0 | → |
| Involutivo | Retroceso | vacio · ind · dua · tot · invol | 0 · 1 · 2 · 3 · 4 | ← |

RDF conserva por separado el índice visual, el eje, la etiqueta y la flecha. Son 20 pasos en total.

## Formalización Lean

`IOM/Core.lean` define el estado `State(time : Int, payload : List String)`, el vacío, deduplicación e inversión. `IOM/Operators.lean` define `E`, `S_fwd`, `Ivo` y `S_rev`, junto con teoremas de composición y del punto fijo estricto del vacío. `IOM/Specification.lean` formaliza posiciones, espejo involutivo, inversión de índice y cotas 0–4. La construcción se compila con Lean 4.9.0 sin `sorry` ni `admit`.

Las pruebas prueban los tipos y propiedades expresamente modelados, no el significado filosófico de los conceptos.

## Ontología y restricciones

`scripts/generate_ontology.py` consume la especificación JSON y genera `ontology/io_ontology.ttl` más tres CSV. El grafo declara vocabulario OWL: clases, propiedades de objeto y de datos, dominios, rangos, propiedades funcionales y simetría de `io:mirrorOf`. `scripts/validate_shacl.py` verifica axiomas esperados, ejecuta expansión OWL RL y evalúa `ontology/io_shapes.ttl`.

SHACL restringe cardinalidad, valores permitidos, fase-dirección, posición-perspectiva, espejo recíproco, `creates` y las cuatro secuencias vectoriales. Las pruebas negativas alteran enlaces/datos para verificar que las formas detectan incompatibilidades.

## Experimento PI-HGAT-T

Se implementa una definición operacional propia del repositorio: *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Un codificador con atención multi-cabeza consume atributos de fase y posición de los seis nodos de cada par de filas; un decodificador predice relaciones dirigidas `none`, `mirrorOf` o `creates`. No usa el rótulo textual ni el índice de tríada.

Los 390 candidatos derivados de las 13 filas se evalúan con 13 particiones leave-one-triad-out. Se ejecutan tres variantes: atributos completos, ablación sin fase y ablación sin posición. Los datasets tienen 78 nodos, 78 aristas dirigidas de espejo, 104 aristas dirigidas `creates` y 208 pares sin relación.

Las métricas se atan explícitamente a las propiedades ontológicas: F1 de `mirrorOf` evalúa inversión lateral y reciprocidad; F1 de `creates` evalúa las cuatro reglas; la conformidad semántica de aristas predichas mide su admisibilidad bajo las reglas que SHACL define. En la ejecución registrada, el modelo completo obtiene 1.0 en exactitud y macro-F1; la ablación sin fase obtiene 0.6000 de exactitud y la ablación sin posición 0.6359. Como la clase objetivo se deriva precisamente de fase/posición y reglas fijas, esos scores miden reconstrucción de la especificación pequeña, no una prueba independiente del marco. La referencia formal es igualdad exacta (score 1.0) con la especificación determinista; **no** se eligen umbrales estadísticos discrecionales. Resultados por pliegue, configuración y versiones se archivan en `experiments/results/` y `experiments/logs/`.

## Reproducción y límites

Sigue [`REPRODUCCION.md`](REPRODUCCION.md). La CI compila Lean, regenera los artefactos, ejecuta pruebas, valida OWL RL/SHACL y corre PI-HGAT-T.

El dataset es una codificación pequeña de reglas suministradas, no observaciones independientes. Los resultados son una prueba de consistencia y reconstrucción computacional; no permiten inferir desempeño fuera de la especificación ni sostienen una conclusión empírica física o psicológica.
