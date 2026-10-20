# Especificación metodológica: alineación y verificación ontológica para la integración de tríadas semánticas en sistemas empíricos

> Especificación operativa del marco I.O. como **prueba empírica de interpretabilidad y medibilidad semántica** sobre fenómenos del mundo real.  
> Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md) · Protocolo: [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · Suite: [`../experiments/domain_mapping/registry.json`](../experiments/domain_mapping/registry.json)

---

## 1. Objetivos, alcance y delimitación

### 1.1 Cinco perspectivas

| Perspectiva | Función |
|---|---|
| **Individualidad** | Fronteras de identidad y propiedades no derivables de la singularidad |
| **Dualidad** | Correspondencia, complementariedad, simetría o polaridad entre pares |
| **Totalidad** | Cohesión sistémica y clausura semántica del conjunto de tríadas |
| **Evolución** | Transformación direccional, progresión de fases, emergencia |
| **Involución** | Repliegue, simplificación, disolución, retorno a estados primitivos |

### 1.2 Separación metodológica

| Criterio | Diagnóstico sintético (interno) | Validez semántica (mundo real) |
|---|---|---|
| Objetivo | Recuperación de relaciones generadas por reglas | Acuerdo humano ciego sobre conceptos externos |
| Herramientas | PI-HGAT-T, baselines | Protocolo ciego, Fleiss' κ |
| Afirmación | Coherencia algorítmica / sintáctica | Interpretabilidad provisional (n=14, κ=0.6871) |
| Límite | **No** mide validez en el mundo real | **No** es prueba universal del marco |

## 2. Arquitectura multicapa

1. **Validez semántica (mundo real)** — eje del repositorio (`datasets/independent_eval/`, EXP-A, EXP-E).
2. **Formal** — Lean 4.9.0 (`IOM/FormalRules.lean`); prerrequisito, no validez empírica.
3. **Estructural** — OWL/SHACL, CSV canónicos.
4. **Diagnóstico sintético** — PI-HGAT-T / baselines; solo recuperación de reglas.

## 3. Alineación de dominios (cosmología náhuatl)

Secuencia:

1. Catalogar pares empíricos y fuentes en [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md).
2. Asignar `mirrorOf` o `creates` según [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
3. Verificar premisas (vacío, unidad, infinito, transformación) en [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md).
4. Persistir CSV y validar SHACL; luego evaluación ciega de dominio cuando proceda.

Ejemplos operativos (EXP-E):

| Dominio | Par | Relación típica |
|---|---|---|
| Cosmología náhuatl | Tezcatlipoca ↔ Quetzalcóatl | `mirrorOf` |
| Cosmología náhuatl | Vida ↔ muerte | `mirrorOf` |
| Cosmología náhuatl | Sol de fuego → Sol de agua | `creates` |
| Cosmología náhuatl | Camino al Mictlán → Mictlán | `creates` |
| Cosmología náhuatl | Nahui Ollin vs Sol de viento | `none` (contraste de edades) |

Artefactos: [`experiments/domain_mapping/examples.json`](../experiments/domain_mapping/examples.json).

## 4. Validación semántica en el mundo real

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo moderado-sustancial (14 pares) |
| Unánime | 10/14 | Controles estructurales estables |
| Desacuerdos | NC01, NC02, AM01, AM03 | Conceptos nuevos y casos ambiguos |

κ es **demostración provisional**, no validez universal.

## 5. Pipeline

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
