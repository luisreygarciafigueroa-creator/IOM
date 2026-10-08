# IOM — Marco I.O. formal y reproducible

Repositorio de comprobación ejecutable del documento [MARCOI.O.txt](docs/MARCOI.O.txt). El texto fuente se conserva **íntegro y byte a byte**. El código implementa los operadores temporales en Lean 4 y genera una ontología RDF validada con SHACL, además de pruebas de regresión.

> El repositorio prueba propiedades del modelo formalizado; no convierte afirmaciones filosóficas, neurocientíficas o físicas del documento en hechos empíricos demostrados.

## Ejecutar toda la verificación

Requisitos: Elan/Lean 4.9.0, Python 3.9 o superior, `venv` y acceso a Internet para descargar dependencias.

```bash
# Instalar Lean 4.9.0 si Elan no está instalado:
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain leanprover/lean4:v4.9.0
export PATH="$HOME/.elan/bin:$PATH"

python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

La CI de GitHub ejecuta las mismas etapas al abrir o actualizar una rama/PR.

## Qué se comprueba

- **Lean 4.9.0:** cuatro operadores (`E`, `S_fwd`, `Ivo`, `S_rev`) y 16 teoremas/lemas compilados, incluido `strict_fixed_point`, que demuestra la restauración exacta de `vacuum t` bajo `S_rev (Ivo (E (vacuum t)))`.
- **RDF/SHACL:** 78 identificadores estructurales (`13 × 2 fases × 3 posiciones locales`), correspondencia avance/evolución y retroceso/involución, y espejos recíprocos con índice y posición coincidentes.
- **Extensión enumerada:** 21 categorías distribuidas exactamente en niveles `1 + 4 + 6 + 6 + 4`, con etiquetas contrastadas con el texto fuente.
- **Regresión:** pruebas positivas y mutaciones que deben ser rechazadas por SHACL.

## Estructura

| Ruta | Contenido |
|---|---|
| `docs/MARCOI.O.txt` | Copia íntegra del documento entregado; hash SHA-256 `acfdc81d7b78331d60f9a341b8cc5b4be151638826b05a5537d68f183b6ed034`. |
| `IOM/` | Modelo y operadores Lean. |
| `ontology/` | Grafo Turtle generado y formas SHACL. |
| `scripts/` | Generación reproducible y validador SHACL. |
| `tests/` | Pruebas de regresión del grafo y restricciones. |
| `AUDITORIA.md` | Correspondencia entre fuente, implementación y límites verificables. |
| `REPRODUCCION.md` | Pasos reproducibles y criterios de salida. |

## Límite de datos explícito

El documento declara 13 tríadas, pero solo nombra dos ejemplos y no publica el listado completo ni su orden. `T00`–`T12` son por eso **identificadores técnicos**, no nombres atribuidos. Tampoco se asignan a cada posición una de las cinco perspectivas cuando el documento no proporciona esa correspondencia. La auditoría describe otras diferencias entre enunciados del documento e implementación.
