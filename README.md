# IOM — marco formal de 13 tríadas (autonomía verificable)

Arquitectura Lean 4 / OWL / SHACL: cinco perspectivas, `mirrorOf` / `creates`, 78 nodos.

**Manifiesto de sentido** (no requerido para el pipeline): [`MANIFIESTO.md`](MANIFIESTO.md)

## Criterio del marco

El sistema se sostiene en el **punto fijo de su especificación**. Anotadores, dominios y métricas de recuperación de reglas son **encuentro**, no fundamento.

## Verificación prioritaria (núcleo autónomo)

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/self_bootstrap.py --passes 2   # S_{n+1}=S_n (CSV)
lake build                                                # SelfGenesis + FormalRules
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py            # + control negativo
```

Opcional (no bloquean «repo válido»):

```bash
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2
.venv/bin/python experiments/domain_mapping/validate_examples.py  # EXP-E: encuentro
.venv/bin/python experiments/optional/pi_hgat_t.py                 # diagnóstico circular
```

| Prioridad | Criterio | Runner |
|:---------:|----------|--------|
| 1 | Punto fijo ($S_{n+1}=S_n$) | `self_bootstrap.py --passes 2` |
| 1b | Conteos derivados | `lake build` (SelfGenesis) |
| 2 | Invariancia no trivial | `measure_invariance.py` |
| 3 | Destino Mictlán (encuentro) | EXP-E — **fuera del CI bloqueante** |
| 4 | Resonancia κ (encuentro) | EXP-A — requiere log de acceso |

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Núcleo formal

| Artefacto | Rol |
|-----------|-----|
| `data/iom_spec.json` | Spec tabular (`spec_version` 1.9.0) |
| `IOM/FormalRules.lean` | `isMirror` / `isCreates` |
| `IOM/SelfGenesis.lean` | Conteos derivados de la estructura |
| `scripts/self_bootstrap.py` | Regeneración idempotente |
