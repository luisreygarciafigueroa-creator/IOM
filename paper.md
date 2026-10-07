# Realidad I.O.: demostración del punto fijo del vacío y validación estructural

## Resultados verificados con Lean 4 y RDF/SHACL

**Autor:** Luis Rey García Figueroa · **Fecha:** octubre de 2026

## Resumen

Este artículo presenta dos resultados computacionales de Realidad I.O. Primero, Lean 4.9.0 verifica para todo entero `t` que la composición de los operadores de evolución, involución y supresión retroactiva deja invariante el estado vacío. La demostración está formalizada en el teorema `strict_fixed_point`. Segundo, el generador produce una ontología RDF en Turtle con las 78 combinaciones de 13 tríadas, dos fases y tres posiciones locales; el grafo satisface las restricciones SHACL de cardinalidad, valores, correspondencia entre fase y dirección, asignación de perspectiva y simetría de espejos. Las siete pruebas de regresión confirman las propiedades del grafo y detectan mutaciones que las contradicen. Se documentan las definiciones, las demostraciones y los pasos exactos para reproducir los resultados.

**Palabras clave:** Lean 4, demostración formal, estado vacío, operador temporal, RDF, Turtle, SHACL, validación estructural.

## 1. Objetivo y resultados

El trabajo formaliza una dinámica discreta de estados y comprueba sus propiedades ejecutables. Los resultados presentados son:

1. El vacío `vacuum t` es un punto fijo de `S_rev (Ivo (E (vacuum t)))` para todo `t : Int`.
2. El generador crea los 78 identificadores esperados para el producto de 13 tríadas, 2 fases (`adv`, `ret`) y 3 posiciones locales.
3. Cada nodo satisface las restricciones estructurales SHACL, incluidas la relación recíproca con su espejo, la compatibilidad fase-dirección y la fórmula de selección de perspectiva.
4. La suite de pruebas confirma la conformidad del grafo y rechaza ejemplos alterados con índice, espejo, dirección o perspectiva incompatibles.

## 2. Estado y operadores formalizados

### 2.1. Representación

`IOM/Core.lean` define `State` mediante dos campos:

- `time : Int`, el índice temporal;
- `payload : List String`, el contenido del estado.

El estado vacío en el tiempo `t` se define como:

\[
V_t = vacuum(t) = (t, []).
\]

### 2.2. Operadores

`IOM/Operators.lean` implementa los siguientes operadores:

| Operador | Definición | Efecto comprobado |
|---|---|---|
| `E` | `(t, A) ↦ (t + 1, A)` | Avanza un instante y conserva el contenido. |
| `Ivo` | `(t, A) ↦ (t − 1, A)` | Retrocede un instante y conserva el contenido. |
| `S_rev` | `(t, []) ↦ (t, [])`; `(t, A) ↦ (t − 1, [])` cuando `A ≠ []` | Conserva el estado vacío y elimina el contenido de los demás estados. |

## 3. Demostración del punto fijo

**Teorema 1 (`strict_fixed_point`).** Para todo entero `t`,

\[
S_{\mathrm{rev}}\bigl(Ivo(E(vacuum(t)))\bigr) = vacuum(t).
\]

**Demostración.** La aplicación sucesiva de las definiciones da:

\[
E(vacuum(t)) = (t+1, []),
\]

\[
Ivo(E(vacuum(t))) = (t, []),
\]

\[
S_{\mathrm{rev}}(Ivo(E(vacuum(t)))) = S_{\mathrm{rev}}(t, []) = (t, []) = vacuum(t).
\]

La igualdad vale para todo `t : Int`. Lean 4.9.0 verifica el enunciado mediante reducción definicional (`rfl`), y `lake build` compila el módulo que contiene el teorema. ∎

## 4. Generación y validación de la ontología

### 4.1. Conjunto de nodos

El script `scripts/generate_ontology.py` genera `ontology/io_ontology.ttl` a partir de las dimensiones siguientes:

\[
13 \text{ tríadas} \times 2 \text{ fases} \times 3 \text{ posiciones locales} = 78 \text{ nodos}.
\]

Los identificadores cubren índices de tríada `0`–`12`, fases `adv` y `ret`, y posiciones `0`–`2`. Cada nodo contiene una dirección (`evol` para `adv`; `invol` para `ret`), una perspectiva seleccionada según `P[(índice de tríada + posición local) mod 5]` y el literal booleano `restoresVacuum = true`. Para cada combinación de tríada y posición, los nodos de ambas fases se enlazan recíprocamente mediante `mirrorOf`.

### 4.2. Invariantes SHACL

Las formas de `ontology/io_shapes.ttl` se aplican a instancias de `io:OntoNode` y validan:

- el rango del índice de tríada, de `0` a `12`, y de la posición local, de `0` a `2`;
- los valores admitidos y cardinalidad de fase, dirección y perspectiva;
- el valor booleano `true` de `restoresVacuum` y un único destino `mirrorOf` que sea un nodo ontológico;
- la reciprocidad de `mirrorOf`, con igual tríada y posición y fases opuestas;
- la correspondencia `adv=evol` y `ret=invol`;
- la selección de perspectiva conforme al índice de tríada y la posición local.

## 5. Pruebas y reproducción

La suite `tests/test_ontology.py` contiene siete pruebas. Comprueba el conjunto exacto de los 78 nodos, la conformidad global, la alineación de los espejos y las reglas de dirección y perspectiva. Además, verifica que SHACL rechace un índice fuera de rango, un espejo desalineado, una dirección incompatible con la fase y una perspectiva incompatible con la fórmula.

Desde la raíz del repositorio, con Lean 4.9.0 instalado mediante Elan y Python 3.9 o posterior, se reproduce la verificación con:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
```

Resultados observados en octubre de 2026:

- `lake build`: compilación correcta;
- pruebas Python: **7 de 7 pasaron**;
- generación RDF: **78 nodos**;
- validación SHACL: **`Conforms: True`**;
- CI de GitHub: verificaciones de Lean y RDF/SHACL exitosas.

## 6. Conclusión

La composición `S_rev ∘ Ivo ∘ E` deja fijo el vacío `vacuum t` para todo entero `t`, resultado demostrado y compilado en Lean 4.9.0. La ontología generada contiene las 78 combinaciones previstas y satisface las restricciones SHACL que especifican sus propiedades y relaciones. La suite de regresión confirma esas invariantes y detecta las alteraciones estructurales probadas.

Estos resultados establecen una demostración formal del comportamiento definido para el estado vacío y una validación reproducible de la estructura RDF/SHACL de Realidad I.O.

## Disponibilidad de código y datos

El código y los datos están disponibles en el [repositorio IOM](https://github.com/luisreygarciafigueroa-creator/IOM). Los módulos Lean están en `IOM/`; el generador, el validador y las pruebas Python están en `scripts/` y `tests/`; y los archivos RDF/SHACL están en `ontology/`.

## Referencias

- Moura, L. de, & Ullrich, S. (2021). The Lean 4 Theorem Prover and Programming Language. En *Automated Deduction – CADE 28*. Springer.
- W3C. (2014). *RDF 1.1 Turtle: Terse RDF Triple Language*. W3C Recommendation.
- Knublauch, H., & Kontokostas, D. (2017). *Shapes Constraint Language (SHACL)*. W3C Recommendation.

---

**Nota de versión:** resultados reproducidos sobre el código y las validaciones de `main`, octubre de 2026.
