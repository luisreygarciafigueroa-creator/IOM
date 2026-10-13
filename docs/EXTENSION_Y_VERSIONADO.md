# Extender el marco y versionar releases

## Añade un dominio en 15 minutos

1. **Elige mapeos** (3 min): revisa `docs/CATALOGO_DOMINIOS.md` y asigna cada concepto a un ID existente de `datasets/triad_nodes.csv`; la ingesta no altera reglas core.
2. **Crea CSV** (4 min): copia `datasets/ingestion/templates/biologia_depredador_presa.csv`; conserva `external_id`, `external_label`, `mapped_node_id`; `perspective`, `phase`, `position` son opcionales y se cotejan con el nodo canónico.
3. **Alinea** (2 min):
   ```bash
   python scripts/importar_datos_personalizados.py \
     --input datasets/ingestion/templates/biologia_depredador_presa.csv \
     --output /tmp/biologia_aligned.csv --report /tmp/biologia_report.json
   ```
4. **Interpreta** (3 min): el ejemplo tiene 6 filas; se espera `rows_processed: 6`, `error_count: 0`, `warning_count: 0`, `ok_count: 6`; cada fila de salida debe tener `status: "ok"` y completar los campos `canonical_*`.
5. **Revisa** (3 min): usa `--strict` si quieres elevar warnings a errores; si hay mapeo inválido, corrige `mapped_node_id` contra los 78 IDs canónicos. No confundas `relation_candidate` aportada por la plantilla con un juicio humano independiente.

El informe incluye `input`, `output`, `canonical_nodes`, `rows_processed`, listas de `errors` y `warnings` y contadores por estado. Las rutas exactas quedan registradas en el JSON, por lo que para publicaciones conviene pasar paths relativos o sanitizarlos.

## Política SemVer y releases

- `MAJOR`: incompatibilidad en contrato del JSON/CSV, semántica de reglas o formato de resultados.
- `MINOR`: regla, dominio, experimento o capacidad añadida compatible.
- `PATCH`: corrección compatible/documentación.
- La especificación mantiene `spec_version` propia en `data/iom_spec.json`; cambios deben tener entrada de migración y pasar `python scripts/migrate_spec.py --check`.
- Para publicar una versión: dejar pasar CI y crear un tag anotado semver `vX.Y.Z` que apunte al commit revisado. El [workflow de release](https://github.com/luisreygarciafigueroa-creator/IOM/blob/main/.github/workflows/release.yml) valida la forma del tag, regenera `MANIFEST.sha256`, crea la release y adjunta el manifiesto con su SHA-256 registrado en las notas. El workflow aún no comprueba que CI haya pasado en el tag: verifica ese estado antes de etiquetar.
- `spec_version` es la versión de contrato de la especificación; el tag `vX.Y.Z` versiona el repositorio/release. El `CITATION.cff` recoge la versión citable vigente; actualizarlo junto al siguiente release.
