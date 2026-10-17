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

### Mapeo de una relación depredador-presa

| Concepto biológico | Perspectiva IOM | Posición sugerida | Fase | Justificación operativa |
|--------------------|-----------------|-------------------|------|-------------------------|
| Depredador (individuo) | Individualidad | left o right | adv | Unidad singular que actúa |
| Presa (individuo) | Individualidad | left o right (opuesta) | ret | Unidad singular que es afectada |
| Interacción depredación | Dualidad | center | adv/ret | Relación / diferencia entre dos unidades |
| Población / red trófica | Totalidad | center | adv | Sistema integrado |
| Colapso poblacional | Involución | vector Invol | ret | Disolución de estructura hacia vacío |
| Recuperación / sucesión | Evolución | vector Evol | adv | Proyección del vacío hacia nueva estructura |

**Ejemplo de alineación CSV** (ver `datasets/ingestion/templates/biologia_depredador_presa.csv`):

```csv
external_id,external_label,mapped_node_id,perspective,phase,position,notes
bio_pred_01,lobo,T03_adv_P0,Ind,adv,left,"Depredador como singularidad en fase de avance (muerte/artificial/vida)"
bio_prey_01,ciervo,T03_ret_P2,Ind,ret,right,"Presa como singularidad reflejada"
bio_inter_01,depredacion,T03_adv_P1,D,adv,center,"Relación dual que crea el centro de la fase opuesta"
```

**Uso de vectores de involución**: un biólogo puede modelar la extinción local como un paso del vector `Invol` (disolución) y la recolonización como un paso del vector `Evol`.

---

## 3. Economía — Transacciones de alto riesgo y ciclos de mercado

### Mapeo de una transacción de alto riesgo

| Concepto económico | Perspectiva IOM | Posición sugerida | Fase | Justificación operativa |
|--------------------|-----------------|-------------------|------|-------------------------|
| Agente individual (trader) | Individualidad | left | adv | Unidad decisora |
| Activo / contraparte | Individualidad | right | ret | Unidad reflejada |
| Contrato / riesgo | Dualidad | center | adv | Relación que media |
| Mercado / sistema financiero | Totalidad | center | ret | Integración sistémica |
| Burbuja / expansión | Evolución | vector Evol | adv | Proyección hacia estructura |
| Crash / liquidación | Involución | vector Invol | ret | Disolución hacia vacío |

**Ejemplo de alineación CSV** (ver `datasets/ingestion/templates/economia_transaccion_riesgo.csv`):

```csv
external_id,external_label,mapped_node_id,perspective,phase,position,notes
econ_agent_01,trader_A,T09_adv_P0,Ind,adv,left,"Agente como singularidad (singularidad/tiempo/infinito)"
econ_asset_01,derivado_X,T09_ret_P2,Ind,ret,right,"Activo como singularidad reflejada"
econ_risk_01,exposicion,T09_adv_P1,D,adv,center,"Riesgo como dualidad mediadora"
econ_mkt_01,mercado,T09_ret_P1,Tot,ret,center,"Mercado como totalidad"
```

Las tres tríadas más útiles para economistas suelen ser las de *singularidad/tiempo/infinito*, *hardware/virtual/software* (por analogía con instrumentos) y *muerte/artificial/vida* (ciclo de creación-destrucción de valor).

---

## 4. Otras disciplinas (plantilla rápida)

| Disciplina | Fenómeno típico | Tríada sugerida | Vector dominante |
|------------|-----------------|-----------------|------------------|
| Sociología | Cambio de norma social | caracter / subconsciente / personalidad | Invol → Evol |
| Física / sistemas complejos | Transición de fase | oscuridad / consciencia / luz | Evol / Invol |
| Psicología | Insight / represión | imaginación / inconsciente / memoria | Invol |
| Ingeniería de software | Refactoring / deuda técnica | hardware / virtual / software | Invol (deuda) → Evol (refactor) |
| IA / cognición artificial | Transición animal→humano→IA | animal / humano / IA | Evol / Invol |

---

## 5. Cómo contribuir un nuevo dominio

1. Copia la plantilla `datasets/ingestion/templates/plantilla_dominio.csv`.
2. Rellena las columnas obligatorias (`external_id`, `external_label`, `mapped_node_id` o `proposed_label`).
3. Ejecuta:
   ```bash
   python scripts/importar_datos_personalizados.py \
       --input datasets/ingestion/templates/mi_dominio.csv \
       --output datasets/ingestion/aligned/mi_dominio_aligned.csv
   ```
4. El script valida que los `mapped_node_id` existan en los 78 nodos canónicos y genera un informe de alineación.
5. Los datos alineados pueden usarse como *candidatos externos* en evaluación independiente o como features adicionales, **sin modificar** `data/iom_spec.json` ni la ontología core.
6. Para que el dominio cuente como **prueba de validez semántica**, someter un subconjunto a anotación ciega independiente y publicar κ y desacuerdos.

---

## 6. Referencias internas

- Nodos canónicos: [`datasets/triad_nodes.csv`](../datasets/triad_nodes.csv)
- Método de la prueba semántica: [`VALIDACION_INDEPENDIENTE.md`](VALIDACION_INDEPENDIENTE.md)
- Reglas de relaciones: [`docs/RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md)
- Especificación: [`data/iom_spec.json`](../data/iom_spec.json)
- Script de ingesta: [`scripts/importar_datos_personalizados.py`](../scripts/importar_datos_personalizados.py)
