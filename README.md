# IOM — construcción formal de la unidad informativa

IOM es un marco formal para **construir y verificar unidades informativas
autocontenidas** mediante cinco perspectivas, trece tríadas y relaciones de
transformación (`mirrorOf` / `creates`).

> **Unidad informativa:** mínima estructura autocontenida capaz de conservar una
> distinción, relacionarla con su opuesto, integrarla en un sistema y
> transformarse sin perder la trazabilidad de su identidad.

La **autonomía verificable** es el *mecanismo* que permite constituir, conservar
y validar esa unidad desde su propia estructura (`data/iom_spec.json` + Lean +
SHACL), sin depender de una semántica externa como fundamento. Anotadores,
dominios y métricas de recuperación de reglas son **encuentro**, no fundamento.

**Manifiesto de sentido** (no requerido para el pipeline): [`MANIFIESTO.md`](MANIFIESTO.md)

## Cadena operativa

```text
vacío informativo
→ distinción
→ relación
→ integración
→ transformación
→ unidad informativa autocontenida
```

| Perspectiva | Función en la unidad informativa |
|-------------|----------------------------------|
| Individualidad | Conserva el elemento distinguible |
| Dualidad | Registra la diferencia o relación |
| Totalidad | Integra los elementos en una estructura |
| Evolución | Expande o proyecta la información |
| Involución | Regresa, comprime o reorganiza la información |

Las 13 tríadas son **modos de composición** de la unidad informativa (78 nodos).

## Verificación prioritaria (núcleo)

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
| `data/iom_spec.json` | Spec tabular (`spec_version` 1.9.0) + propósito canónico |
| `IOM/FormalRules.lean` | `isMirror` / `isCreates` |
| `IOM/SelfGenesis.lean` | Conteos derivados de la estructura |
| `IOM/InformationalUnit.lean` | Núcleo mínimo: identidad, relación, trazabilidad |
| `scripts/self_bootstrap.py` | Regeneración idempotente |

## Afirmación rigurosa

El repositorio **implementa una construcción formal de unidad informativa**.
No afirma, por sí solo, una unidad informativa absoluta independiente del
runtime (Python, Lean, SO). La validez interna se mide por derivabilidad y
trazabilidad desde la especificación canónica.
