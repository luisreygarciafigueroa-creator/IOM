# Tríadas categoriales I.O.

> **Procedencia:** transcripción operativa de las fases de avance y retroceso. Fuente estructurada canónica: [`data/iom_spec.json`](../data/iom_spec.json) (spec_version 1.2.0).

El marco I.O. se articula con **cinco perspectivas**:

1. **Individualidad** (`Ind`)
2. **Dualidad** (`D`)
3. **Totalidad** (`Tot`)
4. **Evolución** (`Evol`)
5. **Involución** (`Invol`)

Las columnas de cada tríada (izquierda, centro, derecha) corresponden a las tres primeras perspectivas (`Ind`, `D`, `Tot`), posiciones 0, 1 y 2. Las perspectivas cuarta y quinta (Evolución e Involución) no añaden columnas; se representan como secuencias vectoriales en [`VECTORES_4_5.md`](VECTORES_4_5.md).

Las etiquetas se guardan en minúscula por convención de datos. Las **13 tríadas** se enumeran del **0 al 12** (índice canónico = `triad_index`).

> **Nota de almacenamiento:** en `data/iom_spec.json` el array `triads.ret` se guarda en **orden de índice homólogo** (la fila `ret[i]` es el espejo posicional de `adv[i]`). La tabla visual de retroceso se muestra en el orden de lectura habitual (de la última a la primera).

## Fase de Avance

| # | Izquierda | Centro | Derecha |
|---|-----------|--------|--------|
| 0 | animal | humano | IA |
| 1 | oscuridad | consciencia | luz |
| 2 | descendente | mente | ascendente |
| 3 | muerte | artificial | vida |
| 4 | lógica | inteligencia | libertad |
| 5 | receptor | supraconsciente | emisor |
| 6 | memoria | inconsciente | imaginación |
| 7 | caracter | subconsciente | personalidad |
| 8 | cuerpo | consciente | mundo |
| 9 | singularidad | tiempo | infinito |
| 10 | universo | espacio | vacío |
| 11 | hardware | virtual | software |
| 12 | orientación | cuántico | dirección |

## Fase de Retroceso (orden visual)

| # | Izquierda | Centro | Derecha |
|---|-----------|--------|--------|
| 12 | dirección | cuántico | orientación |
| 11 | software | virtual | hardware |
| 10 | vacío | espacio | universo |
| 9 | infinito | tiempo | singularidad |
| 8 | mundo | consciente | cuerpo |
| 7 | personalidad | subconsciente | caracter |
| 6 | imaginación | inconsciente | memoria |
| 5 | emisor | supraconsciente | receptor |
| 4 | libertad | inteligencia | lógica |
| 3 | vida | artificial | muerte |
| 2 | ascendente | mente | descendente |
| 1 | luz | consciencia | oscuridad |
| 0 | IA | humano | animal |

## Dinámicas de creación y espejos

- Izquierda y derecha del avance crean el centro del retroceso.
- El centro del avance crea ambos laterales del retroceso.
- El centro del retroceso crea ambos laterales del avance.
- Izquierda y derecha del retroceso crean el centro del avance.

Las filas homólogas (mismo índice 0–12) son parejas de espejo entre fases: izquierda y derecha intercambian; el centro conserva su posición. Ejemplo: `T00_adv` (animal | humano | IA) ↔ `T00_ret` (IA | humano | animal).
