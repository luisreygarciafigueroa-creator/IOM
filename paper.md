# IOM — Resultados ejecutables y alcance de la comprobación

## Alcance

Este documento describe código y comprobaciones reproducibles. El MARCO I.O. original se conserva byte a byte en [docs/MARCOI.O.txt](docs/MARCOI.O.txt); las listas y secuencias añadidas posteriormente por el usuario están transcritas en [docs/TRIADAS_CATEGORIALES.md](docs/TRIADAS_CATEGORIALES.md) y [docs/VECTORES_4_5.md](docs/VECTORES_4_5.md). El contenido conceptual no se presenta como resultado experimental cuando no hay una prueba o conjunto de datos que lo respalde.

## Formalización Lean

`IOM/Core.lean` define un estado `State = (time : Int, payload : List String)`, el vacío `vacuum t`, la reducción `List.eraseDups` y la inversión `List.reverse`. `IOM/Operators.lean` implementa:

| Operador | Definición ejecutada |
|---|---|
| `E` | `(t, σ) ↦ (t + 1, σ)` |
| `S_fwd` | `(t, σ) ↦ (t, red σ)` |
| `Ivo` | `(t, σ) ↦ (t − 1, reverse σ)` |
| `S_rev` | Si `σ=[]`, `(t,[])`; en otro caso `(t−1, red (reverse σ))`. |

`lake build` compila 16 teoremas/lemas, sin `sorry` ni `admit`. Incluyen `strict_fixed_point` para todo entero `t`, no repetición del estado inicial para contenido no vacío, las ecuaciones de cada operador, la involutividad de la inversión y la cancelación de los operadores en la componente temporal.

Las pruebas se refieren exactamente a este tipo de datos y definiciones. No demuestran por sí solas la interpretación filosófica de “unidad informativa”.

## Las primeras tres perspectivas: tríadas estructurales

Las perspectivas se asocian a las columnas: **izquierda = Individualidad**, **centro = Dualidad**, **derecha = Totalidad**. En [docs/TRIADAS_CATEGORIALES.md](docs/TRIADAS_CATEGORIALES.md) se transcriben las 13 filas por fase y las cuatro reglas proporcionadas por el usuario:

- lateral izquierdo y derecho de avance crean el centro del retroceso;
- el centro del avance crea ambos laterales del retroceso;
- el centro del retroceso crea ambos laterales del avance;
- laterales del retroceso crean el centro del avance.

El generador las materializa en **78 nodos** (13 filas × 3 posiciones × 2 fases), **39 parejas espejo recíprocas** (izquierda y derecha intercambian; centro queda en centro) y **104 relaciones `io:creates`** (8 aristas por fila). Los rótulos conservan la ortografía recibida para cada fase, sin normalización silenciosa.

## Cuarta y quinta perspectivas: vectores

[docs/VECTORES_4_5.md](docs/VECTORES_4_5.md) contiene las tablas de las perspectivas vectoriales. Cada una tiene filas de avance y retroceso, cinco conceptos, posiciones de eje, índices visuales y dirección de flecha. RDF representa **20 pasos `io:VectorStep`** (4 filas × 5 posiciones). Las etiquetas de los diagramas se conservan literalmente, incluida `vacio` sin acento cuando así fue recibida.

La extensión de **21 categorías** se mantiene aparte como estructura pentádica adicional, con conteos por nivel `1, 4, 6, 6, 4`.

## RDF, SHACL y pruebas

`scripts/generate_ontology.py` genera `ontology/io_ontology.ttl`. `ontology/io_shapes.ttl` valida cardinalidad, rangos, direcciones, correspondencia posición-perspectiva, etiquetas, espejos, enlaces `creates`, pasos vectoriales y metadatos. La suite de `tests/test_ontology.py` compara los rótulos literales de las 26 filas, el conjunto exacto de 104 enlaces, las secuencias vectoriales, los conteos y mutaciones negativas. SHACL valida las restricciones codificadas, no la verdad científica de todas las afirmaciones del documento.

## Reproducción

Sigue [REPRODUCCION.md](REPRODUCCION.md). En resumen:

```bash
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

La CI de GitHub ejecuta los mismos pasos.

## Límites

1. Las tablas completas de tríadas y los detalles de las perspectivas 4–5 se aportaron después del archivo MARCOI.O.txt original. Se mantienen en anexos distintos para preservar el archivo original.
2. El grafo se valida como RDF/Turtle con SHACL; no ejecuta un razonador OWL.
3. La afirmación `restoresVacuum` se modela como propiedad del operador/composición, no como una propiedad verdadera de cada nodo categorial.
4. Las analogías neurocientíficas, termodinámicas y físicas del documento no se verifican empíricamente en este repositorio.
5. `payload : List String` es una representación computacional finita y no una teoría física de la información.

Véase [AUDITORIA.md](AUDITORIA.md) para el inventario de alcance y decisiones de transcripción.
