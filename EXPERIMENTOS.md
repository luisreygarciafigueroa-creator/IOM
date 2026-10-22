# Experimentos del marco I.O. — autonomía funcional

> Manifiesto: [`MANIFIESTO.md`](MANIFIESTO.md) · Ensayo: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)  
> Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

El marco se auto-constituye. Lo externo es **encuentro**, no fundamento.

---

## 1. Jerarquía

| Prioridad | Capa | Runner | Afirmación legítima |
|:---------:|------|--------|---------------------|
| **1** | Punto fijo idempotente | `self_bootstrap.py --passes 2` | $S_{n+1}=S_n$ sobre CSV derivados |
| **1b** | Lean SelfGenesis | `lake build` | Conteos derivados de la estructura |
| **2** | Invariancia **no trivial** | `measure_invariance.py` | Canónico = 1.0; corrupción detectada |
| **3** | Destino Mictlán | EXP-E | Sendero expresable; predicción falsable |
| **4** | Resonancia provisional | EXP-A | κ = dato sobre el mundo, no fundamento |

---

## 2. Punto fijo (CSV y manifiesto)

```bash
python scripts/self_bootstrap.py --passes 2
python scripts/create_manifest.py && git add MANIFEST.sha256 && git commit   # si el árbol cambió
python scripts/self_bootstrap.py --with-manifest --passes 2
```

`MANIFEST.sha256` **no** se hashea a sí mismo. El punto fijo del manifiesto es
**pariente del árbol versionado**: autogestión, no juez exterior.

---

## 3. Invariancia no trivial

```bash
python scripts/measure_invariance.py
```

Control negativo obligatorio: una arista corrupta debe bajar el rate.

---

## 4. Destino Mictlán (EXP-E) — predicción falsable

```bash
python experiments/domain_mapping/validate_examples.py
```

Fallos de anclaje si la díada E/Ivo está mal asignada en dominio.

---

## 5. Resonancia provisional (EXP-A)

κ ≈ 0.6871 (histórico): registro del **encuentro**, no fundamento.

La ceguera es un **estado del anotador**, no del repo público. Rondas nuevas:

1. Entregar solo [`datasets/independent_eval/instrument/`](datasets/independent_eval/instrument/) (`INSTRUCTIONS.md` + `pairs.csv`), **sin** clon del repo.
2. Rellenar el **log de acceso** (`ACCESS_LOG.template.json`): cuándo se entregó qué; exposición previa al manifiesto/README.
3. Excluir del κ primario a quien declare o documente haber leído el marco antes de anotar.

El κ solo vale si el otro fue genuinamente libre de no ver lo que el marco esperaba.

---

## 6. Pipeline interno

```bash
python scripts/self_bootstrap.py --passes 2
lake build
python scripts/validate_shacl.py
python scripts/measure_invariance.py
python experiments/domain_mapping/validate_examples.py
```
