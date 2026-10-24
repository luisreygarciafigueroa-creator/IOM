# results/ — salidas opcionales (no versionadas)

| Propiedad | Valor |
|-----------|--------|
| ¿Fundamenta el punto fijo? | **No** |
| ¿Participa en CI core? | **No** |
| ¿Reproducible offline? | Solo tras regenerar CSV y ejecutar scripts opcionales |

**Generan contenido:**
- `python experiments/optional/pi_hgat_t.py`
- `python experiments/optional/baselines.py`
- `python scripts/generate_audit_report.py`

Los JSON de esta carpeta **no** se versionan. Accuracy 1.0 aquí es tautología informativa.
