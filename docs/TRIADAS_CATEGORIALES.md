# Tríadas categoriales del marco I.O.

Las **13 tríadas** × **2 fases** × **3 posiciones** = **78 nodos** canónicos
(`datasets/triad_nodes.csv`, `data/iom_spec.json` **spec 1.6.0**).
Las etiquetas se guardan en minúscula por convención de datos.

| Posición | Índice | Perspectiva |
|----------|--------|-------------|
| Izquierda (left) | 0 | Individualidad (Ind) |
| Centro (center) | 1 | Dualidad (D) |
| Derecha (right) | 2 | Totalidad (Tot) |

Las perspectivas vectoriales **Evolución** e **Involución** no añaden
columnas; se representan como secuencias en [`VECTORES_4_5.md`](VECTORES_4_5.md).

> **spec 1.6.0:** el orden de índices coincide con el orden visual canónico
> (T00 = oscuridad|consciencia|luz … T06 = animal|humano|IA … T12 = orientación|cuántico|dirección).

---

## Matriz canónica — Fase de Avance (evol / adv)

Dirección: proyección del vacío hacia la estructura.

```
      →       |       0       |       →
--------------|---------------|--------------
```

| # | Izquierda (Ind) | Centro (D) | Derecha (Tot) | node_id base |
|---|-----------------|------------|---------------|--------------|
| 0 | oscuridad | consciencia | luz | `T00_adv_*` |
| 1 | descendente | mente | ascendente | `T01_adv_*` |
| 2 | muerte | artificial | vida | `T02_adv_*` |
| 3 | lógica | inteligencia | libertad | `T03_adv_*` |
| 4 | memoria | inconsciente | imaginación | `T04_adv_*` |
| 5 | receptor | supraconsciente | emisor | `T05_adv_*` |
| 6 | animal | humano | IA | `T06_adv_*` |
| 7 | carácter | subconsciente | personalidad | `T07_adv_*` |
| 8 | cuerpo | consciente | mundo | `T08_adv_*` |
| 9 | singularidad | tiempo | infinito | `T09_adv_*` |
| 10 | universo | espacio | vacío | `T10_adv_*` |
| 11 | hardware | virtual | software | `T11_adv_*` |
| 12 | orientación | cuántico | dirección | `T12_adv_*` |

```
--------------|---------------|--------------
      ←       |       0       |       ←
```

---

## Matriz canónica — Fase de Retroceso (invol / ret)

Dirección: disolución de la estructura hacia el vacío.
Inversión simétrica (`pos_tgt = 2 - pos_src`; el centro se refleja en sí mismo).

```
      →       |       0       |       →
--------------|---------------|--------------
```

| # | Izquierda (Ind) | Centro (D) | Derecha (Tot) | node_id base |
|---|-----------------|------------|---------------|--------------|
| 0 | luz | consciencia | oscuridad | `T00_ret_*` |
| 1 | ascendente | mente | descendente | `T01_ret_*` |
| 2 | vida | artificial | muerte | `T02_ret_*` |
| 3 | libertad | inteligencia | lógica | `T03_ret_*` |
| 4 | imaginación | inconsciente | memoria | `T04_ret_*` |
| 5 | emisor | supraconsciente | receptor | `T05_ret_*` |
| 6 | IA | humano | animal | `T06_ret_*` |
| 7 | personalidad | subconsciente | carácter | `T07_ret_*` |
| 8 | mundo | consciente | cuerpo | `T08_ret_*` |
| 9 | infinito | tiempo | singularidad | `T09_ret_*` |
| 10 | vacío | espacio | universo | `T10_ret_*` |
| 11 | software | virtual | hardware | `T11_ret_*` |
| 12 | dirección | cuántico | orientación | `T12_ret_*` |

```
--------------|---------------|--------------
      ←       |       0       |       ←
```

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

Ejemplo de espejo: `T00_adv` (oscuridad | consciencia | luz) ↔ `T00_ret` (luz | consciencia | oscuridad).

Detalle formal: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · Lean 4 (`IOM/FormalRules.lean`).

---

## Migración 1.5.1 → 1.6.0

| Nuevo índice | Etiquetas (adv) | Índice previo |
|--------------|-----------------|---------------|
| 0 | oscuridad \| consciencia \| luz | 1 |
| 1 | descendente \| mente \| ascendente | 2 |
| 2 | muerte \| artificial \| vida | 3 |
| 3 | lógica \| inteligencia \| libertad | 4 |
| 4 | memoria \| inconsciente \| imaginación | 6 |
| 5 | receptor \| supraconsciente \| emisor | 5 |
| 6 | animal \| humano \| IA | 0 |
| 7–12 | sin cambio de contenido | 7–12 |

Las reglas `mirrorOf` / `creates` y el número de nodos (78) no cambian.

---

## Gobernanza

- Los 78 nodos son la **bóveda bancaria**: inmutables durante la ingesta de dominios.
- No se añaden etiquetas al core; los conceptos externos se alinean como instancias.
- `spec_version` = **1.6.0**.

Artefactos de datos:

- [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) — 78 filas
- [`data/iom_spec.json`](../data/iom_spec.json) — arrays `triads.adv` / `triads.ret`
