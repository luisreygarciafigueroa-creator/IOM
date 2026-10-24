# Experimentos opcionales (diagnóstico / encuentro)

**No** forman parte del núcleo autónomo ni del CI bloqueante.

| Script | Rol | Salida |
|--------|-----|--------|
| `pi_hgat_t.py` | Diagnóstico circular (recupera reglas embebidas) | `experiments/results/` |
| `baselines.py` | Baselines sin grafo | `experiments/results/` |

```bash
.venv/bin/python experiments/optional/pi_hgat_t.py
.venv/bin/python experiments/optional/baselines.py
```

Workflow: `.github/workflows/encuentro.yml` (manual).
Tests: `tests/optional/` (no corren en CI core).
