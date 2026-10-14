# Delimitación epistemológica del marco IOM

El repositorio adopta un **enfoque de validación independiente** como eje de las afirmaciones interpretativas y empíricas. Este documento separa tres capas para que no se confundan entre sí.

Detalle operativo: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md).

---

## Tres capas (la validación independiente es el eje)

| Capa | Naturaleza | Artefactos | Qué demuestra | Qué **no** demuestra |
|---|---|---|---|---|
| **Validación independiente** | Juicios o datos **no** derivados del generador de reglas; protocolo ciego | `datasets/independent_eval/`, `datasets/external_eval/`, anotación humana | Interpretabilidad, acuerdo inter-anotador, robustez ante conceptos nuevos/ambiguos | — (única capa que autoriza afirmaciones de validación del marco hacia el exterior) |
| **Formal** | Determinista, a priori | Lean 4 (`IOM/*.lean`) | Corrección de operadores y predicados **dentro del sistema formal** | Verdad empírica sobre el mundo |
| **Sintética / estructural** | Datos generados por las reglas canónicas | SHACL, CSV, PI-HGAT-T, baselines | Consistencia y recuperabilidad de relaciones *generadas por reglas* | Validación independiente del marco |

---

## Reglas de lenguaje

1. **Validación independiente** → «evaluación independiente», «acuerdo inter-anotador», «interpretabilidad bajo protocolo ciego».
2. **Lean** → «demostrado formalmente».
3. **SHACL / CSV canónicos** → «conforme a la especificación».
4. **PI-HGAT-T / baselines = 1.0** → «recuperabilidad de relaciones generadas por reglas» (diagnóstico interno); **nunca** «validación independiente» ni «validación empírica del marco».
5. **Ingesta de dominios** → «alineación estructural»; requiere etiquetas independientes propias para contar como validación independiente.

---

## Referencias

- Enfoque del repo: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)
- Auditoría métricas 100 %: [`AUDITORIA_METRICAS.md`](AUDITORIA_METRICAS.md)
- Independent eval: [`datasets/independent_eval/`](../datasets/independent_eval/)
