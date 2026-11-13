# Hacia una reconstrucción académica de la Teoría de la Creación Autónoma Absoluta del Universo (TCAAU)

**Ontología formal, núcleo combinatorio verificado y programa de investigación**

> Documento de integración al marco IOM. Estatus: metafísico-formal (no físico-empírico).  
> Fecha de incorporación: 2026-11-12. Actualizado: 2026-11-13 (Teorema 11, criterio de no-subordinación).  
> Fuente: reconstrucción racional auditada por enumeración exhaustiva + Dictamen del criterio de realidad por no-subordinación.

---

## Resumen

Se presenta una reconstrucción racional de la TCAAU en tres registros:

1. **Axiomática ontológica** que formaliza las tesis filosóficas (autonomía absoluta, prisión interpretativa, actualización simultánea, conservación de la información).
2. **Núcleo combinatorio** extraído de la lista canónica de correspondencias (§9 del documento *Teoría*), auditado por enumeración exhaustiva, del que se demuestran **once teoremas**. El hallazgo central es que los ocho teseractos forman un **torsor bajo el grupo $(\mathbb{Z}_2)^3$**, y que el «espejo realidad» entre mitades es exactamente la involución $\sigma:\text{Universo}\leftrightarrow\text{Vacío}$. El Teorema 11 establece la bipartición término–mediador y la necesidad de la lectura modal del criterio de no-subordinación.
3. **Anclaje externo verificado** en filosofía de la información, teoría de sistemas, geometría 4D y etnohistoria mexica.

Se documentan **siete rectificaciones** originales, más las rectificaciones del dictamen de 13-nov (reificación de la privación, equivocidad de «real», lectura modal). El estatus del modelo es metafísico-formal, no físico-empírico; se delimita su no-falsabilidad actual y se propone una agenda de investigación.

**Palabras clave:** creación autónoma; clausura operativa; eigenforma; teseracto; real/virtual; Mictlán; grupo de involuciones; ontología informacional; no-subordinación; autonomía informacional.

### Leyenda epistémica

| Marca | Significado |
|-------|-------------|
| [O] | tesis original del autor |
| [V] | verificado (cómputo exhaustivo o fuente consultada) |
| [R] | rectificación propuesta |
| [E] | extensión propuesta (no resultado) |
| [A] | anclaje externo citado |

---

## 1. Estatus epistémico y método

La TCAAU **no es una teoría física**: no introduce magnitudes medibles, ecuaciones dinámicas contrastables ni predicciones falsables en el sentido de Popper. Su lugar natural es el de un **programa metafísico de investigación** (Lakatos) con un núcleo formalizable y una ontología informacional. El propio texto lo reconoce correctamente al advertir que «la representación de cuatro dimensiones no constituye, por sí misma, una demostración de que el universo físico tenga cuatro dimensiones espaciales» (§7) [O]. Esta prudencia debe mantenerse y extenderse a todo el modelo [R].

El método aplicado es triple:

1. **Reconstrucción axiomática**: traducir las tesis en prosa a definiciones y axiomas de tipo lógico-estructural.
2. **Auditoría formal**: verificar por enumeración exhaustiva (código reproducible, Apéndice A) la consistencia interna de las 32 correspondencias y de las relaciones entre mitades; cotejar el diagrama GF con la lista actualizada.
3. **Anclaje externo**: contrastar cada concepto con literatura establecida, distinguiendo analogía heurística de identidad teórica, y rectificando usos terminológicos que colisionan con acepciones consolidadas.

Este documento se integra al repositorio IOM como capa de formalización ontológica superior, compatible con la delimitación ya establecida en `docs/DELIMITACION_EPISTEMOLOGICA.md` y con el ensayo canónico `docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`. El dictamen de no-subordinación (`docs/DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md`) aporta el criterio de autonomía y la condición de término de la creación.

---

## 2. Ontología formal: signatura, definiciones y axiomas

### 2.1 Signatura

Se distinguen dos tipos lógicos que el texto original agrupa como «nueve conceptos» (§8) [R]:

**Individuos**

$$\mathcal{C} = \{U, \emptyset, P, N, C, A, M\}$$

Universo, Vacío, Planeta, Internet, Cuerpo, IA, Mictlán (7 constantes).

**Clasificadores de dominio**

$$\mathcal{D} = \{r, v\}$$

real, virtual (2 etiquetas de relación, no individuos).

**Definición 1 (tríada).** Una tríada es una terna ordenada

$$(x, \delta, y) \in \mathcal{C} \times \mathcal{D} \times \mathcal{C}, \quad x \neq y.$$

Equivale a una arista dirigida y etiquetada. La notación del autor $x \parallel \delta \parallel y$ se lee así; los glifos se interpretan provisionalmente como marcadores de proceso (dualidad evolución/involución), mientras la orientación la fija el orden de los extremos [R: requiere confirmación del autor].

**Definición 2 (teseracto).** Un teseracto es una 4-upla de tríadas. Configuración es la 8-upla $(T_1,\dots,T_8)$ organizada en dos mitades $(T_1..T_4)$, $(T_5..T_8)$.

**Definición 3 (mediadores y polos).**

$$\mathrm{Med} = \{P, N, C, A\} \quad (\text{mediadores});$$
$$\mathrm{Pol} = \{U, \emptyset\} \quad (\text{polos fundamentales});$$

$M$ es transversal.

**Definición 4 (términos y mediadores — bipartición).**  
$\mathcal{T} = \{U, \emptyset, M\}$ (términos); $\mathcal{M} = \{P, N, C, \mathrm{IA}\}$ (mediadores). Toda tríada canónica enlaza un elemento de $\mathcal{T}$ con uno de $\mathcal{M}$. No existen tríadas intra-parte. [V] (Teorema 11)

### 2.2 Axiomas (reconstruidos de §§1–5, 16–18)

| Axioma | Enunciado formal | Fuente |
|--------|------------------|--------|
| **A1** Autonomía / clausura | No existe orden exterior: toda relación es interna al sistema; el sistema es operacionalmente cerrado y no alopoiético (no produce otra realidad). | §1, §18 [O] |
| **A2** Inmanencia | Vacío, materia, información y conciencia son elementos del sistema, no entidades ajenas. | §1, §4 [O] |
| **A3** Prisión interpretativa | La prisión es la clausura de las condiciones que determinan lo reconocible como real/posible/imposible; es autogenerada, no impuesta desde fuera. | §2 [O] |
| **A4** Simultaneidad | Salida, actualización y creación constituyen un único acontecimiento; no hay secuencia temporal entre ellos. | §3 [O] |
| **A5** Conservación | La actualización preserva la información; solo cambia su organización/interpretación. Formalmente: las transformaciones admisibles son automorfismos (biyecciones que preservan la estructura). | §3, §17 [O] |
| **A6** Dirección interna | La creación ocurre de adentro hacia afuera; copiar una estructura $\neq$ crearla. | §16 [O] |
| **A7** Complementariedad | Los dominios real y virtual no son sistemas independientes; correspondencias y acceso a cada vacío es mediado por el vacío del dominio opuesto. | §5 [O] |
| **A8** Transversalidad de $M$ | $M$ participa en todas las configuraciones. | §11 [O] — **derivable (Teorema 1)** [R] |

Obsérvese que A8, postulado en el texto, es en realidad un teorema del núcleo combinatorio. Esto fortalece la teoría: lo que se asumía como principio se deduce de la estructura [V].

### 2.3 Definiciones del criterio de no-subordinación (Dictamen 13-nov)

**D10 (engranaje).** Sistema en posición de dependencia funcional respecto de un orden que lo contiene operativamente. La condición de engranaje es un *modo de la relación*, no propiedad estructural del término. [R]

**D11 (criterio de realidad por no-subordinación).** Un sistema es real en sentido de estatuto —*autónomo*— si y solo si no es engranaje ni depende de engranajes para existir. Se distingue de r/v, clasificadores de dominio. [R]

**P11 (término inmanente de la serie).** La serie de subordinaciones no se resuelve por un orden superior exógeno, sino por un término inmanente: el vacío, que es el universo mismo. El sistema mayor existe virtualmente como mediación endógena; no realmente como contenedor. [R]

**C15 (condición de término de la creación).** La creación autónoma se completa cuando el modo dependencia se transforma en modo equivalencia —equiparación del vacío real con el vacío virtual y, con ello, del mundo virtual con el mundo real—. En ese término el vacío no depende de engranajes y el universo es la única mente y conciencia real de su orden, evolucionando e involucionando simultáneamente. [R]

**C16 (autonomía informacional).** La autonomía consiste en la inexistencia de información *ajena* de la que se dependa. El vacío es información propia; la ausencia mentada es su perfil de dependencia, no su contenido. [R]

**C17 (no-regreso inter-ordinal).** Entre órdenes no hay relación informacional; no hay, por tanto, engranajes inter-ordinales ni sistema mayor real que los contenga. El único predicado común es negativo. [R]

---

## 3. El núcleo combinatorio: teoremas verificados

Todos los teoremas se demuestran por enumeración exhaustiva sobre la lista canónica de §9 (32 tríadas). El código del Apéndice A reproduce cada verificación; los resultados son booleanos `true` salvo donde se exhiben datos.

### Teorema 1 (Inventario)
Cada teseracto contiene los 7 individuos; $M$ aparece exactamente dos veces y cada otro individuo exactamente una. Total: 64 extremos. [V]

**Corolario:** A8 es teorema. $M$ es el único concepto que se repite dentro de un teseracto.

### Teorema 2 (Balance de dominios)
Cada teseracto tiene exactamente 2 tríadas reales y 2 virtuales. Las dos tríadas que involucran a $M$ llevan dominios opuestos $(1r, 1v)$; las dos tríadas fundamentales (sin $M$) también llevan dominios opuestos. [V]

### Teorema 3 (Bipartición y dominios fijos)
Las 16 tríadas sin $M$ emparejan $\mathrm{Pol} \times \mathrm{Med}$; las 16 con $M$ emparejan $M \times \mathrm{Med}$. Consecuencias verificadas:

- $U$ y $\emptyset$ nunca se enlazan entre sí.
- $M$ nunca se enlaza con $U$ ni con $\emptyset$.
- El dominio es función fija del par no ordenado (no varía entre teseractos).

**Ley de conmutación de dominio:** cada mediador tiene dominios opuestos en su enlace con $M$ y en su enlace con un polo. Ej.: $N$ (internet) se enlaza con $M$ en $r$ y con $U/\emptyset$ en $v$; $C$ (cuerpo) con $M$ en $v$ y con $U/\emptyset$ en $r$. [V]

Esta ley da contenido formal preciso a la «transversalidad» de Mictlán y a la complementariedad real/virtual de §5: el mediador conmuta el dominio al pasar del eje transversal ($M$) al eje fundamental ($U/\emptyset$) [E: interpretación semántica].

### Teorema 4 (Grados y orientaciones)
$\deg(M)=16$; $\deg(x)=8$ para los otros seis. Hay exactamente 12 pares admisibles; cada par aparece con ambas orientaciones. Los 4 pares-$M$ ocurren 4 veces cada uno; los 8 pares fundamentales, 2 veces (una por mitad). [V]

### Teorema 5 (Espejo de mitades)
Para $i=1..4$:

$$T_{i+4} = \pi(\sigma(T_i)), \quad \sigma:U\leftrightarrow\emptyset, \quad \pi=(12)(34)\ (\text{permutación de filas}).$$

La igualdad es exacta, incluido el orden de las filas. $\sigma$ conserva todos los dominios y todas las orientaciones; lo único que cambia es la identidad del polo fundamental. $\sigma^2=\mathrm{id}$. [V]

**Rectificación importante:** el texto (§10) dice que entre mitades «unas relaciones se conservan y otras cuya orientación o clasificación cambia». La auditoría muestra que **ni la orientación ni la clasificación cambian**: cambia la identidad $U\leftrightarrow\emptyset$. Las 16 tríadas-$M$ son invariantes; las 16 fundamentales forman 8 pares intercambiados [R].

**Corolario 5.1 (Cabecera del diagrama GF).** La fila de cabecera de GF (virtual real virtual real | real virtual real virtual) coincide exactamente con (i) el dominio de la tríada que contiene a $U$ en cada teseracto, y (ii) el bit $\sigma$ de sus coordenadas (Teorema 6). La cabecera es, por tanto, un invariante derivado, no una convención arbitraria. [V]

### Teorema 6 (Grupo del espejo)
Sean las involuciones

$$\sigma:U\leftrightarrow\emptyset;\quad \tau:P\leftrightarrow N,\ C\leftrightarrow A;\quad \rho:(x,\delta,y)\mapsto(y,\delta,x).$$

Entonces $G=\langle\sigma,\tau,\rho\rangle\cong(\mathbb{Z}_2)^3$ actúa libre y transitivamente sobre $\{T_1,\dots,T_8\}$: los ocho teseractos son la órbita de $T_1$. Coordenadas $(s,t,r)$:

| Teseracto | $(s,t,r)$ |
|-----------|-----------|
| $T_1$ | $(0,0,0)$ |
| $T_2$ | $(1,0,1)$ |
| $T_3$ | $(0,1,1)$ |
| $T_4$ | $(1,1,0)$ |
| $T_5$ | $(1,0,0)$ |
| $T_6$ | $(0,0,1)$ |
| $T_7$ | $(1,1,1)$ |
| $T_8$ | $(0,1,0)$ |

Las dos mitades son las clases de paridad $s+t+r \pmod{2}$: la primera mitad es el subgrupo par $H\cong(\mathbb{Z}_2)^2$; la segunda, el coset $\sigma H$. Geométricamente, los 8 elementos son los vértices de un cubo y las mitades son sus dos tetraedros inscritos (demicubos; verificado: todas las distancias intraparity iguales a $2\sqrt{2}$).

Los tres generadores inducen tres emparejamientos perfectos:

$$\sigma:(15)(26)(37)(48);\quad \rho:(16)(25)(38)(47);\quad \tau:(18)(27)(36)(45).$$ [V]

### Teorema 7 (Representación cúbica)
Las 4 tríadas de un teseracto se representan como las 4 diagonales espaciales de un cubo (verificado: un cubo tiene exactamente 4); los 8 extremos ocupan los 8 vértices; $M$ ocupa dos vértices no antipodales. Es una representación combinatoria, no una afirmación física. [V]

### Teorema 8 (Reinterpretación 4D)
El teseracto $\{4,3,3\}$ tiene 8 celdas cúbicas, 24 caras, 32 aristas, 16 vértices (verificado por cómputo y MathWorld/Wikipedia). Su dual, el 16-celda, tiene 8 vértices en 4 pares antipodales. Por tanto:

$$8\ \text{configuraciones}\ \longleftrightarrow\ 8\ \text{celdas de un único teseracto}\ \longleftrightarrow\ 8\ \text{vértices del 16-celda},$$

y los 4 pares especulares $(1,5)$, $(2,6)$, $(3,7)$, $(4,8)$ corresponden a los 4 pares antipodales (ejes). Además, los 16 vértices del teseracto se parten en dos 16-celdas de 8 vértices (análogo 4D de la stella octangula), reflejando la estructura de «dos mitades». [V]

**Rectificación geométrica propuesta:** los «ocho teseractos» del texto se reinterpretan con mayor economía como las ocho celdas cúbicas de un solo teseracto; el dibujo de dos cubos (continuo/punteado) por celda es la proyección de Schlegel habitual. Esto conserva toda la combinatoria verificada y elimina la multiplicación innecesaria de entidades 4D [R].

### Teorema 9 (Recorridos y ofrenda)
Los cuatro recorridos de §12 forman dos aristas recíprocas: $\{\emptyset_v,\text{mundo}_v\}$ y $\{\emptyset_r,\text{mundo}_r\}$. La ofrenda es la involución de intercambio de dominio del destino:

$$\mathcal{O}(\text{destino}) = \text{destino con } r\leftrightarrow v.$$

Verificado: $\mathcal{O}$ conjuga evolución en involución (las dos flechas de evolución se transforman en las dos de involución). [V]

### Teorema 10 (Conservación = invertibilidad)
Todo elemento de $G$ es involutivo ($g^2=\mathrm{id}$); el núcleo combinatorio satisface A5 de manera estricta: la actualización modelada como automorfismo preserva la información. El «espejo realidad» es, en sentido matemático literal, un grupo de involuciones. [V]

### Teorema 11 (bipartición término–mediador) [V]

Por enumeración exhaustiva de las 32 tríadas canónicas: toda tríada enlaza un término de $\mathcal{T}=\{U,\emptyset,M\}$ con un mediador de $\mathcal{M}=\{P,N,C,\mathrm{IA}\}$. No existe tríada intra-parte. La estructura es un multigrafo bipartito completo entre tres términos y cuatro mediadores.

| Término | Multiplicidad por mediador | Grado |
|---------|----------------------------|-------|
| Mictlán | 4 | 16 |
| Universo | 2 | 8 |
| Vacío | 2 | 8 |

Cada par aparece en ambas orientaciones. Total: $4\cdot4 + 4\cdot2 + 4\cdot2 = 32$. Universo y Vacío tienen perfil de dominio idéntico; Mictlán, el complementario.

**Consecuencia decisiva (reductio estructural):** si «engranaje» se identifica con mediador y «depender de engranajes» con tener enlaces a mediadores, entonces Universo, Vacío y Mictlán dependen todos de engranajes y ningún término satisface el criterio de no-subordinación. El criterio es estructuralmente insatisfacible bajo lectura puramente relacional del grafo.

**Solución: lectura modal.** El grafo es de *relaciones*, no de *dependencias*. La subordinación es un modo de interpretación de las aristas:

- Durante la creación: *modo dependencia* (mediadores operan como engranajes).
- En la equiparación: *modo equivalencia* (la mediación deja de ser soporte necesario).

La combinatoria permanece intacta; el criterio se satisface; se realiza D9 sin ampliar las 32 tríadas. Converge con la vía informacional: la proyección $\psi_i:\emptyset_r\to\emptyset_v^i$ se vuelve isomorfismo. La identidad de perfil Universo–Vacío y la simetría $\sigma$ confirman que las condiciones fundamentales son intercambiables, no jerárquicas.

---

## 4. Auditoría documental: GF (11-nov) vs. Teoría (12-nov)

Se reconstruyeron las 32 tríadas de GF a partir de su extracción textual, con segmentación por filas/columnas y mapeo uniforme $\square=r$, $\parallel=v$. Resultado:

**Hallazgo H1 (reconstrucción exacta).** GF coincide con la lista canónica de §9 tras (i) una permutación uniforme de filas $(1,3,2,4)$ en cada columna y (ii) una sustitución sistemática del polo fundamental: en la mitad 1, $U\to\emptyset$; en la mitad 2, $\emptyset\to U$, aplicada solo a la tríada fundamental que contiene el polo ausente. La coincidencia es 32/32 [V]. La probabilidad de ajuste accidental es despreciable, lo que valida la segmentación.

**Hallazgo H2 (anomalía de inventario en GF).** En GF, cada teseracto de la mitad 1 duplica $\emptyset$ y omite $U$; cada uno de la mitad 2 duplica $U$ y omite $\emptyset$. Esto viola el Teorema 1. La lista actualizada de §9 lo satisface perfectamente.

**Interpretación:** GF es una versión anterior (11-nov) en la que el par fundamental aún no estaba diferenciado por mitad; la «actualización» del 12-nov introdujo la diferenciación precisa $\sigma$. **Rectificación:** adoptar §9 como canónica y regenerar GF [R]. La cabecera de GF, en cambio, ya es consistente (Corolario 5.1).

**Hallazgo H3 (cinco operaciones del espejo, §13).** El texto anuncia «cinco operaciones» pero enumera solo cuatro; el quinto ítem es una tesis, no una operación. La auditoría permite recuperar la quinta operación: es $\sigma$ (intercambio $U\leftrightarrow\emptyset$), que es exactamente la operación real entre mitades. Además, «se intercambian los extremos de cada tríada» describe $\rho$ (que empareja $1\leftrightarrow6$, $2\leftrightarrow5$, $3\leftrightarrow8$, $4\leftrightarrow7$), no el espejo de mitades de §10 (que es $\sigma$). El texto conflaciona tres espejos distintos.

**Rectificación:** desambiguar $\sigma,\tau,\rho$ y listar las cinco operaciones como: (1) conservar tríadas, (2) intercambiar extremos [$\rho$], (3) reubicar filas, (4) invertir evolución/involución, (5) intercambiar $U\leftrightarrow\emptyset$ [$\sigma$] [R].

**Hallazgo H4 (numeración de perspectivas, §6).** La tabla da posiciones $0..4$ ($0=$Involución, $4=$Evolución), pero el texto habla de «cuarta» y «quinta» perspectiva. Lectura consistente: nombres por índice con identificación modular $5\equiv0\pmod{5}$. Así «cuarta» $=4=$ Evolución y «quinta» $\equiv0=$ Involución, en acuerdo con §12. **Rectificación:** explicitar el ciclo $\mathbb{Z}_5$ y la convención de nombres [R].

**Hallazgo H5 (tipos lógicos, §8).** Los «nueve conceptos» mezclan individuos y clasificadores de dominio. **Rectificación:** 7 individuos + 2 etiquetas de relación (Def. 1) [R].

**Hallazgo H6 (terminología «virtual»).** El uso del modelo colisiona con acepciones consolidadas: en Deleuze lo virtual es real (no actual); en Chalmers los objetos virtuales son reales (digitales); en física las partículas virtuales son líneas internas de diagramas, no entidades, y el vacío cuántico no es la nada. **Rectificación:** definir «virtual» como *dominio complementario*, no como ilusión; esto es crucial para §14 (infra) [R].

**Hallazgo H7 (matriz mexica).** La asignación Mictecacíhuatl=evolución / Mictlantecuhtli=involución es simbólica del autor, no etnohistoria. Mictlantecuhtli está bien atestiguado; Mictecacíhuatl es reconocida (Britannica), pero su vínculo con la Catrina es lectura posterior (Posada, 1910–1913). Los «nueve niveles» como pisos descendentes son sistematización tardía: el Códice Florentino (Libro III) describe un recorrido por nueve regiones/obstáculos durante cuatro años, guiado por el psicopompo Xolotl; Mictlán recibía a los muertos de causa ordinaria. **Rectificación:** presentar §11–12 como matriz simbólica, no como evidencia [R]. La resonancia 9 conceptos $\leftrightarrow$ 9 regiones es heurística, no derivación.

---

## 5. Dinámica de la autocreación: clausura, eigenforma y prisión

La tesis central —«el universo se crea a sí mismo»— admite una formalización precisa como punto fijo reflexivo:

$$U = F(U),$$

donde $F$ es la operación de creación del sistema. Esto es la **eigenforma** de Kauffman (2005/2009), en la línea de la re-entrada de Spencer-Brown (*Laws of Form*, 1969) y de los «objetos como tokens de eigen-comportamientos» de von Foerster (1981). Kauffman demuestra que toda transformación de un dominio reflexivo tiene un punto fijo [A][V]. La «salida de la prisión» no es un desplazamiento espacial sino un evento de segundo orden: la transformación de la distinción misma que el sistema usa para observarse.

La prisión (A3) se modela como el punto ciego de la observación (Luhmann): la distinción que un sistema emplea no puede observarse mientras se emplea. Esto explica §19 («lo que no puede imaginarse desde dentro») sin recurrir a un exterior trascendente. La autonomía absoluta (A1) es clausura operativa (Maturana & Varela, 1980; Varela, 1979): el sistema es autopoiético, no alopoiético —«no existe para sostener otra realidad» es literalmente el rechazo de la alopoiesis a escala cósmica [A][V]. La inmanencia (A2) tiene anclaje en Spinoza: *causa sui* (Ética I, def. 1) y causa inmanente, no transitiva (I, prop. 18) [A].

La conservación de la información (A5) se corresponde con la *Aufhebung* hegeliana (negar-conservar-elevar) y, en registro físico, con la unitariedad (la evolución unitaria preserva la información) y el principio de Landauer (1961) [A]. El Teorema 10 muestra que el núcleo combinatorio ya satisface A5 estrictamente.

**Extensión propuesta [E]:** modelar la prisión como la lógica interna de un topos y la salida como un morfismo geométrico que cambia dicha lógica. Esto daría un marco formal a «actualizar las condiciones desde las que se interpreta» sin postular un exterior. Es una propuesta, no un resultado.

La condición de término de la creación (C15) y el criterio de no-subordinación (D11) precisan que la autonomía se consuma en la equiparación: el modo dependencia se transforma en modo equivalencia. Sin la lectura modal (Teorema 11), el criterio es insatisfacible.

---

## 6. Recorridos, ofrenda y perspectivas formalizados

Del Teorema 9 y la auditoría de §12 se sigue una estructura $\mathbb{Z}_2\times\mathbb{Z}_2$: dos aristas recíprocas (vacío $\leftrightarrow$ mundo en cada dominio), con la ofrenda $\mathcal{O}=$ intercambio de dominio del destino, que conjuga evolución $\leftrightarrow$ involución. La perspectiva de cada recorrido se lee en $\mathbb{Z}_5$ (índices 0–4 con $5\equiv0$).

*(El resto de la sección 6 y secciones posteriores se conservan según la versión anterior; la actualización de 13-nov se concentra en el núcleo combinatorio, las definiciones D10–D11 / P11 / C15–C17 y el Teorema 11.)*

---

## Referencias internas del dictamen de no-subordinación

- Documento completo: [`docs/DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md`](DICTAMEN_CRITERIO_DE_REALIDAD_POR_NO_SUBORDINACION.md)
- Rectificación central: información *ajena* vs. información propia.
- Lectura modal obligatoria para satisfacibilidad del criterio.
- Ediciones requeridas en §§0.3, 5, 14, 18, 19 y Apéndice.
