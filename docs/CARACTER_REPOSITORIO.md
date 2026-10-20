# Carácter del repositorio IOM

> **Enfoque canónico:** el marco I.O. se lee como **isomorfismo operativo** entre la arquitectura de cinco perspectivas + 13 tríadas y la cosmología náhuatl de los **Cinco Soles** y el **Mictlán**.

Este repositorio **no** se presenta prioritariamente como producto de software ni como prueba genérica de «validez semántica en el mundo real». Su eje es **equiparar y cartografiar**:

1. Las **cinco perspectivas** con los **cinco soles** (ciclo de edades / principios cosmológicos).
2. Cada perspectiva con una **figura ancla** del mito del Quinto Sol y del inframundo.
3. Las **13 tríadas** con la **estructura del Mictlán** (camino, niveles y polaridades de la región de los muertos).

La formalización Lean 4, OWL/SHACL y los 78 nodos siguen siendo la **bóveda bancaria** (invariante técnica). El *sentido* del repositorio es la equivalencia cosmológica náhuatl.

---

## 1. Equivalencia perspectivas ↔ figuras

| Perspectiva I.O. | Figura ancla | Lectura operativa |
|------------------|--------------|-------------------|
| **Individualidad** | **Nanahuatzin** | Singularidad que se entrega al fuego; el sol que nace del sacrificio del cuerpo mínimo. Unidad irreductible. |
| **Dualidad** | **Xólotl** | Gemelo / doble de Quetzalcóatl; tránsito, desdoblamiento, acompañamiento al inframundo. Polaridad y reflejo (`mirrorOf`). |
| **Totalidad** | **Tecuciztécatl** | Pretensión de totalidad / plenitud solar; el que aspira a ser el sol y queda como luna. Integración ambicionada del sistema. |
| **Evolución** | **Mictecacíhuatl** | Señora del Mictlán; vector de renovación / ciclo de la muerte que genera continuidad. Proyección hacia nueva estructura. |
| **Involución** | **Mictlantecuhtli** | Señor del Mictlán; disolución, oscuridad, retorno al vacío-matriz. Reabsorción de estructura. |

> **Nota:** Tecuciztécatl y Nanahuatzin son, en las fuentes del Quinto Sol, los candidatos a convertirse en sol; Xólotl opera el desdoblamiento y el paso; Mictecacíhuatl y Mictlantecuhtli rigen el Mictlán. La tabla fija **anclas semánticas del marco I.O.**, no un orden histórico único de los Cinco Soles elementales (*Ehécatl, Quiáhuitl, Atl, Océlotl, Ollin*).

---

## 2. Cinco perspectivas ↔ Cinco Soles

Las cinco perspectivas se **equiparan** al ciclo de los Cinco Soles como principios de temporalización y transformación:

| Orden operativo | Principio solar (edades) | Perspectiva |
|-----------------|--------------------------|-------------|
| I | Edad / principio de movimiento inicial (viento, apertura) | Individualidad (Nanahuatzin) |
| II | Edad de fuego / prueba | Dualidad (Xólotl) |
| III | Edad de agua / disolución parcial | Totalidad (Tecuciztécatl) |
| IV | Edad de tierra / devoración | Evolución (Mictecacíhuatl) |
| V | *Nahui Ollin* — Sol de Movimiento (edad presente) | Involución ↔ cierre de ciclo con Mictlantecuhtli / apertura del camino |

La **lucha** (Tezcatlipoca ↔ Quetzalcóatl; Tecuciztécatl ↔ Nanahuatzin) se modela con `mirrorOf`. Los **cataclismos** y el **camino al Mictlán** se modelan con `creates` bajo los vectores Evolución / Involución.

---

## 3. Trece tríadas ↔ Mictlán

Las **13 tríadas** del núcleo canónico se equiparan a la **arquitectura del Mictlán**:

- Cada tríada es un **umbral o nivel relacional** del camino (no necesariamente 1:1 con los nueve niveles literarios del Códice Vaticano A).
- Las posiciones **→ / 0 / ←** dentro de cada tríada corresponden a polos de tránsito (entrada, mediación, retorno).
- Las fases **adv / ret** corresponden a proyección hacia estructura (salida del vacío) y disolución hacia el vacío-matriz (Tlaltecuhtli / Mictlán).
- `mirrorOf` = polaridad cielo ↔ inframundo, vida ↔ muerte, Nanahuatzin ↔ Tecuciztécatl, etc.
- `creates` = generación de edad, de *teyolia* en tránsito, o de disolución hacia Mictlantecuhtli / Mictecacíhuatl.

El Mictlán no se trata aquí como «infierno» cristiano, sino como **topología de las 13 tríadas**: lugar de los muertos y ruta al origen.

---

## 4. Qué permanece y qué cambia

| Capa | Estado |
|------|--------|
| 78 nodos, Lean, SHACL, CSV canónicos | **Inmutables** (bóveda técnica) |
| Carácter del proyecto | **Cambia:** eje = equivalencia cosmológica náhuatl |
| EXP-A…E | Siguen como capas de verificación; EXP-E es el experimento natural de este carácter |
| Dominio prioritario | [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md) · medios en `media/cosmos_nahuatl/` |

---

## 5. Lectura breve del mito bajo el marco

1. **Nanahuatzin** (Individualidad) se arroja al fuego → nace el sol.
2. **Tecuciztécatl** (Totalidad) duda y sigue; queda como luna (totalidad reflejada, no solar).
3. **Xólotl** (Dualidad) desdobla y acompaña el tránsito.
4. El ciclo de edades (Cinco Soles) despliega las cinco perspectivas.
5. **Mictecacíhuatl** y **Mictlantecuhtli** (Evolución / Involución) cierran el vector en el Mictlán, que **es** el sistema de tríadas.

Documento de dominio: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md).  
Relaciones formales: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).
