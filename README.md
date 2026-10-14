# IOM — formalización, ontología y experimentos empíricos reproducibles

Repositorio ejecutable del marco I.O. El marco se articula con **cinco perspectivas** (Individualidad, Dualidad, Totalidad, Evolución e Involución). El documento de referencia [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt) se conserva íntegro. La especificación operativa de tríadas y vectores está centralizada en [`data/iom_spec.json`](data/iom_spec.json).

> El código verifica propiedades formales de la especificación y mide la **recuperación de relaciones estructurales generadas por reglas**. La interpretación humana independiente está **completada** en `datasets/independent_eval/` (κ=0.6871).

## Verificación completa

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python experiments/baselines.py
.venv/bin/python scripts/score_independent_eval.py
.venv/bin/python scripts/generate_audit_report.py
```

## Contenido verificado

- **Premisas y teoremas:** [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md)
- **Cinco perspectivas:** Individualidad, Dualidad, Totalidad, Evolución, Involución
- **Lean 4.9.0:** operadores, espejos, `creates`, vectores (`IOM/FormalRules.lean`); puente CSV↔predicado
- **RDF/OWL + SHACL:** restricción estructural y semántica
- **PI-HGAT-T:** recuperación de relaciones por reglas (leave-one-triad-out)
- **Evaluación independiente:** **completada** — κ=0.6871; controles unánimes; desacuerdos en NEW/ambiguos publicados
- **Baselines y auditoría automática**

Para metodología: [`EXPERIMENTOS.md`](EXPERIMENTOS.md). Auditoría: [`AUDITORIA.md`](AUDITORIA.md).
