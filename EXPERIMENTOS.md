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
# tras una transición de árbol que se decide versionar:
python scripts/create_manifest.py && git add MANIFEST.sha256 && git commit
python scripts/self_bootstrap.py --with-manifest --passes 2
```

- **CSV** (triad_nodes, vector_steps, relation_candidates): derivados solo de `iom_spec.json`; dos pasadas idénticas.
- **`MANIFEST.sha256` no se hashea a sí mismo** (`create_manifest.py` lo excluye) — no hay hash auto-referente.

### Propiedad (no limitación)

El punto fijo del manifiesto es **pariente del árbol versionado**: el estado $S$ incluye el git tree. La iteración es estable *dentro de un árbol dado*; los cambios de árbol requieren re-versionado explícito. Eso es **autogestión**, no dependencia de un juez exterior: el sistema que se crea a sí mismo también decide cuándo su nueva versión es él mismo.

---

## 3. Invariancia no trivial

```bash
python scripts/measure_invariance.py
```

| Chequeo | Esperado |
|---------|----------|
| Auto-regeneración canónica | rate = 1.0 |
| Invariancia bajo índice de tríada | true |
| Reconstrucción desde 12 tríadas | true |
| **Control negativo** (`mirrorOf`→`none`) | rate < 1.0 |

---

## 4. Destino Mictlán (EXP-E) — predicción falsable

```bash
python experiments/domain_mapping/validate_examples.py
```

Si la díada Evolución/Involución estuviera mal asignada en los pares de dominio, el validador reportaría fallos de anclaje (`aligned` falso, arista `none` indebida, o violación de misma tríada).

---

## 5. Resonancia provisional (EXP-A)

κ ≈ 0.6871: registro del **encuentro** con el mundo compartido. No fundamenta el marco.

Protocolo: anotadores **sin** leer `MANIFIESTO.md` ni este documento antes de anotar (ceguera de sentido preservada).

---

## 6. Pipeline

```bash
python scripts/self_bootstrap.py --passes 2
lake build
python scripts/validate_shacl.py
python scripts/measure_invariance.py
python experiments/domain_mapping/validate_examples.py
```
