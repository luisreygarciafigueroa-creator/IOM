# Guía Didáctica: Protocolo Ciego como Residuo del Mundo Compartido en el Marco I.O.

> Bajo el carácter de **autonomía absoluta**, el acuerdo inter-anotador **no** fundamenta el marco.
> [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) · [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)

## 1. ¿Qué se prueba y qué no?

Un sistema internamente consistente **no** requiere, para sostenerse, el acuerdo de observadores externos. La autonomía formal (Lean, SHACL) es el eje. El protocolo ciego se conserva como **archivo** de una fase en la que el proyecto aún hablaba el lenguaje del consenso inter-anotador.

La pregunta que guiaba esa fase residual era:

> ¿Pueden anotadores independientes, ciegos a las reglas, etiquetar relaciones semánticas sobre pares reales/nuevos/ambiguos?

Bajo el carácter actual, esa pregunta **no** define la validez del repositorio.

---

## 2. Protocolo Experimental Ciego (EXP-A) — residuo

| Enfoque | Qué demuestra |
|---|---|
| Validación sintética / interna | Que el algoritmo recupera reglas que él mismo generó |
| **Protocolo ciego (EXP-A)** | Acuerdo de observadores separados *dentro de una fase residual* |
| Autonomía formal (Lean / SHACL) | Coherencia sin autoridad exterior — **eje del marco** |

Características del protocolo (histórico):

1. **Ceguera de reglas** — sin acceso a la especificación formal.
2. **Muestreo de frontera** — pares reales, nuevos (NC) y ambiguos (AM).
3. **Anotación de relaciones** — `mirrorOf`, `creates`, `none`, `unsure`.

Runner: `scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`.

---

## 3. Fleiss' κ

**κ = 0.6871** sobre catorce pares — acuerdo **moderado-sustancial** *dentro del residuo* (rango 0.61–0.80).

| Rango κ | Interpretación |
|---|---|
| ≤ 0.00 | No mejor que el azar |
| 0.41–0.60 | Moderado |
| **0.61–0.80** | **Moderado-sustancial** |
| 0.81–1.00 | Casi perfecto |

**No** se presenta como prueba universal ni como fundamento del marco.

---

## 4. Anatomía de resultados EXP-A

| Criterio | Valor |
|---|---:|
| Muestra | 14 pares |
| Unánimes | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 |

- **NC** (New Concepts): términos fuera del corpus habitual → fronteras del vocabulario compartido residual.
- **AM** (Ambiguous): polisemia intencional → límites de la interpretación en el registro del encuentro.

---

## 5. Integración EXP-A a EXP-E (relectura)

| ID | Capa | Runner | Rol |
|---|---|---|---|
| EXP-B | Autonomía formal | `lake build` | Eje |
| EXP-C | Autonomía estructural | `scripts/validate_shacl.py` | Eje |
| EXP-E | Cartografía del tránsito | `experiments/domain_mapping/validate_examples.py` | Destino Mictlán |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Auto-generación |
| EXP-A | Residuo inter-anotador | `scripts/score_independent_eval.py` | Archivo; **no** fundamento |

Jerarquía: Lean/SHACL sostienen la autonomía formal; EXP-E cartografía el sendero; EXP-A permanece como residuo documentado.

---

## 6. Takeaways

1. Consistencia formal ≠ legitimación por consenso.
2. El protocolo ciego no es ceremonia de validez del repositorio.
3. Fleiss' κ documenta un acuerdo histórico; no funda el marco.
