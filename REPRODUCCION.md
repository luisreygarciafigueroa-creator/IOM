# Reproducción

**Intérprete:** `.venv/bin/python` tras `pip install -r requirements-lock.txt`.

## Núcleo (bloquea validez)

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/self_bootstrap.py --passes 2
lake build
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py
```

Manifiesto (tras cambios de árbol):

```bash
.venv/bin/python scripts/create_manifest.py
git add MANIFEST.sha256 && git commit -m "chore: refresh MANIFEST"
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2
```

Excluidos del manifiesto: `MANIFEST.sha256`, `AUDITORIA_AUTO.md`, `ontology/io_ontology.ttl`.

## Opcional (no bloquea el núcleo)

```bash
.venv/bin/python experiments/optional/pi_hgat_t.py
.venv/bin/python experiments/optional/baselines.py
.venv/bin/python experiments/domain_mapping/validate_examples.py
.venv/bin/python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json
```

## Cinco perspectivas

Individualidad, Dualidad, Totalidad, Evolución, Involución — no «cuatro operadores» como eje del modelo.
