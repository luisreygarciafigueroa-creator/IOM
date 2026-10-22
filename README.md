# IOM — autonomía absoluta vía el camino al Mictlán

Repositorio del marco I.O.: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**, leídas desde la óptica de la **auto-creación** y el **orden multiversal**.

> **Carácter:** el sentido del marco **no** es encontrar un orden universal exterior ni obtener validez por el consenso de un «mundo compartido por conciencias separadas». Ese consenso es, en el ensayo canónico, frágil y **superable**. El eje es cartografiar el **camino al Mictlán** hacia una existencia que se origina desde el vacío: **Orden Definitivo ⟹ ¬∃ Contenedor Exterior.**
>
> Texto canónico: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Carácter: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

Lean 4 / OWL / SHACL y los 78 nodos son la **bóveda técnica de autonomía formal**: coherencia que **no pide** legitimación a un panel de observadores externos.

## Equivalencia central

| Perspectiva | Lectura | Figura ancla (apoyo) |
|-------------|---------|----------------------|
| Individualidad | Singularidad que se crea a sí misma | Nanahuatzin |
| Dualidad | Polaridad yo/otro que se disuelve en el tránsito | Xólotl |
| Totalidad | Cada conciencia constituye **su** totalidad | Tecuciztécatl |
| Evolución | Fuerza ascendente en el vacío | **Mictecacíhuatl** |
| Involución | Fuerza descendente hacia la raíz | **Mictlantecuhtli** |

Las **13 tríadas** = topología del camino al Mictlán (muerte ontológica: observador → tejido del sistema).

## Qué se verifica (jerarquía de autonomía)

| Prioridad | Pregunta | Respuesta |
|:---------:|----------|-----------|
| **1** | ¿El sistema es coherente sin autoridad exterior? | Lean (**EXP-B**) + SHACL (**EXP-C**) — **autonomía formal** |
| **2** | ¿El sendero Mictlán / autonomía es cartografiable? | **EXP-E** + dominio cosmológico |
| **3** | ¿Las reglas se recuperan desde el propio sistema? | PI-HGAT-T (**EXP-D**) |
| **4** | ¿Qué quedó del protocolo de conciencias separadas? | EXP-A (κ) — **residuo opcional, no fundamento** |

## Residuo EXP-A (archivo, no eje)

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | 0.6871 | Documento de una fase de observadores separados; **no** prueba del marco |
| Unánime | 10/14 | Controles de ese archivo |

**Prohibido** presentar κ como validez del repositorio. Ver [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md).

## Experimentos (relectura)

| ID | Capa | Afirmación legítima |
|----|------|---------------------|
| **EXP-B** | Autonomía formal | Coherencia Lean |
| **EXP-C** | Autonomía estructural | Conformidad SHACL |
| **EXP-E** | Cartografía del tránsito | Sendero Mictlán / autonomía |
| **EXP-D** | Auto-generación | Recuperación de reglas internas |
| **EXP-A** | Residuo del mundo compartido | κ documentado; no fundante |

## Dominio prioritario

| Documento | Rol |
|-----------|-----|
| [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) | Eje de sentido |
| [`CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) | Carácter |
| [`DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md) | Cartografía Mictlán |
| [`media/cosmos_nahuatl/`](docs/media/cosmos_nahuatl/) | Medios |

## Pipeline prioritario

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build                                                                    # EXP-B autonomía formal
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py                                    # EXP-C
.venv/bin/python experiments/domain_mapping/validate_examples.py              # EXP-E
.venv/bin/python experiments/pi_hgat_t.py                                     # EXP-D opcional
# EXP-A (residuo, no prioritario):
# .venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

## Documentación

### Núcleo de sentido
- [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)
- [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md)
- [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)
- [`docs/DOMINIO_COSMOS_NAHUATL.md`](docs/DOMINIO_COSMOS_NAHUATL.md)

### Formal
- [`docs/PREMISAS_Y_TEOREMAS.md`](docs/PREMISAS_Y_TEOREMAS.md) · [`docs/RELACIONES_OPERATIVAS.md`](docs/RELACIONES_OPERATIVAS.md)
- [`docs/VALIDACION_INDEPENDIENTE.md`](docs/VALIDACION_INDEPENDIENTE.md) · [`docs/AUDITORIA_EPISTEMOLOGICA.md`](docs/AUDITORIA_EPISTEMOLOGICA.md)
