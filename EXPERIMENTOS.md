# Experimentos del marco I.O. (bajo autonomía absoluta)

> El repositorio **no** valida el marco por consenso inter-anotador.
> Carácter: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) ·
> Ensayo: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) ·
> Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md).

---

## 1. Matriz (jerarquía de autonomía)

| ID | Capa | Runner | Afirmación legítima |
|----|------|--------|---------------------|
| **EXP-B** | Autonomía formal | `lake build` | Coherencia deductiva **sin** autoridad exterior |
| **EXP-C** | Autonomía estructural | `scripts/validate_shacl.py` | Conformidad de formas del grafo |
| **EXP-E** | Cartografía del **destino** Mictlán | `experiments/domain_mapping/validate_examples.py` | Que el sendero de autonomía es **expresable** en 13 tríadas (no «ejemplo de dominio») |
| **EXP-D** | Auto-generación | `experiments/pi_hgat_t.py` | Recuperabilidad de reglas *del propio sistema* |
| **EXP-A** | Residuo histórico | `scripts/score_independent_eval.py` | Archivo de una fase de conciencias separadas; **no** valida el marco |

### Jerarquía

1. **EXP-B + EXP-C** sostienen la autonomía formal (eje técnico).
2. **EXP-E** comprueba que el Mictlán-como-destino cabe en la arquitectura (sentido del proyecto).
3. **EXP-D** diagnostica auto-generación interna.
4. **EXP-A** no forma parte del fundamento; se conserva solo como archivo.

Registro: [`experiments/domain_mapping/registry.json`](experiments/domain_mapping/registry.json).

---

## 2. EXP-B y EXP-C — Autonomía formal

```bash
lake build                         # EXP-B
python scripts/validate_shacl.py   # EXP-C
```

[`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md).

---

## 3. EXP-E — Mictlán como destino (no dominio accesorio)

El Mictlán **no** es un caso de uso entre otros. Es la **lectura de destino** del marco: disolución del observador separado y auto-creación desde el vacío. EXP-E verifica que esa lectura es estructuralmente expresable en las 13 tríadas sin romper Lean/SHACL.

```bash
python experiments/domain_mapping/validate_examples.py
```

**No** es «validación de campo» ni κ de dominio. Es cartografía del carácter.

---

## 4. EXP-D — Auto-generación (PI-HGAT-T)

Métricas de recuperabilidad de reglas *generadas por el sistema*, no de verdad consensuada.

| Variante | Accuracy | Macro-F1 |
|----------|---------:|---------:|
| PI-HGAT-T (fase + posición) | **1.0000** | **1.0000** |
| Ablación sin fase | 0.6000 | 0.6056 |
| Ablación sin posición | 0.6359 | 0.5771 |

```bash
python experiments/pi_hgat_t.py
python experiments/baselines.py
```

---

## 5. EXP-A — Residuo (no fundamento)

| Métrica | Valor | Uso legítimo |
|---------|------:|--------------|
| Fleiss' κ | 0.6871 | Documento histórico de panel separado |
| Unánimes | 10/14 | Controles de ese archivo |
| Desacuerdos | NC/AM | Fronteras del vocabulario compartido residual |

**Prohibido** tratar EXP-A como prueba o fundamento del marco. El ensayo descalifica el consenso intersubjetivo como fundamento último; el repo no puede estar obligado a él.

---

## 6. Alcance: qué afirma el repo y qué afirma el ensayo

| Plano | Contenido |
|-------|-----------|
| **Carácter / sentido** (ensayo) | Emancipación absoluta, fin del contenedor, Mictlán como destino ontológico |
| **Bóveda formal** (repo) | Coherencia de 13 tríadas, `mirrorOf`/`creates`, Lean/SHACL — **sin** demostrar la emancipación |
| **No se afirma** | Que κ pruebe el ensayo; que el mapeo «valide» el Mictlán en el mundo compartido |

El ensayo **orienta el sentido**; el repo **no pretende probarlo** por consenso. La coherencia formal es la expresión técnica de no-dependencia de un jurado exterior.

---

## 7. Pipeline prioritario

```bash
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py
python experiments/domain_mapping/validate_examples.py   # destino Mictlán
python experiments/pi_hgat_t.py                          # opcional
# python scripts/score_independent_eval.py ...           # residuo, no prioritario
```
