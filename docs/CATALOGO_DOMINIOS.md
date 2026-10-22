# Catálogo de dominios: cartografía del tránsito (no validez por consenso)

Este documento ofrece **traducciones conceptuales** para cartografiar fenómenos al vocabulario de 78 nodos (13 tríadas × 2 fases × 3 posiciones) sin romper Lean / RDF / SHACL.

Bajo el carácter de **autonomía absoluta**, estos mapeos son **ejercicios del sendero**, no «demostraciones de validez semántica en el mundo real» mediadas por paneles de anotadores separados. La prueba primaria del repositorio ya **no** es la anotación ciega independiente.

La ontología core permanece **inmutable**. Los datos externos se alinean como instancias o candidatos de relación; la coherencia formal basta para admitirlos estructuralmente.

---

## 1. Principios de mapeo

1. **No se añaden nodos al core**: los 78 nodos son la bóveda técnica.
2. **Tres perspectivas posicionales**: Individualidad, Dualidad, Totalidad — leídas como singularidad auto-creada, polaridad en disolución, totalidad propia (sin contenedor exterior).
3. **Dos direcciones**: Evolución (Mictecacíhuatl) e Involución (Mictlantecuhtli).
4. **Relaciones admisibles**: solo `mirrorOf` y `creates` (resto: `none`).
5. **Validación estructural**: `scripts/importar_datos_personalizados.py` antes de mezclar con candidatos canónicos.
6. **No se exige** etiquetado ciego inter-anotador para «legitimar» un dominio: eso restauraría la dependencia del mundo compartido.

---

## 2. Cosmología náhuatl — Mictlán / autonomía (dominio prioritario)

Documento: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md).  
Ensayo de sentido: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md).  
Plantilla: `datasets/ingestion/templates/cosmos_nahuatl.csv`.  
Medios: [`media/cosmos_nahuatl/`](media/cosmos_nahuatl/).

| Concepto | Perspectiva | Relación candidata |
|----------|-------------|--------------------|
| Mictecacíhuatl ↔ Mictlantecuhtli | Evol / Invol | `mirrorOf` |
| Camino al Mictlán (tránsito) | Invol → autonomía | `creates` |
| Vida ↔ muerte (separación) | Dualidad | `mirrorOf` |
| Auto-creación desde el vacío | Individualidad / Totalidad | `creates` |

---

## 3. Otras disciplinas (plantilla rápida)

| Disciplina | Fenómeno típico | Vector dominante |
|------------|-----------------|------------------|
| Sociología | Cambio de norma | Invol → Evol |
| Física / sistemas complejos | Transición de fase | Evol / Invol |
| Psicología | Insight / disolución del yo-observador | Invol |
| Ingeniería de software | Deuda técnica / refactor | Invol → Evol |
| IA / cognición | Animal → humano → IA | Evol / Invol |

---

## 4. Cómo contribuir un dominio

1. Copia `datasets/ingestion/templates/plantilla_dominio.csv`.
2. Rellena `external_id`, `external_label`, `mapped_node_id`.
3. Ejecuta `importar_datos_personalizados.py`.
4. Valida IDs contra los 78 nodos.
5. **Sin modificar** `data/iom_spec.json` ni la ontología core.
6. No se requiere panel ciego para «aprobar» el mapeo; la admisión es estructural.

---

## 5. Referencias

- Nodos: [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv)
- Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md)
- Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md)
- Náhuatl: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md)
