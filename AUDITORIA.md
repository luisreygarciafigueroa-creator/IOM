# Auditoría de correspondencia con MARCO I.O.

**Fuente de autoridad:** [documento original íntegro](docs/MARCOI.O.txt). Esta auditoría no corrige ni reinterpreta el texto; registra qué datos se implementan y cuáles no son deducibles o no están respaldados por código/datos.

## Hechos que el repositorio representa y prueba

| Afirmación/estructura del documento | Representación | Prueba/validación |
|---|---|---|
| Tiempo discreto `t ∈ ℤ`, estado `(t,A)` y vacío `(t,∅)` (§4.1) | `State(time : Int, payload : List String)`, `vacuum` | Compilación Lean y ecuaciones de los operadores |
| Cuatro operadores `E`, `S_fwd`, `Ivo`, `S_rev` (§3.1, §4.1) | Funciones ejecutables en `IOM/Operators.lean` | Teoremas Lean; build sin `sorry`/`admit` |
| `S_rev ∘ Ivo ∘ E` restaura el vacío (§3.2, §4.2) | Teorema `strict_fixed_point` | Lean para todo `t : Int` |
| Conteo 13 × 2 fases × 3 posiciones = 78 (§5.1 y especificación del repositorio) | Identificadores internos `T00`–`T12`, `adv`/`ret`, posiciones 0–2 | Tests de conjunto exacto, recuento y SHACL |
| Inversión entre fases, mismos índice y posición (§3.3 y §5.1) | `mirrorOf` recíproco | Test y restricción SHACL negativa/positiva |
| Correspondencia de direcciones avance/evolución y retroceso/involución | `hasDirection` | Test y restricción SHACL |
| Extensión pentádica de 21 categorías (§III.4.2) | Individuos etiquetados por nivel | Test de 21 etiquetas y recuentos `1,4,6,6,4` |

## Datos no presentes en la fuente

- **No existe una enumeración de las 13 tríadas.** El texto menciona solo `Oscuridad-Consciencia-Luz` y `Hardware-Virtual-Software` como ejemplos y añade “etc.”. No identifica los once nombres restantes ni el índice de esos dos ejemplos. `T00`–`T12` son únicamente claves generadas, no los nombres reales.
- **No existe una tabla completa de asignación de cada nodo a una de las cinco perspectivas.** Por ello se retiró la fórmula `(índice + posición) mod 5` del generador/SHACL anterior: tal fórmula no figura en el MARCO I.O.
- El documento nombra 39 posiciones por fase, exige una ubicación en eje `[0,4]` y, al describir tríadas, habla de posiciones izquierda/centro/derecha. No da una tabla para convertir estos tres esquemas. La ontología no adivina esa correspondencia.
- Los 21 rótulos sí enumerados en la extensión son otra estructura declarada. No se identifican como nombres de las 13 tríadas originales ni se asignan a sus índices.

## Discrepancias entre declaraciones y comprobación

1. El MARCO I.O. anuncia una validación RDF/OWL y SHACL. El grafo del repositorio es RDF serializado en Turtle y usa restricciones SHACL. No hay importación/razonamiento OWL que verifique consistencia ontológica OWL.
2. La afirmación fuente de que cada instancia de `S_rev` declara `io:restoresVacuum true` no se interpreta como atributo verdadero de cada posición categorial: la implementación pone la restauración como propiedad del operador/composición, no de los 78 nodos. Esto evita afirmar que cualquier categoría individual restaura por sí misma el vacío.
3. En §4.1 del documento, el caso vacío de `S_rev` conserva `n`; la regla general `(n−1, red(iota(σ)))` produciría otra marca temporal incluso para `σ=[]`. El código sigue la excepción explícita para el vacío y aplica la rama general solo a contenido no vacío.
4. La fuente reporta 16 teoremas críticos, una versión modular (incluidos `IOM_Theorems`) y una compilación anterior. Esas cifras/historiales no se dan por verificadas automáticamente. Se reportará el conteo del código actual, no el relato histórico.
5. Una conclusión filosófica (por ejemplo, “resuelve la paradoja”) no se sigue solamente del teorema para el estado vacío. El alcance del teorema es el modelo definido en Lean.
6. Las asociaciones neurocientíficas y físicas se presentan en la fuente como mapeos, analogías o propuestas. El repositorio no incorpora datos experimentales, mediciones ni simulaciones que las comprueben empíricamente.

## Reglas para mantener exactitud

- Cambiar el documento fuente requiere editar deliberadamente `docs/MARCOI.O.txt` y actualizar su hash indicado en `README.md`.
- No asignar etiquetas ni índices a tríadas sin recibir su lista oficial.
- No escribir “demostrado” salvo que exista una prueba Lean compilada o una prueba automatizada ejecutada que respalde exactamente la frase.
- No presentar la conformidad SHACL como prueba de verdad científica ni de todas las tesis del documento.
