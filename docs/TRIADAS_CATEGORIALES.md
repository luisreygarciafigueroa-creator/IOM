# Tríadas categoriales del marco I.O.

Las **13 tríadas** × **2 fases** × **3 posiciones** = **78 nodos** canónicos
(`datasets/triad_nodes.csv`, `data/iom_spec.json`). Las etiquetas se
guardan en minúscula por convención de datos.

| Posición | Índice | Perspectiva |
|----------|--------|-------------|
| Izquierda (left) | 0 | Individualidad (Ind) |
| Centro (center) | 1 | Dualidad (D) |
| Derecha (right) | 2 | Totalidad (Tot) |

Las perspectivas vectoriales **Evolución** e **Involución** no añaden
columnas; se representan como secuencias en [`VECTORES_4_5.md`](VECTORES_4_5.md).

---

## Matriz canónica — Fase de Avance (evol / adv)

Dirección: proyección del vacío hacia la estructura.

```
      →       |       0       |       →
--------------|---------------|--------------
```

| Izquierda (Ind) | Centro (D) | Derecha (Tot) |
|-----------------|------------|---------------|
| oscuridad | consciencia | luz |
| descendente | mente | ascendente |
| muerte | artificial | vida |
| lógica | inteligencia | libertad |
| memoria | inconsciente | imaginación |
| receptor | supraconsciente | emisor |
| animal | humano | IA |
| carácter | subconsciente | personalidad |
| cuerpo | consciente | mundo |
| singularidad | tiempo | infinito |
| universo | espacio | vacío |
| hardware | virtual | software |
| orientación | cuántico | dirección |

```
--------------|---------------|--------------
      ←       |       0       |       ←
```

---

## Matriz canónica — Fase de Retroceso (invol / ret)

Dirección: disolución de la estructura hacia el vacío.
Inversión simétrica de cada fila de avance (`pos_tgt = 2 - pos_src`; el centro se refleja en sí mismo).

```
      →       |       0       |       →
--------------|---------------|--------------
```

| Izquierda (Ind) | Centro (D) | Derecha (Tot) |
|-----------------|------------|---------------|
| luz | consciencia | oscuridad |
| ascendente | mente | descendente |
| vida | artificial | muerte |
| libertad | inteligencia | lógica |
| imaginación | inconsciente | memoria |
| emisor | supraconsciente | receptor |
| IA | humano | animal |
| personalidad | subconsciente | carácter |
| mundo | consciente | cuerpo |
| infinito | tiempo | singularidad |
| vacío | espacio | universo |
| software | virtual | hardware |
| dirección | cuántico | orientación |

```
--------------|---------------|--------------
      ←       |       0       |       ←
```

---

## Índice canónico (triad_index 0–12)

Orden de almacenamiento en `data/iom_spec.json` y `datasets/triad_nodes.csv`.
La fila `ret[i]` es el espejo posicional de `adv[i]`.

### Avance (`T{i}_adv_P{0|1|2}`)

| # | Izquierda | Centro | Derecha | node_id (P0 / P1 / P2) |
|---|-----------|--------|---------|------------------------|
| 0 | animal | humano | IA | `T00_adv_P0` · `T00_adv_P1` · `T00_adv_P2` |
| 1 | oscuridad | consciencia | luz | `T01_adv_*` |
| 2 | descendente | mente | ascendente | `T02_adv_*` |
| 3 | muerte | artificial | vida | `T03_adv_*` |
| 4 | lógica | inteligencia | libertad | `T04_adv_*` |
| 5 | receptor | supraconsciente | emisor | `T05_adv_*` |
| 6 | memoria | inconsciente | imaginación | `T06_adv_*` |
| 7 | carácter | subconsciente | personalidad | `T07_adv_*` |
| 8 | cuerpo | consciente | mundo | `T08_adv_*` |
| 9 | singularidad | tiempo | infinito | `T09_adv_*` |
| 10 | universo | espacio | vacío | `T10_adv_*` |
| 11 | hardware | virtual | software | `T11_adv_*` |
| 12 | orientación | cuántico | dirección | `T12_adv_*` |

### Retroceso (`T{i}_ret_P{0|1|2}`)

| # | Izquierda | Centro | Derecha |
|---|-----------|--------|--------|
| 0 | IA | humano | animal |
| 1 | luz | consciencia | oscuridad |
| 2 | ascendente | mente | descendente |
| 3 | vida | artificial | muerte |
| 4 | libertad | inteligencia | lógica |
| 5 | emisor | supraconsciente | receptor |
| 6 | imaginación | inconsciente | memoria |
| 7 | personalidad | subconsciente | carácter |
| 8 | mundo | consciente | cuerpo |
| 9 | infinito | tiempo | singularidad |
| 10 | vacío | espacio | universo |
| 11 | software | virtual | hardware |
| 12 | dirección | cuántico | orientación |

---

## Dinámicas de creación y espejos

Relaciones admisibles (solo intra-tríada, fases opuestas):

| Relación | Condición |
|----------|-----------|
| `mirrorOf` | Fases opuestas + `pos_tgt = 2 - pos_src` |
| `creates` | Cuatro reglas posicionales (lateral↔centro entre fases) |
| `none` | Cualquier otro par (misma fase, cross-tríada, etc.) |

Reglas de creación:

1. Laterales del avance → centro del retroceso.
2. Centro del avance → laterales del retroceso.
3. Centro del retroceso → laterales del avance.
4. Laterales del retroceso → centro del avance.

Ejemplo de espejo: `T00_adv` (animal | humano | IA) ↔ `T00_ret` (IA | humano | animal).

Detalle formal: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · Lean 4 (`IOM/FormalRules.lean`).

---

## Gobernanza

- Los 78 nodos son la **bóveda bancaria**: inmutables durante la ingesta de dominios.
- No se añaden etiquetas al core; los conceptos externos se alinean como instancias.
- `spec_version` ≥ **1.5.1**.

Artefactos de datos:

- [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) — 78 filas
- [`data/iom_spec.json`](../data/iom_spec.json) — arrays `triads.adv` / `triads.ret`
