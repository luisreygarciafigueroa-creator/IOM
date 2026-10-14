# IOM — validación independiente, formalización y ontología

Repositorio del marco I.O. (cinco perspectivas: Individualidad, Dualidad, Totalidad, Evolución e Involución).

> **Enfoque rector:** la **validación independiente** (protocolo ciego, datos no generados por las reglas canónicas, métricas de acuerdo publicadas) es el eje de las afirmaciones interpretativas sobre el marco. Lean y SHACL garantizan consistencia formal/estructural; PI-HGAT-T solo diagnostica recuperabilidad de reglas en corpus sintético.

Metodología: [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Eje empírico: evaluación independiente

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Unánime | 10/14 |
| Controles unánimes | sí |
| Desacuerdos | NC01, NC02, AM01, AM03 (NEW / ambiguos) |

Datos y protocolo: [`datasets/independent_eval/`](datasets/independent_eval/)  
Puntuación: `python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json`

## Pipeline

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
# Validación independiente (eje)
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
# Diagnóstico sintético (no sustituye lo anterior)
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python experiments/baselines.py
.venv/bin/python scripts/generate_audit_report.py
```

## Capas del repositorio

| Capa | Contenido | Afirmación legítima |
|---|---|---|
| **Validación independiente** | `independent_eval/`, protocolo ciego, κ y desacuerdos | Interpretabilidad / acuerdo inter-anotador |
| **Formal** | Lean 4.9.0, `IOM/FormalRules.lean` | Teoremas dentro del sistema formal |
| **Estructural** | OWL/SHACL, CSV canónicos, puentes de prueba | Conformidad con la especificación |
| **Diagnóstico sintético** | PI-HGAT-T, baselines | Recuperación de relaciones *generadas por reglas* |

## Documentación

- [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) — enfoque del repo
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) — vacío, unidad, infinito, transformación
- [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md) — `mirrorOf` / `creates`
- [`paper.md`](paper.md) · [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`AUDITORIA.md`](AUDITORIA.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
