# Tríadas categoriales del marco I.O.

**13 tríadas** × **2 fases** × **3 posiciones** = **78 nodos**  
`spec_version` **1.9.0** · [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) · [`data/iom_spec.json`](../data/iom_spec.json)

- Índice: **1 … 13** (`T01` … `T13`)
- Avance: **→ \| 0 \| →** · Retroceso: **← \| 0 \| ←**
- `position_index`: 0 = lateral →/← · 1 = centro · 2 = lateral →/←

Orden canónico: **#1** orientación\|cuántico\|dirección … **#13** animal\|humano\|IA.

---

## Fase de Avance (`adv` / evol)

```
#   |       →       |       0       |       →       |
1   | orientación | cuántico | dirección |
2   | hardware | virtual | software |
3   | universo | espacio | vacío |
4   | singularidad | tiempo | infinito |
5   | cuerpo | consciente | mundo |
6   | carácter | subconsciente | personalidad |
7   | memoria | inconsciente | imaginación |
8   | receptor | supraconsciente | emisor |
9   | lógica | inteligencia | libertad |
10  | muerte | artificial | vida |
11  | descendente | mente | ascendente |
12  | oscuridad | consciencia | luz |
13  | animal | humano | IA |
#   |       ←       |       0       |       ←       |
```

| # | → | 0 | → | node_id |
|---|---|---|---|--------|
| 1 | orientación | cuántico | dirección | `T01_adv_*` |
| 2 | hardware | virtual | software | `T02_adv_*` |
| 3 | universo | espacio | vacío | `T03_adv_*` |
| 4 | singularidad | tiempo | infinito | `T04_adv_*` |
| 5 | cuerpo | consciente | mundo | `T05_adv_*` |
| 6 | carácter | subconsciente | personalidad | `T06_adv_*` |
| 7 | memoria | inconsciente | imaginación | `T07_adv_*` |
| 8 | receptor | supraconsciente | emisor | `T08_adv_*` |
| 9 | lógica | inteligencia | libertad | `T09_adv_*` |
| 10 | muerte | artificial | vida | `T10_adv_*` |
| 11 | descendente | mente | ascendente | `T11_adv_*` |
| 12 | oscuridad | consciencia | luz | `T12_adv_*` |
| 13 | animal | humano | IA | `T13_adv_*` |

---

## Fase de Retroceso (`ret` / invol)

```
#   |       →       |       0       |       →       |
1   | dirección | cuántico | orientación |
2   | software | virtual | hardware |
3   | vacío | espacio | universo |
4   | infinito | tiempo | singularidad |
5   | mundo | consciente | cuerpo |
6   | personalidad | subconsciente | carácter |
7   | imaginación | inconsciente | memoria |
8   | emisor | supraconsciente | receptor |
9   | libertad | inteligencia | lógica |
10  | vida | artificial | muerte |
11  | ascendente | mente | descendente |
12  | luz | consciencia | oscuridad |
13  | IA | humano | animal |
#   |       ←       |       0       |       ←       |
```

| # | ← | 0 | ← | node_id |
|---|---|---|---|--------|
| 1 | dirección | cuántico | orientación | `T01_ret_*` |
| 2 | software | virtual | hardware | `T02_ret_*` |
| 3 | vacío | espacio | universo | `T03_ret_*` |
| 4 | infinito | tiempo | singularidad | `T04_ret_*` |
| 5 | mundo | consciente | cuerpo | `T05_ret_*` |
| 6 | personalidad | subconsciente | carácter | `T06_ret_*` |
| 7 | imaginación | inconsciente | memoria | `T07_ret_*` |
| 8 | emisor | supraconsciente | receptor | `T08_ret_*` |
| 9 | libertad | inteligencia | lógica | `T09_ret_*` |
| 10 | vida | artificial | muerte | `T10_ret_*` |
| 11 | ascendente | mente | descendente | `T11_ret_*` |
| 12 | luz | consciencia | oscuridad | `T12_ret_*` |
| 13 | IA | humano | animal | `T13_ret_*` |

---

## Espejo y creación

| Relación | Condición |
|----------|-----------|
| `mirrorOf` | Fases opuestas + `position_index_tgt = 2 − position_index_src` |
| `creates` | Cuatro reglas lateral↔centro entre fases |
| `none` | Resto |

Ejemplo: tríada **13** avance (animal \| humano \| IA) ↔ retroceso (IA \| humano \| animal).  
Ejemplo: tríada **1** avance (orientación \| cuántico \| dirección) ↔ retroceso (dirección \| cuántico \| orientación).

Detalle: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
