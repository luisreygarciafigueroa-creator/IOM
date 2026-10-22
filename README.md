# IOM — marco formal de 13 tríadas (autonomía verificable)

Arquitectura Lean 4 / OWL / SHACL: cinco perspectivas, relaciones `mirrorOf` / `creates`, 78 nodos.

**Manifiesto de sentido** (no requerido para ejecutar el pipeline):
[`MANIFIESTO.md`](MANIFIESTO.md) → [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)

## Verificación prioritaria

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/self_bootstrap.py --passes 2          # punto fijo idempotente
lake build                                                       # SelfGenesis + FormalRules
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py                   # + control negativo
.venv/bin/python experiments/domain_mapping/validate_examples.py # destino Mictlán
```

| Prioridad | Criterio | Runner |
|:---------:|----------|--------|
| 1 | Punto fijo estable ($S_{n+1}=S_n$) | `self_bootstrap.py --passes 2` |
| 2 | Invariancia no trivial (+ control negativo) | `measure_invariance.py` |
| 3 | Destino Mictlán expresable | EXP-E |
| 4 | Resonancia provisional (κ) | EXP-A — dato sobre el mundo, no fundamento |

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Núcleo formal

| Artefacto | Rol |
|-----------|-----|
| `data/iom_spec.json` | Spec tabular |
| `IOM/FormalRules.lean` | `isMirror` / `isCreates` |
| `IOM/SelfGenesis.lean` | Conteos derivados de la estructura |
| `IOM/Operators.lean` | `E` / `Ivo` (díada Evolución/Involución) |
| `scripts/self_bootstrap.py` | Regeneración idempotente |

## Documentación

| Documento | Audiencia |
|-----------|-----------|
| README (este) | Técnico / CI / evaluador |
| [`MANIFIESTO.md`](MANIFIESTO.md) | Sentido / carácter |
| [`EXPERIMENTOS.md`](EXPERIMENTOS.md) | Suite experimental |
| [`docs/`](docs/) | Especificación y dominio |
