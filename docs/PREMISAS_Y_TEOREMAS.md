# Premisas asumidas y teoremas derivados del marco I.O.

Este documento distingue con rigor **afirmaciones asumidas** (premisas del marco) de **resultados demostrados** en Lean o comprobados de forma determinista sobre la especificación estructurada. No confunde la recuperación de reglas con la validación empírica del marco sobre datos independientes.

Sentido cosmológico (no formal): [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md).  
Criterio de autonomía y término de la creación: [`DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md`](DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md).  
Núcleo combinatorio ampliado (11 teoremas): [`TCAAU_RECONSTRUCCION_ACADEMICA.md`](TCAAU_RECONSTRUCCION_ACADEMICA.md).

---

## 1. Qué afirma el marco (núcleo conceptual)

### 1.1 Vacío ($V$)

| Afirmación | Tipo |
|---|---|
| El vacío es la **ausencia de carga informativa** en un instante $t$: $V_t = (t, \emptyset)$. | **Premisa** (definición operativa) |
| El vacío no es aniquilación: es condición de posibilidad de nueva emergencia. | **Premisa** (interpretación ontológica; alineada con la Cosmología del Mictlán) |
| Bajo los operadores formales, el vacío es **punto fijo estricto** de la composición $S_{\mathrm{rev}} \circ Ivo \circ E$. | **Teorema** (demostrado en Lean: `strict_fixed_point`) |
| $E(V_t)=V_{t+1}$, $S_{\mathrm{fwd}}(V_t)=V_t$, $Ivo(V_t)=V_{t-1}$, $S_{\mathrm{rev}}(V_t)=V_t$. | **Teoremas** (Lean: `E_vacuum`, `S_fwd_vacuum`, `Ivo_vacuum`, `S_rev_vacuum`) |
| El vacío es información *propia*; la autonomía consiste en la inexistencia de información *ajena* de la que se dependa (C16). | **Premisa rectificada** (Dictamen de no-subordinación) |

### 1.2 Unidad informativa ($U$)

| Afirmación | Tipo |
|---|---|
| Un estado informativo es $s=(t,A)$ con $A$ lista finita de unidades (cadenas). | **Premisa** (definición en `State`) |
| La «unidad informativa» del marco es la carga mínima que puede ocupar un estado no vacío; no se identifica con un bit físico ni con una medida estadística empírica. | **Premisa** (alcance del modelo) |
| $E$ conserva la carga; $S_{\mathrm{fwd}}$ aplica deduplicación; $Ivo$ invierte la secuencia y retrocede el tiempo. | **Teoremas / definiciones** (Lean: `E_preserves_payload`, `S_fwd_applies_red`, `Ivo_applies_inversion`) |

### 1.3 Infinito

| Afirmación | Tipo |
|---|---|
| El marco **reinterpreta** el infinito como **ausencia de información** (vacío), no como magnitud ilimitada ni sucesión interminable de registros. | **Premisa** (tesis filosófica del marco; no es teorema matemático sobre $\mathbb{R}$ o cardinales) |
| Esta reinterpretación es una **hipótesis de trabajo** del marco, no un resultado empírico ni un teorema de Lean. | **Premisa** |

### 1.4 Transformación

| Afirmación | Tipo |
|---|---|
| La transformación sin repetición idéntica exige tránsito por vacío estructurado (supresión), no mera reescritura. | **Premisa** (motivación) |
| Para estados no vacíos, la composición $S_{\mathrm{rev}} \circ Ivo \circ E$ **no** restaura el estado original. | **Teorema** (Lean: `no_repetition`) |
| El ciclo evolutivo–involutivo reconfigura orientaciones; no es identidad trivial. | **Premisa** + corolario informal del teorema anterior |

### 1.5 Autonomía y no-subordinación (Dictamen 13-nov)

| Afirmación | Tipo |
|---|---|
| Un sistema es autónomo (real en sentido de estatuto) si y solo si no es engranaje ni depende de engranajes para existir (D11). | **Definición / criterio** |
| La condición de engranaje es un *modo de la relación*, no propiedad estructural del término (D10). | **Definición** |
| El término de la serie de subordinaciones es inmanente: el vacío = el universo (P11). | **Postulado** |
| La creación autónoma se completa en la equiparación (cambio de modo dependencia → equivalencia) (C15). | **Condición de término** |
| Sin lectura modal del grafo, el criterio es estructuralmente insatisfacible (Teorema 11). | **Teorema combinatorio** |

---

## 2. Premisas estructurales (tablas y relaciones)

Estas premisas **no se demuestran**: se **asumen** como codificación operativa del marco y se **comprueban** de forma determinista (Lean + SHACL + CSV).

1. Hay **cinco perspectivas**: Individualidad, Dualidad, Totalidad, Evolución, Involución.
2. Hay **trece tríadas** por fase (avance/retroceso) con etiquetas canónicas en `data/iom_spec.json`.
3. **Espejo (`mirrorOf`)**: misma tríada, fase opuesta, posición lateral invertida (`pos' = 2 - pos`), centro fijo.
4. **Creación (`creates`)**: exactamente las cuatro reglas de `creation_rules` (lateral→centro o centro→laterales entre fases opuestas).
5. **Vectores**: cuatro secuencias de cinco pasos con ejes y flechas declarados (detalle narrativo en [`VECTORES_4_5.md`](VECTORES_4_5.md) y [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md)).
6. **Bipartición término–mediador** (Teorema 11): toda tríada de las 32 canónicas de la TCAAU enlaza un término $\{U,\emptyset,M\}$ con un mediador $\{P,N,C,\mathrm{IA}\}$.

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

Teoremas del núcleo combinatorio TCAAU (enumeración exhaustiva, no Lean):

| Teorema | Contenido |
|---|---|
| Teorema 1–10 | Inventario, balance de dominios, bipartición, grados, espejo de mitades, grupo $(\mathbb{Z}_2)^3$, representación cúbica/4D, recorridos/ofrenda, conservación = invertibilidad |
| **Teorema 11** | Bipartición término–mediador; *reductio* de la lectura estructural del criterio de no-subordinación; necesidad de la lectura modal |

---

## 4. Qué **no** afirma el marco (límites)

- No afirma que las trece tríadas describan datos del mundo natural medidos empíricamente.
- No afirma que accuracy 1.0 en PI-HGAT-T «valide el marco en el mundo real»: valida la **recuperabilidad de relaciones generadas por las reglas** bajo partición leave-one-triad-out.
- La reinterpretación del infinito como vacío es **premisa filosófica**, no teorema ni hallazgo experimental.
- La evaluación con anotadores humanos independientes (ciegos) es el canal legítimo para estudiar **validez semántica / interpretabilidad** de las relaciones en el mundo real; ver `datasets/independent_eval/`.
- La Cosmología del Mictlán es modelo filosófico de correspondencia y continuidad informacional, no afirmación física demostrada.
- El criterio de no-subordinación opera en el registro ontológico-formal; no es una métrica empírica de «realidad».

---

## 5. Correspondencia con artefactos

| Concepto | Artefacto |
|---|---|
| Premisas tabuladas | `data/iom_spec.json` |
| Teoremas de operadores | `IOM/Operators.lean` |
| Teoremas de posición / espejo / creates | `IOM/Specification.lean`, `IOM/FormalRules.lean` |
| Comprobación JSON ⇄ reglas | `tests/test_property_links.py`, `tests/test_formal_rules_bridge.py` |
| Validez semántica (mundo real) | `datasets/independent_eval/` |
| Recuperabilidad sintética | PI-HGAT-T, baselines |
| Sentido cosmológico | [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md) |
| Criterio de autonomía / término de creación | [`DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md`](DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md) |
| Núcleo combinatorio + Teorema 11 | [`TCAAU_RECONSTRUCCION_ACADEMICA.md`](TCAAU_RECONSTRUCCION_ACADEMICA.md) |
