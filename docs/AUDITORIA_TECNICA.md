# Informe de evaluación técnica: validez semántica, coherencia formal y acuerdo inter-anotador del marco I.O.

> Documento de auditoría externa alineado al carácter del repositorio: **prueba de validez semántica en el mundo real**.  
> Spec de referencia: `data/iom_spec.json` · Metodología: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md) · Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)

---

## 1. Contexto y delimitación epistemológica del marco I.O.

El desarrollo de marcos ontológicos y sistemas de representación del conocimiento exige conciliar el rigor deductivo de la lógica formal con la capacidad demostrable para interpretar estructuras y fenómenos del mundo real. En este marco metodológico, el sistema I.O. se posiciona como un modelo analítico y formal cuya importancia estratégica radica en ofrecer un esquema interpretable y medible para la organización semántica. A diferencia de las ontologías de dominio tradicional orientadas exclusivamente al modelado de datos en entornos cerrados, el marco I.O. busca evaluar si sus categorías y relaciones operativas reflejan patrones semánticos consistentes cuando se aplican a conceptos del mundo real, actuando como un puente entre la formalización axiomática y la interpretación cognoscitiva humana.

### 1.1 Arquitectura semántica y principios fundamentales

La arquitectura del marco I.O. se sostiene conceptualmente sobre cuatro principios ontológicos de fundamento: vacío, unidad, infinito y transformación. A partir de estas bases, el sistema organiza el conocimiento mediante cinco perspectivas centrales: Individualidad, Dualidad, Totalidad, Evolución e Involución. Dichas perspectivas articulan la dinámica semántica en fases y 13 tríadas esenciales, interconectadas mediante relaciones operativas fundamentales, principalmente `mirrorOf` (que formaliza simetrías y correspondencias estructurales) y `creates` (que modela relaciones de generación, derivación y causalidad ontológica).

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

### 1.2 Delimitación metodológica y pregunta de investigación

Es indispensable delimitar el alcance metodológico del repositorio del marco I.O.: este no debe ser conceptualizado ni evaluado como un producto de software convencional ni como un mero experimento sintético autoprovechoso donde un algoritmo valida reglas generadas por el propio sistema. Por el contrario, su verdadero carácter radica en actuar como una **prueba y demostración** de si la estructura semántica abstracta del marco I.O. posee aplicabilidad interpretable, medible y consistente frente a conceptos y pares del mundo real.

Para guiar esta evaluación técnica, el marco responde formalmente a cuatro preguntas de investigación centrales:

1. **Evaluación de validez semántica externa:** ¿Pueden anotadores independientes, ciegos a las reglas axiomáticas internas del sistema, etiquetar relaciones semánticas sobre pares reales, nuevos y ambiguos de manera consistente y replicable?
2. **Coherencia formal interna:** ¿Es la estructura axiomática del marco internamente consistente, deductivamente sólida y libre de contradicciones lógicas?
3. **Diagnóstico de recuperación sintética:** ¿Las reglas generadas sintéticamente por el marco son recuperables mediante arquitecturas de aprendizaje profundo en grafos?
4. **Alineación empírica de dominios:** ¿Es posible cartografiar fenómenos de ciencias empíricas (como la cosmología náhuatl) hacia la estructura de 13 tríadas del marco I.O.?

## 2. Diferenciación modular de las capas del repositorio

Desde la perspectiva de la ingeniería de ontologías y la semántica formal, es metodológicamente imperativo deslindar las garantías lógicas internas de los diagnósticos sintéticos y las pruebas empíricas del mundo real. Confundir la consistencia matemática deducible dentro de un sistema axiomático con la validez semántica empírica representa un error categórico frecuente en la representación del conocimiento.

### 2.1 Desagregación sistemática de capas

| Capa | Componentes / archivos clave | Tipo de prueba / herramienta | Afirmación legítima |
|---|---|---|---|
| Validez semántica (mundo real) | `datasets/independent_eval/`, `scripts/score_independent_eval.py` | Evaluación a ciegas por anotadores independientes, Fleiss' κ | Demuestra interpretabilidad humana y acuerdo inter-anotador sobre conceptos externos al generador de reglas. |
| Formal | `IOM/FormalRules.lean`, `lean-toolchain`, `lakefile.lean` | Verificación de teoremas en Lean 4 (`lake build`) | Demuestra solidez deductiva y ausencia de contradicción axiomática en un asistente de pruebas. |
| Estructural | OWL/SHACL, CSV canónicos, `scripts/validate_shacl.py` | Validación SHACL y unittests | Garantiza la conformidad intencional y extensional (shape constraints) de los grafos RDF frente a la especificación. |
| Diagnóstico sintético | `experiments/pi_hgat_t.py`, `experiments/baselines.py` | Aprendizaje en grafos (PI-HGAT-T) y líneas base | Mide la capacidad de recuperación y completitud sintáctica de un modelo sobre reglas inyectadas previamente. |

### 2.2 Evaluación crítica: rigor formal vs. diagnósticos sintéticos

- **Rigor formal y estructural (Lean 4 y SHACL):** La formalización en Lean 4 demuestra la solidez deductiva y la no-contradicción axiomática de la ontología. SHACL impone restricciones de forma sobre los grafos RDF/OWL. La validez deductiva constituye únicamente un **prerrequisito** de consistencia interna; no prueba interpretabilidad empírica.
- **Diagnóstico sintético (PI-HGAT-T):** Evalúa la capacidad del modelo para recuperar tripletas sintéticas. Es un **diagnóstico interno** de recuperación de reglas; **no** demuestra validez semántica en el mundo real.

## 3. Análisis empírico de validez semántica y acuerdo inter-anotador

La validez semántica externa se somete a verificación mediante un protocolo de evaluación **ciego**. El objetivo es medir si evaluadores humanos independientes, sin adiestramiento previo sobre los axiomas internos, asignan de forma convergente las categorías y relaciones operativas a conceptos del mundo real.

### 3.1 Interpretación del coeficiente Fleiss' κ

Muestra: 14 pares en `datasets/independent_eval/`. Script: `scripts/score_independent_eval.py`.

| Métrica | Valor |
|---|---:|
| Fleiss' κ | **0.6871** |
| Nivel de acuerdo | Moderado a sustancial bajo protocolo ciego |
| Coincidencia unánime | 10/14 (71,4 %) |
| Alcance | Demostración **provisional** de interpretabilidad semántica |

Un κ de 0.6871 confirma que las definiciones operativas de las perspectivas y sus conectores (`mirrorOf`, `creates`) inducen clasificaciones humanas no aleatorias. El acuerdo unánime en el 71,4 % de la muestra evidencia la estabilidad de los controles estructurales en conceptos consolidados.

### 3.2 Diagnóstico cualitativo de desacuerdos

Desacuerdos concentrados en **NC01, NC02, AM01, AM03**:

- **Conceptos nuevos (NC01, NC02):** pruebas de estrés ante expansión de vocabulario; brechas epistémicas por terminología emergente.
- **Casos ambiguos (AM01, AM03):** solapamiento semántico entre perspectivas (p. ej. Dualidad vs Evolución); necesidad de reglas secundarias de desambiguación.

La localización de divergencias en pares con vaguedad léxica o solapamiento categorial valida la sensibilidad del diseño experimental: el núcleo es estable y se identifican con precisión los límites de la especificación actual.

## 4. Verificación del pipeline y alineación de dominios

### 4.1 Secuencia del pipeline de reproducción

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

### 4.2 Alineación a dominios empíricos

Documentada en [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) (cosmología náhuatl). Arquitectura documental de apoyo:

- [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)
- [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)
- [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md)
- [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · [`INTEGRACION_METODOLOGICA.md`](INTEGRACION_METODOLOGICA.md)
- `paper.md`, `EXPERIMENTOS.md`, `AUDITORIA.md`, `REPRODUCCION.md`

## 5. Dictamen evaluativo y conclusiones metodológicas

### 5.1 Balance de evidencia y alcance

**Pilares de fortaleza:**

1. Solidez deductiva formal (Lean 4).
2. Conformidad estructural rigurosa (SHACL + unittests).
3. Validez semántica empírica prometedora (κ = 0.6871; 71,4 % unanimidad en conceptos consolidados).

**Áreas de atención:**

1. Anclaje léxico de neologismos y conceptos nuevos (NC01, NC02).
2. Desambiguación fronteriza entre perspectivas ortogonales (AM01, AM03).

### 5.2 Recomendaciones para investigadores en ontología

1. Tratar κ = 0.6871 como demostración **provisional** de interpretabilidad, no como aval de validez universal.
2. Ampliar `datasets/independent_eval/` con más conceptos ambiguos y multidisciplinarios.
3. Interpretar PI-HGAT-T solo como prueba interna de recuperabilidad de reglas.
4. Basar extensiones en [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md) y [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
