# Ingesta guiada de dominios externos

Esta carpeta permite a investigadores de otras disciplinas **alinear conceptos nuevos** a la ontología canónica de 78 nodos **sin modificar** `data/iom_spec.json`, Lean, RDF/OWL ni SHACL.

## Estructura

```
datasets/ingestion/
├── README.md                 ← este archivo
├── templates/
│   ├── plantilla_dominio.csv                 ← plantilla vacía
│   ├── biologia_depredador_presa.csv         ← ejemplo biología
│   └── economia_transaccion_riesgo.csv       ← ejemplo economía
└── aligned/                  ← salida del script (generada)
```

## Flujo rápido

1. Copia una plantilla o crea tu CSV con las columnas:
   - `external_id` (obligatorio)
   - `external_label` (obligatorio)
   - `mapped_node_id` (uno de los 78 de `datasets/triad_nodes.csv`)
   - `perspective`, `phase`, `position`, `relation_candidate`, `notes` (opcionales)

2. Ejecuta el script de validación y alineación:

```bash
python scripts/importar_datos_personalizados.py \
    --input datasets/ingestion/templates/biologia_depredador_presa.csv \
    --output datasets/ingestion/aligned/biologia_aligned.csv
```

3. Revisa el informe JSON generado junto al CSV alineado. Solo se aceptan mapeos a nodos existentes.

## Documentación de mapeo por dominio

Consulta el catálogo completo con ejemplos de biología, economía y otras disciplinas:

→ [`docs/CATALOGO_DOMINIOS.md`](../../docs/CATALOGO_DOMINIOS.md)

## Reglas de oro

- La ontología core es **inmutable** (bóveda bancaria).
- Los datos externos viven solo en `datasets/ingestion/`.
- Las relaciones candidatas se validan contra las mismas reglas `mirrorOf` / `creates` documentadas en [`docs/RELACIONES_OPERATIVAS.md`](../../docs/RELACIONES_OPERATIVAS.md).
