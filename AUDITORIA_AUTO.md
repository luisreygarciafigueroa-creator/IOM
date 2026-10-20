# Auditoría automática IOM

**Generado:** 2026-10-20T12:26:38.660342+00:00
**Commit:** `064de84` (`064de843b097cd30551da704210c82debc4041e6`)
**Rama:** `main`
**spec_version:** 1.8.0
**schema_version:** 1.1.0

## Hashes SHA-256 de artefactos de datos

| Archivo | SHA-256 |
|---|---|
| `data/iom_spec.json` | `acc28fa6a0d1cb6deb8d4ddd066c7e9d7c4a7410d1db631dfe77febbdeac84f9` |
| `data/iom_spec.schema.json` | `175b0b0966536c653b728de3d06f3988d9f6e05f72a288d9586fbc0a32341662` |
| `datasets/triad_nodes.csv` | `671542bd75b282143475847b65a0fd40be8e995c6afefb70f691518ea225d1b6` |
| `datasets/relation_candidates.csv` | `d1f68f147b658ac5e02cb851642e6b66a68789c074fab57eb496f50c265204cf` |
| `datasets/vector_steps.csv` | `3f0ea42710f9ab5b20e042ad5bd3c5dda2c6f9c64682348314ea7e2a6868601b` |
| `ontology/io_ontology.ttl` | `38b0775f53960900f04e036c3ccec890ccbb9107c2b990e77133103fb8130505` |
| `ontology/io_shapes.ttl` | `6a2cf8cd9da638130b26dcd3e77179c133036e0b36fd340d45ab6838075ca957` |
| `requirements-lock.txt` | `73593871a75c2a4f71f827a31b86281fc6aaa6d40891263588b97baf8df4e915` |
| `experiments/config.json` | `5d284eb9c04c386a90b6e835483bcaf36acf84469b52559891c1bb73d27d15a6` |

## Entorno

- Python: 3.12.3
- Platform: Linux-6.18.38+-x86_64-with-glibc2.39

## Métricas primarias PI-HGAT-T

- **candidate_relation_accuracy**: 1.0
- **relation_macro_f1**: 1.0
- **mirrorOf_precision**: 1.0
- **mirrorOf_recall**: 1.0
- **mirrorOf_f1**: 1.0
- **creates_precision**: 1.0
- **creates_recall**: 1.0
- **creates_f1**: 1.0
- **predicted_edge_rule_conformance**: 1.0

## Resumen de baselines

- **deterministic_rules**: accuracy=1.0, macro_f1=1.0
- **logistic_regression**: accuracy=0.533333, macro_f1=0.242424
- **mlp_no_graph**: accuracy=1.0, macro_f1=1.0

## Estado del working tree

```
(limpio)
```

---
Generado por `scripts/generate_audit_report.py`.
