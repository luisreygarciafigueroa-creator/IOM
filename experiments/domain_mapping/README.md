# Experimento EXP-E: alineación de dominios empíricos

Demostración operativa del protocolo descrito en:

- [`docs/PROTOCOLO_DE_MAPEO.md`](../../docs/PROTOCOLO_DE_MAPEO.md)
- [`docs/INTEGRACION_METODOLOGICA.md`](../../docs/INTEGRACION_METODOLOGICA.md)
- [`docs/CATALOGO_DOMINIOS.md`](../../docs/CATALOGO_DOMINIOS.md)

## Qué mide

| Mide | No mide |
|---|---|
| Que los nodos sugeridos existen en la bóveda de 78 nodos | Validez empírica de teorías biológicas o económicas |
| Que una relación propuesta es comparable al gold canónico | Fleiss' κ de dominio (requiere anotación ciega propia) |
| Trazabilidad del mapeo dominio → tríada | Validez universal del marco |

## Ejecución

```bash
python experiments/domain_mapping/validate_examples.py
```

Artefacto: `experiments/results/domain_mapping_validation.json`.

## Relación con otras capas experimentales

| ID | Capa | Runner |
|---|---|---|
| EXP-A | Validez semántica (mundo real) | `scripts/score_independent_eval.py` |
| EXP-B | Formal | `lake build` |
| EXP-C | Estructural | `scripts/validate_shacl.py` |
| EXP-D | Diagnóstico sintético | `experiments/pi_hgat_t.py` |
| **EXP-E** | Mapeo de dominios (demostración) | `experiments/domain_mapping/validate_examples.py` |

Registro completo: [`registry.json`](registry.json).
