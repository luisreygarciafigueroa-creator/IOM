# Auditoría automática IOM

**Generado:** 2026-10-08T21:40:57.708728+00:00
**Commit:** ver historial de `main`
**Rama:** `main`
**spec_version:** 1.1.0
**schema_version:** 1.0.0

## Hashes SHA-256 de artefactos de datos

Regenerar con:

```bash
python scripts/generate_audit_report.py
```

El informe actualizado se escribe en `experiments/results/audit_report.json` y sobrescribe este archivo.

## Entorno

- Python 3.12+
- Platform: Linux (CI: Ubuntu 24.04)

## Métricas primarias PI-HGAT-T

- **candidate_relation_accuracy**: 1.0
- **relation_macro_f1**: 1.0
- **mirrorOf_f1**: 1.0
- **creates_f1**: 1.0
- **predicted_edge_rule_conformance**: 1.0

---
Generado por `scripts/generate_audit_report.py`.
