# Realidad I.O: Dinámica Temporal del Vacío y la Unidad Informativa

## Propuesta ontológica y estado de su implementación formal

**Luis Rey García Figueroa**
**Octubre de 2026**

---

## Resumen

Este artículo presenta **Realidad I.O** como una propuesta ontológica que explora la relación entre vacío, información, temporalidad y perspectivas categoriales. El marco conceptual considera cinco perspectivas —Individualidad, Dualidad, Totalidad, Evolución e Involución— y una estructura combinatoria de trece tríadas, tres posiciones locales y dos fases. Se distingue expresamente esa propuesta de lo que verifica el software disponible. El repositorio `IOM-verified` contiene una biblioteca Lean 4 mínima con un tipo de estado formado por un entero y una lista de cadenas, tres operadores (`E`, `Ivo`, `S_rev`) y un único teorema Lean explícito: `strict_fixed_point`, que establece que el ciclo conserva los estados vacíos. También incluye un generador de un grafo RDF de 78 instancias `OntoNode` y formas SHACL para restricciones estructurales locales. Las comprobaciones automatizadas no demuestran la teoría filosófica completa, la consistencia lógica global, una transformación sin repetición ni propiedades globales de simetría. Se describen los artefactos, su alcance y los pasos para reproducir sus verificaciones.

**Palabras clave:** ontología, vacío, información, temporalidad discreta, Lean 4, RDF, SHACL, reproducibilidad.

---

## 1. Introducción

Realidad I.O propone pensar el vacío no como un espacio físico, sino como una condición conceptual asociada a la ausencia de contenido informativo, y estudiar su relación con estados que sí contienen información. El marco también organiza ciertas categorías mediante perspectivas y tríadas. Estas ideas se presentan aquí como una **propuesta filosófica y un programa de formalización**, no como resultados establecidos por la física ni como conclusiones derivadas íntegramente por un asistente de pruebas.

El objetivo de esta versión del artículo es describir con precisión tanto la propuesta como la implementación existente. Para evitar confundir niveles de evidencia, se usan tres distinciones:

1. **Propuesta conceptual:** definiciones e interpretaciones filosóficas que plantea el marco.
2. **Artefacto computacional:** estructuras y reglas codificadas en Lean, Python, RDF y SHACL.
3. **Resultado comprobado:** propiedades efectivamente aceptadas por Lean o conformidades reportadas por el validador SHACL.

La compilación de Lean confirma que el código Lean del proyecto compila y que el teorema incluido se acepta. SHACL evalúa las formas declaradas sobre el grafo RDF cargado. Ninguno de esos hechos, por sí solo, prueba todas las interpretaciones teóricas del artículo.

---

## 2. Marco conceptual

### 2.1. Vacío y estado informativo

Como notación conceptual, se denomina **vacío** al estado sin contenido informativo, y **estado informativo** a uno que contiene algún contenido. La implementación usa una representación más concreta y limitada: un estado Lean consta de un instante entero y una lista finita de cadenas:

\[
\texttt{State} = (\texttt{time}:\mathbb{Z},\;\texttt{payload}:\texttt{List String}).
\]

El constructor `vacuum t` produce el estado `(t, [])`. En consecuencia, dentro del programa, vacío significa específicamente **lista vacía**. La lista de cadenas no formaliza un universo general de unidades informativas, ni incorpora una teoría de significado, equivalencia, redundancia o contenido físico.

### 2.2. Cinco perspectivas

El vocabulario del proyecto considera las etiquetas `Ind`, `D`, `Tot`, `Evol` e `Invol`, interpretadas en la propuesta como Individualidad, Dualidad, Totalidad, vector Evolutivo y vector Involutivo. En el grafo, son valores permitidos de la propiedad `hasPerspective`. Su presencia como etiquetas RDF no formaliza por sí misma sus interpretaciones filosóficas ni una teoría de relaciones entre ellas.

La propuesta conceptual separa las tres primeras etiquetas, asociadas a modos de ser o de organización, de las dos últimas, asociadas a direcciones de cambio. Esta distinción es una organización interpretativa del marco, no un teorema Lean ni una restricción global de SHACL.

### 2.3. Estructura de tríadas

El generador recorre trece índices de tríada (`0` a `12`), dos fases (`adv` y `ret`) y tres posiciones locales (`0`, `1` y `2`). Por tanto, crea:

\[
13\times 2\times 3 = 78
\]

instancias de `io:OntoNode`. Para cada instancia, el script asigna la dirección según la fase (`evol` para `adv`; `invol` para `ret`) y calcula la perspectiva con el índice `(triad_idx + pos) mod 5`. Empareja las instancias `adv` y `ret` de igual índice y posición mediante `mirrorOf` en ambos sentidos.

Estas son reglas de construcción del generador. La existencia de los 78 nodos y de esos enlaces en el grafo generado no equivale a una demostración de una simetría categorial universal ni de las interpretaciones de las tríadas.

---

## 3. Operadores incluidos en Lean

### 3.1. Definiciones del código

La biblioteca Lean actual define tres operadores; no define el operador `S_fwd`, una función `red`, ni una transformación categorial `iota`. Para un estado `s = (t, p)`, las definiciones exactas son:

\[
E(t,p)=(t+1,p),
\]

\[
Ivo(t,p)=(t-1,p),
\]

\[
S_{rev}(t,p)=
\begin{cases}
(t,[]) & \text{si }p=[],\\
(t-1,[]) & \text{si }p\ne[].
\end{cases}
\]

Estas ecuaciones resumen `IOM/Operators.lean`. En particular, para cualquier estado no vacío, `S_rev` descarta el payload y retrocede un paso temporal. Esta definición de código no debe confundirse con formulaciones más generales del marco que invoquen reducción de redundancia, inversión de categorías u otros operadores aún no implementados.

### 3.2. Ciclo y teorema formalizado

Se considera el ciclo `S_rev (Ivo (E s))`, equivalente a la composición \(S_{rev}\circ Ivo\circ E\) con la convención usual de aplicación de derecha a izquierda.

Para `vacuum t = (t, [])`, las definiciones implican:

| Paso | Estado |
|:---|:---|
| `vacuum t` | `(t, [])` |
| `E (vacuum t)` | `(t + 1, [])` |
| `Ivo (E (vacuum t))` | `(t, [])` |
| `S_rev (Ivo (E (vacuum t)))` | `(t, [])` |

El repositorio formaliza exactamente esta propiedad como:

```lean
theorem strict_fixed_point (t : Int) :
  S_rev (Ivo (E (vacuum t))) = vacuum t := by rfl
```

La prueba se cierra por reducción definicional (`rfl`). La igualdad es exacta para los estados construidos por `vacuum`.

Para un estado con payload no vacío, una evaluación directa de las definiciones produce `(t - 1, [])` después del ciclo. Esto es una descripción del comportamiento del código, pero el repositorio **no contiene un teorema Lean separado** que formalice una propiedad de no repetición o un atractor para esos estados. Tampoco contiene una prueba de que dicho resultado sea una propiedad de la teoría ontológica general.

### 3.3. Alcance de la verificación

`lake build` compila la biblioteca declarada en `lakefile.lean` usando la versión fijada en `lean-toolchain` (`leanprover/lean4:v4.9.0`). La compilación no demuestra automáticamente proposiciones informales que no estén expresadas como tipos o teoremas Lean. En el estado documentado aquí, hay **un teorema explícito**, `strict_fixed_point`; no hay una suite de 16 teoremas.

---

## 4. Grafo RDF y validación SHACL

### 4.1. Datos generados

El script `scripts/generate_ontology.py` genera `ontology/io_ontology.ttl`, un grafo Turtle con 78 sujetos tipados como `io:OntoNode`. Cada instancia recibe índice de tríada, fase, posición local, dirección, perspectiva, el valor booleano `restoresVacuum = true` y un enlace `mirrorOf`. El espacio de nombres empleado es `http://example.org/iom#`; funciona como identificador del vocabulario de ejemplo del proyecto, no como prueba de que exista un vocabulario OWL publicado y formalmente axiomatizado.

El script genera instancias RDF. No hay en este artefacto una demostración de que los nodos representen exhaustivamente una realidad ontológica, ni una inferencia automática del significado de `restoresVacuum` a partir de los operadores Lean.

### 4.2. Restricciones SHACL efectivamente declaradas

`ontology/io_shapes.ttl` declara un `NodeShape` dirigido a los nodos de clase `io:OntoNode`, con restricciones locales para siete propiedades:

| Propiedad | Comprobación local declarada |
|:---|:---|
| `hasTriadIndex` | Un valor entero entre 0 y 12, inclusive. |
| `hasPhase` | Exactamente un valor, perteneciente a `adv` o `ret`. |
| `hasLocalPos` | Exactamente un entero, perteneciente a 0, 1 o 2. |
| `hasDirection` | Exactamente un valor, `evol` o `invol`. |
| `hasPerspective` | Exactamente un valor de `Ind`, `D`, `Tot`, `Evol` o `Invol`. |
| `restoresVacuum` | Exactamente un valor con valor booleano verdadero. |
| `mirrorOf` | Al menos un valor y como máximo uno. No se comprueba que el enlace sea recíproco ni que apunte a una instancia existente. |

Estas son restricciones por nodo y propiedad. La forma actual no exige que el grafo tenga exactamente 78 nodos, que estén presentes todas las combinaciones índice/fase/posición, que cada referencia `mirrorOf` sea recíproca, ni que la perspectiva siga una secuencia global. Tales propiedades no deben atribuirse a SHACL en esta versión.

### 4.3. Pruebas y significado del resultado

La suite Python contiene dos pruebas de regresión: (1) verifica que el grafo cargado contiene 78 sujetos `OntoNode` y que conforma con la forma SHACL; (2) cambia el índice de un nodo a 13 y verifica que el grafo deja de conformar. El validador `scripts/validate_shacl.py` ejecuta PySHACL y comunica la conformidad del grafo cargado.

Una respuesta `Conforms: True` significa que los datos evaluados satisfacen las restricciones SHACL cargadas. No significa que el modelo filosófico sea verdadero, que el grafo sea completo respecto de una ontología externa o que se haya probado la corrección semántica de sus interpretaciones.

---

## 5. Reproducibilidad y automatización

La versión Lean está fijada por `lean-toolchain`. Las dependencias Python para RDFLib y PySHACL se declaran en `requirements.txt`. Desde la raíz del repositorio, los pasos principales son:

```bash
lake build
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/generate_ontology.py
python scripts/validate_shacl.py
```

El flujo de GitHub Actions en `.github/workflows/ci.yml` ejecuta la compilación Lean y las comprobaciones de generación y validación RDF/SHACL en `push` y `pull_request`. El estado concreto de una ejecución de CI debe consultarse en la interfaz de GitHub; la mera presencia del archivo de flujo no se presenta como evidencia de que una ejecución remota haya pasado.

---

## 6. Discusión

La implementación actual es deliberadamente acotada frente al alcance filosófico sugerido por Realidad I.O. Su aporte verificable es una pequeña representación ejecutable que conecta una definición de vacío como payload vacío, tres funciones sobre estados, un teorema de punto fijo para el estado vacío y una tabla de datos RDF sometida a reglas SHACL locales.

Conviene no identificar tres niveles distintos de afirmación:

- La composición conserva el vacío **en el caso definido y probado** por `strict_fixed_point`.
- La lectura de las perspectivas, los vectores y el cierre del circuito pertenece a la propuesta conceptual mientras no se formalice y se pruebe de manera correspondiente.
- La conformidad SHACL se refiere exclusivamente a las restricciones de datos descritas en la sección 4.

En particular, el código disponible no demuestra una ley general de no repetición, un comportamiento de atractor, la consistencia global de axiomas de temporalidad y reciprocidad, ni una isomorfía entre la semántica Lean y el grafo RDF. La formalización de esas afirmaciones requeriría definiciones adicionales, enunciados explícitos y pruebas o validaciones adecuadas.

---

## 7. Conclusiones

1. Realidad I.O se presenta como una propuesta ontológica sobre vacío, información y organización categorial; su interpretación filosófica excede la formalización computacional actualmente incluida.
2. La biblioteca Lean representa estados como pares de tiempo entero y lista de cadenas, define `E`, `Ivo` y `S_rev`, y contiene un teorema explícito: `strict_fixed_point`.
3. El teorema prueba, por reducción definicional, que el ciclo devuelve `vacuum t` cuando se parte de un estado vacío. No prueba una propiedad de no repetición para estados informativos.
4. El generador RDF produce 78 instancias de `OntoNode`; las formas SHACL comprueban restricciones estructurales locales para siete propiedades, no integridad global ni semántica filosófica.
5. La compilación Lean, las pruebas Python y el validador SHACL proporcionan comprobaciones reproducibles y de alcance limitado. Las afirmaciones más amplias deberán incorporarse al código antes de describirse como verificadas.

---

## Disponibilidad de código

El código y los artefactos descritos están en el repositorio **IOM-verified**:

<https://github.com/luisreygarciafigueroa-creator/IOM-verified>

El repositorio está configurado como **privado** al momento de esta revisión, por lo que el acceso depende de los permisos concedidos por su propietario. Incluye los módulos Lean, el generador RDF, las formas SHACL, pruebas Python, instrucciones de reproducción y un flujo de integración continua.

---

## Referencias

1. Moura, L. de & Ullrich, S. (2021). *The Lean 4 Theorem Prover and Programming Language*. En *Automated Deduction – CADE 28*. Springer.
2. W3C. (2014). *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation.
3. W3C. (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation.
4. García Figueroa, L. R. (2026). *IOM-verified: Realidad I.O — implementación Lean y validación RDF/SHACL* [código fuente]. GitHub: <https://github.com/luisreygarciafigueroa-creator/IOM-verified>.

---

## Apéndice A. Correspondencia entre afirmaciones y artefactos

| Afirmación | Artefacto que la respalda | Límite |
|:---|:---|:---|
| `vacuum t` es un estado con payload vacío | `IOM/Core.lean` | Lista vacía como representación concreta. |
| El ciclo conserva el estado vacío | `strict_fixed_point` en `IOM/Operators.lean` | Solo el caso vacío codificado. |
| El grafo generado contiene 78 nodos | `scripts/generate_ontology.py` y prueba Python | No demuestra completitud ontológica global. |
| El grafo satisface las formas SHACL cargadas | `ontology/io_shapes.ttl`, `scripts/validate_shacl.py` | Solo las restricciones locales descritas arriba. |
| Las pruebas de código se ejecutan en cambios | `.github/workflows/ci.yml` | El resultado de cada ejecución debe verificarse en GitHub Actions. |

---

*Fin del artículo.*
