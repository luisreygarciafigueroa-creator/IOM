# Reproducción de IOM

Cadena del **núcleo autónomo**: spec → punto fijo → Lean (SelfGenesis) → SHACL → invariancia.

Anotadores, dominios y PI-HGAT-T son **opcionales** (encuentro / diagnóstico).

## Entorno

- Python 3.12 · Lean 4.9.0 (`lean-toolchain`) · `requirements-lock.txt`

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
  | sh -s -- -y --default-toolchain leanprover/lean4:v4.9.0
export PATH="$HOME/.elan/bin:$PATH"
```

## Núcleo (obligatorio)

```bash
.venv/bin/python scripts/self_bootstrap.py --passes 2
lake build   # importa IOM/SelfGenesis.lean vía IOM.lean
.venv/bin/python scripts/validate_spec.py
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python scripts/measure_invariance.py
.venv/bin/python -m unittest discover -s tests -v
```

Conteos esperados **derivados del spec / SelfGenesis**, no de tablas doradas independientes:

- $13 \times 2 \times 3 = 78$ nodos
- $13 \times 6 = 78$ espejos dirigidos
- candidatos dirigidos $13 \times 6 \times 5 = 390$
- `creates` = suma sobre `creation_rules` × 13 tríadas (en spec actual: 104)

## Manifiesto (opcional)

```bash
.venv/bin/python scripts/create_manifest.py
git add MANIFEST.sha256 && git commit -m "chore: refresh MANIFEST"
.venv/bin/python scripts/self_bootstrap.py --with-manifest --passes 2
```

Excluidos del manifiesto: `MANIFEST.sha256`, `AUDITORIA_AUTO.md`, `ontology/io_ontology.ttl`.

## Opcional (no bloquea el núcleo)

```bash
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python experiments/baselines.py
.venv/bin/python experiments/domain_mapping/validate_examples.py
.venv/bin/python scripts/score_independent_eval.py \
  --annotations datasets/independent_eval/annotations.json
```

## Cinco perspectivas

Individualidad, Dualidad, Totalidad, Evolución, Involución — no «cuatro operadores» como eje del modelo.
