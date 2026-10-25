# IOM — construcción formal de la unidad informativa

Este informe describe el repositorio IOM como una **construcción formal de
unidad informativa**: estructura autocontenida de distinciones, relaciones,
integración y transformación, verificable desde `data/iom_spec.json` (punto
fijo, Lean, SHACL). La autonomía verificable es el *mecanismo* de constitución
y validación; anotadores, dominios y learners de recuperación de reglas son
**encuentro**, no fundamento.

Referencia conceptual: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Spec: [`data/iom_spec.json`](data/iom_spec.json) · Jerarquía: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Propósito

La unidad informativa es la mínima estructura autocontenida capaz de conservar una distinción, relacionarla con su opuesto, integrarla en un sistema y transformarse sin perder la trazabilidad de su identidad.

Las 13 tríadas son modos de composición de esa unidad.

## Núcleo (fundamento)

1. Punto fijo: `self_bootstrap.py --passes 2`
2. SelfGenesis / FormalRules / InformationalUnit: `lake build`
3. SHACL sobre TTL regenerado
4. Invariancia no trivial (`measure_invariance.py`)

## Encuentro (no fundamenta)

EXP-E (dominio / Mictlán) y EXP-A (κ) son proyección provisional. Sin
`ACCESS_LOG`, κ histórico no se declara demostración cerrada.

## Diagnóstico circular (opcional)

PI-HGAT-T y baselines (`experiments/optional/`) recuperan etiquetas que **ya
están** en (fase, posición). Accuracy 1.0 es tautología informativa, no validez
del marco en el mundo. PyTorch no es dependencia del núcleo.

## Límite de la afirmación

El repositorio **implementa** una construcción formal de unidad informativa.
No afirma por sí solo una unidad absoluta independiente del entorno de
ejecución. La validez interna se mide por derivabilidad y trazabilidad desde
la especificación canónica.
