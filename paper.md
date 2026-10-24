# IOM — formalismo auto-fundamentado y encuentros provisionales

Este informe describe el repositorio IOM como un **sistema que se auto-constituye** desde `data/iom_spec.json` y se verifica por punto fijo, Lean y SHACL. Anotadores, dominios externos y learners de recuperación de reglas son **encuentro** con el mundo compartido, **no** el fundamento del marco.

Referencia conceptual: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Spec: [`data/iom_spec.json`](data/iom_spec.json) · Jerarquía: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Núcleo (fundamento)

1. Punto fijo: `self_bootstrap.py --passes 2`
2. SelfGenesis / FormalRules: `lake build`
3. SHACL sobre TTL regenerado
4. Invariancia no trivial (`measure_invariance.py`)

## Encuentro (no fundamenta)

EXP-E (dominio / Mictlán) y EXP-A (κ) son proyección provisional. Sin `ACCESS_LOG`, κ histórico no se declara demostración cerrada.

## Diagnóstico circular (opcional)

PI-HGAT-T y baselines MLP/reglas (`experiments/optional/`) recuperan etiquetas que **ya están** en (fase, posición). Accuracy 1.0 es tautología informativa, no validez del marco en el mundo. PyTorch no es dependencia del núcleo autónomo.
