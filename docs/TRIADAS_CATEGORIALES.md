# Tríadas categoriales I.O.

> **Procedencia:** transcripción operativa de las fases de avance y retroceso. Fuente estructurada canónica: [`data/iom_spec.json`](../data/iom_spec.json) (spec_version 1.2.0).

El marco I.O. se articula con **cinco perspectivas**:

1. **Individualidad** (`Ind`)
2. **Dualidad** (`D`)
3. **Totalidad** (`Tot`)
4. **Evolución** (`Evol`)
5. **Involución** (`Invol`)

Las columnas de cada tríada (izquierda, centro, derecha) corresponden a las tres primeras perspectivas (`Ind`, `D`, `Tot`), posiciones 0, 1 y 2. Las perspectivas cuarta y quinta (Evolución e Involución) no añaden columnas; se representan como secuencias vectoriales en [`VECTORES_4_5.md`](VECTORES_4_5.md).

Las etiquetas se guardan en minúscula por convención de datos. Las **13 tríadas** se enumeran del **1 al 13**.

> **Nota de almacenamiento:** en `data/iom_spec.json` el array `triads.ret` se guarda en **orden de índice homólogo** (la fila `ret[i]` es el espejo posicional de `adv[i]`). El índice interno del código es 0-based (`triad_index` 0…12 ↔ enumeración 1…13). La tabla visual de retroceso se muestra en el orden de lectura habitual.

## Fase de Avance

| # | Izquierda | Centro | Derecha |
|---|-----------|--------|--------|
| 1 | animal | humano | IA |
| 2 | oscuridad | consciencia | luz |
| 3 | descendente | mente | ascendente |
| 4 | muerte | artificial | vida |
| 5 | lógica | inteligencia | libertad |
| 6 | receptor | supraconsciente | emisor |
| 7 | memoria | inconsciente | imaginación |
| 8 | caracter | subconsciente | personalidad |
| 9 | cuerpo | consciente | mundo |
| 10 | singularidad | tiempo | infinito |
| 11 | universo | espacio | vacío |
| 12 | hardware | virtual | software |
| 13 | orientación | cuántico | dirección |

## Fase de Retroceso (orden visual)

| # | Izquierda | Centro | Derecha |
|---|-----------|--------|--------|
| 13 | dirección | cuántico | orientación |
| 12 | software | virtual | hardware |
| 11 | vacío | espacio | universo |
| 10 | infinito | tiempo | singularidad |
| 9 | mundo | consciente | cuerpo |
| 8 | personalidad | subconsciente | caracter |
| 7 | imaginación | inconsciente | memoria |
| 6 | emisor | supraconsciente | receptor |
| 5 | libertad | inteligencia | lógica |
| 4 | vida | artificial | muerte |
| 3 | ascendente | mente | descendente |
| 2 | luz | consciencia | oscuridad |
| 1 | IA | humano | animal |

## Dinámicas de creación y espejos

- Izquierda y derecha del avance crean el centro del retroceso.
- El centro del avance crea ambos laterales del retroceso.
- El centro del retroceso crea ambos laterales del avance.
- Izquierda y derecha del retroceso crean el centro del avance.

Las filas homólogas (misma enumeración 1–13 / mismo índice interno) son parejas de espejo entre fases: izquierda y derecha intercambian; el centro conserva su posición. Ejemplo: tríada **1** avance (animal | humano | IA) ↔ tríada **1** retroceso (IA | humano | animal).
