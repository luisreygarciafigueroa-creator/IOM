# IOM — marco de las cinco perspectivas como camino al Mictlán y autonomía multiversal

Repositorio del marco I.O.: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**, leídas desde la óptica de la **auto-creación** y el **orden multiversal**.

> **Carácter del proyecto:** el sentido del marco no es encontrar un orden universal exterior cada vez mayor (regresión infinita de contenedores), sino cartografiar el **camino al Mictlán** como tránsito hacia la **autonomía ontológica**: una existencia que se origina desde el vacío y no recibe su identidad de ninguna autoridad exterior. **Orden Definitivo ⟹ ¬∃ Contenedor Exterior.**
>
> Texto canónico de sentido: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Carácter: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md)

La formalización Lean 4 / OWL / SHACL y los 78 nodos son la **bóveda técnica**. El *sentido* es la emancipación vía el sendero del Mictlán (pulso **Mictecacíhuatl** = Evolución / **Mictlantecuhtli** = Involución).

## Equivalencia central (bajo esta óptica)

| Perspectiva | Lectura | Figura ancla (apoyo) |
|-------------|---------|----------------------|
| Individualidad | Singularidad que se crea a sí misma | Nanahuatzin |
| Dualidad | Polaridad yo/otro que se disuelve en el tránsito | Xólotl |
| Totalidad | Cada conciencia constituye **su** totalidad (no la del sistema exterior) | Tecuciztécatl |
| Evolución | Fuerza ascendente: recombina y perfecciona en el vacío | **Mictecacíhuatl** |
| Involución | Fuerza descendente: despoja y purifica hacia la raíz | **Mictlantecuhtli** |

Las **13 tríadas** = topología del **camino al Mictlán** (muerte ontológica: observador → tejido del sistema; posiciones → / 0 / ←; fases adv / ret).

Detalle: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md).

## Qué se verifica en el repo

| Pregunta | Cómo se responde |
|---|---|
| ¿La arquitectura del tránsito es formalmente coherente? | Lean 4 (**EXP-B**) + SHACL (**EXP-C**) |
| ¿Se puede cartografiar el sendero Mictlán / autonomía a las 13 tríadas? | **EXP-E** + [`MANUAL_ALINEACION_DOMINIOS.md`](docs/MANUAL_ALINEACION_DOMINIOS.md) |
| ¿Hay acuerdo inter-anotador bajo protocolo ciego? | Protocolo ciego + Fleiss' κ (**EXP-A**) — capa auxiliar |
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
| **EXP-E** | Cartografía del tránsito | `experiments/domain_mapping/validate_examples.py` | Alineación Mictlán / autonomía (Mictecacíhuatl…Mictlantecuhtli) |

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Dominio prioritario

| Dominio | Documento |
|---------|-----------|
| Sendero del Mictlán / autonomía multiversal | [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) |
| Cosmología náhuatl (apoyo: Cinco Soles, figuras) | [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) |
| Carácter del repositorio | [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) |
| Medios | [`docs/media/cosmos_nahuatl/`](docs/media/cosmos_nahuatl/) |

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
- [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)
- [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md)
- [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md)
- [`docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md`](docs/GUIA_CONCEPTUAL_PERSPECTIVAS.md)

### Formal y metodológico
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md)
- [`docs/MANUAL_ALINEACION_DOMINIOS.md`](docs/MANUAL_ALINEACION_DOMINIOS.md)
- [`docs/ESPECIFICACION_ONTOLOGICA.md`](docs/ESPECIFICACION_ONTOLOGICA.md) · [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)
- [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`paper.md`](paper.md) · [`REPRODUCCION.md`](REPRODUCCION.md)
