# IOM — formalismo auto-fundamentado y encuentros provisionales

Este informe describe el repositorio IOM como un **sistema que se auto-constituye** desde `data/iom_spec.json` y se verifica por punto fijo, Lean y SHACL. Anotadores, dominios externos y learners de recuperación de reglas son **encuentro** con el mundo compartido, **no** el fundamento del marco.

Referencia conceptual: [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt) · Spec: [`data/iom_spec.json`](data/iom_spec.json) · Jerarquía: [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

## Jerarquía (lo que el marco exige)

| Prioridad | Capa | Qué afirma |
|:---------:|------|------------|
| 1 | Punto fijo + SelfGenesis | $S_{n+1}=S_n$; conteos derivados |
| 2 | Invariancia no trivial | Regeneración de relaciones + control negativo |
| 3 | Destino Mictlán (EXP-E) | Expresabilidad en dominio; **no** tumba el núcleo |
| 4 | Resonancia (EXP-A) | κ como dato de encuentro **si** hay log de acceso |

## Núcleo autónomo

- Spec → CSV/ontología → `self_bootstrap.py --passes 2`
- Lean: `FormalRules`, `SelfGenesis` (sin `sorry`)
- SHACL sobre el grafo regenerado
- `measure_invariance.py` (canónico 1.0; grafo corrompido detectado)

## Diagnóstico sintético (no es fundamento)

PI-HGAT-T y baselines MLP/reglas recuperan etiquetas que **ya están** en (fase, posición). Accuracy 1.0 es tautología informativa, no validez del marco en el mundo. PyTorch no es dependencia del núcleo autónomo.

## Resonancia inter-subjetiva (EXP-A)

Un κ histórico (~0.6871) se publicó sin **ACCESS_LOG** de exposición previa. Bajo el protocolo actual, **no** se presenta como demostración cerrada. Rondas nuevas: instrumento en `datasets/independent_eval/instrument/` + log de acceso.

## Especificación categorial

Trece tríadas × dos fases × tres posiciones = 78 nodos; aristas `creates` y espejos según reglas del spec. Identidad de tríada por **etiquetas**, no por índice móvil entre migraciones.
