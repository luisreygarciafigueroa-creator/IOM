# Manual de Alineación Ontológica y Cartografía de Dominios Empíricos en el Marco I.O.

> Los mapeos de dominio son **demostraciones de aplicabilidad semántica**, no validaciones de campo ni teorías definitivas de las disciplinas analizadas. La prueba primaria de validez semántica sigue siendo EXP-A (protocolo ciego).

---

## 1. Principios de invarianza del núcleo

El núcleo canónico de **78 nodos** (13 tríadas × 2 fases × 3 posiciones) opera como ancla semántica invariante. Al cartografiar dominios heterogéneos (cosmogonías náhuatl y otros), todo concepto externo se asimila como instancia o proyección **sin alterar** `data/iom_spec.json`, Lean 4 ni SHACL.

### Cuatro axiomas ontológicos

| Axioma | Rol |
|--------|-----|
| **Vacío** | Condición de posibilidad; potencia no estructurada |
| **Unidad informativa** | Principio de individuación / singularidad |
| **Infinito** | Horizonte de diferenciación y multiplicidad |
| **Transformación** | Dinámica relacional; tránsito y disolución |

### Cinco perspectivas

| ID | Perspectiva | Tipo | Rol operativo |
|----|-------------|------|---------------|
| Ind | Individualidad | Posicional | Unidad / singularidad (→) |
| D | Dualidad | Posicional | Relación / tensión (0) |
| Tot | Totalidad | Posicional | Integración / sistema (←) |
| Evol | Evolución | Vectorial | Vacío → estructura (adv) |
| Invol | Involución | Vectorial | Estructura → vacío (ret) |

**Bóveda bancaria:** prohibido modificar los 78 nodos, `IOM/*.lean` o `ontology/io_shapes.ttl` durante la ingesta.

---

## 2. Reglas operativas formales

Solo dos conectores admisibles entre nodos canónicos **intra-tríada**:

### `mirrorOf` (simetría / isomorfismo)

1. Fases opuestas: `adv ↔ ret`.
2. Posición reflejada: `pos_tgt = 2 - pos_src` (0↔2, 1↔1, 2↔0).

### `creates` (generación / transición)

| Regla | Origen | Destino |
|-------|--------|---------|
| 1 | Lateral adv (`pos ∈ {0,2}`) | 0 ret (`pos = 1`) |
| 2 | 0 adv (`pos = 1`) | Laterales ret (`pos ∈ {0,2}`) |
| 3 | 0 ret (`pos = 1`) | Laterales adv (`pos ∈ {0,2}`) |
| 4 | Lateral ret (`pos ∈ {0,2}`) | 0 adv (`pos = 1`) |

Cualquier otro par → `none` (incluye cross-tríada e intra-fase).

**Garantías:** `lake build` (Lean 4, `isMirror` / `isCreates`) y `scripts/validate_shacl.py`.

Detalle: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md).

---

## 3. Protocolo de ingesta (6 pasos)

1. **Identificar** el fenómeno empírico.
2. **Asignar perspectiva** posicional (Ind / D / Tot).
3. **Determinar fase/vector** (adv–Evol o ret–Invol).
4. **Anclar** a un `mapped_node_id` de los 78 (`datasets/triad_nodes.csv`).
5. **Evaluar aristas** candidatas (`mirrorOf` / `creates` / `none`).
6. **Validar** con el script de ingesta.

```bash
python scripts/importar_datos_personalizados.py \
  --input datasets/ingestion/templates/<dominio>.csv \
  --output datasets/ingestion/aligned/<dominio>_aligned.csv
```

Columnas obligatorias: `external_id`, `external_label`, `mapped_node_id`.  
Opcionales: `perspective`, `phase`, `position`, `relation_candidate`, `notes`.

---

## 4. Catálogo de dominios ilustrativos

### 4.1 Cosmología náhuatl — Cinco Soles y Mictlán

Documento: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md).  
Plantilla: `datasets/ingestion/templates/cosmos_nahuatl.csv`.

| Concepto | Perspectiva | Relación candidata |
|----------|-------------|--------------------|
| Cada Sol (edad) | Ind / Tot | — |
| Cataclismo que cierra la edad | Invol | `creates` |
| Aparición del siguiente Sol | Evol | `creates` |
| Tezcatlipoca ↔ Quetzalcóatl | D | `mirrorOf` |
| Camino al Mictlán (9 niveles) | Invol | `creates` |
| Tlaltecuhtli | D + Invol | `mirrorOf` |
| *teyolia* → Mictlán | Ind → Tot | `creates` |

Fuentes de trabajo: Moreno de los Arcos; Luna López (2017); León-Portilla.

Catálogo general: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md).

---

## 5. Gobernanza y suite EXP-A a EXP-E

| Capa | Runner | Afirmación legítima | Límite |
|------|--------|---------------------|--------|
| **EXP-A** Validez semántica | `scripts/score_independent_eval.py` | Fleiss' κ = **0.6871** (n=14); interpretabilidad provisional | No prueba universal |
| **EXP-B** Formal | `lake build` | Solidez deductiva Lean 4 | No validez empírica |
| **EXP-C** Estructural | `scripts/validate_shacl.py` | Conformidad RDF/SHACL | No significado empírico |
| **EXP-D** Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperación de reglas autogeneradas | **Prohibido** como validez real |
| **EXP-E** Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | Alineación técnica sin romper axiomas | Requiere ciego propio para validez de campo |

### Evidencia EXP-A (resumen)

- κ = 0.6871 (moderado-sustancial); 10/14 unánimes.
- Desacuerdos: NC01, NC02, AM01, AM03 (conceptos nuevos y ambiguos).
- Módulo didáctico: [`MODULO_DIDACTICO_EVALUACION_CIEGA.md`](MODULO_DIDACTICO_EVALUACION_CIEGA.md).

### Pipeline de reproducción

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
