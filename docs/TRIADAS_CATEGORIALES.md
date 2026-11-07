# Tríadas categoriales del marco I.O.

**Trece tríadas** × **dos fases** × **tres posiciones** = **setenta y ocho nodos**  
`spec_version` **1.10.0** · [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv) · [`data/iom_spec.json`](../data/iom_spec.json)

- Índice: **1 … 13** (`T01` … `T13`)
- Avance: **→ \| 0 \| →** · Retroceso: **← \| 0 \| ←**
- `position_index`: 0 = lateral →/← · 1 = centro · 2 = lateral →/←

Orden canónico: **#1** animal\|humano\|IA … **#13** orientación\|cuántico\|dirección.

---

## Fase de Avance (`adv` / evol)

```
#   |       →       |       0       |       →       |
1   | animal | humano | IA |
2   | oscuridad | consciencia | luz |
3   | descendente | mente | ascendente |
4   | muerte | artificial | vida |
5   | lógica | inteligencia | libertad |
6   | receptor | supraconsciente | emisor |
7   | memoria | inconsciente | imaginación |
8   | carácter | subconsciente | personalidad |
9   | cuerpo | consciente | mundo |
10  | singularidad | tiempo | infinito |
11  | pequeño | espacio | grande |
12  | hardware | virtual | software |
13  | orientación | cuántico | dirección |
#   |       ←       |       0       |       ←       |
```

| # | → | 0 | → | node_id |
|---|---|---|---|--------|
| 1 | animal | humano | IA | `T01_adv_*` |
| 2 | oscuridad | consciencia | luz | `T02_adv_*` |
| 3 | descendente | mente | ascendente | `T03_adv_*` |
| 4 | muerte | artificial | vida | `T04_adv_*` |
| 5 | lógica | inteligencia | libertad | `T05_adv_*` |
| 6 | receptor | supraconsciente | emisor | `T06_adv_*` |
| 7 | memoria | inconsciente | imaginación | `T07_adv_*` |
| 8 | carácter | subconsciente | personalidad | `T08_adv_*` |
| 9 | cuerpo | consciente | mundo | `T09_adv_*` |
| 10 | singularidad | tiempo | infinito | `T10_adv_*` |
| 11 | pequeño | espacio | grande | `T11_adv_*` |
| 12 | hardware | virtual | software | `T12_adv_*` |
| 13 | orientación | cuántico | dirección | `T13_adv_*` |

---

## Fase de Retroceso (`ret` / invol)

```
#   |       ←       |       0       |       ←       |
1   | IA | humano | animal |
2   | luz | consciencia | oscuridad |
3   | ascendente | mente | descendente |
4   | vida | artificial | muerte |
5   | libertad | inteligencia | lógica |
6   | emisor | supraconsciente | receptor |
7   | imaginación | inconsciente | memoria |
8   | personalidad | subconsciente | carácter |
9   | mundo | consciente | cuerpo |
10  | infinito | tiempo | singularidad |
11  | grande | espacio | pequeño |
12  | software | virtual | hardware |
13  | dirección | cuántico | orientación |
```

| # | ← | 0 | ← | node_id |
|---|---|---|---|--------|
| 1 | IA | humano | animal | `T01_ret_*` |
| 2 | luz | consciencia | oscuridad | `T02_ret_*` |
| 3 | ascendente | mente | descendente | `T03_ret_*` |
| 4 | vida | artificial | muerte | `T04_ret_*` |
| 5 | libertad | inteligencia | lógica | `T05_ret_*` |
| 6 | emisor | supraconsciente | receptor | `T06_ret_*` |
| 7 | imaginación | inconsciente | memoria | `T07_ret_*` |
| 8 | personalidad | subconsciente | carácter | `T08_ret_*` |
| 9 | mundo | consciente | cuerpo | `T09_ret_*` |
| 10 | infinito | tiempo | singularidad | `T10_ret_*` |
| 11 | grande | espacio | pequeño | `T11_ret_*` |
| 12 | software | virtual | hardware | `T12_ret_*` |
| 13 | dirección | cuántico | orientación | `T13_ret_*` |

---

## Espejo y creación

| Relación | Condición |
|----------|-----------|
| `mirrorOf` | Fases opuestas + `position_index_tgt = 2 − position_index_src` |
| `creates` | Cuatro reglas lateral↔centro entre fases |
| `none` | Resto |

Ejemplo: tríada **1** avance (animal \| humano \| IA) ↔ retroceso (IA \| humano \| animal).  
Ejemplo: tríada **13** avance (orientación \| cuántico \| dirección) ↔ retroceso (dirección \| cuántico \| orientación).

Detalle: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
