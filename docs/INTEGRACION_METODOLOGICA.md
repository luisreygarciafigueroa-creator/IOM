# Propuesta de integración metodológica: mapeo de dominios al marco I.O.

> Guía operativa para alinear dominios (cosmología náhuatl y otros) a las cinco perspectivas y trece tríadas, sin confundir capas formales, estructurales y de encuentro.  
> Bajo el carácter de **autonomía absoluta**, la prueba primaria **no** es la anotación ciega inter-anotador.  
> Catálogo: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) · Relaciones: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · Protocolo: [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md)

---

## 1. Fundamentos sistemáticos y arquitectura de cinco perspectivas

### 1.1 Contexto estratégico y estructura semántica multicapa

La arquitectura metodológica del marco I.O. traduce la complejidad de dominios heterogéneos —cosmogonías náhuatl y otros— en estructuras semánticas medibles e interoperables. El compromiso epistémico central es **desacoplar** la deducción lógica interna de la dependencia de un contenedor de consenso exterior, evitando tanto la autorreferencialidad vacía como la legitimación por panel de observadores separados.

| Perspectiva | Función |
|---|---|
| **Individualidad** | Fronteras, identidad de objeto, propiedades intrínsecas |
| **Dualidad** | Simetría polar, reflejo topológico, oposiciones complementarias |
| **Totalidad** | Integración mereológica, colectividades de orden superior |
| **Evolución** | Progresión temporal, morfogénesis, complejización |
| **Involución** | Repliegue, estabilización por contracción, conservación de principios |

| Capa | Contenido | Afirmación legítima |
|---|---|---|
| Autonomía formal | Lean 4 (`IOM/FormalRules.lean`) | Teoremas y coherencia axiomática sin autoridad exterior |
| Estructural | OWL/SHACL, CSV canónicos | Conformidad sintáctica y shape constraints |
| Cartografía del tránsito | Mapeos de dominio, EXP-E | Expresabilidad en trece tríadas |
| Diagnóstico sintético | PI-HGAT-T, baselines | Recuperación de relaciones generadas por reglas |
| Residuo inter-anotador | Pares independientes, κ | Archivo histórico; **no** fundamento |

OWL/SHACL garantizan conformidad sintáctica; Lean 4 prueba solidez matemática. Bajo el carácter actual, estas capas **bastan** para sostener la autonomía formal. El residuo inter-anotador no se promociona a prueba de validez del marco.

### 1.2 Operacionalización de relaciones y tríadas

Antes de ingerir datos, Lean 4 restringe el comportamiento de los constructos:

- **`mirrorOf`:** simetría estructural entre perspectivas/fases; no basta la semejanza temática; exige isomorfismo funcional (fase opuesta, posición reflejada).
- **`creates`:** generación orientada de estructuras o fases; direccionalidad asimétrica e irreflexiva; gobierna transiciones evolutivas e involutivas.
- **Fases y tríadas:** cada entidad se posiciona en fase y en una de las trece tríadas; las relaciones solo son válidas si respetan restricciones de fase.

---

## 2. Protocolo de alineación para dominios complejos

### 2.1 Mapeo sistemático a las tríadas

Procedimiento ([`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md), [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md)):

1. Aislar el observable e identificar límites fenoménicos.
2. Clasificar por perspectiva dominante.
3. Ubicar en fase y tríada canónica.
4. Instanciar `mirrorOf` o `creates` según reglas formales.
5. Serializar en CSV y validar SHACL / `importar_datos_personalizados.py`.

| Dominio | Ejemplo de entidades | Perspectiva / fase | Relación | Impacto analítico |
|---|---|---|---|---|
| Cosmología náhuatl | Tezcatlipoca ↔ Quetzalcóatl | Dualidad | `mirrorOf` | Reflejo de fuerzas cósmicas polares |
| Cosmología náhuatl | Vida ↔ muerte | Dualidad | `mirrorOf` | Dicotomía mesoamericana |
| Cosmología náhuatl | Sol de fuego → Sol de agua | Involución | `creates` | Transición entre edades / cataclismo |
| Cosmología náhuatl | Camino al Mictlán → Mictlán | Involución | `creates` | Retorno al vacío |

### 2.2 Delimitación epistemológica del mapeo

Fundamento: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md), [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) (vacío, unidad, infinito, transformación).

1. Lean 4 demuestra consistencia interna, **no** veracidad empírica automática.
2. Prohibido asignar `creates`/`mirrorOf` por semejanza discursiva.
3. Evolución/Involución deben respetar fronteras de unidad y vacío.
4. La admisión de un mapeo es estructural; no se exige panel ciego para legitimarlo.

---

## 3. Residuo inter-anotador y control de calidad

### 3.1 Protocolo ciego (archivo, no eje)

Metodología: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md). Datos: `datasets/independent_eval/`.

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo *dentro del residuo* |
| Unanimidad | 10/14 | Controles estructurales estables |
| Desacuerdos | 4/14 (NC01, NC02, AM01, AM03) | Fronteras del vocabulario compartido residual |

### 3.2 Diagnóstico de desacuerdos

- **NC (conceptos nuevos):** tensionan límites de las tríadas; refinar notas de alcance o expandir subsunción.
- **AM (ambiguos):** solapamiento entre perspectivas; reglas de desempatado más estrictas en [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

**Contraste:** PI-HGAT-T mide recuperación de reglas sintéticas; κ mide interpretabilidad humana no guiada. Ninguno de los dos **funda** el marco bajo el carácter de autonomía absoluta.

---

## 4. Pipeline operativo, verificación formal y auditoría

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python experiments/domain_mapping/validate_examples.py
.venv/bin/python experiments/pi_hgat_t.py   # opcional
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json  # residuo opcional
.venv/bin/python scripts/generate_audit_report.py
```

Este flujo vincula la comprobación sintáctica en CI/CD con la verificación lógica de los teoremas formales y con el eje central del repositorio: la **autonomía formal** y la cartografía del tránsito hacia la no-dependencia de contenedor exterior.
