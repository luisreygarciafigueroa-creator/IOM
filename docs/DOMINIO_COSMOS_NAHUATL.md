# Dominio: Cosmología náhuatl — Cinco Soles, figuras ancla y Mictlán

> **Carácter:** el marco I.O. se **equipara** a este dominio: cinco perspectivas ↔ Cinco Soles;
> **Nanahuatzin** = Individualidad, **Xólotl** = Dualidad, **Tecuciztécatl** = Totalidad,
> **Mictecacíhuatl** = Evolución, **Mictlantecuhtli** = Involución; **13 tríadas** = **Mictlán**.
> Documento canónico de sentido: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md).
> La ontología core (78 nodos) permanece inmutable como bóveda técnica.

Fuentes integradas (literatura secundaria):

- Roberto Moreno de los Arcos, «Los cinco soles cosmogónicos», *Estudios de Cultura Náhuatl*.
- Mónica Luna López, «El camino al Mictlán: ¿ruta al tormento o al origen?», *Vita Brevis*, 2017.

### Figuras ancla ↔ perspectivas I.O.

| Perspectiva | Figura | Rol en el mito / marco |
|-------------|--------|------------------------|
| Individualidad | **Nanahuatzin** | Se arroja al fuego; nace el Quinto Sol |
| Dualidad | **Xólotl** | Gemelo, desdoblamiento, tránsito al inframundo |
| Totalidad | **Tecuciztécatl** | Aspira al sol; queda como luna (totalidad reflejada) |
| Evolución | **Mictecacíhuatl** | Señora del Mictlán; continuidad del ciclo |
| Involución | **Mictlantecuhtli** | Señor del Mictlán; disolución / vacío |

Las **13 tríadas** se leen como la **topología del Mictlán** (umbrales del camino; no 1:1 forzado con los nueve niveles literarios).

---

## 1. Los Cinco Soles cosmogónicos

El mito postula una sucesión de edades del mundo destruidas por cataclismos asociados a elementos. El orden varía entre fuentes; aquí se usa el de la interpretación de la Piedra del Sol (Chavero / Moreno):

| Sol | Nombre | Destrucción | Transformación típica |
|-----|--------|-------------|----------------------|
| I | *Nahui Ehécatl* (Viento) | Huracanes | Hombres → monos |
| II | *Nahui Quiáhuitl* (Fuego / lluvia de fuego) | Fuego del cielo | Hombres → guajolotes |
| III | *Nahui Atl* (Agua) | Diluvio | Hombres → peces |
| IV | *Nahui Océlotl* (Tierra / tigre) | Temblores / ocelotes | Gigantes devorados |
| V | *Nahui Ollin* (Movimiento) | Edad actual; fin por temblores y hambre | — |

Las cinco perspectivas se **equiparan** a este ciclo de principios (detalle en [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md)).

### Alineación a perspectivas I.O.

| Concepto náhuatl | Perspectiva | Relación candidata | Justificación operativa |
|------------------|-------------|--------------------|-------------------------|
| Nanahuatzin / sol que nace | Individualidad | `creates` | Singularidad sacrificial |
| Xólotl / doble y tránsito | Dualidad | `mirrorOf` | Polaridad y desdoblamiento |
| Tecuciztécatl / luna | Totalidad | — | Plenitud reflejada del sistema |
| Mictecacíhuatl | Evolución | `creates` | Continuidad del ciclo de muertos |
| Mictlantecuhtli | Involución | `creates` | Disolución hacia el vacío |
| Lucha de dioses (Tezcatlipoca ↔ Quetzalcóatl) | Dualidad | `mirrorOf` | Polaridad de fuerzas |
| Cataclismo que destruye la edad | Involución | `creates` | Disolución estructura → vacío |
| Quinto Sol (*Nahui Ollin*) | Totalidad + Evolución | — | Edad presente |

---

## 2. El camino al Mictlán (= sistema de tríadas)

El **Mictlán** se equipara a la **arquitectura de las 13 tríadas**: umbrales relacionales del camino, no «infierno» cristiano. Lecturas recientes (Luna López; Matos Moctezuma; López Austin) lo leen como **ruta al origen** — retorno al útero de la Tierra (Tlaltecuhtli), reciclaje de *teyolia*.

### Niveles (síntesis Códice Vaticano A / Florentino)

| Nivel (Vaticano A) | Lectura operativa |
|--------------------|-------------------|
| 1. La Tierra (Tlaltecuhtli) | Entrada: cueva-matriz que devora |
| 2. Pasadero de agua | Cruce con xoloitzcuintle (eco de Xólotl) |
| 3. Montañas que se juntan | Dualidad vida/muerte |
| 4–5. Obsidiana / viento de navajas | Descomposición del cuerpo |
| 6. Banderas que tremolan | Desprendimiento de valores mundanos |
| 7. Lugar donde se flecha | Obstáculo |
| 8. Corazones comidos (jaguar) | Separación *teyolia* / cuerpo |
| 9. Sin orificio para el humo | Mictlán propio: **Mictlantecuhtli** / **Mictecacíhuatl** |

### Alineación a perspectivas I.O.

| Concepto | Perspectiva | Relación candidata |
|----------|-------------|--------------------|
| Difunto individual | Individualidad (Nanahuatzin) | — |
| Vida ↔ muerte; cielo ↔ inframundo | Dualidad (Xólotl) | `mirrorOf` |
| Cuatro destinos + niveles | Totalidad (Tecuciztécatl) | — |
| Renovación de fuerza anímica | Evolución (Mictecacíhuatl) | `creates` |
| Camino de disolución / retorno | Involución (Mictlantecuhtli) | `creates` |

---

## 3. Pares candidatos para anotación / alineación

Plantilla CSV: `datasets/ingestion/templates/cosmos_nahuatl.csv`.

| id | source | target | perspectiva sugerida | relación candidata |
|----|--------|--------|----------------------|--------------------|
| NAH-01 | Sol de Viento | Sol de Movimiento | Evolución / Involución | `creates` |
| NAH-02 | Tezcatlipoca | Quetzalcóatl | Dualidad | `mirrorOf` |
| NAH-03 | vida | muerte | Dualidad | `mirrorOf` |
| NAH-04 | Tlaltecuhtli | Mictlán | Involución | `creates` |
| NAH-05 | *teyolia* | Mictlán | Individualidad → Totalidad | `creates` |
| NAH-06 | Quinto Sol | cataclismo futuro | Involución | `creates` |
| NAH-07 | Nanahuatzin | Quinto Sol | Individualidad / Evolución | `creates` |
| NAH-08 | Tecuciztécatl | luna | Totalidad | `none` |
| NAH-09 | Xólotl | Quetzalcóatl | Dualidad | `mirrorOf` |
| NAH-10 | Mictecacíhuatl | Mictlantecuhtli | Evolución / Involución | `mirrorOf` |

---

## 4. Límites explícitos

1. **No** se añaden nodos al core de 78.
2. El orden de los Soles **no** se fija como teorema; la equivalencia de perspectivas es **operativa** del marco I.O.
3. Lecturas de «ruta al origen» vs «tormento» son de la literatura secundaria.
4. Sin anotación ciega propia, EXP-A no se reclama como prueba universal.
5. Las fuentes coloniales pueden incorporar categorías cristianas; el mapeo no las «purifica».

---

## 5. Referencias de trabajo

- Moreno de los Arcos, R. «Los cinco soles cosmogónicos». *Estudios de Cultura Náhuatl*.
- Luna López, M. (2017). «El camino al Mictlán…» *Vita Brevis* 6(11).
- León-Portilla, M. *La filosofía náhuatl*.
- Interno: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) · [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) · [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

---

## 6. Medios de referencia

Carpeta: [`docs/media/cosmos_nahuatl/`](media/cosmos_nahuatl/).

| Recurso | Rol |
|---------|-----|
| Piedra del Sol (`Piedra_del_Sol.png`) | Iconografía del Quinto Sol (Nahui Ollin) |
| Láminas codiciales | Dualidad, Xólotl / inframundo, ciclo ritual |
| Tesis *Códice Xólotl* (`PECDSV03T.pdf`) | Edición de divulgación (Peña Cisneros, UAEM 2017) |
