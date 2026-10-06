# Realidad I.O: Dinámica Temporal del Vacío y la Unidad Informativa

## Una ontología formal verificada mediante Lean 4 y RDF/OWL

---

**Luis Rey García Figueroa**

*Octubre de 2026*

**Clasificación:** Marco ontológico-formal

---

## Resumen

El presente artículo introduce y formaliza el marco ontológico-temporal denominado **Realidad I.O**, una reinterpretación del infinito como *ausencia de información* (vacío, $V$) en dinámica recíproca con la *unidad informativa* ($U$). La realidad se articula mediante cinco perspectivas complementarias, cuatro operadores temporales y trece tríadas categoriales con inversión simétrica distribuidas sobre un eje posicional $[0,4]$. La tesis central se expresa en la **Fórmula Nuclear** $S_{\mathrm{rev}} \circ Ivo \circ E \approx \mathrm{Id}_{\mathrm{vacío}}$, la cual restaura el vacío como punto fijo estricto para estados vacíos y opera como atractor funcional (transformación sin repetición) para estados informativos arbitrarios. El marco ha sido verificado formalmente mediante el asistente de pruebas Lean 4 (16 teoremas compilados sin `sorry` ni `admit`) y validado ontológicamente mediante RDF/OWL con restricciones SHACL. Se presentan las definiciones formales, la demostración paso a paso de la Fórmula Nuclear, la verificación aritmética de la estructura categorial y los resultados de la validación computacional.

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

- **Módulos:** `IOM_Core`, `IOM_Operators`, `IOM_Theorems`.
- **Compilación:** `lake build`.
- **Criterio de integridad:** Ausencia total de `sorry` y `admit` en los 16 teoremas.

### 5.2. Teoremas críticos

| N.º | Teorema | Enunciado |
|:---:|:---|:---|
| 1 | **Lema del Vacío** | $E(V_t) = V_{t+1}$; $\;S_{\mathrm{fwd}}(V_t) = V_t$; $\;Ivo(V_t) = V_{t-1}$ |
| 2 | **Punto Fijo Estricto** | $\forall t \in \mathbb{Z}:\; S_{\mathrm{rev}}(Ivo(E(V_t))) = V_t$ |
| 3 | **Simultaneidad** | $Ivo \circ E = E \circ Ivo = \mathrm{Id}$ (componente temporal) |
| 4 | **No Repetición** | $\forall s_0 = (0, \sigma_0),\; \sigma_0 \neq \emptyset:\; S_{\mathrm{rev}} \circ Ivo \circ E(s_0) \neq s_0$ |

**Resultado:** 16 teoremas compilados y verificados sin excepciones.

### 5.3. Estructura del proyecto formal

```
IOM/
├── IOM_Core.lean          → Definiciones: V, U, P, estados, eje temporal
├── IOM_Operators.lean     → E, S_fwd, Ivo, S_rev
├── IOM_Perspectives.lean  → Cinco perspectivas y eje [0,4]
├── IOM_Triads.lean        → 13 tríadas categoriales e inversión ι
├── IOM_Theorems.lean      → 16 teoremas verificados
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

| Restricción | Condición | Estado |
|:---|:---|:---:|
| Consistencia estructural | Cada categoría posee exactamente una fase y posición dentro del eje $[0,4]$ | ✓ |
| Inversión lateral perfecta | Para cada tríada de avance en posición Izquierda, existe su espejo en posición Derecha en retroceso (13/13) | ✓ |
| Cierre de circuito | Toda instancia de $S_{\mathrm{rev}}$ declara `io:restoresVacuum true` | ✓ |
| Coherencia perspectival | Cada instancia declara pertenencia a una de las cinco perspectivas y su dirección de flujo | ✓ |

Las cuatro restricciones estructurales fueron satisfechas en su totalidad.

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

2. La formalización sobre un eje temporal discreto ($t \in \mathbb{Z}$) permite la verificación mecánica de todas las propiedades fundamentales mediante Lean 4, alcanzando **16 teoremas compilados sin excepciones**.

3. La estructura de **cinco perspectivas** y **trece tríadas categoriales** con inversión simétrica queda validada tanto lógica como ontológicamente (RDF/OWL + SHACL), con un total de **78 nodos** y **4 restricciones estructurales** satisfechas.

4. La Fórmula Nuclear $S_{\mathrm{rev}} \circ Ivo \circ E \approx \mathrm{Id}_{\mathrm{vacío}}$ constituye el principio de cierre del sistema: garantiza que el vacío es punto fijo estricto y que la información, al recorrer el ciclo completo, se transforma sin repetirse.

5. El documento establece un puente entre la ontología filosófica y la verificación formal asistida por computadora, ofreciendo un marco reproducible, auditable y extensible.

---

## Disponibilidad de datos y código

El código fuente completo, los 16 teoremas verificados en Lean 4, el grafo ontológico RDF/OWL (78 nodos) y las restricciones SHACL que sustentan los resultados de este artículo están disponibles públicamente bajo licencia MIT en el repositorio oficial del proyecto:

> **Repositorio IOM:** https://github.com/luisreygarciafigueroa-creator/IOM

El repositorio incluye un entorno de Codespaces preconfigurado que permite reproducir la compilación `lake build` y la validación SHACL sin instalación local. Todas las cifras reportadas (13 tríadas × 3 posiciones × 2 fases = 78 nodos; 16 teoremas sin `sorry` ni `admit`) pueden verificarse de forma independiente mediante los scripts contenidos en las carpetas `IOM/`, `ontology/` y `scripts/`.

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
| **Estado de verificación** | 16 teoremas compilados en Lean 4 sin `sorry` ni `admit`; restricciones SHACL validadas |

---

## Apéndice B: Nota de rigor

Toda la información contenida en este artículo ha sido contrastada internamente con las definiciones formales del documento fuente. La verificación aritmética de posiciones, transiciones, nodos y composiciones operatorias confirma la consistencia del marco presentado. En particular:

- 4 transiciones para 5 posiciones (consistente).
- 13 × 3 × 2 = 78 nodos (consistente).
- 39 + 39 = 78 (consistente).
- La demostración de la Fórmula Nuclear procede por aplicación directa de las definiciones (1)–(4) sin pasos omitidos.

---

*Fin del artículo.*
