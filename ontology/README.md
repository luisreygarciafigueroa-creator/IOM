# ontology/

| Archivo | Rol |
|---------|-----|
| `io_shapes.ttl` | Restricciones SHACL **escritas**; se versionan |
| `io_ontology.ttl` | OWL **derivado** desde `data/iom_spec.json` |

## Regenerar / materializar

```bash
# Fuente canónica (requiere rdflib)
python scripts/generate_ontology.py

# Derivado determinista embebido (hash fijo, sin rdflib)
python scripts/materialize_ttl.py
```

SHA-256 esperado:

```text
84e2fe878fcf4a41b7ad364fb6f22e28e16db9132b7e2de89d36de55deeb87ba
```

CI regenera antes de tests y SHACL. El punto fijo compara CSV + `GENERATED_FROM.json`, **no** el TTL byte-a-byte.

## Versionar el TTL en el árbol

```bash
python scripts/materialize_ttl.py
git add ontology/io_ontology.ttl
python scripts/create_manifest.py
git add MANIFEST.sha256
git commit -m "chore: versionar io_ontology.ttl alineado al generador"
git push
```
