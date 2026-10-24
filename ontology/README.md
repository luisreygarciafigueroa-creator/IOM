# ontology/

| Archivo | Rol |
|---------|-----|
| `io_shapes.ttl` | Restricciones SHACL **escritas**; se versionan |
| `io_ontology.ttl` | OWL **generado** desde `data/iom_spec.json` |

## Regenerar

```bash
python scripts/generate_ontology.py
```

CI regenera el TTL antes de tests y SHACL. El punto fijo compara CSV + `GENERATED_FROM.json`, **no** el TTL byte-a-byte (serialización rdflib).

El TTL versionado, si existe, debe coincidir con el generador actual; no es fundamento, pero sí **derivado correcto** para inspección offline.
