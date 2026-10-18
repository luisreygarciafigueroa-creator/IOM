# Dictamen Técnico sobre la Validez Semántica, Consistencia Formal y Rigor Metodológico del Marco I.O.

> Auditoría de infraestructura semántica, consistencia lógica y metodología de verificación.
> Objeto: **demostración provisional de validez semántica en el mundo real** — no producto comercial ni marco autorreferencial sintético.

---

## 1. Objeto, Alcance y Delimitación

El marco formaliza dinamismos relacionales mediante cinco perspectivas (Individualidad, Dualidad, Totalidad, Evolución, Involución) y conectores `mirrorOf` / `creates` indexados por fases.

Delimitación operacional ([`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)):

- **Demostración provisional** bajo protocolo ciego, no prueba universal.
- **No** es producto de software comercial.
- **Separación estricta** entre diagnóstico sintético y validez semántica empírica.
- Mapeo empírico acotado (8 pares bio/econ; 14 pares en evaluación ciega).
- Módulos pedagógicos (`experiments/learning/`) **excluidos** de las métricas de validez.

---

## 2. Consistencia Formal y Estructural

| Capa | Mecanismo | Función |
|---|---|---|
| Axiomática | Lean 4 (`IOM.lean`, `lake build`) | Prueba de teoremas e invariantes ([`PREMISAS_Y_TEOREMAS.md`](PREMISAS_Y_TEOREMAS.md)) |
| Estructural | SHACL (`scripts/validate_shacl.py`) | Restricciones de forma, cardinalidad y enlaces `mirrorOf`/`creates` |

La no-contradicción lógica es **prerrequisito** de toda validación empírica; no la sustituye.

---

## 3. Validez Semántica Empírica (EXP-A)

```bash
python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json
```

| Resultado | Valor |
|---|---:|
| Fleiss' κ | **0.6871** (moderado-sustancial, n=14) |
| Consenso unánime | 10/14 |
| Desacuerdos | NC01, NC02, AM01, AM03 |

Los desacuerdos se localizan en conceptos nuevos y ambiguos: delimitan fronteras de precisión sin comprometer el núcleo estructural.

---

## 4. Auditoría de la Suite EXP-A a EXP-E

| ID | Capa | Runner | Propósito epistemológico |
|---|---|---|---|
| **EXP-A** | Validez semántica empírica | `scripts/score_independent_eval.py` | Interpretabilidad ciega + Fleiss' κ |
| **EXP-B** | Formal | `lake build` | No-contradicción en Lean 4 |
| **EXP-C** | Estructural | `scripts/validate_shacl.py` | Conformidad RDF/SHACL |
| **EXP-D** | Diagnóstico sintético | `experiments/pi_hgat_t.py` | Recuperabilidad de reglas autogeneradas — **no** validez real |
| **EXP-E** | Mapeo de dominios | `experiments/domain_mapping/validate_examples.py` | 8 pares bio/econ → 13 tríadas |

**Advertencia:** usar solo PI-HGAT-T (EXP-D) como prueba de validez implica circularidad epistemológica. La validez sustantiva reside en EXP-A y, de forma acotada, en EXP-E.

Detalle de EXP-D: [`EXPERIMENTOS.md`](../EXPERIMENTOS.md).

---

## 5. Dictamen y Condicionantes

1. **Solidez formal:** Lean 4 + SHACL garantizan ausencia de contradicciones lógicas y de forma en las cinco perspectivas y conectores.
2. **Reproducibilidad:** pipeline de extremo a extremo auditable (sección 6).
3. **Aplicabilidad empírica provisional:** κ = 0.6871 y alineación EXP-E demuestran interpretabilidad no arbitraria en la muestra evaluada — no omnicomprensión ontológica.

### Recomendaciones

1. Preservar el cerco entre diagnóstico sintético y validez empírica en toda publicación.
2. Formalizar criterios de asignación para nodos NC/AM.
3. Ampliar EXP-E hacia nuevos dominios ([`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md), [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md)).
4. Toda modificación ontológica debe pasar `lake build` y `validate_shacl.py` antes de evaluación empírica.

---

## 6. Pipeline de reproducción

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
