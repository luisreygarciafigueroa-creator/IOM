# IOM — Resultados ejecutables y alcance de la comprobación

## Alcance

Este documento describe el código verificable del repositorio. El original completo, sin modificaciones, se conserva en [docs/MARCOI.O.txt](docs/MARCOI.O.txt). Las afirmaciones conceptuales del marco no se presentan como resultados experimentales ni como teoremas cuando no existe una prueba ejecutable correspondiente.

## Estado formal

`IOM/Core.lean` define un estado `State = (time : Int, payload : List String)`, el vacío `vacuum t`, una reducción estable de duplicados (`List.eraseDups`) y la inversión de una lista (`List.reverse`). `IOM/Operators.lean` define:

| Operador | Definición ejecutada |
|---|---|
| `E` | `(t, σ) ↦ (t + 1, σ)` |
| `S_fwd` | `(t, σ) ↦ (t, red σ)` |
| `Ivo` | `(t, σ) ↦ (t − 1, reverse σ)` |
| `S_rev` | Si `σ=[]`, `(t,[])`; en otro caso `(t−1, red (reverse σ))`. |

La supresión retroactiva conserva el vacío literalmente; para contenido no vacío aplica la definición general `red (invert σ)` del documento. Por eso la carga resultante puede no ser vacía.

## Resultados Lean

`lake build` compila los teoremas y lemas declarados en `IOM/Operators.lean`, sin `sorry` ni `admit`. Entre ellos:

- las ecuaciones de los cuatro operadores para el vacío;
- `strict_fixed_point`: para todo entero `t`, `S_rev (Ivo (E (vacuum t))) = vacuum t`;
- `no_repetition`: para una carga no vacía en el instante 0, el ciclo definido en Lean no devuelve el mismo estado;
- conservación o transformación del tiempo y la carga conforme a cada definición;
- involutividad de la inversión de lista;
- cancelación en la componente temporal de `E` e `Ivo`.

Estas pruebas comprueban las definiciones de este modelo Lean; no prueban por sí mismas las interpretaciones ontológicas, neurocientíficas o físicas del marco.

## Grafo y restricciones

`scripts/generate_ontology.py` produce un Turtle con:

- 78 nodos estructurales creados a partir de los contadores declarados: 13 índices técnicos × dos fases × tres posiciones locales;
- 39 vínculos espejo recíprocos, con mismo índice y posición y fase contraria;
- dirección `evol` en `adv`, e `invol` en `ret`;
- los dos nombres de tríadas que aparecen como ejemplos en el original, no asociados a índices;
- las 21 categorías enumeradas en la extensión (niveles `1, 4, 6, 6, 4`).

`ontology/io_shapes.ttl` valida rango y cardinalidad de índices, fase, posición y dirección, así como existencia, alineación y reciprocidad de espejos. No asigna nombres faltantes a las 13 tríadas ni calcula una perspectiva por nodo. SHACL verifica las restricciones codificadas, no toda la semántica del artículo.

## Ejecución

Sigue [REPRODUCCION.md](REPRODUCCION.md). La CI ejecuta `lake build`, genera el Turtle, corre los tests y valida SHACL. Los tests incluyen aserciones de cantidades y etiquetas, comprobaciones de espejos, conformidad y mutaciones negativas.

## Límites precisos

1. El MARCO I.O. declara 13 tríadas categoriales, pero no incluye una tabla completa con sus 13 nombres/elementos ni el orden. Solo da dos ejemplos.
2. El texto usa distintos esquemas de posición: eje `[0,4]` para perspectivas y posiciones de tríada descritas como izquierda/centro/derecha; el RDF existente usa tres posiciones locales. No se inventa una función de correspondencia entre esos ejes.
3. La extensión de 21 categorías está enumerada en el texto, pero se presenta como despliegue/extensión teórica; no se trata como sustitución probada de las 13 tríadas.
4. Las analogías con neurociencia, Landauer, teoría cuántica de campos y holografía permanecen como contenido del documento fuente; este repositorio no contiene experimentos ni un modelo físico que las verifique.
5. La identidad de datos usada por el programa es `List String`; la semántica de “unidad informativa” queda representada computacionalmente por esa estructura, no por una teoría física de información.

El registro íntegro de discrepancias está en [AUDITORIA.md](AUDITORIA.md).
