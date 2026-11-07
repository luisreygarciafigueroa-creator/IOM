# Manual de aprendizaje: evaluación de concordancia como residuo del mundo compartido

> Segunda guía pedagógica: protocolo ciego, Fleiss' κ y valor didáctico del desacuerdo.  
> Bajo el carácter de **autonomía absoluta**, κ **no** fundamenta el marco.  
> Complementa: [`MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)

---

## 1. Autonomía formal vs residuo consensual

| Tipo | Pregunta |
|---|---|
| Formal / sintética | ¿El sistema es coherente consigo mismo sin autoridad exterior? |
| Residuo inter-anotador | ¿Observadores separados convergen en etiquetas sobre pares dados? |

La primera sostiene el marco; la segunda documenta una fase histórica.

## 2. Protocolo ciego (archivo)

- Anotación a ciegas (sin gramática interna del generador).
- Muestreo: reales, nuevos (NC), ambiguos (AM).
- Etiquetado: `mirrorOf`, `creates`, `none`, `unsure`.

## 3. Fleiss' κ (EXP-A)

```bash
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

| Métrica | Valor |
|---|---:|
| κ | **0.6871** |
| Unánimes | 10/14 (71,4 %) |
| Desacuerdos | NC01, NC02, AM01, AM03 |

Registro histórico; **no** demostración de validez del repositorio.

## 4. Desacuerdo como diagnóstico (dentro del residuo)

- **NC:** neologismos → fronteras del vocabulario compartido residual.
- **AM:** solapamiento contextual → límites de la especificación en el registro del encuentro.

## 5. Capas A–E

| Capa | Rol |
|------|-----|
| EXP-B / EXP-C | Autonomía formal (eje) |
| EXP-E | Destino Mictlán / cartografía del tránsito |
| EXP-D | Auto-generación |
| EXP-A | Residuo; no fundamento |

## 6. Tres lecciones

1. Lean y SHACL sostienen la autonomía formal sin requerir panel exterior.
2. κ = 0.6871 documenta un acuerdo residual; no funda el proyecto.
3. NC/AM localizan fricción del vocabulario compartido, no fallo de la bóveda técnica.
