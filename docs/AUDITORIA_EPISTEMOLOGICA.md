# Informe de auditoría epistemológica: validez semántica e interpretabilidad empírica del marco I.O.

> Auditoría del carácter del repositorio: **prueba y demostración empírica de interpretabilidad** — no producto de software ni validación sintética autorreferencial.  
> Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md) · Independiente: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)

---

## 1. Contexto y capas

| Capa | Afirmación legítima |
|---|---|
| **Validez semántica (mundo real)** | Interpretabilidad y acuerdo inter-anotador sobre conceptos externos (κ, desacuerdos, mapeos) |
| **Formal** | Coherencia deductiva en Lean 4.9.0 |
| **Estructural** | Conformidad OWL/SHACL y CSV |
| **Diagnóstico sintético** | Recuperación de relaciones *generadas por reglas* (PI-HGAT-T) |

La frontera entre consistencia interna y validez empírica externa es **infranqueable**: Lean/SHACL/PI-HGAT-T no demuestran interpretabilidad en el mundo real.

## 2. Validez semántica (evaluación inter-anotador)

```bash
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

| Hallazgo | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Unánimes | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 |

κ = 0.6871 es **demostración provisional** de interpretabilidad; **no** validez universal. Los desacuerdos en NC/AM indican fronteras elásticas de las definiciones operativas, no fallo aleatorio.

## 3. Consistencia formal y estructural

- Lean 4: teoremas sobre vacío, unidad, infinito, transformación ([`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)).
- SHACL/CSV: conformidad de formas.

Condición **necesaria e insuficiente** para validez empírica.

## 4. Crítica: prueba empírica vs diagnóstico sintético

| Criterio | Prueba empírica (mundo real) | Diagnóstico sintético |
|---|---|---|
| Datos | `datasets/independent_eval/` | `experiments/pi_hgat_t.py` |
| Métrica | Fleiss' κ | Accuracy / F1 |
| Afirmación | Interpretabilidad humana externa | Recuperabilidad de reglas internas |

PI-HGAT-T **no** aporta evidencia de verdad, utilidad o interpretabilidad de las 13 tríadas en la realidad.

## 5. Dictamen y recomendaciones

**Dictamen:** favorable **condicionado**. Coherencia formal en Lean y promesa empírica (κ=0.6871).

1. Tratar κ como prueba de concepto **provisional**; prohibido reclamar validez universal sin ampliar panel y corpus.
2. Redefinir fronteras de `mirrorOf`/`creates` en NC01, NC02, AM01, AM03 antes de inferencia automatizada.
3. Toda ingesta de dominio debe superar evaluación ciega **específica del dominio**.
4. **Excluir** métricas de PI-HGAT-T/baselines de expedientes que certifiquen validez semántica real.

Suite experimental: [`../experiments/domain_mapping/registry.json`](../experiments/domain_mapping/registry.json).
