# Autonomía formal y capas de verificación (no «validez por consenso»)

Este documento **no** define el repositorio como prueba de validez semántica en un mundo compartido por conciencias separadas. Ese modo de legitimación es exactamente el que el ensayo canónico declara **superable**.

Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) · Ensayo: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)

---

## Principio rector

> El marco se sostiene por **auto-coherencia** (bóveda Lean / SHACL / 78 nodos), no por el acuerdo de observadores externos.
> Un panel de anotadores separados reproduce el «mundo real» provisional del ensayo; **no** lo fundamenta.

| Fuente | Rol bajo autonomía absoluta |
|--------|-----------------------------|
| `data/iom_spec.json` + CSV + ontología | **Arquitectura autónoma** bajo prueba de coherencia interna |
| Lean / SHACL | **Autonomía formal** — no pide permiso a un consenso exterior |
| PI-HGAT-T / baselines | Auto-recuperabilidad de reglas *del propio sistema* |
| `datasets/independent_eval/` | **Residuo** de la fase de conciencias separadas (documentado, no fundante) |
| Cartografía de dominios | Ejercicio del tránsito; no certificado de «mundo real» |

---

## Qué se establece y qué no

| Se establece | No se establece |
|--------------|-----------------|
| Coherencia deductiva y de forma del sistema de 13 tríadas | Que el marco «describe la realidad» por acuerdo inter-subjetivo |
| Que las reglas son recuperables desde sí mismas (diagnóstico interno) | Que κ ≈ 0.69 **funda** la validez del proyecto |
| Que el sendero Mictlán / autonomía es cartografiable en el vocabulario formal | Cobertura empírica de todos los dominios por paneles externos |
| Que el requisito del sistema puede ser la abolición de requisitos impuestos | Verdad ontológica universal por consenso |

---

## Jerarquía de afirmaciones (reordenada)

| Prioridad | Afirmación legítima | Artefacto |
|:---------:|---------------------|-----------|
| **1** | Autonomía formal (coherencia sin contenedor exterior) | Lean, SHACL, CSV, `iom_spec.json` |
| **2** | Cartografía del tránsito (Mictlán / autonomía) | EXP-E, dominio cosmológico, ensayo |
| **3** | Auto-generación recuperable de reglas | PI-HGAT-T, baselines |
| **4** | Residuo documentado del mundo compartido | `independent_eval`, κ (opcional) |

La prioridad 4 **no** se promociona a «prueba de validez del marco».

---

## Sobre el protocolo ciego (EXP-A)

El protocolo y las anotaciones se **conservan como archivo** de una fase en la que el proyecto aún hablaba el lenguaje del consenso inter-anotador. Bajo el carácter actual:

- κ no es el eje del repositorio.
- No se reclama «validez semántica en el mundo real» a partir de ellos.
- Quien los ejecute lo hace como **ejercicio histórico / comparado**, no como ceremonia de legitimación.

---

## Pipeline prioritario

```bash
# 1) Autonomía formal (eje)
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py

# 2) Cartografía del tránsito
python experiments/domain_mapping/validate_examples.py

# 3) Diagnóstico de auto-generación (opcional)
python experiments/pi_hgat_t.py
python experiments/baselines.py
python scripts/audit_perfect_metrics.py

# 4) Residuo del mundo compartido (opcional, no fundante)
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

---

## Referencias

- Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md)
- Ensayo: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)
