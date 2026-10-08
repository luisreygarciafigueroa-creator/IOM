# Reproducción de IOM

Esta guía reproduce las verificaciones que ejecuta el repositorio. Los resultados se limitan a los teoremas Lean y a los invariantes RDF/SHACL descritos en [AUDITORIA.md](AUDITORIA.md); no constituyen validación empírica de las afirmaciones filosóficas, neurocientíficas o físicas del marco.

## Requisitos e instalación

- Python 3.9 o posterior, con `venv`.
- Elan y Lean 4.9.0, versión fijada en `lean-toolchain`.
- Conexión a Internet para instalar Lean o descargar paquetes Python cuando aún no estén disponibles en caché.

Instala Elan/Lean si `elan` no existe en PATH:

```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
  | sh -s -- -y --default-toolchain leanprover/lean4:v4.9.0
export PATH="$HOME/.elan/bin:$PATH"
```

## Verificación completa, desde la raíz

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

Criterios de éxito:

1. `lake build` termina con código `0` y compila la biblioteca `IOM`.
2. El generador informa **78 nodos estructurales**, **104 relaciones crea**, **20 pasos vectoriales** y **21 categorías de la extensión**.
3. Todas las pruebas de `tests/test_ontology.py` terminan con `OK`. Las pruebas negativas confirman que mutaciones incompatibles no pasan SHACL.
4. El validador imprime `Conforms: True` y sale con código `0`.

Cada comando devuelve código distinto de cero ante error, por lo que puede usarse como gate de integración continua.

## Reproducción de un paso

- Solo Lean: `lake build`.
- Regenerar RDF: `.venv/bin/python scripts/generate_ontology.py`.
- Pruebas: `.venv/bin/python -m unittest discover -s tests -v`.
- SHACL: `.venv/bin/python scripts/validate_shacl.py`.

El Turtle se regenera desde el script; no edites a mano `ontology/io_ontology.ttl`. El marco original se encuentra en `docs/MARCOI.O.txt` y se conserva sin modificaciones.
