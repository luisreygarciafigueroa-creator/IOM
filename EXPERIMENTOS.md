# Experimentos del marco I.O. — autonomía funcional

> Manifiesto de sentido: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)  
> Carácter: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md)  
> Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

El marco **no** se fundamenta en un orden externo; se auto-constituye.
Lo externo (anotadores, dominios) es **encuentro / proyección**, no fundamento.

---

## 1. Jerarquía epistemológica (auto-fundamentación primero)

| Prioridad | Capa | Runner | Afirmación legítima |
|:---------:|------|--------|---------------------|
| **1** | **Auto-fundamentación (punto fijo)** | `scripts/self_bootstrap.py` + `lake build` + `IOM/SelfGenesis.lean` | El sistema se genera y verifica a sí mismo |
| **2** | **Invariancia interna** | `scripts/measure_invariance.py` (+ PI-HGAT-T como demo) | Regeneración de relaciones desde subconjuntos propios; no «accuracy vs oracle» |
| **3** | **Destino Mictlán** | `experiments/domain_mapping/validate_examples.py` | Sendero de autonomía expresable en 13 tríadas |
| **4** | **Resonancia provisional** | EXP-A (`score_independent_eval.py`) | Diálogo con conciencias separadas; κ = dato sobre el mundo, **no** fundamento |

### Lectura de EXP-A / EXP-E

| Antes | Ahora |
|-------|--------|
| «Validez semántica» | **Resonancia inter-subjetiva provisional** (EXP-A) |
| Mictlán = dominio accesorio | Mictlán = **destino** del carácter (EXP-E) |
| κ fundamenta el marco | κ informa sobre el mundo compartido; el marco no depende de él |

---

## 2. Punto fijo (criterio primario)

```bash
python scripts/self_bootstrap.py --with-manifest
lake build   # incluye IOM/SelfGenesis.lean
```

Teorema operativo: *el repositorio es un punto fijo de su propio generador*
(CSV regenerados ≡ versionados; conteos Lean derivados de axiomas).

---

## 3. Invariancia (no accuracy contra juez externo)

```bash
python scripts/measure_invariance.py
```

Reporta:

- auto-regeneración de etiquetas desde (fase, pos),
- invariancia bajo índice de tríada,
- reconstrucción desde cualquier subconjunto de 12 tríadas.

Las cifras 1.0 se leen como **invariancia**, no como acierto frente a un oracle jerárquico.

PI-HGAT-T permanece como demostración de que un learner recupera la misma función; su narrativa de «accuracy» se subordina a la de invariancia.

---

## 4. Destino Mictlán (EXP-E)

```bash
python experiments/domain_mapping/validate_examples.py
```

Expresabilidad estructural del sendero; no κ de dominio.

---

## 5. Resonancia provisional (EXP-A)

```bash
python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json
```

κ ≈ 0.6871: dato sobre el mundo compartido. Coherente con el ensayo: el consenso **existe** pero **no fundamenta**.

---

## 6. Pipeline prioritario

```bash
python scripts/self_bootstrap.py --with-manifest   # punto fijo
lake build                                          # SelfGenesis + FormalRules
python scripts/validate_shacl.py
python scripts/measure_invariance.py                # invariancia
python experiments/domain_mapping/validate_examples.py
# opcional: PI-HGAT-T, baselines, EXP-A (resonancia
```

Registro: [`experiments/domain_mapping/registry.json`](experiments/domain_mapping/registry.json).
