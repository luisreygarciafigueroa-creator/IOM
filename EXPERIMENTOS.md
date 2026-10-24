# Experimentos del marco I.O. — autonomía funcional

> Manifiesto: [`MANIFIESTO.md`](MANIFIESTO.md) · Ensayo: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)

El marco se auto-constituye. Lo externo es **encuentro**, no fundamento.

**Intérprete:** `.venv/bin/python` tras instalar `requirements-lock.txt`.

---

## 1. Jerarquía

| Prioridad | Capa | Runner | ¿Bloquea «repo válido»? |
|:---------:|------|--------|:-----------------------:|
| **1** | Punto fijo | `self_bootstrap.py --passes 2` | sí |
| **1b** | SelfGenesis | `lake build` | sí |
| **2** | Invariancia no trivial | `measure_invariance.py` | sí |
| **3** | Destino Mictlán | EXP-E | **no** (encuentro) |
| **4** | Resonancia κ | EXP-A | **no** (requiere ACCESS_LOG) |

---

## 2. Punto fijo

```bash
.venv/bin/python scripts/self_bootstrap.py --passes 2
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2  # tras versionar MANIFEST
```

`io_ontology.ttl` no entra en el manifiesto (serialización no determinista). `AUDITORIA_AUTO.md` y `experiments/results/` no se versionan: son derivados de encuentro.

---

## 3. Invariancia no trivial

```bash
.venv/bin/python scripts/measure_invariance.py
```

Control negativo obligatorio.

---

## 4. EXP-E (opcional)

```bash
.venv/bin/python experiments/domain_mapping/validate_examples.py
```

Un fallo de anclaje de dominio **no** invalida el núcleo formal.

---

## 5. EXP-A (opcional; κ no cerrado sin log)

Instrumento: `datasets/independent_eval/instrument/`.

Un κ histórico (~0.6871) **no** se presenta como demostración completada mientras no exista `ACCESS_LOG` de exposición previa. `rule_reference.json` es post-hoc; no se entrega al anotador.

---

## 6. Diagnóstico circular (opcional)

PI-HGAT-T / baselines (`experiments/optional/`): recuperan la regla embebida en (fase, pos). No son criterio primario.

```bash
.venv/bin/python experiments/optional/pi_hgat_t.py
.venv/bin/python experiments/optional/baselines.py
```
