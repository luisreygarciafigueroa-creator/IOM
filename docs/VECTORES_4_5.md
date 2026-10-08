# Perspectivas cuarta y quinta: secuencias vectoriales I.O.

> **Procedencia:** transcripción estructurada de la aclaración del usuario del 8 de octubre de 2026. Se preserva la secuencia, los nombres abreviados y la flecha que aparece en cada fila.

Las tres primeras perspectivas son **Ind** (individualidad), **D** (dualidad) y **Tot** (totalidad). La cuarta y quinta son vectores que recorren esos estados; no son categorías adicionales de las tríadas.

## Cuarta perspectiva — Vector Evolutivo

La secuencia descrita como avance va de vacío a evolución plena. La fila de retroceso se representa con las posiciones, conceptos y flecha recibidos:

| Fila | Conceptos de izquierda a derecha | Posiciones | Flecha |
|---|---|---|---|
| Avance | vacio · ind · dua · tot · evol | 0 · 1 · 2 · 3 · 4 | → |
| Retroceso | evol · fut · pre · pas · vacio | 4 · 3 · 2 · 1 · 0 | ← |

El texto asociado describe la evolución como proyección desde pasado hacia presente y futuro, pasando por individualidad, dualidad y totalidad, orientada a la reconfiguración del vacío.

## Quinta perspectiva — Vector Involutivo

| Fila | Conceptos de izquierda a derecha | Posiciones | Flecha |
|---|---|---|---|
| Avance | invol · tot · dua · ind · vacio | 4 · 3 · 2 · 1 · 0 | → |
| Retroceso | vacio · pas · pre · fut · invol | 0 · 1 · 2 · 3 · 4 | ← |

El texto asociado describe supresión desde futuro a presente y pasado, pasando por totalidad, dualidad e individualidad, como proceso de reorganización que da origen al vacío.

## Filas formales del grafo

Cada fila se materializa en cinco instancias `io:VectorStep`, cada una con vector, fase (avance/retroceso), posición de eje, índice visual de izquierda a derecha, etiqueta y flecha. Por tanto hay **20 instancias**. Las etiquetas `ind`, `dua`, `tot`, `evol`, `invol`, `fut`, `pre`, `pas` y `vacío` se almacenan como literales, sin sustituirlas por otras acepciones.
