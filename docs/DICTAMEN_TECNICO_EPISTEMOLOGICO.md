# Dictamen de auditoría técnica y epistemológica: evaluación integral del marco ontológico I.O.

> Dictamen sobre madurez técnica, formal y semántica del repositorio.  
> Objeto: **prueba y demostración de validez semántica en el mundo real** — no producto de software ni validación sintética autorreferencial.

---

## 1. Delimitación

Se audita si la estructura del marco (cinco perspectivas; `mirrorOf`/`creates`; 13 tríadas) es interpretable, medible y repetible por observadores humanos independientes.

## 2. Capas y experimentos

| Capa | Afirmación legítima | Experimento |
|---|---|---|
| Validez semántica (mundo real) | Interpretabilidad sobre conceptos externos | EXP-A, EXP-E |
| Formal | Teoremas en el sistema formal | EXP-B |
| Estructural | Conformidad con la especificación | EXP-C |
| Diagnóstico sintético | Recuperación de relaciones *generadas por reglas* | EXP-D |

EXP-D es autoconsistencia circular: **no** evidencia de validez semántica real.

## 3. Resultados

| Fuente | Hallazgo |
|---|---|
| EXP-A | κ = **0.6871**; 10/14 unánimes; desacuerdos NC01, NC02, AM01, AM03 |
| EXP-E | 8 pares bio/econ anclados al gold canónico |

**Demostración provisional.** No prueba universal.

## 4. Lean 4 y SHACL

Condición necesaria e insuficiente. Coherencia formal ≠ relevancia empírica.

## 5. Dictamen y hoja de ruta

**Conclusión:** madurez técnica notable; limitación = escala muestral (14 + 8 pares).

1. Ampliar EXP-A (pares y anotadores).
2. Protocolizar guías NC/AM.
3. Extender EXP-E a más disciplinas.
4. **Prohibir** usar PI-HGAT-T como prueba de validez ontológica.

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
