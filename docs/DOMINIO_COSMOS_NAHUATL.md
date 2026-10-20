# Dominio: Cosmología náhuatl — Cinco Soles y camino al Mictlán

> **Carácter:** demostración de *alineación semántica* al marco I.O., no teoría
> de dominio validada en campo ni reinterpretación histórica de las fuentes.
> La ontología core (78 nodos) permanece inmutable. Para contar como evidencia
> de validez semántica se requiere anotación ciega independiente propia.

Fuentes integradas (literatura secundaria):

- Roberto Moreno de los Arcos, «Los cinco soles cosmogónicos», *Estudios de Cultura Náhuatl*.
- Mónica Luna López, «El camino al Mictlán: ¿ruta al tormento o al origen?», *Vita Brevis*, 2017.

Categorías cosmológicas de referencia (León-Portilla, cit. Moreno): (1) fundamentación universal, (2) temporalización en edades, (3) elementos primordiales, (4) espacialización por rumbos, (5) lucha como molde del acaecer cósmico.

---

## 1. Los Cinco Soles cosmogónicos

El mito postula una sucesión de edades del mundo destruidas por cataclismos
asociados a elementos. El orden varía entre fuentes; aquí se usa el de la
interpretación de la Piedra del Sol (Chavero / Moreno):

| Sol | Nombre | Destrucción | Transformación típica |
|-----|--------|-------------|----------------------|
| I | *Nahui Ehécatl* (Viento) | Huracanes | Hombres → monos |
| II | *Nahui Quiáhuitl* (Fuego / lluvia de fuego) | Fuego del cielo | Hombres → guajolotes |
| III | *Nahui Atl* (Agua) | Diluvio | Hombres → peces |
| IV | *Nahui Océlotl* (Tierra / tigre) | Temblores / ocelotes | Gigantes devorados |
| V | *Nahui Ollin* (Movimiento) | Edad actual; fin por temblores y hambre | — |

Otras fuentes (Anales de Cuauhtitlán, *Historia de los mexicanos por sus pinturas*,
Códice Vaticano A, Motolinía, Ixtlilxóchitl) alteran el orden; el mapeo I.O.
no privilegia un orden canónico único, sino la **estructura de ciclo**.

### Alineación a perspectivas I.O.

| Concepto náhuatl | Perspectiva | Relación candidata | Justificación operativa |
|------------------|-------------|--------------------|-------------------------|
| Cada Sol como edad singular | Individualidad | — | Unidad temporal discreta |
| Lucha de dioses (Tezcatlipoca ↔ Quetzalcóatl) | Dualidad | `mirrorOf` | Polaridad de fuerzas divinas |
| Cosmos de cuatro/cinco edades + rumbos | Totalidad | — | Sistema integrado de ciclos |
| Aparición de un nuevo Sol / creación de hombres | Evolución | `creates` | Proyección vacío → estructura |
| Cataclismo que destruye la edad | Involución | `creates` (hacia disolución) | Disolución estructura → vacío |
| Quinto Sol (edad presente) | Totalidad + Evolución | — | Integración del ciclo actual |

La **lucha** como molde del acaecer cósmico se alinea de forma natural con
Dualidad (`mirrorOf` entre fuerzas opuestas) y con el par Evolución/Involución
como vectores de generación y disolución.

---

## 2. El camino al Mictlán

Cuatro destinos post-mortem según modo de muerte: Chichihualcuahco (nonatos),
Tlalocan (muertes por agua), Tonatiuh Ilhuicac / Sol (guerreros, parturientas),
**Mictlán** (muerte común).

El Mictlán («lugar de los muertos») se asocia a oscuridad, frío, putrefacción,
número 9, Norte / centro / debajo de la Tierra. No es «infierno» cristiano:
fuentes y análisis recientes (Luna López; Matos Moctezuma; López Austin)
lo leen como **ruta al origen** — retorno al útero de la Tierra (Tlaltecuhtli),
reciclaje de fuerza anímica (*teyolia*).

### Niveles (síntesis Códice Vaticano A / Florentino)

| Nivel (Vaticano A) | Lectura operativa |
|--------------------|-------------------|
| 1. La Tierra (Tlaltecuhtli) | Entrada: cueva-matriz que devora |
| 2. Pasadero de agua | Cruce con ayuda de xoloitzcuintle |
| 3. Montañas que se juntan | Dualidad vida/muerte; aceptación |
| 4–5. Obsidiana / viento de navajas | Descomposición del cuerpo |
| 6. Banderas que tremolan | Desprendimiento de valores mundanos |
| 7. Lugar donde se flecha | Obstáculo (posible lectura colonial) |
| 8. Corazones comidos (jaguar) | Separación final *teyolia* / cuerpo |
| 9. Sin orificio para el humo | Mictlán propio: Mictlantecuhtli / Mictecacíhuatl |

Entidades anímicas: *teyolia* (corazón → región de muertos), *tonalli* (cabeza → Sol),
*ihiyotl* (hígado → inframundo / pasiones).

### Alineación a perspectivas I.O.

| Concepto | Perspectiva | Relación candidata | Justificación |
|----------|-------------|--------------------|---------------|
| Difunto individual | Individualidad | — | Singularidad del viajero |
| Vida ↔ muerte; cielo ↔ inframundo | Dualidad | `mirrorOf` | Dicotomías mesoamericanas |
| Cuatro destinos + nueve niveles | Totalidad | — | Geografía cósmica integrada |
| Renovación / reciclaje de fuerza | Evolución | `creates` | Nueva existencia potencial |
| Camino de descomposición / retorno al origen | Involución | `creates` | Disolución hacia el vacío-matriz |
| Tlaltecuhtli (devoradora-partidora) | Dualidad + Involución | `mirrorOf` | Polaridad que engendra y reabsorbe |

---

## 3. Pares candidatos para anotación / alineación

Plantilla CSV: `datasets/ingestion/templates/cosmos_nahuatl.csv`.

Pares ilustrativos (material *no ciego* — sólo demostración de mapeo):

| id | source | target | perspectiva sugerida | relación candidata |
|----|--------|--------|----------------------|--------------------|
| NAH-01 | Sol de Viento | Sol de Movimiento | Evolución / Involución | `creates` (ciclo) |
| NAH-02 | Tezcatlipoca | Quetzalcóatl | Dualidad | `mirrorOf` |
| NAH-03 | vida | muerte | Dualidad | `mirrorOf` |
| NAH-04 | Tlaltecuhtli | Mictlán | Involución | `creates` |
| NAH-05 | *teyolia* | Mictlán | Individualidad → Totalidad | `creates` |
| NAH-06 | Quinto Sol | cataclismo futuro | Involución | `creates` |
| NAH-07 | Tlalocan | Mictlán | Dualidad | `mirrorOf` / `none` |
| NAH-08 | gigantes | ocelotes | Dualidad / Involución | `creates` |

---

## 4. Límites explícitos

1. **No** se añaden nodos al core de 78.
2. El orden de los Soles **no** se fija como teorema; solo se mapea la estructura de ciclo.
3. Lecturas de «ruta al origen» vs «tormento» son de la literatura secundaria; el marco I.O. no adjudica verdad histórica.
4. Sin anotación ciega propia, este dominio **no** aporta κ ni evidencia de validez semántica de campo.
5. Las fuentes coloniales (Sahagún, Vaticano A) pueden incorporar categorías cristianas; el mapeo no las «purifica».

---

## 5. Referencias de trabajo

- Moreno de los Arcos, R. «Los cinco soles cosmogónicos». *Estudios de Cultura Náhuatl*.
- Luna López, M. (2017). «El camino al Mictlán: ¿ruta al tormento o al origen?» *Vita Brevis* 6(11).
- León-Portilla, M. *La filosofía náhuatl* (categorías cosmológicas).
- López Austin, A.; Matos Moctezuma, E.; Johansson, P. (cosmovisión, muerte, inframundo).
- Interno: [`CATALOGO_DOMINIOS.md`](CATALOGO_DOMINIOS.md) · [`PROTOCOLO_DE_MAPEO.md`](PROTOCOLO_DE_MAPEO.md) · [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

---

## 6. Medios de referencia

Carpeta: [`docs/media/cosmos_nahuatl/`](media/cosmos_nahuatl/).

| Recurso | Rol |
|---------|-----|
| Piedra del Sol (`Piedra_del_Sol.png`) | Iconografía del Quinto Sol (Nahui Ollin) y edades previas |
| Láminas codiciales (`4_Kingdoms.jpg`, `xolotl1.jpg`, `CodexBorgia.jpg`) | Dualidad, Xólotl / inframundo, ciclo ritual |
| Tesis *Códice Xólotl* (`PECDSV03T.pdf`) | Edición de divulgación (Peña Cisneros, UAEM 2017) |

Catálogo de medios: [`media/cosmos_nahuatl/README.md`](media/cosmos_nahuatl/README.md).
