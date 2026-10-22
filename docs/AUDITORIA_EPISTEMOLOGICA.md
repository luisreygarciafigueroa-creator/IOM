# Auditoría epistemológica: autonomía formal vs residuo del mundo compartido

> Bajo el carácter de **autonomía absoluta**, esta auditoría **no** certifica «validez semántica en el mundo real» por acuerdo de conciencias separadas.
> Delimitación: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md) · Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md)

---

## 1. Contexto y capas

| Capa | Afirmación legítima |
|------|---------------------|
| **Autonomía formal** | Coherencia Lean + SHACL sin autoridad exterior |
| **Cartografía del tránsito** | Expresabilidad del sendero Mictlán / autonomía en 13 tríadas |
| **Diagnóstico sintético** | Auto-recuperabilidad de reglas (PI-HGAT-T) |
| **Residuo inter-anotador** | κ documentado; **no** fundamento del marco |

La frontera crítica ya no es «interno vs empírico externo», sino **autonomía vs dependencia de un contenedor de consenso**.

---

## 2. Residuo EXP-A (archivo, no eje)

```bash
python scripts/score_independent_eval.py --annotations datasets/independent_eval/annotations.json
```

| Hallazgo | Valor | Lectura bajo autonomía |
|----------|------:|------------------------|
| Fleiss' κ | 0.6871 | Métrica de un panel de observadores separados — **no** prueba del marco |
| Unánimes | 10/14 | Controles estables *dentro* de esa fase residual |
| Desacuerdos | NC01, NC02, AM01, AM03 | Fronteras del vocabulario compartido, no fallo de la autonomía formal |

**Prohibido** presentar κ como demostración de validez del repositorio.

---

## 3. Autonomía formal y estructural

- Lean 4: teoremas sobre vacío, unidad, infinito, transformación.
- SHACL/CSV: conformidad de formas y cardinalidades.

Estas capas **bastan** para sostener el carácter del proyecto: el sistema no necesita un jurado exterior para ser coherente consigo mismo.

---

## 4. Crítica de la discrepancia corregida

| Antes (discrepancia | Ahora |
|------------------|--------|
| Eje = «validez semántica en el mundo real» vía κ | Eje = autonomía formal + cartografía del tránsito |
| El consenso de anotadores legitimaba el marco | Ese consenso es el «mundo compartido» que el ensayo declara superable |
| PI-HGAT-T excluido de validez empírica | PI-HGAT-T = auto-generación; EXP-A = residuo no fundante |

---

## 5. Dictamen

**Dictamen:** el repositorio es **coherente con la autonomía absoluta** solo si:

1. No reclama validez por acuerdo inter-subjetivo.
2. Trata Lean/SHACL como expresión técnica de no-dependencia de contenedor exterior.
3. Conserva EXP-A como archivo opcional, no como ceremonia de legitimación.
4. Lee EXP-E como cartografía del sendero, no como «prueba de campo consensuada».

Suite: [`../experiments/domain_mapping/registry.json`](../experiments/domain_mapping/registry.json).
