# Guía Conceptual: Las Cinco Perspectivas Fundamentales del Marco I.O.

## 1. Introducción

El Marco I.O. es una estructura de análisis semántico diseñada para categorizar e interpretar relaciones entre conceptos y pares del mundo real de manera **interpretable y medible**, sin constituir un producto de software.

Componentes clave:

- **Relaciones operativas**: `mirrorOf` (simetría / reflejo) y `creates` (generación causal).
- **Fases**: etapas secuenciales del ciclo conceptual.
- **13 tríadas**: esquema de articulación en conjuntos de tres elementos.

---

## 2. Las Cinco Perspectivas

### 2.1 Individualidad

Aísla y define una entidad en su forma singular. Delimita fronteras intrínsecas antes de analizar interacciones.

- Cosmología náhuatl: Sol/edad, entidad anímica (teyolia).

### 2.2 Dualidad

Categoriza pares en correspondencia, polaridad u oposición especular. Usa de forma directa `mirrorOf`.

> Ningún concepto opera completamente aislado; las entidades se definen a través de su par opuesto o reflejo.

### 2.3 Totalidad

Agrupa entidades e interacciones dentro de un sistema integrado (edad cosmológica, horizonte del Quinto Sol).

### 2.4 Evolución

Describe el dinamismo mediante el cual conceptos generan nuevos estados. Se apoya principalmente en `creates`.

### 2.5 Involución

Complemento de la evolución: repliegue, concentración o reestructuración interna dentro del ciclo de fases (p. ej. camino al Mictlán).

---

## 3. Matriz Comparativa

| Perspectiva | Pregunta clave | Rol |
|---|---|---|
| Individualidad | ¿Qué es la entidad por sí misma? | Aísla y define fronteras |
| Dualidad | ¿Cuál es su par o reflejo? | Polaridad / `mirrorOf` |
| Totalidad | ¿A qué sistema pertenecen? | Red o conjunto integrado |
| Evolución | ¿Qué nuevo estado se genera? | Generación / `creates` |
| Involución | ¿Cómo se repliega o consolida? | Reestructuración interna |

### Mapeo empírico (EXP-E)

El experimento EXP-E (`experiments/domain_mapping/validate_examples.py`) analiza **5 pares** de cosmología náhuatl (Cinco Soles, Mictlán) para comprobar si las 13 tríadas se sostienen al aplicarse a la realidad. Estandariza el dominio bajo un lenguaje común e asegura interpretabilidad para especialistas del dominio alineado.

---

## 4. Validación y Casos Complejos

| Capa | Qué hace |
|---|---|
| Lean 4 (EXP-B) / SHACL (EXP-C) | Prerrequisito de consistencia interna |
| PI-HGAT-T (EXP-D) | Diagnóstico sintético — **no** validez real |
| Protocolo ciego (EXP-A) | Única vía de validez semántica empírica |

**Fleiss' κ = 0.6871** (14 pares) — acuerdo moderado-sustancial.

| Tipo | Casos | Lectura |
|---|---|---|
| Claros | 10/14 unánimes | Controles estructurales estables |
| Frontera | NC01, NC02, AM01, AM03 | Conceptos nuevos y ambiguos |

Identificar desacuerdos NC/AM no es falla: delimita los límites del sistema.

---

## 5. Lista de Cotejo para Categorizar

1. **Individualidad** — ¿He aislado la entidad en sus términos intrínsecos?
2. **Dualidad / Totalidad** — ¿Identifiqué su par (`mirrorOf`) y el sistema que los engloba?
3. **Evolución / Involución** — ¿La interacción genera un nuevo estado (`creates`) o un repliegue de fases?
