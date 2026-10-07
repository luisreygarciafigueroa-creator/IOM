# Guía de reproducción — Realidad I.O

Esta guía describe comandos reproducibles para el contenido que actualmente existe en el repositorio. El proyecto contiene una biblioteca Lean pequeña y scripts Python para generar y validar la ontología RDF. No afirma que haya 16 teoremas: el código formal debe revisarse directamente en `IOM/`.

## Requisitos

- Lean 4.9.0, instalado mediante Elan, para compilar el proyecto Lean. La versión está fijada en `lean-toolchain`.
- Python 3.9 o posterior para los scripts RDF.

## Compilación Lean

Desde la raíz del repositorio, ejecuta:

```bash
lake build
```

La compilación solo verifica los módulos Lean que forman parte del proyecto actual. Para comprobar qué teoremas contiene el repositorio, revisa los archivos `.lean` bajo `IOM/`.

## Generación y validación RDF/SHACL

Desde la raíz del repositorio, crea un entorno virtual e instala las dependencias declaradas. Así se evitan instalaciones globales que Ubuntu reciente puede bloquear:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

El generador crea 78 instancias. El validador comprueba sus propiedades con las formas definidas en `ontology/io_shapes.ttl`; un resultado no conforme devuelve un código de salida distinto de cero.

## Entorno de desarrollo

El archivo `.devcontainer/devcontainer.json` configura Python y prepara Lean mediante Elan. Después de crear el entorno, ejecuta los mismos comandos de compilación y validación indicados arriba.
