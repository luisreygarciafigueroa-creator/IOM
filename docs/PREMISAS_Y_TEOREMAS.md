# Premisas y teoremas del marco I.O.

Este documento separa **afirmaciones asumidas** (premisas del marco) de **resultados demostrados** en Lean o comprobados de forma determinista sobre la especificación estructurada. No confunde recuperación de reglas con validación empírica del marco sobre datos independientes.

---

## 1. Vacío, unidad informativa, infinito y transformación

### Vacío

| Afirmación | Tipo |
|---|---|
| El infinito se reinterpreta como **ausencia de información** (vacío ontológico, $V$), no como magnitud ilimitada. | **Premisa** (filosófica) |
| El vacío estructurado es el punto de partida y de retorno del ciclo evolutivo–involutivo. | **Premisa** operativa |
| $S_{\mathrm{rev}}(Ivo(E(V_t))) = V_t$ (punto fijo estricto del vacío). | **Teorema** (Lean: `strict_fixed_point`) |

### Unidad informativa

| Afirmación | Tipo |
|---|---|
| La unidad informativa ($U$) es el átomo de presencia informativa frente al vacío. | **Premisa** |
| Los operadores $E$, $S_{\mathrm{fwd}}$, $Ivo$, $S_{\mathrm{rev}}$ actúan sobre estados que combinan tiempo discreto y carga informativa. | **Premisa** formalizada en `IOM/Core.lean` |

### Infinito

| Afirmación | Tipo |
|---|---|
| Tratar el infinito como repetición perpetua exigiría un registro informativo infinito; la ausencia total de información carece de él. | **Premisa** argumentativa |
| El vacío como infinito informacional es una **reinterpretación**, no un teorema empírico. | **Premisa** |

### Transformación

| Afirmación | Tipo |
|---|---|
| La transformación sin repetición idéntica exige tránsito por vacío estructurado (supresión), no mera reescritura. | **Premisa** (motivación) |
| Para estados no vacíos, la composición $S_{\mathrm{rev}} \circ Ivo \circ E$ **no** restaura el estado original. | **Teorema** (Lean: `no_repetition`) |
| El ciclo evolutivo–involutivo reconfigura orientaciones; no es identidad trivial. | **Premisa** + corolario informal del teorema anterior |

---

## 2. Premisas estructurales (tablas y relaciones)

Estas premisas **no se demuestran**: se **asumen** como codificación operativa del marco y se **comprueban** de forma determinista (Lean + SHACL + CSV).

1. Hay **cinco perspectivas**: Individualidad, Dualidad, Totalidad, Evolución, Involución.
2. Hay **13 tríadas** por fase (avance/retroceso) con etiquetas canónicas en `data/iom_spec.json`.
3. **Espejo (`mirrorOf`)**: misma tríada, fase opuesta, posición lateral invertida (`pos' = 2 - pos`), centro fijo.
4. **Creación (`creates`)**: exactamente las cuatro reglas de `creation_rules` (lateral→centro o centro→laterales entre fases opuestas).
5. **Vectores**: cuatro secuencias de cinco pasos con ejes y flechas declarados.

---

## 3. Teoremas derivados en Lean (operadores y posiciones)

Demostrados en `IOM/Core.lean`, `IOM/Operators.lean`, `IOM/Specification.lean`, `IOM/FormalRules.lean`:

| Teorema | Contenido |
|---|---|
| `strict_fixed_point` | $S_{\mathrm{rev}}(Ivo(E(V_t))) = V_t$ |
| `mirror_involutive` | Espejo de posición es involutivo |
| `mirror_index` | `mirror.pos.index = 2 - pos.index` |
| `isMirror` / `isCreates` | Predicados formales de aristas admisibles |
| `expected_partition` | 78 + 104 + 208 = 390 |
| `invert_involutive` | La inversión de carga es involutiva |
| `no_repetition` | Estados no vacíos no se restauran idénticos |

---

## 4. Qué **no** afirma el marco (límites)

- No afirma que las 13 tríadas describan datos del mundo natural medidos empíricamente.
- No afirma que accuracy 1.0 en PI-HGAT-T «valide el marco en el mundo real»: valida la **recuperabilidad de relaciones generadas por las reglas** bajo partición leave-one-triad-out.
- La reinterpretación del infinito como vacío es **premisa filosófica**, no teorema ni hallazgo experimental.
- La evaluación con anotadores humanos independientes (ciegos) es el canal legítimo para estudiar **validez semántica / interpretabilidad** de las relaciones en el mundo real; ver `datasets/independent_eval/`.

---

## 5. Correspondencia con artefactos

| Capa | Artefacto |
|---|---|
| Premisas filosóficas | `docs/MARCOI.O.txt`, este documento |
| Premisas estructurales | `data/iom_spec.json` |
| Teoremas | `IOM/*.lean` |
| Conformidad | SHACL, CSV, puentes de prueba |
| Validez semántica (mundo real) | `datasets/independent_eval/` |
| Recuperabilidad sintética | PI-HGAT-T, baselines |
