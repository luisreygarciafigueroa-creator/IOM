# Delimitación epistemológica del marco IOM

El repositorio tiene carácter de **prueba y demostración de validez semántica en el mundo real**. Este documento separa las capas para que no se confundan entre sí.

Detalle operativo: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md).

---

## Capas (la validez semántica real es el eje)

| Capa | Naturaleza | Artefactos | Qué demuestra | Qué **no** demuestra |
|---|---|---|---|---|
| **Validez semántica (mundo real)** | Juicios o datos **no** derivados del generador de reglas; protocolo ciego; mapeos de dominio | `datasets/independent_eval/`, `datasets/external_eval/`, `CATALOGO_DOMINIOS.md`, anotación humana | Interpretabilidad, acuerdo inter-anotador, aplicabilidad semántica a conceptos externos | Verdad universal del marco; cobertura completa de dominios |
| **Formal** | Determinista, a priori | Lean 4 (`IOM/*.lean`) | Corrección de operadores **dentro del sistema formal** | Validez semántica empírica |
| **Sintética / estructural** | Datos generados por las reglas canónicas | SHACL, CSV, PI-HGAT-T, baselines | Consistencia y recuperabilidad de relaciones *generadas por reglas* | Validez semántica en el mundo real |

---

## Reglas de lenguaje

1. **Validez semántica / mundo real** → «prueba de validez semántica», «demostración de interpretabilidad», «acuerdo inter-anotador bajo protocolo ciego», «alineación a dominio real».
2. **Lean** → «demostrado formalmente».
3. **SHACL / CSV canónicos** → «conforme a la especificación».
4. **PI-HGAT-T / baselines = 1.0** → «recuperabilidad de relaciones generadas por reglas» (diagnóstico interno); **nunca** «validez semántica en el mundo real» ni «validación empírica del marco».
5. **Ingesta de dominios** → «demostración de alineación»; requiere etiquetas independientes propias para contar como prueba semántica de campo.

---

## Referencias

- Método de la prueba: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)
- Dominios: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md)
- Auditoría métricas 100 %: [`AUDITORIA_METRICAS.md`](AUDITORIA_METRICAS.md)
- Independent eval: [`datasets/independent_eval/`](../datasets/independent_eval/)
