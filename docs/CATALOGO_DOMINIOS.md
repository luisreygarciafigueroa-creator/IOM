# Catálogo de dominios: demostración de alineación semántica al mundo real

Este documento ofrece **traducciones conceptuales** para demostrar cómo fenómenos de disciplinas reales pueden alinearse con la ontología canónica de 78 nodos (13 tríadas × 2 fases × 3 posiciones) sin romper las restricciones formales (Lean, RDF/OWL, SHACL).

En el carácter actual del repositorio, estos mapeos son **demostraciones de aplicabilidad semántica**, no teorías de dominio validadas en campo. La prueba primaria de validez semántica sigue siendo la anotación ciega independiente (`datasets/independent_eval/`).

La ontología core permanece **inmutable**. Los datos externos se mapean como *instancias de alineación* o *candidatos de relación* que se validan estructuralmente antes de cualquier experimento predictivo.

---

## 1. Principios de mapeo

1. **No se añaden nodos al core**: los 78 nodos (`datasets/triad_nodes.csv`) son la bóveda bancaria. Los conceptos nuevos se alinean a etiquetas existentes o se registran como *extensiones externas* en `datasets/ingestion/`.
2. **Tres perspectivas posicionales**: cada fenómeno se interpreta bajo Individualidad (unidad/singularidad), Dualidad (relación/diferencia) o Totalidad (integración/sistema).
3. **Dos direcciones vectoriales**: Evolución (proyección del vacío hacia estructura) e Involución (disolución de estructura hacia el vacío).
4. **Relaciones admisibles**: solo `mirrorOf` (fase opuesta + posición reflejada) y `creates` (las cuatro reglas de creación). Cualquier otra arista se etiqueta `none`.
5. **Validación previa**: todo CSV de entrada debe pasar por `scripts/importar_datos_personalizados.py` antes de mezclarse con los candidatos canónicos.
6. **Validez semántica de campo**: un mapeo de dominio solo cuenta como evidencia de mundo real tras etiquetado ciego independiente propio (mismo estándar que `independent_eval`).

---

## 2. Biología — Depredador / presa y ciclos ecológicos

Plantilla: `datasets/ingestion/templates/biologia_depredador_presa.csv`.

| Concepto | Perspectiva IOM | Fase | Justificación |
|----------|-----------------|------|---------------|
| Depredador / presa | Ind | adv / ret | Singularidades reflejadas |
| Interacción depredación | D | adv | Tensión binaria |
| Red trófica | Tot | adv | Sistema integrado |
| Extinción / recolonización | Invol / Evol | ret / adv | Disolución / emergencia |

---

## 3. Economía — Transacciones de alto riesgo y mercado

Plantilla: `datasets/ingestion/templates/economia_transaccion_riesgo.csv`.

| Concepto | Perspectiva IOM | Fase | Justificación |
|----------|-----------------|------|---------------|
| Trader / activo | Ind | adv / ret | Agente y contraparte |
| Riesgo contractual | D | adv | Mediación |
| Mercado | Tot | ret | Sistema |
| Burbuja / crash | Evol / Invol | adv / ret | Expansión / disolución |

---

## 4. Cosmología náhuatl — Cinco Soles y Mictlán

Documento: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md).  
Plantilla: `datasets/ingestion/templates/cosmos_nahuatl.csv`.

| Concepto | Perspectiva | Relación candidata |
|----------|-------------|--------------------|
| Lucha Tezcatlipoca ↔ Quetzalcóatl | D | `mirrorOf` |
| Cataclismo / nuevo Sol | Invol / Evol | `creates` |
| Camino al Mictlán | Invol | `creates` |
| Vida ↔ muerte | D | `mirrorOf` |

Fuentes: Moreno de los Arcos; Luna López (2017).

---

## 5. Mitología comparada e historia de las religiones

Documento: [`DOMINIO_MITOLOGIA_RELIGIONES.md`](DOMINIO_MITOLOGIA_RELIGIONES.md).  
Plantilla: `datasets/ingestion/templates/mitologia_religiones.csv`.

| Concepto transversal | Perspectiva | Relación candidata |
|----------------------|-------------|--------------------|
| Sagrado ↔ profano | Dualidad | `mirrorOf` |
| Cielo ↔ inframundo | Dualidad | `mirrorOf` |
| Caos → cosmos ordenado | Evolución | `creates` |
| Edad del mundo → cataclismo | Involución | `creates` |
| Dios singular → panteón | Ind → Tot | — |
| Sacrificio individual → fecundidad colectiva | Ind → Tot | `creates` |
| Camino al más allá → origen/matriz | Involución | `creates` |

Fuentes de trabajo: Díez de Velasco (*Historia de las religiones*); Lora Cam (*Mitologías Universales y Latinoamericanas*). **No** se reproduce texto de las obras; solo mapeo de roles. Sin κ propio hasta anotación ciega.

---

## 6. Otras disciplinas (plantilla rápida)

| Disciplina | Fenómeno típico | Vector dominante |
|------------|-----------------|------------------|
| Sociología | Cambio de norma social | Invol → Evol |
| Física / sistemas complejos | Transición de fase | Evol / Invol |
| Psicología | Insight / represión | Invol |
| Ingeniería de software | Deuda técnica / refactor | Invol → Evol |
| IA / cognición artificial | Animal → humano → IA | Evol / Invol |

---

## 7. Cómo contribuir un nuevo dominio

1. Copia `datasets/ingestion/templates/plantilla_dominio.csv`.
2. Rellena `external_id`, `external_label`, `mapped_node_id`.
3. Ejecuta:
   ```bash
   python scripts/importar_datos_personalizados.py \
       --input datasets/ingestion/templates/mi_dominio.csv \
       --output datasets/ingestion/aligned/mi_dominio_aligned.csv
   ```
4. Validar IDs contra los 78 nodos canónicos.
5. **Sin modificar** `data/iom_spec.json` ni la ontología core.
6. Para validez semántica de campo: anotación ciega independiente + κ.

---

## 8. Referencias internas

- Nodos: [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv)
- Alineación: [`MANUAL_ALINEACION_DOMINIOS.md`](MANUAL_ALINEACION_DOMINIOS.md)
- Náhuatl: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md)
- Mitología / religiones: [`DOMINIO_MITOLOGIA_RELIGIONES.md`](DOMINIO_MITOLOGIA_RELIGIONES.md)
- Reglas: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md)
- Script: [`scripts/importar_datos_personalizados.py`](../scripts/importar_datos_personalizados.py)
