# Experimentos del marco I.O. — autonomía funcional

> Manifiesto: [`MANIFIESTO.md`](MANIFIESTO.md) · Ensayo: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)  
> Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

El marco se auto-constituye. Lo externo es **encuentro**, no fundamento.

**Intérprete:** todos los comandos asumen el venv del repo (`.venv/bin/python` tras `python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt`).

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
.venv/bin/python scripts/self_bootstrap.py --passes 2
# tras una transición de árbol versionada:
.venv/bin/python scripts/create_manifest.py && git add MANIFEST.sha256 && git commit -m "chore: refresh MANIFEST"
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2
```

- **CSV**: derivados de `iom_spec.json`; dos pasadas idénticas.
- **`MANIFEST.sha256` no se hashea a sí mismo**; **`AUDITORIA_AUTO.md` está excluido** (timestamped).
- Con `--with-manifest`, la **cobertura es dura**: si faltan runners críticos en el manifiesto, el script **falla** (no solo advierte).

Propiedad: el punto fijo del manifiesto es **pariente del árbol versionado** (autogestión, no juez exterior).

---

## 3. Invariancia no trivial

```bash
.venv/bin/python scripts/measure_invariance.py
```

Control negativo: una arista `mirrorOf`→`none` debe bajar el rate.

---

## 4. Destino Mictlán (EXP-E)

```bash
.venv/bin/python experiments/domain_mapping/validate_examples.py
```

Fallos de anclaje si la díada E/Ivo está mal asignada en dominio.

---

## 5. Resonancia provisional (EXP-A)

κ ≈ 0.6871 (histórico). Instrumento: [`datasets/independent_eval/instrument/`](datasets/independent_eval/instrument/).

---

## 6. Pipeline interno

```bash
.venv/bin/python scripts/self_bootstrap.py --passes 2
lake build
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py
.venv/bin/python experiments/domain_mapping/validate_examples.py
```
