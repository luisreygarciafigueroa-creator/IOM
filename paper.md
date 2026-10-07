# Realidad I.O.: dinámica temporal del vacío y la unidad informativa

## Propuesta conceptual y prototipo computacional reproducible

**Autor:** Luis Rey García Figueroa · **Fecha:** octubre de 2026
**Clasificación:** marco ontológico-formal en desarrollo

## Resumen

Este artículo presenta Realidad I.O como una propuesta conceptual sobre la relación recíproca entre vacío e información. El modelo plantea un tiempo discreto, operadores de evolución y retroceso, cinco perspectivas y una organización de trece tríadas. Se distingue aquí la propuesta teórica de su alcance computacional actual: el repositorio implementa en Lean 4 un estado con tiempo entero y una lista de cadenas, tres operadores (`E`, `Ivo` y `S_rev`) y un teorema que prueba que la composición restaura el estado vacío. En paralelo, un generador Python crea una ontología RDF en Turtle con 78 nodos y un validador comprueba las restricciones SHACL declaradas. Estas herramientas verifican propiedades acotadas de las definiciones y de los datos generados; no prueban la consistencia global de la ontología filosófica, la dinámica completa de las cinco perspectivas ni todas las afirmaciones de este artículo. Se especifican las definiciones vigentes, los resultados reproducibles y las limitaciones que deben resolverse para ampliar la formalización.

**Palabras clave:** ontología, vacío, información, tiempo discreto, Lean 4, RDF, Turtle, SHACL, verificación formal.

## 1. Introducción

Realidad I.O propone interpretar el vacío no como un espacio físico, sino como una condición conceptual de ausencia de información, en relación recíproca con la aparición de información. El marco organiza esta dinámica mediante un eje temporal discreto y categorías que buscan describir tanto modos de ser como direcciones de cambio.

El propósito de esta versión es exponer la propuesta y documentar qué parte está implementada y se puede reproducir en el repositorio. Esta distinción es importante: que un programa compile o que un grafo satisfaga unas formas SHACL solo garantiza propiedades expresadas en ese programa o esas formas. No constituye, por sí mismo, una demostración de las tesis filosóficas ni de una interpretación física del modelo.

### 1.1. Objetivos

1. Presentar la intuición conceptual de reciprocidad entre vacío e información.
2. Especificar las definiciones operativas que hoy aparecen en el código Lean.
3. Reportar los resultados de la generación y validación RDF/SHACL sin extender su alcance.
4. Identificar brechas concretas entre el marco propuesto y el prototipo disponible.

## 2. Propuesta conceptual

### 2.1. Vacío, información y tiempo

En el plano conceptual, sea `V_t` el estado de vacío en el instante discreto `t`, con `t ∈ ℤ`. La unidad informativa `U` representa la noción de diferenciación mínima. Un estado informativo puede describirse abstractamente como `(t, A)`, donde `A` recoge contenido informativo.

La reciprocidad entre vacío e información es una premisa interpretativa del marco: el vacío designa una condición de ausencia y la información una diferencia que puede emerger en relación con esa condición. Esta premisa no está axiomatizada ni demostrada en Lean en la versión examinada.

### 2.2. Perspectivas y tríadas

La propuesta considera cinco etiquetas perspectivales: `Ind`, `D`, `Tot`, `Evol` e `Invol`. En términos conceptuales, las tres primeras se asocian con modos de descripción de lo actualizado y las dos últimas con direcciones de flujo. También propone trece tríadas y una distinción entre las fases `adv` y `ret`.

La estructura RDF actual registra esas etiquetas como valores y distribuye nodos entre tríadas, posiciones locales y fases. No formaliza en Lean una teoría de las cinco perspectivas ni demuestra una partición exhaustiva, una dinámica direccional completa o una simetría categorial general.

## 3. Modelo operativo implementado en Lean

### 3.1. Representación del estado

El módulo `IOM/Core.lean` define el estado computacional como una estructura con dos campos:

- `time : Int`, el índice temporal;
- `payload : List String`, una lista finita de cadenas que representa el contenido.

El vacío implementado se define como `vacuum t = State(t, [])`. Esta representación concreta no incorpora un tipo separado para la unidad informativa, ni establece que el contenido sea un conjunto matemático de unidades distintas.

### 3.2. Operadores disponibles

En `IOM/Operators.lean` se definen los siguientes operadores sobre `State`:

| Operador | Definición implementada | Efecto |
|---|---|---|
| `E` | `(t, A) ↦ (t + 1, A)` | Avanza el tiempo y conserva el contenido. |
| `Ivo` | `(t, A) ↦ (t − 1, A)` | Retrocede el tiempo y conserva el contenido. |
| `S_rev` | `(t, []) ↦ (t, [])`; `(t, A) ↦ (t − 1, [])` si `A ≠ []` | Conserva el tiempo en el vacío; si hay contenido, lo elimina y retrocede un paso. |

No se implementa actualmente un operador `S_fwd`. Tampoco aparecen en el código una función de reducción `red`, una transformación categorial `ι` ni axiomas de idempotencia o involución. Por tanto, las fórmulas que dependan de esas entidades deben entenderse como extensiones propuestas y no como definiciones del prototipo.

### 3.3. Resultado probado

El único teorema declarado en los módulos Lean actuales es `strict_fixed_point`:

\[
\forall t \in \mathbb{Z},\quad
S_{\mathrm{rev}}\bigl(Ivo(E(vacuum(t)))\bigr) = vacuum(t).
\]

La igualdad se obtiene directamente de las definiciones: `E` suma uno al tiempo, `Ivo` lo resta y conserva la lista vacía; `S_rev` deja intacto un estado cuyo contenido está vacío. Lean comprueba esta igualdad por reducción (`rfl`).

Para un estado con contenido no vacío, las definiciones actuales implican que la composición produce `(t − 1, [])`: primero `E` y `Ivo` cancelan sus cambios temporales, y después `S_rev` elimina el contenido y retrocede un paso. Esta consecuencia se deriva de las definiciones, pero **no está declarada como un teorema Lean independiente**. Tampoco se implementa una noción formal de “atractor” ni se prueba una propiedad de no repetición de manera general.

En consecuencia, la fórmula nuclear puede presentarse como un punto fijo probado en el subespacio de estados vacíos. Su extensión a estados informativos debe expresarse con las definiciones concretas anteriores y no como una propiedad global ya formalizada.

## 4. Ontología RDF y restricciones SHACL

### 4.1. Generación del grafo

El script `scripts/generate_ontology.py` genera `ontology/io_ontology.ttl`. Recorre trece índices de tríada (`0` a `12`), dos fases (`adv` y `ret`) y tres posiciones locales (`0`, `1` y `2`):

\[
13 \times 2 \times 3 = 78 \text{ nodos}.
\]

Cada nodo registra un índice de tríada, una fase, una posición local, una dirección (`evol` para `adv` e `invol` para `ret`), una perspectiva elegida por la regla `P[(índice de tríada + posición local) mod 5]` entre las cinco etiquetas y el valor booleano `restoresVacuum = true`. Para cada índice y posición, el generador crea además enlaces `mirrorOf` recíprocos entre los nodos `adv` y `ret`.

Esta construcción usa posiciones locales `0` a `2`; no equivale por sí sola a una formalización del eje perspectival `[0,4]` que se describe en la propuesta conceptual.

### 4.2. Alcance de las formas SHACL

`ontology/io_shapes.ttl` define una forma dirigida a instancias de `io:OntoNode`. Comprueba que los índices estén entre `0` y `12`, que las fases y direcciones pertenezcan a las listas permitidas, que la posición local sea `0`, `1` o `2`, que la perspectiva sea una de las cinco etiquetas previstas, que `restoresVacuum` sea un booleano `true` y que cada nodo tenga exactamente un `mirrorOf` cuyo destino también sea un `io:OntoNode`.

Además de las restricciones por propiedad y cardinalidad, tres restricciones SPARQL comprueban que `mirrorOf` sea recíproco entre nodos de la misma tríada y posición con fases opuestas, que la dirección corresponda a la fase (`adv=evol`, `ret=invol`) y que la perspectiva siga la regla cíclica indicada. Las pruebas Python inspeccionan los 78 nodos y contienen casos negativos que alteran cada una de esas correspondencias para confirmar que la validación los rechaza. Aun así, `restoresVacuum = true` es un dato declarado; no prueba por sí mismo una propiedad matemática de restauración.

El formato usado es RDF serializado como Turtle y validado con SHACL. El flujo descrito no ejecuta un razonador OWL ni acredita inferencias OWL.

## 5. Procedimiento de reproducción y resultados

Desde la raíz del repositorio, con Lean 4.9.0 instalado mediante Elan y Python 3.9 o posterior:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

La generación de este artículo se contrastó con el estado del repositorio disponible en octubre de 2026. En esa comprobación:

- `lake build` terminó correctamente con Lean 4.9.0;
- las siete pruebas Python pasaron, incluyendo conteo y conformidad globales, alineación de espejos, correspondencia fase-dirección y fórmula perspectival, además del rechazo de índices y mutaciones inconsistentes;
- el generador informó 78 nodos;
- el validador SHACL reportó `Conforms: True`.

Estos resultados son reproducibles para el contenido actual del repositorio. No equivalen a dieciséis teoremas, a una prueba de consistencia lógica global ni a una verificación de todas las propiedades filosóficas o categoriales enunciadas en la propuesta.

## 6. Discusión y limitaciones

El prototipo ofrece un punto de partida ejecutable y reproducible: una representación mínima de estado, tres operadores, un resultado formal sobre el vacío y una tubería de generación y validación de datos. La separación entre código Lean y RDF permite inspeccionar dos aspectos distintos: comportamiento de funciones y conformidad de datos frente a restricciones declaradas.

Las principales brechas pendientes son:

1. **Formalización del vocabulario conceptual.** No hay tipos Lean separados para vacío, unidad informativa, perspectiva, fase o tríada.
2. **Cobertura de operadores.** Falta implementar `S_fwd` y especificar formalmente las transformaciones que el marco conceptual atribuye a operadores adicionales.
3. **Cobertura de teoremas.** Solo se declara `strict_fixed_point`; las afirmaciones de no repetición, simetría general, idempotencia y cierre global no están demostradas en el proyecto.
4. **Alcance global de la validación RDF.** El conteo de 78 nodos se comprueba en Python; las formas SHACL validan propiedades y relaciones por instancia, no prueban unicidad global de todos los nombres ni una semántica OWL inferida. `restoresVacuum` sigue siendo una anotación, no una prueba del operador Lean.
5. **Semántica y alcance empírico.** El modelo es una propuesta ontológica formal. El código no constituye evidencia experimental ni una teoría validada de la realidad física.

Estas limitaciones no invalidan la propuesta conceptual; delimitan qué conclusiones se pueden atribuir hoy a la implementación y señalan un camino de desarrollo verificable.

## 7. Conclusiones

Realidad I.O plantea un marco para pensar la relación entre vacío e información mediante tiempo discreto, perspectivas y tríadas. El prototipo actual materializa solo una parte acotada de esa propuesta.

La afirmación formal demostrada en Lean es precisa: el vacío `vacuum t` es un punto fijo de `S_rev ∘ Ivo ∘ E` para todo entero `t`. El grafo RDF contiene 78 nodos generados de manera determinista y satisface las restricciones SHACL vigentes, que comprueban también el emparejamiento de espejos y la correspondencia entre fase, dirección y perspectiva. Siete pruebas cubren tanto la conformidad global como mutaciones inválidas representativas.

Por rigor, estos resultados deben describirse como una **implementación inicial verificada en aspectos específicos**, no como una verificación completa de dieciséis teoremas o de todas las tesis del marco. Ampliar los tipos, operadores y teoremas permitiría cerrar gradualmente la distancia entre la propuesta conceptual y su codificación ejecutable.

## Disponibilidad de código y datos

El código y los datos están disponibles en el [repositorio IOM](https://github.com/luisreygarciafigueroa-creator/IOM), bajo la licencia indicada por el archivo `LICENSE`. Los módulos Lean se encuentran en `IOM/`; el generador, validador y pruebas Python en `scripts/` y `tests/`; y los archivos RDF/SHACL en `ontology/`.

## Referencias

- García Figueroa, L. R. (2026). *Realidad I.O: dinámica temporal del vacío y la unidad informativa*. Documento fuente.
- Moura, L. de, & Ullrich, S. (2021). The Lean 4 Theorem Prover and Programming Language. En *Automated Deduction – CADE 28*. Springer.
- W3C. (2014). *RDF 1.1 Turtle: Terse RDF Triple Language*. W3C Recommendation.
- Knublauch, H., & Kontokostas, D. (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation.

---

**Nota de versión:** este artículo describe el contenido del repositorio observado en octubre de 2026. Si cambian las definiciones, datos, pruebas o formas SHACL, deben actualizarse en conjunto el texto y los resultados reproducidos.
