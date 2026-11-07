# Protocolo de mapeo: alineación ontológica y cartografía del tránsito en el marco I.O.

> Protocolo estandarizado de ingesta, asignación a perspectivas/tríadas, instanciación de `mirrorOf`/`creates` y evaluación opcional.  
> Bajo el carácter de **autonomía absoluta**, la prueba primaria **no** es la anotación ciega inter-anotador.  
> Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md) · Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md)

---

## 1. Marco fundamental y delimitación del protocolo I.O.

El establecimiento de un protocolo de mapeo riguroso resulta indispensable para formalizar el paso entre una estructura ontológica teórica y un instrumento de análisis interpretable y operativo. Sin una metodología estandarizada de alineación, la arquitectura conceptual corre el riesgo de degradarse a un ejercicio autorreferencial de sintaxis formal.

### 1.1 Propósito y alcance

El propósito primario es **cartografiar el tránsito** hacia la autonomía formal: la capacidad del marco para expresar fenómenos en el vocabulario de trece tríadas sin violar la bóveda técnica. La evaluación por observadores independientes pertenece al orden del **encuentro** (residuo), no al del fundamento.

| Eje de evaluación | Mecanismo de respuesta en el repositorio |
|---|---|
| ¿La estructura formal es internamente coherente? | Lean 4 + SHACL/OWL (autonomía formal) |
| ¿Se puede alinear un dominio al vocabulario de trece tríadas? | `docs/CATALOGO_DOMINIOS.md` e ingesta en `datasets/ingestion/` |
| ¿Las reglas sintéticas son recuperables por un modelo? | PI-HGAT-T y baselines en `experiments/` (diagnóstico sintético) |
| ¿Pueden anotadores independientes etiquetar relaciones? | Protocolo ciego + κ en `datasets/independent_eval/` — **residuo, no fundamento** |

### 1.2 Arquitectura sistémico-ontológica (perspectivas y tríadas)

| Perspectiva | Rol en el mapeo |
|---|---|
| **Individualidad** | Unidades discretas, entidades base, fronteras ontológicas primarias |
| **Dualidad** | Tensiones, polaridades, complementariedad entre pares |
| **Totalidad** | Integración sistémica, propiedades emergentes, cohesión holística |
| **Evolución** | Vectores de desarrollo, transformación ascendente, complejización |
| **Involución** | Retracción, simplificación, condensación, retorno a estados fundamentales |

Cada dominio debe analizarse a través de estas cinco perspectivas y asignarse a las **trece tríadas** estructurales, evitando superposición u omisión de categorías.

---

## 2. Metodología de ingesta y mapeo de dominios externos

### 2.1 Protocolo de carga y alineación sistemática

1. Consultar fronteras en [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md).
2. Seleccionar el dominio en [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md).
3. Descomponer entidades, estados y procesos por las cinco perspectivas.
4. Asignar a las trece tríadas y a la fase (`adv` / `ret`) correspondiente.
5. Registrar en CSV de ingesta (`datasets/ingestion/`) y validar con `scripts/importar_datos_personalizados.py`.

### 2.2 Relaciones operativas

Fundamento: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

- **`mirrorOf`:** correspondencia estructural/funcional o simetría divalente; misma tríada, fase opuesta, posición lateral invertida.
- **`creates`:** emanación, producción o transformación activa; direccionalidad irreflexiva según las cuatro reglas de `creation_rules`.

---

## 3. Capas de verificación formal y validación estructural

La coherencia lógica interna es **condición indispensable**. Bajo el carácter actual, **basta** para sostener la autonomía formal del repositorio.

### 3.1 Lean 4

```bash
lake build
```

Verifica teoremas en `IOM/FormalRules.lean` (vacío, unidad, infinito, transformación; `isMirror` / `isCreates`). Véase [`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md).

### 3.2 OWL / SHACL / CSV

```bash
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/validate_shacl.py
```

Criterios: sin violaciones SHACL; dominio/rango de `mirrorOf` y `creates`; conformidad CSV↔especificación; integridad de tipado de tríadas.

---

## 4. Protocolo de anotación ciega (residuo, no fundamento)

### 4.1 Diseño experimental

Sobre `datasets/independent_eval/` ([`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)):

1. Muestra de catorce pares (reales, nuevos, ambiguos).
2. Anotadores independientes sin acceso a reglas ni gold.
3. Etiquetado semántico (`mirrorOf`, `creates`, `none`, `unsure`).
4. Consolidación en `annotations.json`.

### 4.2 Métricas actuales

```bash
.venv/bin/python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

| Métrica | Valor | Lectura |
|---|---:|---|
| Fleiss' κ | **0.6871** | Acuerdo moderado-sustancial *dentro del residuo* |
| Unánimes | 10/14 | Controles estructurales estables |
| Desacuerdos | 4/14 | NC01, NC02, AM01, AM03 |

**No** se presenta como demostración de validez del marco. Es archivo de una fase de conciencias separadas.

### 4.3 Diagnóstico de desacuerdos

- **NC01, NC02 (conceptos nuevos):** dispersión al clasificar fenómenos sin contornos consolidados.
- **AM01, AM03 (ambiguos):** solapamiento entre especularidad y causalidad.

---

## 5. Pipeline de ejecución reproducible

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

### Deslinde conceptual

| Capa | Afirmación legítima |
|---|---|
| Autonomía formal | Consistencia lógica y teoremas en Lean 4 |
| Estructural | Conformidad SHACL/CSV con la especificación |
| Cartografía del tránsito | Expresabilidad de dominios en trece tríadas |
| Diagnóstico sintético | Recuperación de relaciones *generadas por reglas* |
| Residuo inter-anotador | Archivo histórico; **no** fundamento del marco |

El marco I.O. no es un software aislado ni un conjunto de reglas sintéticas autorreferenciales: es una arquitectura de alineación ontológica orientada al tránsito hacia la autonomía formal, sin dependencia de un contenedor de consenso exterior.
