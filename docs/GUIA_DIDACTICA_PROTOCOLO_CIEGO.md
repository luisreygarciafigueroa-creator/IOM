# Guía Didáctica: Validación Semántica y Protocolos Experimentales Ciegos en el Marco I.O.

## 1. ¿Cómo probamos que el significado es real?

Un sistema internamente consistente **no** es automáticamente semánticamente válido. La validez semántica exige evaluadores humanos externos. La pregunta que guía la investigación:

> ¿Pueden anotadores independientes, ciegos a las reglas, etiquetar relaciones semánticas sobre pares reales/nuevos/ambiguos?

Las cinco perspectivas (Individualidad, Dualidad, Totalidad, Evolución, Involución) y las relaciones `mirrorOf` / `creates` se someten a ese examen de interpretabilidad real.

---

## 2. Protocolo Experimental Ciego (EXP-A)

| Enfoque | Qué demuestra |
|---|---|
| Validación sintética / interna | Solo que el algoritmo recupera reglas que él mismo generó |
| **Validación semántica independiente (EXP-A)** | Que humanos externos interpretan la estructura de forma medible y libre de sesgo |

Características esenciales:

1. **Ceguera de reglas** — sin acceso a la especificación formal.
2. **Muestreo de frontera** — pares reales, nuevos (NC) y ambiguos (AM).
3. **Anotación de relaciones** — `mirrorOf`, `creates`, `none`, `unsure`.

Runner: `scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`.

---

## 3. Fleiss' κ

**κ = 0.6871** sobre 14 pares — acuerdo **moderado-sustancial** (rango 0.61–0.80).

| Rango κ | Interpretación |
|---|---|
| ≤ 0.00 | No mejor que el azar |
| 0.41–0.60 | Moderado |
| **0.61–0.80** | **Moderado-sustancial** |
| 0.81–1.00 | Casi perfecto |

Es una **demostración provisional** acotada a la muestra, no una prueba universal.

---

## 4. Anatomía de Resultados EXP-A

| Criterio | Valor |
|---|---:|
| Muestra | 14 pares |
| Unánimes | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 |

- **NC** (New Concepts): términos fuera del corpus habitual → fronteras de generalización.
- **AM** (Ambiguous): polisemia intencional → flexibilidad natural de la interpretación humana.

El desacuerdo en NC/AM es **prueba de autenticidad** del experimento, no fallo del núcleo.

---

## 5. Integración EXP-A a EXP-E

| ID | Capa | Runner | Rol |
|---|---|---|---|
| EXP-A | Semántica empírica | `scripts/score_independent_eval.py` | Única evidencia de validez real |
| EXP-B | Formal | `lake build` | Prerrequisito lógico |
| EXP-C | Estructural | `scripts/validate_shacl.py` | Prerrequisito de forma |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` | **No** mide validez real |
| EXP-E | Mapeo empírico | `experiments/domain_mapping/validate_examples.py` | 8 pares bio/econ → 13 tríadas |

Jerarquía: Lean/SHACL son prerrequisitos técnicos; solo EXP-A aporta evidencia empírica de significado interpretable.

---

## 6. Takeaways

1. Consistencia sintética ≠ validez semántica.
2. El protocolo ciego elimina el sesgo de confirmación del autor.
3. Fleiss' κ corrige por azar; 0.6871 certifica acuerdo moderado-sustancial en la muestra evaluada.
