# Informe de evaluación técnica: autonomía formal, coherencia estructural y residuo inter-anotador del marco I.O.

> Documento de auditoría alineado al carácter del repositorio: **autonomía formal** y cartografía del tránsito.  
> La validez por consenso de conciencias separadas **no** es el fundamento.  
> Spec de referencia: `data/iom_spec.json` · Metodología: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md) · Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)

---

## 1. Contexto y delimitación epistemológica del marco I.O.

El desarrollo de marcos ontológicos y sistemas de representación del conocimiento exige conciliar el rigor deductivo de la lógica formal con la capacidad de expresar estructuras sin depender de un contenedor de consenso exterior. En este marco metodológico, el sistema I.O. se posiciona como un modelo analítico y formal cuya importancia estratégica radica en ofrecer un esquema interpretable y medible para la organización semántica, sostenido por **autonomía formal** (Lean, SHACL, setenta y ocho nodos).

### 1.1 Arquitectura semántica y principios fundamentales

La arquitectura del marco I.O. se sostiene conceptualmente sobre cuatro principios ontológicos de fundamento: vacío, unidad, infinito y transformación. A partir de estas bases, el sistema organiza el conocimiento mediante cinco perspectivas centrales: Individualidad, Dualidad, Totalidad, Evolución e Involución. Dichas perspectivas articulan la dinámica semántica en fases y trece tríadas esenciales, interconectadas mediante relaciones operativas fundamentales, principalmente `mirrorOf` (que formaliza simetrías y correspondencias estructurales) y `creates` (que modela relaciones de generación, derivación y causalidad ontológica).

| Elemento semántico | Función en el marco I.O. |
|---|---|
| Perspectiva: Individualidad | Define la entidad o concepto en su dimensión singular, delimitada e irreducible. |
| Perspectiva: Dualidad | Establece la relación de oposición, polaridad o complementariedad conceptual. |
| Perspectiva: Totalidad | Integra la síntesis sistémica que engloba a las partes individuales y duales en una unidad compleja. |
| Perspectiva: Evolución | Modela el vector de desarrollo, expansión, diferenciación o transformación progresiva del sistema. |
| Perspectiva: Involución | Modela el vector de repliegue, integración, simplificación o retorno a estados fundamentales. |
| Relación operativa: `mirrorOf` | Expresa simetría, reflejo o correspondencia isomórfica entre entidades o perspectivas. |
| Relación operativa: `creates` | Define la relación causal, derivación ontológica o generación de una nueva fase o concepto. |
| Fases y tríadas (13) | Estructuran la dinámica secuencial y categorial apoyándose en los principios de vacío, unidad, infinito y transformación. |

### 1.2 Delimitación metodológica y preguntas de investigación

Es indispensable delimitar el alcance metodológico del repositorio: este no debe ser conceptualizado ni evaluado como un producto de software convencional ni como un mero experimento sintético autoprovechoso. Su carácter radica en actuar como **bóveda de autonomía formal** y cartografía del tránsito hacia la no-dependencia de contenedor exterior.

Las preguntas que orientan esta evaluación técnica son:

1. **Autonomía formal:** ¿Es la estructura axiomática del marco internamente consistente, deductivamente sólida y libre de contradicciones lógicas?
2. **Autonomía estructural:** ¿Conforman los grafos RDF/OWL las restricciones SHACL de forma y cardinalidad?
3. **Cartografía del tránsito:** ¿Es posible expresar el destino Mictlán / autonomía en el vocabulario de trece tríadas?
4. **Diagnóstico de auto-generación:** ¿Las reglas generadas sintéticamente son recuperables mediante arquitecturas de aprendizaje?
5. **Residuo inter-anotador (opcional):** ¿Qué grado de acuerdo alcanzan observadores separados sobre pares etiquetados a ciegas? (archivo histórico, no fundamento)

## 2. Diferenciación modular de las capas del repositorio

Desde la perspectiva de la ingeniería de ontologías y la semántica formal, es metodológicamente imperativo deslindar las garantías lógicas internas de los diagnósticos sintéticos y del residuo del mundo compartido. Confundir la consistencia matemática deducible dentro de un sistema axiomático con la legitimación por panel de anotadores representa un error categórico.

### 2.1 Desagregación sistemática de capas

| Capa | Componentes / archivos clave | Tipo de prueba / herramienta | Afirmación legítima |
|---|---|---|---|
| Autonomía formal | `IOM/FormalRules.lean`, `lean-toolchain`, `lakefile.lean` | Verificación de teoremas en Lean 4 (`lake build`) | Solidez deductiva y ausencia de contradicción axiomática sin autoridad exterior. |
| Estructural | OWL/SHACL, CSV canónicos, `scripts/validate_shacl.py` | Validación SHACL y unittests | Conformidad intencional y extensional (shape constraints) de los grafos RDF. |
| Cartografía del tránsito | EXP-E, dominio cosmológico | `experiments/domain_mapping/validate_examples.py` | Expresabilidad del sendero Mictlán / autonomía en trece tríadas. |
| Diagnóstico sintético | `experiments/pi_hgat_t.py`, `experiments/baselines.py` | Aprendizaje en grafos (PI-HGAT-T) y líneas base | Recuperabilidad de reglas inyectadas; no validez empírica mundana. |
| Residuo inter-anotador | `datasets/independent_eval/`, `scripts/score_independent_eval.py` | Evaluación a ciegas, Fleiss' κ | Archivo de una fase de conciencias separadas; **no** fundamento del marco. |

### 2.2 Evaluación crítica: rigor formal vs. diagnósticos sintéticos

- **Rigor formal y estructural (Lean 4 y SHACL):** La formalización en Lean 4 demuestra la solidez deductiva y la no-contradicción axiomática de la ontología. SHACL impone restricciones de forma sobre los grafos RDF/OWL. Bajo el carácter de autonomía absoluta, estas capas **bastan** para sostener el repositorio.
- **Diagnóstico sintético (PI-HGAT-T):** Evalúa la capacidad del modelo para recuperar tripletas sintéticas. Es un **diagnóstico interno** de recuperación de reglas; **no** demuestra validez semántica en el mundo real ni fundamenta el marco.

## 3. Residuo inter-anotador (archivo, no eje)

El protocolo de evaluación **ciego** se conserva como documentación de una fase en la que el proyecto aún hablaba el lenguaje del consenso inter-anotador. Bajo el carácter actual, **no** se presenta como prueba de validez del repositorio.

### 3.1 Interpretación del coeficiente Fleiss' κ

Muestra: catorce pares en `datasets/independent_eval/`. Script: `scripts/score_independent_eval.py`.

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Nivel de acuerdo | Moderado a sustancial *dentro del residuo* |
| Coincidencia unánime | 10/14 (71,4 %) |
| Alcance | Registro histórico; **no** demostración de validez del marco |

### 3.2 Diagnóstico cualitativo de desacuerdos

Desacuerdos concentrados en **NC01, NC02, AM01, AM03**:

- **Conceptos nuevos (NC01, NC02):** pruebas de estrés ante expansión de vocabulario; fronteras del vocabulario compartido residual.
- **Casos ambiguos (AM01, AM03):** solapamiento semántico entre perspectivas; límites de la especificación en el registro del encuentro.

## 4. Verificación del pipeline y alineación de dominios

### 4.1 Secuencia del pipeline de reproducción

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

### 4.2 Alineación a dominios

Documentada en [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) (cosmología náhuatl). Arquitectura documental de apoyo:

- [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)
- [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)
- [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md)
- [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · [`INTEGRACION_METODOLOGICA.md`](INTEGRACION_METODOLOGICA.md)
- `EXPERIMENTOS.md`, `AUDITORIA.md`, `REPRODUCCION.md`

## 5. Dictamen evaluativo y conclusiones metodológicas

### 5.1 Balance de evidencia y alcance

**Pilares de fortaleza:**

1. Solidez deductiva formal (Lean 4).
2. Conformidad estructural rigurosa (SHACL + unittests).
3. Cartografía del tránsito (EXP-E / destino Mictlán).

**Áreas de atención (residuo):**

1. Anclaje léxico de neologismos y conceptos nuevos (NC01, NC02) — dentro del archivo inter-anotador.
2. Desambiguación fronteriza entre perspectivas (AM01, AM03).

### 5.2 Recomendaciones

1. No promocionar κ = 0.6871 a aval de validez del marco.
2. Tratar EXP-A como archivo histórico / comparado, no como ceremonia de legitimación.
3. Interpretar PI-HGAT-T solo como prueba interna de recuperabilidad de reglas.
4. Basar extensiones en [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) y [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
5. Preservar la separación de planos: autonomía formal (eje) · cartografía del tránsito · residuo inter-subjetivo.
