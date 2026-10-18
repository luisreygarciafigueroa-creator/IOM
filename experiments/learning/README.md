# Aprendizaje: protocolo ciego y capas A–E

Material pedagógico derivado de los manuales y del dictamen técnico.

| Artefacto | Descripción |
|---|---|
| [`quiz_blind_protocol.json`](quiz_blind_protocol.json) | 4 preguntas de autoevaluación |
| [`score_quiz.py`](score_quiz.py) | Corrección local del quiz |

```bash
python experiments/learning/score_quiz.py --self-test
python experiments/learning/score_quiz.py Q1=b Q2=b Q3=c Q4=c
```

Manuales:

- [`docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md`](../../docs/MANUAL_APRENDIZAJE_PROTOCOLO_CIEGO.md)
- [`docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md`](../../docs/MANUAL_APRENDIZAJE_CONCORDANCIA.md)
- [`docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md`](../../docs/DICTAMEN_TECNICO_EPISTEMOLOGICO.md)

**No** forma parte de las métricas del marco (κ, PI-HGAT-T, SHACL). Solo evalúa comprensión del diseño experimental.
