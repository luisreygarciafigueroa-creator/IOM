# IOM — prueba de validez semántica en el mundo real

Repositorio del marco I.O. (cinco perspectivas: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**).

> **Carácter del proyecto:** este repositorio es una **prueba y demostración** de si la estructura semántica del marco I.O. (`mirrorOf`, `creates`, perspectivas y fases) puede aplicarse de forma **interpretable y medible** a conceptos y pares del mundo real — no un producto de software ni una validación sintética de reglas generadas por el propio sistema.

Metodología: [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md) · Dictamen: [`docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md) · Aprendizaje: [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)

## Qué se está probando

| Pregunta | Cómo se responde en el repo |
|---|---|
| ¿Pueden anotadores independientes, ciegos a las reglas, etiquetar relaciones semánticas sobre pares reales/nuevos/ambiguos? | Protocolo ciego + Fleiss' κ (EXP-A) |
| ¿La estructura formal es internamente coherente? | Lean 4 + SHACL (prerrequisito) |
| ¿Las reglas sintéticas son recuperables por un modelo? | PI-HGAT-T (diagnóstico interno; **no** validez semántica real) |
| ¿Se puede alinear un dominio empírico a las 13 tríadas? | EXP-E (8 pares bio/econ) |

## Evidencia actual de validez semántica (mundo real)

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo moderado-sustancial (14 pares) |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Conceptos nuevos y casos ambiguos |

**Demostración provisional** bajo protocolo ciego; no prueba universal del marco.

## Experimentos integrados (A–E)

| ID | Capa | Runner |
|---|---|---|
| EXP-A | Validez semántica (ciego) | `scripts/score_independent_eval.py` |
| EXP-B | Formal | `lake build` |
| EXP-C | Estructural | `scripts/validate_shacl.py` |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` |
| EXP-E | Mapeo de dominios (8 pares) | `experiments/domain_mapping/validate_examples.py` |

Aprendizaje (pedagógico, no métrica del marco): [`experiments/learning/`](experiments/learning/)

## Pipeline

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

## Documentación

- [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md) — manual del protocolo ciego
- [`docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md`](docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md) — manual de concordancia semántica
- [`docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md) — dictamen técnico y epistemológico
- [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · [`docs/ESPECIFICACION_METODOLOGICA.md`](docs/ESPECIFICACION_METODOLOGICA.md) · [`docs/AUDITORIA_EPISTEMOLOGICA.md`](docs/AUDITORIA_EPISTEMOLOGICA.md)
- [`docs/ARQUITECTURA_ONTOLOGICA.md`](docs/ARQUITECTURA_ONTOLOGICA.md) · [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) · [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md)
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md)
- [`paper.md`](paper.md) · [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`AUDITORIA.md`](AUDITORIA.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
