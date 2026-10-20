# Tríadas categoriales del marco I.O.

**13 tríadas** × **2 fases** × **3 posiciones** = **78 nodos**  
`spec_version` **1.7.0** · [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) · [`data/iom_spec.json`](../data/iom_spec.json)

- Índice: **1 … 13** (`T01` … `T13`)
- Avance: **→ \| 0 \| →**· Retroceso: **← \| 0 \| ←**
- `position_index`: 0 = lateral izq. · 1 = centro · 2 = lateral der.

---

## Fase de Avance (`adv` / evol)

```
#   |       →       |       0       |       →       |
1   | oscuridad | consciencia | luz |
2   | descendente | mente | ascendente |
3   | muerte | artificial | vida |
4   | lógica | inteligencia | libertad |
5   | memoria | inconsciente | imaginación |
6   | receptor | supraconsciente | emisor |
7   | animal | humano | IA |
8   | carácter | subconsciente | personalidad |
9   | cuerpo | consciente | mundo |
10  | singularidad | tiempo | infinito |
11  | universo | espacio | vacío |
12  | hardware | virtual | software |
13  | orientación | cuántico | dirección |
#   |       ←       |       0       |       ←       |
```

| # | → | 0 | → | node_id |
|---|---|---|---|--------|
| 1 | oscuridad | consciencia | luz | `T01_adv_*` |
| 2 | descendente | mente | ascendente | `T02_adv_*` |
| 3 | muerte | artificial | vida | `T03_adv_*` |
| 4 | lógica | inteligencia | libertad | `T04_adv_*` |
| 5 | memoria | inconsciente | imaginación | `T05_adv_*` |
| 6 | receptor | supraconsciente | emisor | `T06_adv_*` |
| 7 | animal | humano | IA | `T07_adv_*` |
| 8 | carácter | subconsciente | personalidad | `T08_adv_*` |
| 9 | cuerpo | consciente | mundo | `T09_adv_*` |
| 10 | singularidad | tiempo | infinito | `T10_adv_*` |
| 11 | universo | espacio | vacío | `T11_adv_*` |
| 12 | hardware | virtual | software | `T12_adv_*` |
| 13 | orientación | cuántico | dirección | `T13_adv_*` |

---

## Fase de Retroceso (`ret` / invol)

```
#   |       →       |       0       |       →       |
1   | luz | consciencia | oscuridad |
2   | ascendente | mente | descendente |
3   | vida | artificial | muerte |
4   | libertad | inteligencia | lógica |
5   | imaginación | inconsciente | memoria |
6   | emisor | supraconsciente | receptor |
7   | IA | humano | animal |
8   | personalidad | subconsciente | carácter |
9   | mundo | consciente | cuerpo |
10  | infinito | tiempo | singularidad |
11  | vacío | espacio | universo |
12  | software | virtual | hardware |
13  | dirección | cuántico | orientación |
#   |       ←       |       0       |       ←       |
```

| # | ← | 0 | ← | node_id |
|---|---|---|---|--------|
| 1 | luz | consciencia | oscuridad | `T01_ret_*` |
| 2 | ascendente | mente | descendente | `T02_ret_*` |
| 3 | vida | artificial | muerte | `T03_ret_*` |
| 4 | libertad | inteligencia | lógica | `T04_ret_*` |
| 5 | imaginación | inconsciente | memoria | `T05_ret_*` |
| 6 | emisor | supraconsciente | receptor | `T06_ret_*` |
| 7 | IA | humano | animal | `T07_ret_*` |
| 8 | personalidad | subconsciente | carácter | `T08_ret_*` |
| 9 | mundo | consciente | cuerpo | `T09_ret_*` |
| 10 | infinito | tiempo | singularidad | `T10_ret_*` |
| 11 | vacío | espacio | universo | `T11_ret_*` |
| 12 | software | virtual | hardware | `T12_ret_*` |
| 13 | dirección | cuántico | orientación | `T13_ret_*` |

---

## Espejo y creación

| Relación | Condición |
|----------|-----------|
| `mirrorOf` | Fases opuestas + `position_index_tgt = 2 − position_index_src` |
| `creates` | Cuatro reglas lateral↔centro entre fases |
| `none` | Resto |

Ejemplo: tríada **1** avance (oscuridad \| consciencia \| luz) ↔ retroceso (luz \| consciencia \| oscuridad).

Detalle: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
