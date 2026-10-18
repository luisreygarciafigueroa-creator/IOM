# IOM — prueba de validez semántica en el mundo real

Repositorio del marco I.O. (cinco perspectivas: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**).

> **Carácter del proyecto:** este repositorio es una **prueba y demostración** de si la estructura semántica del marco I.O. (`mirrorOf`, `creates`, perspectivas y fases) puede aplicarse de forma **interpretable y medible** a conceptos y pares del mundo real — no un producto de software ni una validación sintética de reglas generadas por el propio sistema.

Metodología: [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md) · Dominios reales: [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md) · Protocolo de mapeo: [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md)

## Qué se está probando

| Pregunta | Cómo se responde en el repo |
|---|---|
| ¿Pueden anotadores independientes, ciegos a las reglas, etiquetar relaciones semánticas sobre pares reales/nuevos/ambiguos? | Protocolo ciego + Fleiss' κ en `datasets/independent_eval/` |
| ¿La estructura formal es internamente coherente? | Lean 4 + SHACL (prerrequisito, no prueba de mundo real) |
| ¿Las reglas sintéticas son recuperables por un modelo? | PI-HGAT-T (diagnóstico interno; **no** validez semántica real) |
| ¿Se puede alinear un dominio empírico (biología, economía, …) a las 13 tríadas? | Catálogo e ingesta en `docs/CATALOGO_DOMINIOS.md` + EXP-E |

## Evidencia actual de validez semántica (mundo real)

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo inter-anotador moderado-sustancial sobre 14 pares |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Concentrados en conceptos nuevos y casos ambiguos |

Estos números son una **demostración provisional** de interpretabilidad semántica bajo protocolo ciego; no constituyen prueba universal del marco.

Datos: [`datasets/independent_eval/`](datasets/independent_eval/)  
Puntuación: `python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`

## Experimentos integrados

Registro de capas A–E: [`experiments/domain_mapping/registry.json`](experiments/domain_mapping/registry.json) · Mapeo de dominios: [`experiments/domain_mapping/`](experiments/domain_mapping/) · Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md)

| ID | Capa | Runner |
|---|---|---|
| EXP-A | Validez semántica (ciego) | `scripts/score_independent_eval.py` |
| EXP-B | Formal | `lake build` |
| EXP-C | Estructural | `scripts/validate_shacl.py` |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` |
| EXP-E | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` |

## Pipeline

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
# Prueba de validez semántica (eje del repositorio)
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
# Diagnóstico sintético (no mide validez en el mundo real)
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python experiments/baselines.py
# Demostración de mapeo de dominios (EXP-E)
.venv/bin/python experiments/domain_mapping/validate_examples.py
.venv/bin/python scripts/generate_audit_report.py
```

## Capas del repositorio

| Capa | Contenido | Afirmación legítima |
|---|---|---|
| **Validez semántica (mundo real)** | Pares independientes, anotación ciega, κ, desacuerdos, mapeos de dominio | Interpretabilidad y acuerdo sobre conceptos externos al generador de reglas |
| **Formal** | Lean 4.9.0, `IOM/FormalRules.lean` | Teoremas dentro del sistema formal |
| **Estructural** | OWL/SHACL, CSV canónicos | Conformidad con la especificación |
| **Diagnóstico sintético** | PI-HGAT-T, baselines | Recuperación de relaciones *generadas por reglas* |

## Documentación

- [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) — método de la prueba semántica
- [`docs/PROTOCOLO_DE_MAPEO.md`](docs/PROTOCOLO_DE_MAPEO.md) — protocolo de alineación y validación ciega de dominios
- [`docs/INTEGRACION_METODOLOGICA.md`](docs/INTEGRACION_METODOLOGICA.md) — integración metodológica biología/economía
- [`docs/AUDITORIA_TECNICA.md`](docs/AUDITORIA_TECNICA.md) — informe de evaluación técnica (κ, capas, dictamen)
- [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md) — alineación a fenómenos reales
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) — vacío, unidad, infinito, transformación
- [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md) — `mirrorOf` / `creates`
- [`paper.md`](paper.md) · [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`AUDITORIA.md`](AUDITORIA.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
