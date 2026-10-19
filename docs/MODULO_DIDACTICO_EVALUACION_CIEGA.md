# Módulo Didáctico: Evaluación Ciega Inter-Anotador y Medición del Acuerdo Semántico (Fleiss' κ)

> Objetivo: distinguir **consistencia formal/sintética** de **validez semántica empírica** y comprender por qué solo el protocolo ciego (EXP-A) certifica interpretabilidad en el mundo real.

---

## 1. Pregunta de investigación

> ¿Pueden anotadores independientes, ciegos a las reglas axiomáticas internas, etiquetar relaciones semánticas sobre conceptos reales, nuevos o ambiguos de manera consistente y replicable?

Un sistema impecable en Lean 4 o con Accuracy 1.0 en datos autogenerados **no** demuestra por sí solo que humanos externos compartan el significado de sus categorías.

---

## 2. Protocolo ciego (EXP-A)

### Secuencia operativa

1. Ocultar `rule_label`, gold y consensos previos.
2. Bloquear acceso a `relation_candidates.csv`, métricas de PI-HGAT-T y axiomas de fase/posición como pistas.
3. Entregar solo: `id`, etiquetas léxicas, contexto genérico y definiciones de [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

### Opciones de etiquetado

| Etiqueta | Significado |
|----------|-------------|
| `mirrorOf` | Simetría / reflejo isomórfico (fases opuestas + posición reflejada) |
| `creates` | Generación causal / transición de estado (4 reglas posicionales) |
| `none` | Fuera de reglas (misma fase, cross-tríada, sin relación operativa) |
| `unsure` | Duda legítima / ambigüedad / vocabulario no canónico |

Runner: `scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`.

---

## 3. Fleiss' κ

**Resultado EXP-A:** κ = **0.6871** (3 anotadores, 14 pares).

| Rango κ (Landis & Koch) | Interpretación |
|-------------------------|----------------|
| < 0.00 | Sin acuerdo |
| 0.00–0.20 | Insignificante |
| 0.21–0.40 | Discreto |
| 0.41–0.60 | Moderado |
| **0.61–0.80** | **Sustancial** ← resultado IOM |
| 0.81–1.00 | Casi perfecto |

Es una **demostración provisional** acotada a la muestra, no una prueba universal.

---

## 4. Anatomía del panel de 14 pares

| Tipo (`kind`) | Unanimidad | Ítems | Lección |
|---------------|------------|-------|--------|
| `out_of_rules` | 100% | 3/3 | Restricciones estructurales identificables |
| `control_mirror` | 100% | 2/2 | Espejos del núcleo estables |
| `control_creates` | 100% | 1/1 | Generación causal inequívoca |
| `cross_triad` | 100% | 2/2 | No se proyectan relaciones entre tríadas |
| `new_concept` | 33.3% | 1/3 | Vocabulario ajeno → cautela |
| `ambiguous` | 33.3% | 1/3 | Polisemia / duplicación léxica |
| **Total** | **71.4%** | **14** | |

### Perfiles de anotadores

| ID | Perfil | Comportamiento |
|----|--------|----------------|
| A1 | Estructuralista | Proyecta analogías de fase/posición aunque el léxico sea ajeno |
| A2 | Estructural-semántica | Sigue reglas; cautela ante conceptos no canónicos |
| A3 | Conservadora | Prefiere `unsure` ante ambigüedad o vocabulario nuevo |

### Cuatro desacuerdos publicados

| Par | Juicios | Consenso | Lectura |
|-----|---------|----------|--------|
| **NC01** entropía ↔ síntesis | A1=`mirrorOf`, A2/A3=`unsure` | `unsure` | A1 vio 0↔2; A2/A3 priorizaron falta de anclaje canónico |
| **NC02** ruido ↔ señal | A1=`creates`, A2=`unsure`, A3=`none` | empate | Frontera de generalización |
| **AM01** vacío ↔ vacío (T06) | A1/A2=`mirrorOf`, A3=`unsure` | `mirrorOf` | Estructura vs. «¿espejo de sí mismo?» |
| **AM03** vacío ↔ vacío (T12) | A1/A2=`mirrorOf`, A3=`unsure` | `mirrorOf` | Análogo a AM01 |

Los desacuerdos en NC/AM **no** son fallos del núcleo: delimitan fronteras de generalización y autenticidad del test.

---

## 5. Por qué el 100% sintético ≠ validez real

| Capa | Runner | Qué demuestra | Qué **no** demuestra |
|------|--------|---------------|----------------------|
| **EXP-A** | `score_independent_eval.py` | Acuerdo humano ciego (κ=0.6871) | Cobertura universal |
| **EXP-B** | `lake build` | No-contradicción deductiva | Significado empírico |
| **EXP-C** | `validate_shacl.py` | Conformidad de forma | Interpretabilidad |
| **EXP-D** | `pi_hgat_t.py` | Recuperación de reglas autogeneradas | Validez en el mundo real |
| **EXP-E** | `domain_mapping/validate_examples.py` | Alineación técnica bio/econ | κ de dominio |

> Confundir Accuracy 1.0 en EXP-D con validez semántica empírica es un error epistemológico: el modelo solo recuperó la función que el propio sistema generó.

---

## 6. Cuestionario de autoevaluación

**1.** ¿Para qué se oculta `rule_label` en EXP-A?  
**C)** Garantizar juicios independientes no sesgados por la lógica del creador.

**2.** κ = 0.6871 en la escala Landis & Koch es:  
**C)** Acuerdo sustancial (0.61–0.80).

**3.** ¿Por qué hay `unsure` en NC/AM?  
**B)** Cautela léxica ante vocabulario ajeno o duplicación de términos.

**4.** ¿Por qué Accuracy 1.0 en PI-HGAT-T no implica 100% de validez semántica real?  
**B)** Solo mide recuperación de reglas deterministas autogeneradas, no interpretabilidad humana.

---

## 7. Referencias internas

- Datos: [`datasets/independent_eval/`](../datasets/independent_eval/)
- Manual operativo: [`MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)
- Guía didáctica breve: [`GUIA_DIDACTICA_PROTOCOLO_CIEGO.md`](GUIA_DIDACTICA_PROTOCOLO_CIEGO.md)
- Suite completa: [`EXPERIMENTOS.md`](../EXPERIMENTOS.md)
- Alineación de dominios: [`MANUAL_ALINEACION_DOMINIOS.md`](MANUAL_ALINEACION_DOMINIOS.md)
