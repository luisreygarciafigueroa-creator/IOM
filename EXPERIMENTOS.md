# Experimentos integrados del marco I.O. (EXP-A a EXP-E)

Arquitectura de verificación multinivel que evalúa secuencialmente coherencia
lógica interna, restricciones de forma y validez semántica externa.

Guías: [`docs/ESPECIFICACION_ONTOLOGICA.md`](docs/ESPECIFICACION_ONTOLOGICA.md) ·
[`docs/GUIA_DIDACTICA_PROTOCOLO_CIEGO.md`](docs/GUIA_DIDACTICA_PROTOCOLO_CIEGO.md) ·
[`docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md`](docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md).

---

## 1. Matriz de la suite experimental

| ID | Capa | Runner | Objetivo / función | Afirmación legítima |
|---|---|---|---|---|
| **EXP-A** | Validez semántica (ciego) | `scripts/score_independent_eval.py` | Etiquetado ciego inter-anotador sobre pares reales/nuevos/ambiguos | Fleiss' κ = **0.6871** (n=14); interpretabilidad provisional |
| **EXP-B** | Formal | `lake build` | Teoremas y no-contradicción en Lean 4 | Solidez deductiva |
| **EXP-C** | Estructural | `scripts/validate_shacl.py` | Restricciones RDF/SHACL sobre el grafo ontológico | Conformidad de formas |
| **EXP-D** | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperabilidad de relaciones *generadas por reglas* | **No** validez semántica real |
| **EXP-E** | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | Alineación cosmología náhuatl (Cinco Soles, Mictlán) a 13 tríadas | Cartografía sin romper reglas |

### Jerarquía epistemológica

1. **EXP-B + EXP-C** son prerrequisitos técnicos (lógica y forma).
2. **EXP-D** es control de integridad interna autorreferencial.
3. **EXP-A** es el único criterio de validez semántica empírica.
4. **EXP-E** demuestra aplicabilidad de mapeo a dominios reales acotados.

Registro: [`experiments/domain_mapping/registry.json`](experiments/domain_mapping/registry.json).

---

## 2. EXP-A — Validez semántica empírica (protocolo ciego)

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** (moderado-sustancial) |
| Unánime | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 |

- **NC** (conceptos nuevos): fronteras de generalización.
- **AM** (ambiguos): polisemia intencional; prueba de autenticidad del test.

```bash
python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json
```

Material: [`datasets/independent_eval/`](datasets/independent_eval/) ·
Protocolo: [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md).

---

## 3. EXP-B y EXP-C — Formal y estructural

```bash
lake build                         # EXP-B — Lean 4
python scripts/validate_shacl.py   # EXP-C — SHACL
```

Documentación: [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) ·
[`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md).

---

## 4. EXP-D — Diagnóstico sintético (PI-HGAT-T)

**PI-HGAT-T** (*Perspective-Informed Heterogeneous Graph Attention Network for Triads*) clasifica pares dirigidos como `none` / `mirrorOf` / `creates` a partir de fase y posición (sin etiquetas léxicas ni índice de tríada), bajo leave-one-triad-out (13 folds).

> Las métricas miden recuperabilidad de relaciones *generadas por reglas*,
> **no** la verdad del marco sobre datos independientes del generador.

### Resultados (semilla `20261008`, 100 épocas)

| Variante | Accuracy | Macro-F1 | mirrorOf F1 | creates F1 | Conformidad reglas |
|---|---:|---:|---:|---:|---:|
| **PI-HGAT-T (fase + posición)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| Ablación sin fase | 0.6000 | 0.6056 | 0.7500 | 0.6667 | 0.5385 |
| Ablación sin posición | 0.6359 | 0.5771 | 0.3871 | 0.4870 | 0.3932 |

| Método baseline | Accuracy | Macro-F1 |
|---|---:|---:|
| Reglas deterministas (oracle SHACL) | 1.0000 | 1.0000 |
| MLP sin grafo | 1.0000 | 1.0000 |
| Regresión logística | 0.5333 | 0.2424 |

Datos: 78 nodos, 390 candidatos (78 `mirrorOf`, 104 `creates`, 208 `none`).
Fuente: `experiments/results/pi_hgat_t_metrics.json`.

```bash
python experiments/pi_hgat_t.py
python experiments/baselines.py
```

---

## 5. EXP-E — Mapeo de dominios empíricos

Pares de cosmología náhuatl (Cinco Soles, Mictlán) alineados a las 13 tríadas sin alterar axiomas.

```bash
python experiments/domain_mapping/validate_examples.py
# → experiments/results/domain_mapping_validation.json
```

Protocolo: [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) ·
Catálogo: [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md).

**No** constituyen κ de dominio ni validación de campo.

---

## 6. Pipeline completo

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python experiments/baselines.py
.venv/bin/python experiments/domain_mapping/validate_examples.py
.venv/bin/python scripts/generate_audit_report.py
```
