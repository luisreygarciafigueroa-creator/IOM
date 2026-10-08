# IOM — Marco I.O. formal y reproducible

Repositorio de comprobación ejecutable del documento [MARCOI.O.txt](docs/MARCOI.O.txt), complementado con las listas exactas de tríadas y vectores que el usuario añadió para completar la fuente ([13 tríadas](docs/TRIADAS_CATEGORIALES.md), [perspectivas cuarta y quinta](docs/VECTORES_4_5.md)). El documento original se conserva íntegro y byte a byte.

> El repositorio verifica propiedades del modelo formalizado; no presenta las afirmaciones filosóficas, neurocientíficas o físicas como hechos empíricos demostrados.

## Ejecutar la verificación completa

Requisitos: Elan/Lean 4.9.0, Python 3.9 o posterior, `venv` e Internet para instalar dependencias.

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

La CI de GitHub ejecuta esas etapas en cada actualización.

## Qué se comprueba

- **Lean 4.9.0:** cuatro operadores (`E`, `S_fwd`, `Ivo`, `S_rev`) y 16 teoremas/lemas, incluido el punto fijo estricto del vacío y la no repetición para contenido no vacío. La compilación no usa `sorry` ni `admit`.
- **Perspectivas 1–3:** izquierda ↔ Individualidad, centro ↔ Dualidad, derecha ↔ Totalidad.
- **Tríadas:** las 13 filas nominales en cada fase; **78 nodos**. Los espejos invierten izquierda/derecha y conservan el centro.
- **Dinámicas `crea`:** 104 vínculos entre nodos de fases opuestas, resultado de las cuatro reglas aplicadas a las 13 filas.
- **Perspectivas 4–5:** 20 pasos vectoriales con etiquetas, índices `[0,4]`, fases y flechas transcritos.
- **Extensión adicional:** 21 categorías en niveles `1 + 4 + 6 + 6 + 4`.
- **RDF/SHACL y regresión:** correspondencia de dirección/fase, perspectiva/posición, espejos, reglas de creación y estructura de vectores, con mutaciones negativas.

## Archivos clave

| Ruta | Contenido |
|---|---|
| `docs/MARCOI.O.txt` | Copia byte a byte del documento adjunto; SHA-256 `acfdc81d7b78331d60f9a341b8cc5b4be151638826b05a5537d68f183b6ed034`. |
| `docs/TRIADAS_CATEGORIALES.md` | Lista de las 13 tríadas de avance/retroceso y cuatro reglas de creación añadidas por el usuario. |
| `docs/VECTORES_4_5.md` | Tablas de posición y flechas de las perspectivas cuarta y quinta. |
| `IOM/` y `IOM.lean` | Modelo, operadores, teoremas y módulo raíz Lean. |
| `ontology/` | RDF/Turtle generado y restricciones SHACL. |
| `scripts/`, `tests/` | Generación, validación y pruebas automatizadas. |
| `AUDITORIA.md`, `REPRODUCCION.md`, `paper.md` | Correspondencia de fuente, resultados y reproducción.

La fuente original no contenía las tablas completas de 13 tríadas/vectorial; los dos documentos suplementarios conservan las precisiones posteriores del usuario sin alterar esa copia original.
