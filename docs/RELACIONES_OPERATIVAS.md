# Significado operativo de las relaciones `mirrorOf` y `creates`

Este documento fija la semántica operativa exacta de las dos relaciones estructurales del marco IOM. Las definiciones se alinean con:

- las reglas en `data/iom_spec.json` (`creation_rules`);
- los predicados implementados en `experiments/pi_hgat_t.py` (`admissible_relation`);
- los axiomas OWL y las formas SHACL en `ontology/`;
- los teoremas de posición en Lean (`IOM/Operators.lean`).

No se introducen umbrales estadísticos: una arista es válida o no según las reglas deterministas.

---

## 1. `io:mirrorOf`

### Definición operativa

Una arista dirigida $A \xrightarrow{\text{mirrorOf}} B$ es válida **si y solo si** se cumplen simultáneamente:

1. **Misma tríada**: `triad_index(A) = triad_index(B)`.
2. **Fase opuesta**: `phase(A) ≠ phase(B)` (una es `adv`, la otra `ret`).
3. **Posición reflejada**: `local_pos(B) = 2 - local_pos(A)`.
   - left (0) ↔ right (2)
   - center (1) ↔ center (1)
4. **Reciprocidad**: si $A \xrightarrow{\text{mirrorOf}} B$ entonces también $B \xrightarrow{\text{mirrorOf}} A$ (la propiedad OWL es simétrica).

### Ejemplos positivos

| Fuente | Destino | Justificación |
|--------|---------|---------------|
| `T00_adv_P0` (involución) | `T00_ret_P2` (involución) | misma tríada 0, fases opuestas, 0 ↔ 2 |
| `T00_adv_P1` (vacio) | `T00_ret_P1` (vacio) | centro se refleja en centro |
| `T05_adv_P2` | `T05_ret_P0` | 2 ↔ 0 |

### Ejemplos negativos

| Fuente | Destino | Motivo de rechazo |
|--------|---------|-------------------|
| `T00_adv_P0` | `T00_adv_P2` | misma fase |
| `T00_adv_P0` | `T00_ret_P0` | posición no reflejada (0 ≠ 2−0) |
| `T00_adv_P0` | `T01_ret_P2` | tríada distinta |
| `T00_adv_P0` | `T00_adv_P0` | reflexivo (excluido de candidatos) |

### Casos límite

- **Centro–centro**: permitido y obligatorio para el nodo central de cada tríada.
- **Misma etiqueta léxica**: irrelevante; la relación es puramente estructural (fase + posición).
- **Arista unidireccional**: no puede existir; SHACL y el generador imponen el par recíproco.

---

## 2. `io:creates`

### Definición operativa

Una arista dirigida $A \xrightarrow{\text{creates}} B$ es válida **si y solo si** se cumplen:

1. **Misma tríada**.
2. **Fase opuesta**.
3. **Una de las cuatro reglas de `creation_rules`**:

| source_phase | source_positions | target_phase | target_positions |
|--------------|------------------|--------------|------------------|
| adv          | {0, 2}           | ret          | {1}              |
| adv          | {1}              | ret          | {0, 2}           |
| ret          | {1}              | adv          | {0, 2}           |
| ret          | {0, 2}           | adv          | {1}              |

En lenguaje natural: un lateral (`left`/`right`) crea el centro de la fase opuesta, y el centro crea ambos laterales de la fase opuesta.

### Ejemplos positivos

| Fuente | Destino | Regla aplicada |
|--------|---------|----------------|
| `T00_adv_P0` | `T00_ret_P1` | adv lateral → ret centro |
| `T00_adv_P1` | `T00_ret_P0` | adv centro → ret left |
| `T00_adv_P1` | `T00_ret_P2` | adv centro → ret right |
| `T00_ret_P1` | `T00_adv_P0` | ret centro → adv left |

### Ejemplos negativos

| Fuente | Destino | Motivo |
|--------|---------|--------|
| `T00_adv_P0` | `T00_ret_P0` | lateral no crea lateral |
| `T00_adv_P0` | `T00_ret_P2` | lateral no crea el otro lateral |
| `T00_adv_P0` | `T00_adv_P1` | misma fase |
| `T00_adv_P1` | `T00_ret_P1` | centro no crea centro |

### Casos límite

- **Múltiples targets**: el centro produce **dos** aristas `creates` (una hacia cada lateral).
- **No simétrica**: `creates` no es simétrica ni funcional; el grafo de creación es bipartito por fase.
- **Solapamiento con mirrorOf**: un par puede ser `mirrorOf` **o** `creates`, nunca ambas a la vez (las reglas de posición son disjuntas para un mismo par ordenado).
- **Ausencia de arista**: cualquier par que no satisfaga las reglas anteriores se etiqueta `none`.

---

## 3. Correspondencia con Lean y SHACL

| Concepto | Lean | SHACL / OWL |
|----------|------|-------------|
| Posición reflejada | teoremas de índice en `Operators.lean` | restricción `sh:equals` / cálculo `2 - pos` |
| Fase opuesta | predicados de fase | `sh:not` sobre el mismo valor de `hasPhase` |
| Reglas de creación | — (datos) | formas SHACL que enumeran las cuatro combinaciones |
| Simetría de mirrorOf | — | `owl:SymmetricProperty` |

Las pruebas en `tests/test_property_links.py` verifican que los CSV regenerados satisfacen exactamente estas reglas, cerrando el círculo JSON → CSV → ontología → Lean.
