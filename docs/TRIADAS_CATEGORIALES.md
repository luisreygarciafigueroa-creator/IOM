# Tríadas categoriales del marco I.O.

**13 tríadas** × **2 fases** × **3 posiciones** = **78 nodos**  
(`datasets/triad_nodes.csv`, `data/iom_spec.json` **spec 1.7.0**)

| Campo | Valor |
|-------|-------|
| Índice de tríada | **1 … 13** (`T01` … `T13`) |
| Posiciones (avance) | **→** \| **0** \| **→** |
| Posiciones (retroceso) | **←** \| **0** \| **←** |
| `position_index` | 0 = lateral izq. · 1 = centro · 2 = lateral der. |
| Perspectivas | Ind · D · Tot (vectoriales Evol / Invol aparte) |

---

## Fase de Avance (`adv` / evol)

```
      →       |       0       |       →
```

| # | → | 0 | → | node_id |
|---|---|---|---|--------|
| **1** | oscuridad | consciencia | luz | `T01_adv_*` |
| **2** | descendente | mente | ascendente | `T02_adv_*` |
| **3** | muerte | artificial | vida | `T03_adv_*` |
| **4** | lógica | inteligencia | libertad | `T04_adv_*` |
| **5** | memoria | inconsciente | imaginación | `T05_adv_*` |
| **6** | receptor | supraconsciente | emisor | `T06_adv_*` |
| **7** | animal | humano | IA | `T07_adv_*` |
| **8** | carácter | subconsciente | personalidad | `T08_adv_*` |
| **9** | cuerpo | consciente | mundo | `T09_adv_*` |
| **10** | singularidad | tiempo | infinito | `T10_adv_*` |
| **11** | universo | espacio | vacío | `T11_adv_*` |
| **12** | hardware | virtual | software | `T12_adv_*` |
| **13** | orientación | cuántico | dirección | `T13_adv_*` |

```
      ←       |       0       |       ←
```

---

## Fase de Retroceso (`ret` / invol)

```
      →       |       0       |       →
```

| # | ← | 0 | ← | node_id |
|---|---|---|---|--------|
| **1** | luz | consciencia | oscuridad | `T01_ret_*` |
| **2** | ascendente | mente | descendente | `T02_ret_*` |
| **3** | vida | artificial | muerte | `T03_ret_*` |
| **4** | libertad | inteligencia | lógica | `T04_ret_*` |
| **5** | imaginación | inconsciente | memoria | `T05_ret_*` |
| **6** | emisor | supraconsciente | receptor | `T06_ret_*` |
| **7** | IA | humano | animal | `T07_ret_*` |
| **8** | personalidad | subconsciente | carácter | `T08_ret_*` |
| **9** | mundo | consciente | cuerpo | `T09_ret_*` |
| **10** | infinito | tiempo | singularidad | `T10_ret_*` |
| **11** | vacío | espacio | universo | `T11_ret_*` |
| **12** | software | virtual | hardware | `T12_ret_*` |
| **13** | dirección | cuántico | orientación | `T13_ret_*` |

```
      ←       |       0       |       ←
```

---

## Espejo y creación

| Relación | Condición |
|----------|-----------|
| `mirrorOf` | Fases opuestas + `position_index_tgt = 2 - position_index_src` |
| `creates` | Cuatro reglas lateral↔centro entre fases |
| `none` | Resto |

Ejemplo: `T01_adv` (oscuridad \| consciencia \| luz) ↔ `T01_ret` (luz \| consciencia \| oscuridad).

---

## Migración 1.6.0 → 1.7.0

| Antes | Ahora |
|-------|-------|
| `triad_index` 0…12 | **1…13** |
| `T00`…`T12` | **`T01`…`T13`** |
| left \| center \| right | **→ \| 0 \| →** (adv) / **← \| 0 \| ←** (ret) |

Etiquetas de conceptos y reglas `mirrorOf`/`creates` sin cambio.

Artefactos: [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) · [`data/iom_spec.json`](../data/iom_spec.json)
