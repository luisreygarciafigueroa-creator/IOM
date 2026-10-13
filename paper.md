# IOM — formalización, ontología y experimentos computacionales reproducibles

## Alcance y procedencia

Este informe describe un marco verificable de extremo a extremo. El documento de referencia se conserva en [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt); la especificación operativa canónica se registra en [`data/iom_spec.json`](data/iom_spec.json). Las afirmaciones del marco sobre **vacío**, **unidad informativa**, **infinito** y **transformación**, separadas en premisas asumidas y teoremas derivados, constan en [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md). La formalización Lean de espejos, creates y vectores está en `IOM/FormalRules.lean`.

Las hipótesis estructurales del marco se someten a pruebas formales (Lean, OWL/SHACL) y a evaluación de **recuperación de relaciones generadas por reglas** (validación cruzada, ablaciones, baselines). La interpretación humana independiente se estudia en `datasets/independent_eval/`.

## Ejemplo narrativo de anclaje: depredador–presa y mercado

Para aterrizar las cinco perspectivas antes de la formalización, consideremos dos escenarios:

**Ciclo ecológico.** Un lobo (Individualidad, fase de avance) depreda a un ciervo (Individualidad reflejada, fase de retroceso). La interacción depredación ocupa Dualidad (centro) y genera una arista `creates`. La red trófica o la población constituye Totalidad. Un colapso local se lee como Involución (disolución hacia vacío); la recolonización, como Evolución (proyección hacia estructura). La plantilla [`datasets/ingestion/templates/biologia_depredador_presa.csv`](datasets/ingestion/templates/biologia_depredador_presa.csv) materializa este mapeo.

**Ciclo de mercado.** Un trader (Individualidad) opera un activo (Individualidad reflejada); el riesgo o el contrato ocupa Dualidad; el mercado, Totalidad. Una burbuja se alinea a Evolución; un crash, a Involución. Véase [`datasets/ingestion/templates/economia_transaccion_riesgo.csv`](datasets/ingestion/templates/economia_transaccion_riesgo.csv).

Estos ejemplos muestran que las perspectivas no son etiquetas abstractas: son lecturas operativas de sistemas reales que el marco formaliza y que la herramienta de ingesta CSV permite alinear sin modificar la ontología core.

## Especificación categorial actualizada

La fuente canónica define trece tríadas por fase (spec_version 1.2.0). La fase de avance comienza con `animal | humano | IA`; la fase de retroceso (índice homólogo) termina el ciclo con `IA | humano | animal`. Cada concepto se representa como `io:OntoNode` con índices de fila, fase, posición, perspectiva posicional, dirección y etiqueta.

El marco comprende **cinco perspectivas**: Individualidad (`Ind`), Dualidad (`D`), Totalidad (`Tot`), Evolución (`Evol`) e Involución (`Invol`). Las tres primeras son posicionales (izquierda/centro/derecha en cada tríada) y no sustituyen las etiquetas categoriales de las filas. Las dos últimas son vectoriales y describen las direcciones de flujo informativo.

Las cuatro reglas de creación generan 104 aristas `io:creates`; los espejos entre fases son recíprocos y cambian izquierda/derecha, preservando centro. Hay 78 nodos de tríadas (13 × 2 fases × 3 posiciones).

## Perspectivas cuarta y quinta: Evolución e Involución

Las secuencias vigentes son:

| Vector | Fase | Etiquetas (izquierda a derecha) | Eje | Flecha |
|---|---|---|---|---|
| Evolución | Avance | vacío · ind · dua · tot · evol | 0 · 1 · 2 · 3 · 4 | → |
| Evolución | Retroceso | evol · tot · dua · ind · vacío | 4 · 3 · 2 · 1 · 0 | ← |
| Involución | Avance | invol · tot · dua · ind · vacío | 4 · 3 · 2 · 1 · 0 | → |
| Involución | Retroceso | vacío · ind · dua · tot · invol | 0 · 1 · 2 · 3 · 4 | ← |

RDF conserva por separado el índice visual, el eje, la etiqueta y la flecha. Son 20 pasos en total.

## Formalización Lean

`IOM/Core.lean` define el estado `State(time : Int, payload : List String)`, el vacío, deduplicación e inversión. `IOM/Operators.lean` define `E`, `S_fwd`, `Ivo` y `S_rev`, junto con teoremas de composición y del punto fijo estricto del vacío. `IOM/Specification.lean` formaliza posiciones, espejo involutivo, inversión de índice y cotas 0–4. `IOM/FormalRules.lean` codifica los predicados `isMirror` e `isCreates` y los conteos canónicos; las relaciones del CSV se comprueban contra esos predicados (`tests/test_formal_rules_bridge.py`). La construcción se compila con Lean 4.9.0 sin `sorry` ni `admit`.

## Ontología y restricciones

`scripts/generate_ontology.py` consume la especificación JSON y genera `ontology/io_ontology.ttl` más tres CSV. El grafo declara vocabulario OWL: clases, propiedades de objeto y de datos, dominios, rangos, propiedades funcionales y simetría de `io:mirrorOf`. `scripts/validate_shacl.py` verifica axiomas esperados, ejecuta expansión OWL RL y evalúa `ontology/io_shapes.ttl`.

## Ingesta de dominios personalizados (propuesta de valor central)

La ontología de 78 nodos es inmutable. La herramienta `scripts/importar_datos_personalizados.py` permite a investigadores interdisciplinarios alinear conceptos externos (biología, economía, sociología, software, etc.) mediante archivos CSV, validando que cada `mapped_node_id` exista en el core y generando un informe de alineación. Las plantillas y el catálogo de mapeos están en `datasets/ingestion/` y `docs/CATALOGO_DOMINIOS.md`. Esta funcionalidad conecta el marco formal con datos del mundo real **sin romper** las garantías Lean/SHACL.

## Justificación metodológica: por qué el aprendizaje automático

La Fase 1 (Lean + SHACL + datasets deterministas) demuestra *corrección estructural* en un universo sin ruido. La Fase 2 (PI-HGAT-T, ablaciones, baselines) responde a una pregunta complementaria: **¿las relaciones generadas por reglas siguen siendo recuperables cuando un modelo inductivo solo ve atributos parciales y particiones leave-one-triad-out?**

Esta validación empírica es útil porque:

1. **Demuestra aprendibilidad.** La recuperación perfecta (accuracy/F1 = 1.0) bajo leave-one-triad-out muestra que la ontología no es un artefacto ad hoc: un modelo puede reconstruir `mirrorOf` y `creates` a partir de fase y posición.
2. **Cuantifica robustez estructural.** Las ablaciones (sin fase → accuracy 0.60; sin posición → ~0.64) revelan la contribución de cada factor y los puntos de fragilidad ante información incompleta.
3. **Puentea lo determinista y lo probabilístico.** Fase 1 produce el gold determinista; Fase 2 mide si un learner generaliza ese gold. El mismo pipeline admite, en extensiones, CSV de dominios externos con su ruido inherente, permitiendo evaluar robustez frente a perturbaciones del mundo real sin alterar la bóveda formal.
4. **No sustituye la validación externa.** Las métricas miden recuperabilidad de relaciones *generadas por reglas*, no la verdad del marco sobre datos independientes. Para eso existen `datasets/independent_eval/` y `datasets/external_eval/`.

## Experimento PI-HGAT-T (recuperación de relaciones por reglas)

Se implementa *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Un codificador con atención multi-cabeza consume atributos de fase y posición; un decodificador predice `none`, `mirrorOf` o `creates`. No usa el rótulo textual ni el índice de tríada.

Los 390 candidatos derivados de las 13 filas se evalúan con 13 particiones leave-one-triad-out. Se ejecutan tres variantes: atributos completos, ablación sin fase y ablación sin posición.

Las métricas miden la **recuperación de relaciones estructurales generadas por reglas**: F1 de `mirrorOf` y `creates` respecto al gold determinista; no se interpretan como validación empírica del marco sobre datos independientes del generador.

### Resultados numéricos finales (leave-one-triad-out, semilla 20261008)

**Tabla A. PI-HGAT-T y ablaciones**

| Variante | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 | Conformidad reglas |
|---|---:|---:|---:|---:|---:|
| **PI-HGAT-T (fase + posición)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| Ablación sin fase | 0.6000 | 0.6056 | 0.7500 | 0.6667 | 0.5385 |
| Ablación sin posición | 0.6359 | 0.5771 | 0.3871 | 0.4870 | 0.3932 |

**Tabla B. Matriz de confusión del modelo completo** (filas = gold, columnas = predicted)

| | none | mirrorOf | creates |
|---|---:|---:|---:|
| none | 208 | 0 | 0 |
| mirrorOf | 0 | 78 | 0 |
| creates | 0 | 0 | 104 |

**Tabla C. Variabilidad por fold (accuracy)**

| Variante | Media ± std | Rango |
|---|---|---|
| PI-HGAT-T completo | 1.0000 ± 0.0000 | 1.00 – 1.00 |
| Sin fase | 0.6000 ± 0.0000 | 0.60 – 0.60 |
| Sin posición | 0.6359 ± 0.0253 | 0.60 – 0.67 |

**Tabla D. Baselines (misma partición)**

| Método | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 |
|---|---:|---:|---:|---:|
| Reglas deterministas (oracle SHACL) | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 | 0.0000 | 0.0000 |
| PI-HGAT-T (referencia) | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

La puntuación perfecta del modelo completo y del oracle SHACL confirma la **recuperación de relaciones estructurales generadas por reglas** (`io:mirrorOf` y `io:creates`) a partir de fase y posición bajo leave-one-triad-out. Estas cifras **no** constituyen por sí solas una validación empírica del marco sobre datos del mundo real; para interpretación humana independiente véase `datasets/independent_eval/`.

## Evaluación independiente

`datasets/independent_eval/` define pares fuera de las cuatro reglas, conceptos nuevos y casos ambiguos, con protocolo de anotación **ciega** por anotadores humanos independientes y publicación de desacuerdos y métricas de acuerdo.

## Reproducción y verificación

Sigue [`REPRODUCCION.md`](REPRODUCCION.md). La CI compila Lean, regenera los artefactos, ejecuta las pruebas (incluido el puente formal), valida OWL RL/SHACL, ejecuta PI-HGAT-T, compara baselines y genera la auditoría automática.
