# IOM — marco de las cinco perspectivas como Cinco Soles y Mictlán

Repositorio del marco I.O.: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**, leídas en equivalencia operativa con la cosmología náhuatl.

> **Carácter del proyecto:** equiparar las **cinco perspectivas** con los **Cinco Soles**; anclar **Nanahuatzin** → Individualidad, **Xólotl** → Dualidad, **Tecuciztécatl** → Totalidad, **Mictecacíhuatl** → Evolución, **Mictlantecuhtli** → Involución; y leer las **13 tríadas** como **arquitectura del Mictlán**. No es un producto de software comercial: es un marco formal (Lean / OWL / SHACL) cuyo sentido es esta cartografía cosmológica.

Carácter canónico: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) · Dominio: [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Equivalencia central

| Perspectiva | Figura ancla | Principio |
|-------------|--------------|-----------|
| Individualidad | **Nanahuatzin** | Singularidad que se entrega al fuego (sol) |
| Dualidad | **Xólotl** | Doble / tránsito / reflejo |
| Totalidad | **Tecuciztécatl** | Plenitud ambicionada (luna / sistema) |
| Evolución | **Mictecacíhuatl** | Ciclo de la señora del Mictlán |
| Involución | **Mictlantecuhtli** | Señor del Mictlán; retorno al vacío |

Las **13 tríadas** ↔ **Mictlán** (umbrales del camino; posiciones → / 0 / ←; fases adv / ret).

Detalle: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md).

## Qué se verifica en el repo

| Pregunta | Cómo se responde |
|---|---|
| ¿La equivalencia cosmológica es formalmente coherente? | Lean 4 (**EXP-B**) + SHACL (**EXP-C**) |
| ¿Se puede cartografiar el dominio Cinco Soles / Mictlán a las 13 tríadas? | **EXP-E** + [`MANUAL_ALINEACION_DOMINIOS.md`](docs/MANUAL_ALINEACION_DOMINIOS.md) |
| ¿Hay acuerdo inter-anotador bajo protocolo ciego? | Protocolo ciego + Fleiss' κ (**EXP-A**) — capa auxiliar de interpretabilidad |
| ¿Las reglas sintéticas son recuperables por un modelo? | PI-HGAT-T (**EXP-D**; diagnóstico interno) |

## Evidencia auxiliar de interpretabilidad (EXP-A)

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo sustancial (14 pares; Landis & Koch 0.61–0.80) |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Conceptos nuevos y casos ambiguos |

Módulo didáctico: [`docs/MODULO_DIDACTICO_EVALUACION_CIEGA.md`](docs/MODULO_DIDACTICO_EVALUACION_CIEGA.md).

## Experimentos integrados (EXP-A a EXP-E)

| ID | Capa | Runner | Afirmación legítima |
|---|---|---|---|
| **EXP-A** | Interpretabilidad (ciego) | `scripts/score_independent_eval.py` | κ = 0.6871 — acuerdo provisional |
| **EXP-B** | Formal | `lake build` | Solidez deductiva (Lean 4) |
| **EXP-C** | Estructural | `scripts/validate_shacl.py` | Conformidad RDF/SHACL |
| **EXP-D** | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperación de reglas *generadas por el sistema* |
| **EXP-E** | Cartografía cosmológica | `experiments/domain_mapping/validate_examples.py` | Alineación Cinco Soles / Mictlán (Nanahuatzin…Mictlantecuhtli) |

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Dominio prioritario

| Dominio | Documento |
|---------|-----------|
| Cosmología náhuatl (Cinco Soles, Mictlán, figuras ancla) | [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) |
| Carácter del repositorio | [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) |
| Manual de cartografía | [`docs/MANUAL_ALINEACION_DOMINIOS.md`](docs/MANUAL_ALINEACION_DOMINIOS.md) |
| Medios (Piedra del Sol, códices) | [`docs/media/cosmos_nahuatl/`](docs/media/cosmos_nahuatl/) |

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

### Núcleo de sentido
- [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md)
- [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md)
- [`docs/CATALOGO_DOMINIOS.md`](docs/CATALOGO_DOMINIOS.md)
- [`docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md`](docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md)

### Formal y metodológico
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md)
- [`docs/MANUAL_ALINEACION_DOMINIOS.md`](docs/MANUAL_ALINEACION_DOMINIOS.md)
- [`docs/ESPECIFICACION_ONTOLOGICA.md`](docs/ESPECIFICACION_ONTOLOGICA.md) · [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)
- [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`paper.md`](paper.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
