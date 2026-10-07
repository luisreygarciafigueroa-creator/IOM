# Realidad I.O.: demostración formal del punto fijo del vacío y confirmación estructural

## Resultados Lean 4 y RDF/SHACL del modelo implementado

**Autor:** Luis Rey García Figueroa · **Fecha:** octubre de 2026
**Clasificación:** demostración formal y confirmación computacional de alcance acotado

## Resumen

Este artículo establece resultados verificables para el modelo computacional de Realidad I.O. En Lean 4.9.0 se demuestra, para todo índice temporal entero, que la composición de evolución, involución y supresión retroactiva deja invariante el estado vacío. La prueba está incorporada como el teorema `strict_fixed_point` y Lean la verifica por reducción de las definiciones. De manera independiente, la ontología RDF generada contiene exactamente 78 instancias y satisface las restricciones SHACL sobre sus propiedades, espejos recíprocos, correspondencia entre fase y dirección y asignación de perspectiva. Siete pruebas de regresión confirman esas propiedades y rechazan mutaciones representativas que las violan. Por tanto, quedan demostradas la propiedad algebraica del subsistema formalizado y la conformidad estructural del grafo respecto de las reglas declaradas. El resultado es firme dentro de ese alcance: no se presenta como prueba empírica de una ontología física ni como demostración de aspectos que aún no están formalizados en Lean.

**Palabras clave:** ontología, vacío, información, tiempo discreto, Lean 4, demostración formal, RDF, Turtle, SHACL, validación.

## 1. Introducción

Realidad I.O organiza una interpretación del vacío como ausencia de información y describe su relación con estados informativos mediante un eje temporal discreto. La implementación disponible permite someter a comprobación mecánica una parte precisa de ese marco: la dinámica definida por los operadores `E`, `Ivo` y `S_rev`, además de la estructura de datos que representa las tríadas y sus fases.

El objetivo de este artículo es presentar resultados positivos y reproducibles, no solo una línea de investigación. Se demuestra un punto fijo estricto para los estados vacíos; se verifica que la ontología generada cumple las restricciones estructurales expresadas en SHACL; y se identifican con precisión las fronteras de esas confirmaciones. Una prueba formal establece una consecuencia de definiciones dentro del sistema codificado; no convierte por sí misma una interpretación filosófica en un hecho empírico.

### 1.1. Resultados establecidos

1. Lean verifica para todo `t : Int` que `S_rev (Ivo (E (vacuum t))) = vacuum t`.
2. El generador produce el conjunto completo de 78 identificadores correspondientes a 13 tríadas, 2 fases y 3 posiciones locales.
3. SHACL valida las propiedades de cada nodo y sus correspondencias relacionales: reciprocidad de `mirrorOf`, consistencia fase-dirección y regla de asignación de perspectiva.
4. Las pruebas de regresión confirman la conformidad del grafo correcto y rechazan cambios que vulneran esas condiciones.

## 2. Fundamentos del modelo

### 2.1. Vacío, información y tiempo

Sea `V_t` el estado vacío en el instante discreto `t ∈ ℤ`. En la implementación, ese estado se concreta como `vacuum t = State(t, [])`. El contenido de un estado se representa mediante una lista finita de cadenas. La unidad informativa `U` se emplea en la interpretación del marco como noción de diferenciación mínima, aunque no tiene todavía un tipo independiente en Lean.

El modelo adopta como interpretación semántica la reciprocidad entre vacío e información. La demostración que sigue no depende de probar filosóficamente esa premisa: establece una propiedad matemática de las funciones y estados efectivamente definidos en el código.

### 2.2. Perspectivas y tríadas

La organización categorial utiliza las etiquetas `Ind`, `D`, `Tot`, `Evol` e `Invol`, trece índices de tríada y las fases `adv` y `ret`. En el grafo, la perspectiva asignada a cada nodo sigue la regla cíclica `P[(índice de tríada + posición local) mod 5]`; la dirección es `evol` en fase `adv` e `invol` en fase `ret`.

Esta estructura queda confirmada como dato y como conjunto de relaciones conforme a las formas SHACL descritas en la sección 4. La interpretación filosófica de las etiquetas y la teoría completa de perspectivas no son teoremas Lean en la versión actual.

## 3. Demostración formal de la dinámica del vacío

### 3.1. Estado y operadores

El módulo `IOM/Core.lean` define el estado computacional como una estructura con `time : Int` y `payload : List String`. El vacío se define mediante `vacuum t = ⟨t, []⟩`.

En `IOM/Operators.lean` están implementadas estas funciones:

| Operador | Definición | Efecto |
|---|---|---|
| `E` | `(t, A) ↦ (t + 1, A)` | Avanza un instante y conserva el contenido. |
| `Ivo` | `(t, A) ↦ (t − 1, A)` | Retrocede un instante y conserva el contenido. |
| `S_rev` | `(t, []) ↦ (t, [])`; `(t, A) ↦ (t − 1, [])` si `A ≠ []` | Mantiene el estado vacío; con contenido, lo elimina y retrocede un instante. |

La secuencia que se demuestra es `S_rev ∘ Ivo ∘ E`, aplicada de derecha a izquierda. Para un estado vacío, `E` adelanta el índice temporal, `Ivo` revierte ese incremento y `S_rev` conserva el estado porque la lista sigue vacía.

### 3.2. Teorema de punto fijo estricto

**Teorema 1.** Para todo `t : ℤ`, el vacío es un punto fijo estricto de la composición implementada:

\[
\forall t \in \mathbb{Z},\qquad
S_{\mathrm{rev}}\bigl(Ivo(E(vacuum(t)))\bigr) = vacuum(t).
\]

**Demostración.** Por las definiciones de `vacuum`, `E` e `Ivo`:

\[
E(vacuum(t)) = (t+1, []),\qquad
Ivo(E(vacuum(t))) = (t, []).
\]

Como el contenido está vacío, se aplica la primera rama de `S_rev`:

\[
S_{\mathrm{rev}}(t, []) = (t, []) = vacuum(t).
\]

Luego `S_rev (Ivo (E (vacuum t))) = vacuum t` para todo entero `t`. El teorema `strict_fixed_point` codifica exactamente este enunciado en Lean 4.9.0; la compilación lo comprueba por reducción (`rfl`). ∎

La demostración confirma la invariancia temporal e informacional del vacío **según las definiciones implementadas**. No presupone ni demuestra operadores adicionales que no aparecen en el código.

### 3.3. Alcance para estados con contenido

Para un estado `(t, A)` con `A ≠ []`, las definiciones implican directamente:

\[
S_{\mathrm{rev}}(Ivo(E(t,A))) = (t-1, []).
\]

La composición elimina el contenido y retrocede un instante. Esta igualdad se obtiene por evaluación de las funciones actuales, pero no está declarada como un segundo teorema Lean. Tampoco están formalizadas todavía una noción de atractor, la no repetición general, el operador `S_fwd`, una función `red` ni una transformación categorial `ι`. Por ello, la confirmación formal demostrada aquí es la del punto fijo del vacío y no una verificación global de todas las extensiones posibles de la fórmula nuclear.

## 4. Confirmación estructural de la ontología RDF

### 4.1. Grafo generado

El script `scripts/generate_ontology.py` genera `ontology/io_ontology.ttl`. El conjunto de identificadores cubre las combinaciones de 13 índices (`0`–`12`), 2 fases (`adv`, `ret`) y 3 posiciones locales (`0`–`2`):

\[
13 \times 2 \times 3 = 78 \text{ nodos}.
\]

Cada instancia registra su índice de tríada, fase, posición, dirección, perspectiva y el literal booleano `restoresVacuum = true`. Para cada tríada y posición, `mirrorOf` enlaza recíprocamente los nodos de fases opuestas. Las pruebas comprueban tanto la cantidad como el conjunto esperado completo de identificadores.

### 4.2. Restricciones confirmadas por SHACL

`ontology/io_shapes.ttl` aplica formas a instancias de `io:OntoNode`. Verifica tipos, cardinalidades y rangos de índice y posición, valores admitidos de fase/dirección/perspectiva y el literal booleano `restoresVacuum`. Sus restricciones SPARQL verifican además que:

- el espejo exista como nodo, mantenga la misma tríada y posición, tenga fase opuesta y apunte recíprocamente al nodo de origen;
- la dirección corresponda a la fase (`adv=evol`, `ret=invol`);
- la perspectiva coincida con la regla cíclica del generador.

Las siete pruebas Python verifican la conformidad completa del grafo y sus correspondencias. También alteran, una por una, propiedades representativas —índice inválido, espejo desalineado, dirección incompatible o perspectiva incorrecta— y confirman que SHACL rechaza esos datos.

Este resultado confirma conformidad con restricciones explícitas sobre el grafo RDF serializado en Turtle. `restoresVacuum = true` sigue siendo un literal declarado: SHACL no demuestra con ello la ecuación Lean. El flujo tampoco ejecuta un razonador OWL ni acredita inferencias OWL.

## 5. Reproducción y resultados

Desde la raíz del repositorio, con Lean 4.9.0 instalado mediante Elan y Python 3.9 o posterior, se reproducen las comprobaciones así:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

En la revisión del repositorio de octubre de 2026, los resultados fueron:

- `lake build`: compilación correcta con Lean 4.9.0;
- pruebas Python: **7 de 7 pasaron**;
- generación: **78 nodos**;
- validación SHACL: **`Conforms: True`**;
- CI de GitHub para la integración: los checks de Lean y RDF/SHACL terminaron exitosamente.

La reproducibilidad de esos resultados confirma que la implementación satisface sus especificaciones ejecutables y que las mutaciones de prueba previstas se detectan. No equivale a demostrar consistencia lógica global, a probar dieciséis teoremas ni a verificar en Lean todas las tesis filosóficas o categoriales del marco.

## 6. Discusión y límites de la confirmación

Los resultados tienen dos alcances complementarios y concretos. Lean proporciona una demostración deductiva del punto fijo para el estado vacío con las funciones codificadas. RDF/SHACL proporciona una validación estructural del grafo, reforzada por pruebas positivas y negativas. En ambos casos, la conclusión se deriva de definiciones, datos y restricciones inspeccionables y reproducibles.

Para extender esta confirmación todavía se requiere:

1. **Formalizar el vocabulario ontológico en Lean.** El vacío, la unidad informativa, las perspectivas, fases y tríadas no tienen tipos independientes en los módulos actuales.
2. **Ampliar el sistema de operadores y teoremas.** `S_fwd`, la reducción `red`, la transformación `ι`, sus propiedades y las afirmaciones generales de cierre/no repetición no están implementadas ni demostradas.
3. **Especificar semántica global adicional.** El conteo de 78 instancias se confirma en Python; las formas SHACL verifican restricciones por nodo y relaciones definidas, no unicidad global de nombres ni inferencia OWL.
4. **Separar confirmación formal de evidencia empírica.** El resultado no es un experimento ni una validación de una teoría física. Confirma propiedades matemáticas y estructurales del artefacto computacional.

Estos límites no rebajan la demostración efectivamente obtenida: precisan qué queda probado, bajo qué definiciones y qué trabajo sería necesario para extenderla.

## 7. Conclusiones

La implementación de Realidad I.O contiene una propiedad central que queda **demostrada formalmente**: el vacío `vacuum t` es un punto fijo de `S_rev ∘ Ivo ∘ E` para todo entero `t`. Lean 4.9.0 verifica el teorema `strict_fixed_point` directamente a partir de las definiciones.

De manera independiente, el grafo RDF de 78 nodos queda **confirmado como conforme** con las formas SHACL vigentes. Las restricciones y pruebas corroboran el emparejamiento recíproco de espejos, la consistencia entre fase y dirección, la regla de perspectiva y el rechazo de datos alterados que violan esas condiciones.

Por tanto, los resultados de este artículo constituyen una **demostración formal de una propiedad definida y una confirmación computacional de la estructura codificada**. La conclusión se mantiene deliberadamente delimitada: no afirma que Lean o SHACL hayan demostrado una ontología física, una verdad metafísica ni propiedades todavía ausentes del código.

## Disponibilidad de código y datos

El código y los datos están disponibles en el [repositorio IOM](https://github.com/luisreygarciafigueroa-creator/IOM), bajo la licencia indicada por el archivo `LICENSE`. Los módulos Lean se encuentran en `IOM/`; el generador, validador y pruebas Python en `scripts/` y `tests/`; y los archivos RDF/SHACL en `ontology/`.

## Referencias

- García Figueroa, L. R. (2026). *Realidad I.O: dinámica temporal del vacío y la unidad informativa*. Documento fuente.
- Moura, L. de, & Ullrich, S. (2021). The Lean 4 Theorem Prover and Programming Language. En *Automated Deduction – CADE 28*. Springer.
- W3C. (2014). *RDF 1.1 Turtle: Terse RDF Triple Language*. W3C Recommendation.
- Knublauch, H., & Kontokostas, D. (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation.

---

**Nota de versión:** este artículo describe el contenido de `main` verificado en octubre de 2026. Si cambian las definiciones, los datos, las pruebas o las formas SHACL, deben actualizarse en conjunto el texto y los resultados reproducidos.
