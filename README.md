# IOM — construcción formal de la unidad informativa

IOM constituye un marco formal destinado a la **constitución y verificación de unidades informativas autocontenidas**. Su arquitectura se articula en torno a cinco perspectivas, trece tríadas y un par de relaciones de transformación —`mirrorOf` y `creates`— que permiten dar cuenta de la génesis, la conservación y la metamorfosis de la identidad informacional.

> **Definición canónica.** La unidad informativa es la mínima estructura autocontenida capaz de conservar una distinción, relacionarla con su opuesto, integrarla en un sistema y transformarse sin perder la trazabilidad de su identidad.

La **autonomía verificable** no es un atributo accesorio, sino el mecanismo por el cual la unidad se constituye, se conserva y se valida desde su propia estructura (`data/iom_spec.json`, Lean 4 y SHACL). En este sentido, el marco no depende de una semántica exterior como fundamento. Anotadores, dominios empíricos y métricas de recuperación de reglas pertenecen al orden del **encuentro**, no al del fundamento.

El desarrollo del horizonte de sentido se encuentra en el [`MANIFIESTO.md`](MANIFIESTO.md).

## Cadena operativa de constitución

```text
vacío informativo
→ distinción
→ relación
→ integración
→ transformación
→ unidad informativa autocontenida
```

| Perspectiva   | Función en la constitución de la unidad |
|---------------|-----------------------------------------|
| Individualidad | Conserva el elemento distinguible |
| Dualidad      | Registra la diferencia o la relación |
| Totalidad     | Integra los elementos en una estructura |
| Evolución     | Expande o proyecta la información |
| Involución    | Regresa, comprime o reorganiza la información |

Las trece tríadas no constituyen una mera taxonomía, sino **modos de composición** de la unidad informativa (setenta y ocho nodos).

## Verificación prioritaria del núcleo

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/self_bootstrap.py --passes 2   # S_{n+1}=S_n (CSV)
lake build                                                # SelfGenesis + FormalRules
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py            # + control negativo
```

Procedimientos opcionales (no bloquean la validez del repositorio):

```bash
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2
.venv/bin/python experiments/domain_mapping/validate_examples.py  # EXP-E: encuentro
.venv/bin/python experiments/optional/pi_hgat_t.py                 # diagnóstico circular
```

| Prioridad | Criterio                          | Runner |
|:---------:|-----------------------------------|--------|
| 1         | Punto fijo ($S_{n+1}=S_n$)        | `self_bootstrap.py --passes 2` |
| 1b        | Conteos derivados                 | `lake build` (SelfGenesis) |
| 2         | Invariancia no trivial            | `measure_invariance.py` |
| 3         | Destino Mictlán (encuentro)       | EXP-E — fuera del CI bloqueante |
| 4         | Resonancia κ (encuentro)          | EXP-A — requiere log de acceso |

Detalle: [`EXPERIMENTOS.md`](EXPERIMENTOS.md) · [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## Núcleo formal

| Artefacto                    | Rol |
|------------------------------|-----|
| `data/iom_spec.json`         | Spec tabular (`spec_version` 1.10.0) + propósito canónico |
| `IOM/FormalRules.lean`       | `isMirror` / `isCreates` |
| `IOM/SelfGenesis.lean`       | Conteos derivados de la estructura |
| `IOM/InformationalUnit.lean` | Núcleo mínimo: identidad, relación, trazabilidad |
| `scripts/self_bootstrap.py`  | Regeneración idempotente |

## Afirmación rigurosa

El repositorio **implementa una construcción formal de unidad informativa**. No afirma, por sí solo, una unidad informativa absoluta independiente del runtime (Python, Lean, sistema operativo). La validez interna se mide por derivabilidad y trazabilidad desde la especificación canónica. La autonomía formal no se confunde con una pretensión de validez empírica universal; permanece, en sentido estricto, como capacidad de originarse y sostenerse sin contenedor exterior.
