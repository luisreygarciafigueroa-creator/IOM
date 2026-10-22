# Experimentos del marco I.O. — autonomía funcional

> Manifiesto: [`MANIFIESTO.md`](MANIFIESTO.md) · Ensayo: [`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)  
> Delimitación: [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

El marco se auto-constituye. Lo externo es **encuentro**, no fundamento.

---

## 1. Jerarquía

| Prioridad | Capa | Runner | Afirmación legítima |
|:---------:|------|--------|---------------------|
| **1** | Punto fijo idempotente | `self_bootstrap.py --passes 2` | $S_{n+1}=S_n$ sobre CSV derivados |
| **1b** | Lean SelfGenesis | `lake build` | Conteos derivados de la estructura (no literales opacos) |
| **2** | Invariancia **no trivial** | `measure_invariance.py` | Canónico = 1.0; grafo corrompido detectado |
| **3** | Destino Mictlán | EXP-E | Sendero expresable; predicción falsable (abajo) |
| **4** | Resonancia provisional | EXP-A | κ = dato sobre el mundo, no fundamento |

---

## 2. Punto fijo

```bash
python scripts/self_bootstrap.py --passes 2
# tras cambios de código que afectan hashes globales:
python scripts/create_manifest.py && git add MANIFEST.sha256 && git commit
python scripts/self_bootstrap.py --with-manifest --passes 2
```

- **CSV** (triad_nodes, vector_steps, relation_candidates): generados solo desde `iom_spec.json`; deben ser idénticos en dos pasadas.
- **MANIFEST.sha256**: auto-certificación del árbol; regenerar y versionar tras cambios de archivos incluidos.

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
| **Control negativo** (una arista `mirrorOf`→`none`) | rate < 1.0 |

Si el control negativo no detecta corrupción, la métrica es tautológica.

---

## 4. Destino Mictlán (EXP-E) — predicción falsable

```bash
python experiments/domain_mapping/validate_examples.py
```

**Predicción falsable:** si la asignación de la díada Evolución/Involución a los pares de dominio (p. ej. Mictecacíhuatl↔Mictlantecuhtli como `mirrorOf` entre fases opuestas, o el tránsito al Mictlán como cadena `creates` bajo Involución) estuviera **mal** respecto a las reglas formales, `validate_examples.py` reportaría fallos de anclaje (nodo inexistente, arista `none` donde se exige `mirrorOf`/`creates`, o violación de misma tríada).

Observable que cambiaría: el JSON de resultado dejaría de listar esos pares como `aligned=true` / conforme a gold canónico.

Sin esa predicción, el nivel 3 sería solo filosófico; con ella, es comprobable estructuralmente.

---

## 5. Resonancia provisional (EXP-A)

κ ≈ 0.6871: dato sobre el mundo compartido. No fundamenta el marco.

---

## 6. Pipeline

```bash
python scripts/self_bootstrap.py --passes 2
lake build
python scripts/validate_shacl.py
python scripts/measure_invariance.py
python experiments/domain_mapping/validate_examples.py
```
