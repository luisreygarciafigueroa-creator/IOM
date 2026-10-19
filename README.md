# IOM — prueba de validez semántica en el mundo real

Repositorio del marco I.O. (cinco perspectivas: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**).

> **Carácter del proyecto:** este repositorio es una **prueba y demostración** de si la estructura semántica del marco I.O. (`mirrorOf`, `creates`, perspectivas y fases) puede aplicarse de forma **interpretable y medible** a conceptos y pares del mundo real — no un producto de software ni una validación sintética de reglas generadas por el propio sistema.

Metodología: [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md) · Dictamen: [`docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md) · Aprendizaje: [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)

## Qué se está probando

| Pregunta | Cómo se responde en el repo |
|---|---|
| ¿Pueden anotadores independientes, ciegos a las reglas, etiquetar relaciones semánticas sobre pares reales/nuevos/ambiguos? | Protocolo ciego + Fleiss' κ (**EXP-A**) |
| ¿La estructura formal es internamente coherente? | Lean 4 (**EXP-B**) + SHACL (**EXP-C**) |
| ¿Las reglas sintéticas son recuperables por un modelo? | PI-HGAT-T (**EXP-D**; diagnóstico interno — **no** validez semántica real) |
| ¿Se puede alinear un dominio empírico a las 13 tríadas? | **EXP-E** (8 pares bio/econ) + catálogo de dominios |

## Evidencia actual de validez semántica (mundo real)

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo moderado-sustancial (14 pares) |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Conceptos nuevos y casos ambiguos |

**Demostración provisional** bajo protocolo ciego; no prueba universal del marco.

## Experimentos integrados (EXP-A a EXP-E)

| ID | Capa | Runner | Afirmación legítima |
|---|---|---|---|
| **EXP-A** | Validez semántica (ciego) | `scripts/score_independent_eval.py` | κ = 0.6871 — interpretabilidad provisional |
| **EXP-B** | Formal | `lake build` | Solidez deductiva (Lean 4) |
| **EXP-C** | Estructural | `scripts/validate_shacl.py` | Conformidad RDF/SHACL |
| **EXP-D** | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperación de reglas *generadas por el sistema* |
| **EXP-E** | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | 8 pares bio/econ → 13 tríadas |

Detalle completo: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

Aprendizaje (pedagógico, **no** métrica del marco): [`experiments/learning/`](experiments/learning/)

## Dominios de alineación (catálogo)

Demostraciones de mapeo (sin κ propio hasta anotación ciega):

| Dominio | Documento |
|---------|-----------|
| Biología / Economía | [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md) · EXP-E |
| **Cosmología náhuatl** (Cinco Soles, Mictlán) | [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) |

## Pipeline

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build                                                                    # EXP-B
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py                                    # EXP-C
.venv/bin/python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json                    # EXP-A
.venv/bin/python experiments/pi_hgat_t.py                                     # EXP-D
.venv/bin/python experiments/baselines.py
.venv/bin/python experiments/domain_mapping/validate_examples.py              # EXP-E
.venv/bin/python scripts/generate_audit_report.py
```

## Documentación

### Guías integradas (suite experimental y perspectivas)
- [`docs/ESPECIFICACION_ONTOLOGICA.md`](docs/ESPECIFICACION_ONTOLOGICA.md) — fundamentos, mapeo a 13 tríadas, gobernanza
- [`docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md`](docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md) — las cinco perspectivas y matriz comparativa
- [`docs/GUIA_DIDACTICA_PROTOCOLO_CIEGO.md`](docs/GUIA_DIDACTICA_PROTOCOLO_CIEGO.md) — protocolo ciego, Fleiss' κ y jerarquía EXP-A…E
- [`docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md) — dictamen técnico y condicionantes
- [`EXPERIMENTOS.md`](EXPERIMENTOS.md) — arquitectura multinivel EXP-A a EXP-E

### Dominios y mapeo
- [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md) — biología, economía, cosmología náhuatl
- [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) — Cinco Soles y camino al Mictlán
- [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) · [`docs/ARQUITECTURA_ONTOLOGICA.md`](docs/ARQUITECTURA_ONTOLOGICA.md)

### Núcleo metodológico
- [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md) — manual del protocolo ciego
- [`docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md`](docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md) — manual de concordancia semántica
- [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · [`docs/ESPECIFICACION_METODOLOGICA.md`](docs/ESPECIFICACION_METODOLOGICA.md) · [`docs/AUDITORIA_EPISTEMOLOGICA.md`](docs/AUDITORIA_EPISTEMOLOGICA.md)
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md)
- [`paper.md`](paper.md) · [`AUDITORIA.md`](AUDITORIA.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
