# Auditoría de correspondencia con MARCO I.O.

**Fuentes:** [MARCOI.O.txt](docs/MARCOI.O.txt), copia byte a byte del adjunto; además, las tablas y secuencias aportadas por el usuario en aclaraciones posteriores se preservan por separado en [TRIADAS_CATEGORIALES.md](docs/TRIADAS_CATEGORIALES.md) y [VECTORES_4_5.md](docs/VECTORES_4_5.md). El original no se altera para incorporar material enviado después.

## Hechos representados y verificados

| Especificación | Representación | Comprobación |
|---|---|---|
| Tiempo discreto, estado y vacío (§4.1) | `State(time : Int, payload : List String)`, `vacuum` | Compilación Lean y teoremas de operadores |
| Cuatro operadores (§3.1, §4.1) | `E`, `S_fwd`, `Ivo`, `S_rev` | Código Lean y build sin `sorry`/`admit` |
| Punto fijo del vacío | `strict_fixed_point` | Lean, para todo `t : Int` |
| No repetición para cargas no vacías | `no_repetition` | Teorema Lean compilado |
| Primeras tres perspectivas | izquierda=Individualidad; centro=Dualidad; derecha=Totalidad | Campos `hasPosition`/`hasPerspective`, SHACL y pruebas |
| 13 tríadas de avance y 13 de retroceso | Índices T00–T12 y etiquetas exactas por fase; 78 nodos | Test de etiquetas, recuento y conformidad SHACL |
| Inversión lateral | Avance izquierda ↔ retroceso derecha; centro ↔ centro | `mirrorOf` recíproco, SHACL y tests |
| Cuatro dinámicas `crea` | 8 aristas por fila × 13 filas = 104 relaciones | Test exacto de conjunto y restricciones SHACL |
| Cuarta y quinta perspectivas | Cuatro filas de cinco pasos; 20 `VectorStep` | Test de vectores, fases, flechas y ejes; SHACL de cardinalidad/valores |
| Extensión pentádica | 21 categorías con niveles 1, 4, 6, 6, 4 | Test de conteos y de etiquetas |

## Procedencia y decisiones de transcripción

- El MARCOI.O.txt adjunto inicialmente no contenía la tabla completa. El usuario aportó después los 13 renglones de cada fase y las cuatro reglas de creación; se transcribieron sin sustituir la ortografía recibida.
- La aclaración posterior especificó que las tres perspectivas estructurales son Individualidad, Dualidad y Totalidad y corresponden a las columnas izquierda, centro y derecha. Esa asignación ahora es explícita en cada instancia.
- En etiquetas de filas espejo se respetan las diferencias recibidas, por ejemplo `logica` frente a `lógica`, `imaginación` frente a `imaginacion` y `vacio` frente a `vacío`. Los espejos se conectan por índice de fila y simetría lateral, no por corrección textual.
- Los diagramas de las perspectivas 4–5 se representan como cuatro secuencias de cinco elementos, guardando tanto el índice visual de izquierda a derecha como la posición numérica del eje y la flecha mostrada. Así no se pierde la diferencia entre orientación visual y número de eje.
- La extensión de 21 categorías se conserva como una estructura adicional, separada de las 13 tríadas.

## Límites de la comprobación

1. El documento fuente anuncia RDF/OWL y SHACL. Este proyecto genera RDF en Turtle y aplica restricciones SHACL; no ejecuta un razonador OWL ni prueba consistencia OWL.
2. La afirmación de que una instancia del operador `S_rev` declara `io:restoresVacuum true` se modela como propiedad del operador/composición, no como propiedad verdadera de cada categoría individual.
3. En §4.1 el caso vacío de `S_rev` conserva el tiempo `n`, mientras la regla general `(n−1, red(iota(σ)))` lo reduciría incluso si `σ=[]`. El código respeta la excepción explícita para el vacío y usa la rama general solo para contenido no vacío.
4. Los 16 teoremas/lemas que declara el código actual son los que se compilan en Lean. Esto no valida automáticamente el historial o la modularización descritos por la fuente.
5. Las analogías neurocientíficas y físicas siguen siendo afirmaciones/mapeos del texto fuente; no hay experimentos, datos, mediciones ni simulaciones que se ejecuten aquí.
6. `payload : List String` es una representación computacional de unidades etiquetadas; no constituye una teoría física de la información.

## Mantenimiento

- No modificar `docs/MARCOI.O.txt` al agregar aclaraciones posteriores; registrarlas en anexos versionados con procedencia.
- Al modificar cualquiera de las tablas, actualizar en conjunto generador, formas SHACL, pruebas y documentación.
- Reservar «demostrado» para una prueba Lean compilada y «validado» para una restricción automatizada que se haya ejecutado.
- La conformidad SHACL valida el grafo y las reglas formalizadas, no la verdad científica de las tesis filosóficas.
