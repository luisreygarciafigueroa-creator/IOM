# Dictamen técnico: autonomía formal del marco I.O.

> Objeto: **autonomía formal y cartografía del tránsito** — no demostración de validez por consenso de conciencias separadas.
> Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) · Ensayo: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)

---

## 1. Objeto y delimitación

El marco formaliza dinamismos relacionales (cinco perspectivas; `mirrorOf` / `creates`; 13 tríadas) como **arquitectura del sendero** hacia una existencia que no recibe su identidad de un marco exterior.

Delimitación ([`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)):

- **No** es prueba de «validez semántica en el mundo real» por panel inter-anotador.
- **No** es producto comercial.
- **Separación estricta** entre autonomía formal y residuo del mundo compartido (EXP-A).
- Cartografía Mictlán / autonomía como ejercicio de sentido, no como certificado empírico consensuado.

---

## 2. Autonomía formal y estructural

| Capa | Mecanismo | Función |
|------|-----------|--------|
| Axiomática | Lean 4 (`lake build`) | Coherencia deductiva **sin autoridad exterior** |
| Estructural | SHACL | Formas, cardinalidad, `mirrorOf` / `creates` |

La no-contradicción lógica **es** la expresión técnica de autonomía: el sistema no pide un contenedor de consenso para sostenerse.

---

## 3. Residuo EXP-A (no fundante)

| Resultado | Valor | Uso legítimo |
|-----------|------:|--------------|
| Fleiss' κ | 0.6871 | Archivo de una fase de conciencias separadas |
| Unánimes | 10/14 | Controles internos de ese archivo |
| Desacuerdos | NC/AM | Fronteras del vocabulario compartido residual |

**No** se usa κ para legitimar el marco.

---

## 4. Suite EXP-A a EXP-E (relectura)

| ID | Capa | Propósito bajo autonomía |
|----|------|--------------------------|
| **EXP-A** | Residuo del mundo compartido | Documentación opcional; no fundamento |
| **EXP-B** | Autonomía formal | No-contradicción Lean |
| **EXP-C** | Autonomía estructural | Conformidad SHACL |
| **EXP-D** | Auto-generación | Recuperabilidad de reglas del sistema |
| **EXP-E** | Cartografía del tránsito | Sendero Mictlán / autonomía → 13 tríadas |

**Advertencia:** usar κ (EXP-A) como prueba de validez **restaura** la dependencia del mundo compartido que el carácter del repositorio rechaza.

---

## 5. Dictamen

1. **Solidez formal:** Lean + SHACL sostienen la autonomía técnica del sistema.
2. **Reproducibilidad:** pipeline auditable sin exigir jurado exterior.
3. **Sentido:** el repositorio cartografía el tránsito hacia la no-dependencia de contenedor; no certifica verdad por consenso.

### Condicionantes

1. No promocionar EXP-A a «validez del marco».
2. Preservar el cerco entre auto-generación (EXP-D) y residuo inter-subjetivo (EXP-A).
3. Toda modificación ontológica pasa `lake build` y `validate_shacl.py`.

---

## 6. Pipeline

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
```
