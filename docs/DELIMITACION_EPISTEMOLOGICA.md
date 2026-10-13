# Delimitación epistemológica del marco IOM

Este documento fija, de forma explícita, qué tipo de afirmación corresponde a cada capa del repositorio. Evita confusiones entre demostración formal, evaluación sintética y validación empírica en el mundo real.

---

## Tres capas

| Capa | Naturaleza | Artefactos | Qué demuestra | Qué **no** demuestra |
|---|---|---|---|---|
| **A. Deducciones formales cerradas** | Determinista, a priori | Lean 4 (`IOM/*.lean`), teoremas sin `sorry`/`admit` | Corrección de operadores, espejos, creates, cotas de índice, conteos canónicos **dentro del sistema formal** | Verdad empírica sobre fenómenos del mundo |
| **B. Validaciones sintéticas / estructurales** | Determinista + inductiva sobre datos generados por reglas | RDF/OWL, SHACL, CSV canónicos, PI-HGAT-T, baselines, ablaciones | Que las relaciones generadas por reglas son consistentes (SHACL), recuperables por ML (métricas), y que fase/posición bastan | Que el marco describe correctamente sistemas ecológicos, de mercado, etc. |
| **C. Validación empírica en el mundo real** | Inductiva sobre datos **no** derivados del generador | `datasets/independent_eval/` (anotación humana ciega), `datasets/external_eval/`, CSV de dominios alineados vía ingesta | Acuerdo inter-anotador, interpretabilidad, robustez ante conceptos externos (cuando existan anotaciones) | — (esta capa es el único camino hacia afirmaciones empíricas) |

---

## Reglas de lenguaje en documentación y paper

1. **Lean / teoremas** → «demostrado formalmente», «teorema», «corrección estructural en el sistema formal».
2. **SHACL / conteos CSV** → «validado estructuralmente», «conforme a la especificación», «recuperación de relaciones generadas por reglas».
3. **Métricas PI-HGAT-T / baselines = 1.0** → «recuperabilidad perfecta bajo leave-one-triad-out de relaciones generadas por reglas»; **nunca** «validación empírica del marco».
4. **Anotación humana independiente** → «evaluación de interpretabilidad / acuerdo inter-anotador»; la coincidencia post-hoc con `rule_reference` no es el objetivo primario.
5. **Ingesta de dominios CSV** → «alineación estructural a la ontología canónica»; no implica que el dominio externo valide el marco hasta que existan etiquetas independientes.

---

## Referencias cruzadas

- Auditoría de métricas 100 %: [`docs/AUDITORIA_METRICAS.md`](AUDITORIA_METRICAS.md)
- Protocolo de evaluación independiente: [`datasets/independent_eval/`](../datasets/independent_eval/)
- Paper: [`paper.md`](../paper.md) (sección de delimitación)
- README: puente metodológico y fases 1 / 2
