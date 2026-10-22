# Manual de alineación: cartografía del destino Mictlán

> El Mictlán **no** es un dominio empírico más. Es la **lectura de destino** del marco
> (disolución del observador, auto-creación desde el vacío). Otros dominios son
> ejercicios secundarios. **No** existe «prueba primaria EXP-A» que legitime el mapeo.
>
> [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) ·
> [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md)

---

## 1. Invarianza del núcleo

78 nodos (13 × 2 × 3) = bóveda técnica. Conceptos externos se alinean **sin** alterar `iom_spec.json`, Lean ni SHACL.

| Perspectiva | Lectura bajo autonomía |
|-------------|------------------------|
| Individualidad | Singularidad auto-creada |
| Dualidad | Polaridad en disolución |
| Totalidad | Totalidad propia (sin contenedor exterior) |
| Evolución | Mictecacíhuatl — ascendente |
| Involución | Mictlantecuhtli — descendente |

---

## 2. Relaciones formales

Solo `mirrorOf` y `creates` (reglas canónicas). Resto → `none`.

Garantías: `lake build`, `scripts/validate_shacl.py`.
Detalle: [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md).

---

## 3. Protocolo de ingesta

1. Identificar fenómeno.
2. Asignar perspectiva (Ind / D / Tot).
3. Fase/vector (adv–Evol o ret–Invol).
4. Anclar a `mapped_node_id` de los 78.
5. Evaluar arista (`mirrorOf` / `creates` / `none`).
6. Validar con el script de ingesta.

```bash
python scripts/importar_datos_personalizados.py \
  --input datasets/ingestion/templates/<dominio>.csv \
  --output datasets/ingestion/aligned/<dominio>_aligned.csv
```

**No se exige** panel ciego para «aprobar» el mapeo.

---

## 4. Mictlán — destino, no ejemplo

Documento: [`DOMINIO_COSMOS_NAHUATL.md`](DOMINIO_COSMOS_NAHUATL.md).  
Ensayo: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md).

| Concepto | Perspectiva | Relación |
|----------|-------------|----------|
| Camino al Mictlán (tránsito) | Invol → autonomía | `creates` |
| Mictecacíhuatl ↔ Mictlantecuhtli | Evol / Invol | `mirrorOf` |
| Disolución observador → tejido | Individualidad → Totalidad | `creates` |
| Auto-creación desde el vacío | Individualidad / Totalidad | — |

EXP-E comprueba expresabilidad estructural; **no** es validación de campo ni κ de dominio.

---

## 5. Suite (relectura)

| ID | Rol |
|----|-----|
| EXP-B / EXP-C | Autonomía formal |
| EXP-E | Destino Mictlán expresable en 13 tríadas |
| EXP-D | Auto-generación |
| EXP-A | Residuo; no fundamento |

Pipeline: [`../EXPERIMENTOS.md`](../EXPERIMENTOS.md).
