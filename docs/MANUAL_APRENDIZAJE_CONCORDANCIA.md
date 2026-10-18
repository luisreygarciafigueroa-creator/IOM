# Manual de aprendizaje: evaluación de concordancia semántica mediante pruebas a ciegas

> Segunda guía pedagógica: protocolo ciego, Fleiss' κ y valor didáctico del desacuerdo.  
> Complementa: [`MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)

---

## 1. Validación semántica vs formal

| Tipo | Pregunta |
|---|---|
| Formal / sintética | ¿El sistema es coherente consigo mismo? |
| Semántica empírica | ¿Observadores independientes captan el mismo significado en el mundo real? |

## 2. Protocolo ciego

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

Demostración **provisional**.

## 4. Desacuerdo como diagnóstico

- **NC:** neologismos → notas de alcance más estrictas.
- **AM:** solapamiento contextual → refinamiento de tríadas/fases.

## 5. Capas A–E

Solo EXP-A y EXP-E demuestran legibilidad en la realidad. EXP-B/C/D aseguran salud técnica interna.

## 6. Tres lecciones

1. Ningún Lean, SHACL o PI-HGAT-T sustituye anotadores humanos ciegos.
2. κ = 0.6871 aporta evidencia **provisional**.
3. NC/AM localizan fricción del lenguaje natural a refinar.
