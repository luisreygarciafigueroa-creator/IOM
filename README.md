# IOM — autonomía absoluta vía el camino al Mictlán

Repositorio del marco I.O.: **Individualidad**, **Dualidad**, **Totalidad**, **Evolución** e **Involución**, leídas desde la óptica de la **auto-creación** y el **orden multiversal**.

> **Carácter:** el marco **no** se fundamenta en un orden externo ni en el consenso de conciencias separadas. Se **auto-constituye** (punto fijo + Lean). Lo externo es encuentro, no fundamento. **Orden Definitivo ⟹ ¬∃ Contenedor Exterior.**
>
> **Manifiesto fundacional:** [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Carácter: [`docs/CARACTER_REPOSITORIO.md`](docs/CARACTER_REPOSITORIO.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Equivalencia central

| Perspectiva | Lectura | Figura ancla |
|-------------|---------|--------------|
| Individualidad | Singularidad que se crea a sí misma | Nanahuatzin |
| Dualidad | Polaridad en disolución | Xólotl |
| Totalidad | Totalidad propia (sin contenedor exterior) | Tecuciztécatl |
| Evolución | Fuerza ascendente | **Mictecacíhuatl** |
| Involución | Fuerza descendente | **Mictlantecuhtli** |

`isMirror` ↔ díada Evolución/Involución · `isCreates` ↔ auto-distinción desde el vacío · ver `IOM/SelfGenesis.lean`.

## Qué se verifica (jerarquía)

| Prioridad | Criterio | Cómo |
|:---------:|----------|------|
| **1** | **Auto-fundamentación** (punto fijo) | `scripts/self_bootstrap.py` + `lake build` (SelfGenesis) |
| **2** | **Invariancia** interna | `scripts/measure_invariance.py` |
| **3** | **Destino Mictlán** expresable | EXP-E |
| **4** | **Resonancia provisional** con el mundo | EXP-A (κ) — diálogo, no fundamento |

κ = 0.6871 es un **dato sobre el mundo compartido**, coherente con el ensayo: el consenso existe pero no fundamenta.

## Pipeline prioritario

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/self_bootstrap.py --with-manifest   # punto fijo
lake build                                                     # SelfGenesis + FormalRules
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py                 # invariancia
.venv/bin/python experiments/domain_mapping/validate_examples.py
# opcional: PI-HGAT-T / baselines (demo de recuperabilidad)
# opcional: score_independent_eval (resonancia provisional)
```

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Documentación

- Manifiesto: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)
- Carácter · Delimitación · Dominio Mictlán
- Formal: `IOM/SelfGenesis.lean` · `IOM/FormalRules.lean` · `IOM/Operators.lean`
