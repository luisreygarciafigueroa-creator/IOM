# Dominio: Mitología comparada e historia de las religiones

> **Carácter:** demostración de *alineación semántica* al marco I.O., no
> teoría de dominio validada en campo ni síntesis de las obras citadas.
> La ontología core (78 nodos) permanece inmutable. Sin anotación ciega
> propia, este dominio **no** aporta Fleiss' κ ni evidencia de validez
> semántica de campo.
>
> **Derechos de autor:** no se reproduce texto sustancial de las obras;
> solo se cartografían categorías conceptuales de alto nivel de uso común
> en la disciplina, citando las fuentes de trabajo.

**Fuentes de trabajo (literatura secundaria):**

- Francisco Díez de Velasco, *Breve historia de las religiones* / *Introducción a la Historia de las Religiones* (Alianza; óptica científica, no religiocéntrica).
- José F. W. Lora Cam, *Mitologías Universales y Latinoamericanas* (Editorial Tercer Mundo, 2006).
- Dominio relacionado ya en el repo: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md) (Cinco Soles, Mictlán).

---

## 1. Principios de cartografía en este dominio

La historia de las religiones (en el sentido de Díez de Velasco) trata las
manifestaciones religiosas como **hechos históricos y culturales**
comparables, no como esencias reveladas. El marco I.O. se usa aquí solo
para etiquetar *roles semánticos* recurrentes (singularidad, polaridad,
sistema, generación, disolución), sin adjudicar verdad religiosa.

| Principio I.O. | Aplicación en este dominio |
|----------------|----------------------------|
| Bóveda de 78 nodos | Ningún dios, mito o rito se añade al core |
| Solo `mirrorOf` / `creates` / `none` | Relaciones candidatas entre conceptos mapeados |
| EXP-A como única validez empírica | Este catálogo no sustituye anotación ciega |
| No religiocentrismo | Ninguna tradición se privilegia como norma |

---

## 2. Categorías transversales → perspectivas I.O.

### 2.1 Individualidad (Ind)

- Figura divina o heroica singular (un dios, un fundador, un rey sagrado).
- Creyente / iniciando como unidad de experiencia.
- Víctima sacrificial individual.

### 2.2 Dualidad (D) — candidata natural a `mirrorOf`

- Sagrado ↔ profano.
- Cielo ↔ inframundo / mundo de los vivos ↔ de los muertos.
- Parejas divinas antagónicas o complementarias (p. ej. fuerzas de orden y caos).
- Vida ↔ muerte como polos del ciclo.

### 2.3 Totalidad (Tot)

- Panteón o sistema de dioses como red integrada.
- Cosmos ordenado (edades del mundo, rumbos, niveles).
- Comunidad ritual / iglesia / asamblea como sistema.

### 2.4 Evolución (Evol) — candidata a `creates`

- Cosmogonía: emergencia del orden desde el caos o el vacío.
- Fundación de un culto, revelación, renovación cíclica (fuego nuevo, año nuevo).
- Aparición de un nuevo Sol / era / dispensación.

### 2.5 Involución (Invol) — candidata a `creates` (hacia disolución)

- Escatología: fin de una edad, diluvio, conflagración, disolución del cosmos.
- Camino al inframundo / descomposición del cuerpo / retorno al origen.
- Decadencia de un orden ritual o colapso de un panteón.

---

## 3. Pares candidatos ilustrativos

Material **no ciego** — solo demostración de mapeo. Plantilla CSV:
`datasets/ingestion/templates/mitologia_religiones.csv`.

| id | source | target | perspectiva sugerida | relación candidata |
|----|--------|--------|----------------------|--------------------|
| REL-01 | sagrado | profano | Dualidad | `mirrorOf` |
| REL-02 | cielo | inframundo | Dualidad | `mirrorOf` |
| REL-03 | vida | muerte | Dualidad | `mirrorOf` |
| REL-04 | caos primordial | cosmos ordenado | Evolución | `creates` |
| REL-05 | edad del mundo | cataclismo final | Involución | `creates` |
| REL-06 | dios singular | panteón | Ind → Tot | `none` / sistema |
| REL-07 | sacrificio individual | fecundidad colectiva | Ind → Tot | `creates` |
| REL-08 | fundador / revelador | comunidad ritual | Ind → Tot | `creates` |
| REL-09 | camino al más allá | origen / matriz | Involución | `creates` |
| REL-10 | orden cósmico | disolución cíclica | Evol ↔ Invol | `mirrorOf` / ciclo |

El dominio náhuatl ya documentado (Cinco Soles, Mictlán, Tezcatlipoca
↔ Quetzalcóatl) es un caso especial de REL-04, REL-05, REL-02 y REL-09.

---

## 4. Límites explícitos

1. **No** se añaden nodos al core de 78.
2. **No** se afirma que el marco I.O. «explique» o «verifique» ninguna religión.
3. Las categorías son de trabajo disciplinar (historia de las religiones / mitología comparada), no revelaciones.
4. Sin protocolo ciego propio sobre pares de este dominio, **no** hay κ ni validez semántica de campo.
5. Texto de las obras citadas **no** se incluye; solo referencias bibliográficas y mapeo de roles.
6. Se mantiene la separación historia de las religiones / teología (no normativa, no exclusiva, no esencialista), alineada con la óptica de Díez de Velasco.

---

## 5. Gobernanza respecto a EXP-A…E

| Capa | Rol respecto a este dominio |
|------|-----------------------------|
| EXP-A | Única vía para validar interpretabilidad de pares religiosos mapeados |
| EXP-B / EXP-C | Prerrequisitos formales del núcleo; no juzgan mitos |
| EXP-D | Diagnóstico sintético; **prohibido** como prueba de significado religioso |
| EXP-E | Este documento amplía el catálogo de alineación; no sustituye bio/econ |

Manual de alineación: [`MANUAL_ALINEACION_DOMINIOS.md`](MANUAL_ALINEACION_DOMINIOS.md).  
Catálogo: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md).

---

## 6. Referencias de trabajo

- Díez de Velasco, F. *Breve historia de las religiones* / *Introducción a la Historia de las Religiones*. Alianza Editorial.
- Lora Cam, J. F. W. (2006). *Mitologías Universales y Latinoamericanas*. Editorial Tercer Mundo, Arequipa.
- Interno: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md) · [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
