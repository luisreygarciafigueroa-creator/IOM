# Propuesta de arquitectura ontológica: marco semántico I.O. para la alineación de dominios empíricos

> Arquitectura de alineación interdisciplinaria (biología, economía, …) sobre las cinco perspectivas y 13 tríadas.  
> Premisas: [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) · Relaciones: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · Catálogo: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md)

---

## 1. Fundamentos y relaciones operativas

Axiomas: vacío, unidad, infinito, transformación.

| Perspectiva | Rol arquitectónico |
|---|---|
| Individualidad | Unidad base, identidad primaria |
| Dualidad | Polaridad y tensión binaria |
| Totalidad | Integración sistémica |
| Evolución | Complejización y emergencia |
| Involución | Reabsorción y disolución |

- **`mirrorOf`:** isomorfismo estructural / simetría de roles.
- **`creates`:** generación causal y transición de estado.

## 2. Estratificación multicapa

| Capa | Impacto |
|---|---|
| Validez semántica (mundo real) | **Eje principal** — κ, mapeos, desacuerdos |
| Formal | Prerrequisito matemático (Lean) |
| Estructural | Gobernanza CSV/OWL/SHACL |
| Diagnóstico sintético | Calibración interna (no validez real) |

## 3. Alineación biología / economía

Proceso de 6 pasos: fenómeno → perspectiva → tríada → fase → `mirrorOf`/`creates` → validación SHACL.

### Matriz comparativa (EXP-E ampliado)

| Perspectiva | Biología (expresión celular) | Economía (reestructuración de mercado) | Operación |
|---|---|---|---|
| Individualidad | Célula madre pluripotente | Start-up disruptiva | `mirrorOf` potencial |
| Dualidad | Activación vs represión génica | Oferta vs restricción de demanda | `mirrorOf` tensión |
| Totalidad | Tejido especializado | Sector consolidado | Integración |
| Evolución | Mutación adaptativa | Innovación tecnológica | `creates` emergencia |
| Involución | Apoptosis / senescencia | Quiebra / liquidación | `creates` reorganización |

Ejemplos ejecutables: [`experiments/domain_mapping/examples.json`](../experiments/domain_mapping/examples.json).

## 4. Evaluación empírica

κ = **0.6871** (14 pares, 10/14 unánimes). Desacuerdos: NC01, NC02, AM01, AM03.

Demostración **provisional** de interpretabilidad externa.

## 5. Pipeline y gobernanza

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

Mapa documental: VALIDACION_INDEPENDIENTE, DELIMITACION_EPISTEMOLOGICA, CATALOGO_DOMINIOS, PREMISAS_Y_TEOREMAS, RELACIONES_OPERATIVAS, ESPECIFICACION_METODOLOGICA, AUDITORIA_EPISTEMOLOGICA, ARQUITECTURA_ONTOLOGICA, paper, EXPERIMENTOS, AUDITORIA, REPRODUCCION, MANIFEST.sha256.
