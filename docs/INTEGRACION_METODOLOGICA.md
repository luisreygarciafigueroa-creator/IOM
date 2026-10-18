# Propuesta de integración metodológica: mapeo de dominios empíricos al marco I.O.

> Guía operativa para alinear dominios empíricos (biología, economía, …) a las cinco perspectivas y 13 tríadas, sin confundir capas formales, estructurales y de validez semántica.  
> Catálogo: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) · Relaciones: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · Protocolo: [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md)

---

## 1. Fundamentos sistemáticos y arquitectura de cinco perspectivas

### 1.1 Contexto estratégico y estructura semántica multicapa

La arquitectura metodológica del marco I.O. traduce la complejidad de dominios empíricos heterogéneos —sistemas biológicos, fenómenos económicos— en estructuras semánticas medibles e interoperables. El compromiso epistémico central es **desacoplar** la deducción lógica interna de la validación cognitiva externa, evitando la autorreferencialidad (un sistema que convalida reglas generadas por sí mismo).

| Perspectiva | Función |
|---|---|
| **Individualidad** | Fronteras, identidad de objeto, propiedades intrínsecas |
| **Dualidad** | Simetría polar, reflejo topológico, oposiciones complementarias |
| **Totalidad** | Integración mereológica, colectividades de orden superior |
| **Evolución** | Progresión temporal, morfogénesis, complejización |
| **Involución** | Repliegue, estabilización por contracción, conservación de principios |

| Capa | Contenido | Afirmación legítima |
|---|---|---|
| Validez semántica (mundo real) | Pares independientes, anotación ciega, κ, mapeos de dominio | Interpretabilidad y acuerdo inter-anotador sobre conceptos externos |
| Formal | Lean 4.9.0 (`IOM/FormalRules.lean`) | Teoremas y coherencia axiomática |
| Estructural | OWL/SHACL, CSV canónicos | Conformidad sintáctica y shape constraints |
| Diagnóstico sintético | PI-HGAT-T, baselines | Recuperación de relaciones generadas por reglas |

OWL/SHACL garantizan conformidad sintáctica; Lean 4 prueba solidez matemática. Ambas son **prerrequisitos insuficientes** para reclamar validez empírica: esta queda supeditada a la prueba semántica ciega.

### 1.2 Operacionalización de relaciones y tríadas

Antes de ingerir datos empíricos, Lean 4 restringe el comportamiento de los constructos:

- **`mirrorOf`:** simetría estructural entre perspectivas/fases; no basta la semejanza temática; exige isomorfismo funcional (fase opuesta, posición reflejada).
- **`creates`:** generación orientada de estructuras o fases; direccionalidad asimétrica e irreflexiva; gobierna transiciones evolutivas e involutivas.
- **Fases y tríadas:** cada entidad empírica se posiciona en fase y en una de las 13 tríadas; las relaciones solo son válidas si respetan restricciones de fase.

---

## 2. Protocolo de alineación para dominios empíricos complejos

### 2.1 Mapeo sistemático a las tríadas

Procedimiento ([`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md), [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md)):

1. Aislar el observable e identificar límites fenoménicos.
2. Clasificar por perspectiva dominante.
3. Ubicar en fase y tríada canónica.
4. Instanciar `mirrorOf` o `creates` según reglas formales.
5. Serializar en CSV y validar SHACL / `importar_datos_personalizados.py`.

| Dominio | Ejemplo de entidades | Perspectiva / fase | Relación | Impacto analítico |
|---|---|---|---|---|
| Biología | Replicación de ADN → transcripción de ARNm | Individualidad / Evolución | `creates` | Formaliza direccionalidad del flujo informacional |
| Biología | Diferenciación celular ↔ mantenimiento de pluripotencia | Evolución / Involución | `mirrorOf` | Reflejo entre especialización y estado germinal |
| Economía | Restricciones de liquidez ↔ solvencia sistémica | Dualidad / Totalidad | `mirrorOf` | Isomorfismo entre tensión individual y riesgo macro |
| Economía | Descubrimiento de precios → libro de órdenes | Evolución / Totalidad | `creates` | Emergencia causal del precio de equilibrio |

### 2.2 Delimitación epistemológica del mapeo

Fundamento: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md), [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) (vacío, unidad, infinito, transformación).

1. Lean 4 demuestra consistencia interna, **no** veracidad empírica automática.
2. Prohibido asignar `creates`/`mirrorOf` por semejanza discursiva.
3. Evolución/Involución deben respetar fronteras de unidad y vacío.
4. La idoneidad semántica del mapeo se valida solo con acuerdo inter-anotador independiente.

---

## 3. Validación semántica empírica y control de calidad

### 3.1 Protocolo ciego

Metodología: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md). Datos: `datasets/independent_eval/`.

| Métrica | Valor | Decisión ontológica |
|---|---:|---|
| Fleiss' κ | **0.6871** | Preservar arquitectura de perspectivas |
| Unanimidad | 10/14 | Congelar definiciones de tríadas involucradas en controles |
| Desacuerdos | 4/14 (NC01, NC02, AM01, AM03) | Análisis de frontera y casos ambiguos |

### 3.2 Diagnóstico de desacuerdos

- **NC (conceptos nuevos):** tensionan límites de las tríadas; refinar notas de alcance o expandir subsunción.
- **AM (ambiguos):** solapamiento entre perspectivas; reglas de desempatado más estrictas en [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

**Contraste:** PI-HGAT-T mide recuperación de reglas sintéticas; κ mide interpretabilidad humana no guiada. Solo κ constituye prueba de validez en el mundo real.

---

## 4. Pipeline operativo, verificación formal y auditoría

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
.venv/bin/python scripts/generate_audit_report.py
```

Este flujo vincula la comprobación sintáctica en CI/CD con la verificación lógica de los teoremas formales y con el eje central del repositorio: la **prueba de validez semántica en el mundo real**.
