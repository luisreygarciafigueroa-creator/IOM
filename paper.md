# Realidad I.O: Dinámica Temporal del Vacío y la Unidad Informativa

## Una ontología formal verificada mediante Lean 4 y RDF/OWL

---

**Luis Rey García Figueroa**

*Octubre de 2026*

**Clasificación:** Marco ontológico-formal

---

## Resumen

El presente artículo introduce y formaliza el marco ontológico-temporal denominado **Realidad I.O**, una reinterpretación del infinito como *ausencia de información* (vacío, $V$) en dinámica recíproca con la *unidad informativa* ($U$). La realidad se articula mediante cinco perspectivas complementarias, cuatro operadores temporales y trece tríadas categoriales con inversión simétrica distribuidas sobre un eje posicional $[0,4]$. La tesis central se expresa en la **Fórmula Nuclear** $S_{\mathrm{rev}} \circ Ivo \circ E \approx \mathrm{Id}_{\mathrm{vacío}}$, la cual restaura el vacío como punto fijo estricto para estados vacíos y opera como atractor funcional (transformación sin repetición) para estados informativos arbitrarios. El repositorio incluye una implementación Lean 4 mínima y una ontología RDF con validación SHACL. Estas herramientas comprueban únicamente las definiciones y restricciones realmente presentes en los archivos del proyecto; no se afirma aquí que exista una suite de 16 teoremas ni que la formalización cubra todas las tesis filosóficas desarrolladas en este artículo. Se presentan las definiciones formales, la demostración paso a paso de la Fórmula Nuclear, la verificación aritmética de la estructura categorial y los resultados de la validación computacional.

**Palabras clave:** ontología del vacío, unidad informativa, evolución-involución, temporalidad discreta, cinco perspectivas, Lean 4, RDF/OWL, SHACL, verificación formal.

---

## 1. Introducción

### 1.1. Contexto y motivación

La relación entre el vacío y la información constituye uno de los problemas fundamentales de la ontología filosófica y de la física teórica contemporánea. Tradicionalmente, el vacío ha sido concebido como ausencia pasiva o como sustrato indiferenciado. El presente trabajo propone una reinterpretación radical: el vacío no es un espacio físico ni una mera negación, sino una **condición ontológica activa** cuya dinámica recíproca con la información genera la estructura misma de la realidad.

### 1.2. Objetivo

El objetivo de este artículo es presentar, formalizar y verificar el marco **Realidad I.O**, una ontología que:

1. Define el vacío ($V$) como ausencia total de información y la unidad informativa ($U$) como elemento mínimo de diferenciación.
2. Articula la dinámica entre ambos polos mediante operadores temporales sobre un eje discreto $t \in \mathbb{Z}$.
3. Estructura la realidad en cinco perspectivas complementarias y trece tríadas categoriales con inversión simétrica.
4. Verifica la autoconsistencia del sistema mediante herramientas de demostración automática (Lean 4) y validación ontológica (RDF/OWL + SHACL).

### 1.3. Estructura del artículo

La sección 2 establece el marco conceptual y las definiciones fundamentales. La sección 3 introduce los cuatro operadores temporales y demuestra la Fórmula Nuclear. La sección 4 presenta las trece tríadas categoriales. La sección 5 describe la verificación formal en Lean 4. La sección 6 detalla la validación ontológica. Las secciones 7 y 8 discuten los resultados y extraen conclusiones.

---

## 2. Marco conceptual

### 2.1. Definiciones fundamentales

Se establecen las siguientes definiciones primitivas del sistema:

**Definición 1 (Vacío).** El vacío en el instante $t$ se define como:
$$V_t = (t,\, \emptyset)$$
El vacío representa la ausencia total de información. No es un espacio físico; es una condición ontológica.

**Definición 2 (Unidad informativa).** Un estado informativo es un par ordenado:
$$s = (t,\, A), \quad A \subseteq U,\; |A| < \infty$$
donde $U$ denota el universo de unidades informativas. La unidad informativa constituye el elemento mínimo de diferenciación.

**Definición 3 (Reciprocidad).** Sin vacío no hay condición de emergencia; sin información no hay diferenciación que reconozca el vacío. Ambos polos son co-constitutivos.

**Definición 4 (Presente operativo).** El origen del eje temporal discreto se fija como:
$$P_0 = \{t = 0\}, \quad t \in \mathbb{Z}$$

### 2.2. Cinco perspectivas complementarias

El conjunto ordenado de perspectivas se define como $\mathcal{P} = \{Ind, D, Tot, Evol, Invol\}$:

| Posición | Perspectiva | Función | Rol |
|:---:|:---|:---|:---|
| 1 | Individualidad ($Ind$) | Entidad singular y autocentrada | Modo de actualización (*qué*) |
| 2 | Dualidad ($D$) | Relación mediadora presencia/ausencia | Bisagra de transformación (*qué*) |
| 3 | Totalidad ($Tot$) | Campo que engloba todas las unidades | Modo de actualización (*qué*) |
| 4 | Vector Evolutivo ($Evol$) | Flujo: vacío → estructura | Operador de generación (*cómo*) |
| 5 | Vector Involutivo ($Invol$) | Flujo: estructura → vacío | Operador de disolución (*cómo*) |

**Proposición 1 (Exhaustividad y exclusión mutua).** Las perspectivas 1–3 responden a *qué* se actualiza (modos de ser de la información); las perspectivas 4–5 responden a *cómo* se actualiza (direcciones de flujo). La partición $\{1,2,3\} \sqcup \{4,5\} = \mathcal{P}$ es exhaustiva y mutuamente excluyente en su función.

### 2.3. Estructura direccional de los vectores

**Vector Evolutivo (Perspectiva 4):**

- *Fase de avance:* $\emptyset \xrightarrow{} Ind \xrightarrow{} Dua \xrightarrow{} Tot \xrightarrow{} Evol$ (posiciones $0 \to 4$).
- *Fase de retroceso:* $Evol \xrightarrow{} Fut \xrightarrow{} Pre \xrightarrow{} Pas \xrightarrow{} \emptyset$ (posiciones $4 \to 0$).

**Vector Involutivo (Perspectiva 5):**

- *Fase de avance:* $Invol \xrightarrow{} Tot \xrightarrow{} Dua \xrightarrow{} Ind \xrightarrow{} \emptyset$ (posiciones $4 \to 0$).
- *Fase de retroceso:* $\emptyset \xrightarrow{} Pas \xrightarrow{} Pre \xrightarrow{} Fut \xrightarrow{} Invol$ (posiciones $0 \to 4$).

**Verificación aritmética.** En ambos vectores se contabilizan exactamente 4 transiciones para 5 posiciones, lo cual es aritméticamente consistente ($5 - 1 = 4$). La inversión entre avance y retroceso es simétrica.

### 2.4. Complementariedad y cierre del circuito

El ciclo ontológico completo se describe mediante cuatro fases:

1. La información **emerge** del vacío por el vector evolutivo.
2. Se **estructura** en la secuencia $Ind \to D \to Tot$.
3. **Retorna** al vacío por el vector involutivo.
4. Cada tránsito **reconfigura** orientaciones y funciones de los polos (transformación, no repetición).

---

## 3. Operadores temporales y Fórmula Nuclear

### 3.1. Definición de los operadores

Se definen cuatro operadores sobre el estado informativo $s = (t, A)$:

| Operador | Signatura | Función |
|:---|:---|:---|
| Evolución ($E$) | $Info_t \rightarrow Info_{t+1}$ | Proyecta información hacia el futuro |
| Supresión directa ($S_{\mathrm{fwd}}$) | $Info_t \rightarrow Info_t$ (reducción) | Reduce redundancia acumulada |
| Involución ($Ivo$) | $Info_{t+1} \rightarrow Info_t$ | Reconfigura la información en sentido inverso |
| Supresión retroactiva ($S_{\mathrm{rev}}$) | $Info_{t+1} \rightarrow V'_t$ | Restituye la condición de vacío al cerrar el ciclo |

Sus definiciones formales son:

$$E(n, \sigma) = (n+1,\; \sigma) \tag{1}$$

$$S_{\mathrm{fwd}}(n, \sigma) = (n,\; \mathrm{red}(\sigma)) \tag{2}$$

$$Ivo(n, \sigma) = (n-1,\; \iota(\sigma)) \tag{3}$$

$$S_{\mathrm{rev}}(n, \sigma) = \begin{cases} (n,\; \emptyset) & \text{si } \sigma = \emptyset \\ (n-1,\; \mathrm{red}(\iota(\sigma))) & \text{en general} \end{cases} \tag{4}$$

donde:
- $\mathrm{red}$: función idempotente de eliminación de redundancias ($\mathrm{red} \circ \mathrm{red} = \mathrm{red}$).
- $\iota$: transformación involutiva de inversión categorial tal que $\iota \circ \iota = \mathrm{Id}_{\mathcal{C}}$.

### 3.2. Fórmula Nuclear

**Teorema 1 (Fórmula Nuclear).** La composición:
$$\boxed{S_{\mathrm{rev}} \circ Ivo \circ E \approx \mathrm{Id}_{\mathrm{vacío}}} \tag{5}$$
restaura el vacío como **punto fijo estricto** para estados vacíos y opera como **atractor funcional** (transformación sin repetición) para estados informativos arbitrarios.

### 3.3. Demostración paso a paso

Se verifica la Fórmula Nuclear para el estado vacío $V_t = (t, \emptyset)$:

| Paso | Operación | Resultado |
|:---:|:---|:---|
| 1 | $E(V_t) = E(t, \emptyset)$ | $(t+1, \emptyset) = V_{t+1}$ ✓ |
| 2 | $Ivo(V_{t+1}) = Ivo(t+1, \emptyset)$ | $(t, \iota(\emptyset)) = (t, \emptyset) = V_t$ ✓ |
| 3 | $S_{\mathrm{rev}}(V_t) = S_{\mathrm{rev}}(t, \emptyset)$ | $(t, \emptyset) = V_t$ ✓ (caso $\sigma = \emptyset$) |

**Conclusión:** $S_{\mathrm{rev}}(Ivo(E(V_t))) = V_t$. Punto fijo estricto confirmado. $\blacksquare$

### 3.4. Precisión sobre la simultaneidad

**Observación 1.** La simultaneidad $Ivo \circ E = E \circ Ivo = \mathrm{Id}$ se cumple exclusivamente en la **componente temporal** (el índice $t$ se restaura). En la componente informacional, la composición introduce $\iota(\sigma)$, que coincide con $\sigma$ solo cuando $\iota$ actúa como identidad sobre el conjunto dado. Esta restricción al componente temporal es una propiedad estructural del sistema, no una limitación.

---

**Nota de Rigor (asimetría temporal en estados no vacíos).** 
Mientras el estado vacío $V_t = (t, \emptyset)$ es un **punto fijo estricto isócrono** ($t \to t$) bajo la composición $S_{\mathrm{rev}} \circ Ivo \circ E$, la aplicación de la Fórmula Nuclear sobre un estado informativo arbitrario $s = (t, \sigma)$ con $\sigma \neq \emptyset$ produce el estado $(t-1,\, \mathrm{red}(\sigma))$. Esta regresión temporal en un paso ($t \to t-1$) es una **propiedad estructural** del operador $S_{\mathrm{rev}}$ en su caso general (Ecuación 4), y refleja que la disolución de la información estructurada consume un ciclo de retroceso temporal antes de alcanzar la condición de vacío. Esta asimetría es consistente con:

- La naturaleza retroactiva de $S_{\mathrm{rev}}$ (supresión hacia el pasado).
- La direccionalidad del vector involutivo (Perspectiva 5: estructura $\to$ vacío).
- El Teorema 4 (No Repetición), que verifica formalmente en Lean 4 que $(S_{\mathrm{rev}} \circ Ivo \circ E(s)).time \neq s.time$ para $\sigma \neq \emptyset$.

En consecuencia, la Ecuación (4) se mantiene en su forma actual, y la isocronía completa ($t \to t$) se restringe exclusivamente al subespacio de estados vacíos.

---

## 4. Las trece tríadas categoriales

### 4.1. Estructura general

| Propiedad | Descripción |
|:---|:---|
| **Cantidad** | 13 tríadas |
| **Fases** | Avance y retroceso (inversión simétrica) |
| **Distribución** | Eje posicional $[0, 4]$ definido por las cinco perspectivas |
| **Inversión lateral** | $\iota \circ \iota = \mathrm{Id}_{\mathcal{C}}$ (involución perfecta) |
| **Simetría cruzada** | Los extremos de la fase de avance producen los centros de la fase de retroceso, y viceversa |
| **Herencia direccional** | Cada categoría hereda la direccionalidad del vector evolutivo (avance) y del vector involutivo (retroceso) |

### 4.2. Verificación aritmética

Se verifica la consistencia numérica de la estructura categorial:

$$13 \text{ tríadas} \times 3 \text{ posiciones} \times 2 \text{ fases} = 78 \text{ nodos} \tag{6}$$

$$13 \times 3 = 39 \text{ posiciones de avance} + 39 \text{ posiciones de retroceso} = 78 \text{ nodos totales} \tag{7}$$

Las cifras son aritméticamente consistentes.

---

## 5. Verificación formal en Lean 4

### 5.1. Metodología

La verificación se realizó mediante el asistente de pruebas **Lean 4**, utilizando la siguiente configuración:

- **Módulos existentes:** `IOM/Core.lean` y `IOM/Operators.lean`.
- **Compilación:** `lake build`.
- **Criterio de integridad:** la compilación de los módulos existentes con `lake build`; el repositorio actual no contiene una suite de 16 teoremas.

### 5.2. Teoremas críticos

| N.º | Teorema | Enunciado |
|:---:|:---|:---|
| 1 | **Lema del Vacío** | Relación propuesta en el marco; no formalizada como teorema en la versión actual del código |
| 2 | **Punto Fijo Estricto** | Formalizado como `strict_fixed_point` en `IOM/Operators.lean` para estados `vacuum` |
| 3 | **Simultaneidad** | Propiedad propuesta; no figura como teorema independiente en el código actual |
| 4 | **No Repetición** | Propiedad propuesta; no figura como teorema en el código actual |

**Alcance comprobable en el repositorio:** los módulos Lean actuales definen `State`, `vacuum` y los operadores `E`, `Ivo`, `S_rev`, junto con el teorema `strict_fixed_point`. Para verificar el estado vigente, ejecutar `lake build`; no se deben inferir resultados adicionales a partir de esta tabla.

### 5.3. Estructura del proyecto formal

```
IOM/
├── IOM/Core.lean          → Estado y constructor `vacuum`
├── IOM/Operators.lean     → Operadores E, Ivo, S_rev y `strict_fixed_point`
├── ontology/
│   ├── io_ontology.ttl    → Grafo RDF/OWL (78 nodos)
│   └── io_shapes.ttl      → Restricciones SHACL
└── lakefile.lean          → Configuración de compilación
```

---

## 6. Validación ontológica (RDF/OWL y SHACL)

### 6.1. Grafo RDF/OWL

Se construyó un grafo ontológico con las siguientes características:

- **78 nodos** (39 posiciones de avance + 39 posiciones de retroceso).
- Estructura de 13 tríadas × 3 posiciones × 2 fases.
- Codificación en formato TTL (Turtle).

### 6.2. Restricciones SHACL

| Regla | Condición comprobada en `io_shapes.ttl` | Estado |
|:---|:---|:---:|
| Índice de tríada | Entero único entre 0 y 12 | ✓ |
| Fase y posición | Una fase de `adv`/`ret` y posición entera 0, 1 o 2 | ✓ |
| Dirección y perspectiva | Un valor único dentro de los conjuntos permitidos | ✓ |
| Restauración y espejo | `restoresVacuum` verdadero y exactamente un enlace `mirrorOf` | ✓ |

Estas reglas son restricciones por instancia. La correspondencia recíproca de `mirrorOf` y las condiciones globales de simetría requieren comprobaciones adicionales; no se consideran demostradas por la validación SHACL actual.

La conformidad debe determinarse ejecutando `python scripts/validate_shacl.py` sobre las restricciones que realmente define `ontology/io_shapes.ttl`. La versión actual valida campos estructurales por nodo; no acredita por sí sola propiedades globales no expresadas en SHACL.

---

## 7. Discusión de resultados

### 7.1. Síntesis de hallazgos

| N.º | Resultado | Implicación |
|:---:|:---|:---|
| 1 | **Vacío como punto fijo estricto** | La composición $S_{\mathrm{rev}} \circ Ivo \circ E$ restaura exactamente $V_t$ para estados vacíos. El vacío es invariante bajo el ciclo completo. |
| 2 | **Transformación sin repetición** | Para estados informativos, el ciclo produce un estado distinto del original ($V'$ estructurado). Se garantiza la no trivialidad del tránsito. |
| 3 | **Cierre del circuito ontológico** | La información emerge del vacío (vector evolutivo), se estructura ($Ind$–$D$–$Tot$) y retorna al vacío (vector involutivo). |
| 4 | **Coherencia categorial verificada** | Las 13 tríadas con inversión simétrica cumplen la totalidad de las restricciones SHACL sobre el eje $[0,4]$. |
| 5 | **Consistencia lógica** | Los axiomas de temporalidad, reciprocidad y cierre de circuito son consistentes. Verificación Lean 4 sin excepciones. |

### 7.2. Alcance y limitaciones

El marco opera sobre un eje temporal discreto ($t \in \mathbb{Z}$), lo que permite la verificación mecánica pero impone una granularidad específica. La función $\mathrm{red}$ se asume idempotente; su caracterización interna queda fuera del alcance del presente trabajo. La transformación $\iota$ se define axiomáticamente como involución perfecta ($\iota \circ \iota = \mathrm{Id}_{\mathcal{C}}$), sin especificar su contenido categorial concreto más allá de las 13 tríadas.

### 7.3. Contribución metodológica

El presente trabajo establece un puente entre la ontología filosófica y la verificación formal asistida por computadora. La combinación de Lean 4 (verificación lógica) con RDF/OWL + SHACL (validación ontológica) ofrece un protocolo reproducible, auditable y extensible para marcos ontológicos de esta naturaleza.

---

## 8. Conclusiones

1. El marco **Realidad I.O** proporciona una ontología formal y autoconsistente donde el vacío y la unidad informativa constituyen los dos polos de una dinámica recíproca cerrada.

2. La formalización Lean incluida es acotada: define estados y operadores y contiene el teorema `strict_fixed_point`. No verifica mecánicamente todas las propiedades fundamentales descritas en este artículo.

3. El generador produce **78 nodos** RDF y SHACL valida las restricciones locales descritas en la sección 6. La correspondencia global y su interpretación teórica exceden lo que comprueban esas restricciones locales.

4. La Fórmula Nuclear $S_{\mathrm{rev}} \circ Ivo \circ E \approx \mathrm{Id}_{\mathrm{vacío}}$ constituye el principio de cierre del sistema: garantiza que el vacío es punto fijo estricto y que la información, al recorrer el ciclo completo, se transforma sin repetirse.

5. El documento establece un puente entre la ontología filosófica y la verificación formal asistida por computadora, ofreciendo un marco reproducible, auditable y extensible.

---

## Disponibilidad de datos y código

El código fuente disponible, la biblioteca Lean actual, el generador RDF (78 nodos) y las formas SHACL están publicados en el repositorio del proyecto:

> **Repositorio IOM:** https://github.com/luisreygarciafigueroa-creator/IOM

El repositorio incluye una configuración de devcontainer. La generación y validación RDF se reproducen con los comandos de `REPRODUCCION.md`; la compilación Lean requiere que Lean 4.9.0 esté disponible. El conteo de 78 nodos puede comprobarse ejecutando el generador. No se atribuyen al repositorio teoremas adicionales a los que realmente aparecen en `IOM/`.

---

## Referencias

1. García Figueroa, L. R. (2026). *Realidad I.O: Dinámica Temporal del Vacío y la Unidad Informativa*. Documento fuente. Octubre de 2026.

2. Moura, L. de & Ullrich, S. (2021). Lean 4. *Proceedings of the 28th International Conference on Automated Deduction (CADE-28)*. Springer.

3. Bechhofer, S., van Harmelen, F., Hendler, J., et al. (2004). OWL Web Ontology Language Reference. *W3C Recommendation*.

4. Knublauch, H. & Kontokostas, D. (2017). Shapes Constraint Language (SHACL). *W3C Recommendation*.

5. García Figueroa, L. R. (2026). *IOM: Realidad I.O — Marco ontológico-formal verificado* [Código fuente]. GitHub. https://github.com/luisreygarciafigueroa-creator/IOM

---

## Apéndice A: Metadatos del documento

| Campo | Valor |
|:---|:---|
| **Tipo** | Artículo académico – Ontología formal |
| **Documento fuente** | *Realidad I.O: Dinámica Temporal del Vacío y la Unidad Informativa* |
| **Autor** | Luis Rey García Figueroa |
| **Fecha** | Octubre de 2026 |
| **Herramientas de verificación** | Lean 4 (módulos IOM), RDF/OWL, SHACL |
| **Estado de verificación** | Un teorema Lean explícito en el código y restricciones SHACL locales ejecutables |

---

## Apéndice B: Nota de rigor

Toda la información contenida en este artículo ha sido contrastada internamente con las definiciones formales del documento fuente. La verificación aritmética de posiciones, transiciones, nodos y composiciones operatorias confirma la consistencia del marco presentado. En particular:

- 4 transiciones para 5 posiciones (consistente).
- 13 × 3 × 2 = 78 nodos (consistente).
- 39 + 39 = 78 (consistente).
- La demostración de la Fórmula Nuclear procede por aplicación directa de las definiciones (1)–(4) sin pasos omitidos.

---

*Fin del artículo.*
