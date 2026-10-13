# Auditoría rigurosa de las métricas perfectas (100%)

**Estado:** conclusiones reproducibles por `scripts/audit_perfect_metrics.py` y `tests/test_metrics_audit.py`.

## Pregunta

¿Por qué PI-HGAT-T y el MLP alcanzan accuracy / macro-F1 / F1 por clase = **1.0000** bajo leave-one-triad-out?

## Hallazgos

### 1. Independencia train/test: correcta a nivel de tríada

La partición leave-one-triad-out garantiza que **ninguna pareja** cuya `triad_index` es la held-out aparece en el conjunto de entrenamiento. No hay fuga de identidad de nodo ni de índice de tríada: el modelo solo recibe one-hot de fase y posición.

### 2. Las etiquetas son una función determinista de (fase, posición)

Para cualquier par `(source, target)`, la etiqueta gold se obtiene **únicamente** de:

```
fase_src, pos_src, fase_tgt, pos_tgt  →  {none, mirrorOf, creates}
```

según las mismas reglas SHACL / `FormalRules.lean`:

- `mirrorOf` ⟺ fases opuestas ∧ `pos_tgt = 2 - pos_src`
- `creates` ⟺ fases opuestas ∧ (lateral→centro ∨ centro→lateral)
- `none` en cualquier otro caso

Esta función es **idéntica** en las 13 tríadas. Por tanto, en cada fold LOO, el 100 % de los pares de prueba tiene una clave de features ya vista en entrenamiento con la misma etiqueta.

### 3. Consecuencia: cualquier learner de la función alcanza 1.0

| Método | Accuracy | Interpretación |
|---|---:|---|
| Reglas deterministas (oracle) | 1.0000 | Aplica la función sin aprender |
| MLP (features fase+pos) | 1.0000 | Aprende la función; generaliza por construcción |
| PI-HGAT-T (fase+pos + atención) | 1.0000 | Idem; la atención de grafo no aporta información adicional en este corpus |
| Regresión logística lineal | 0.5333 | No separa `mirrorOf` / `creates` |
| Ablación sin fase | 0.6000 | Rompe la función determinista |
| Ablación sin posición | ~0.64 | Idem |

### 4. ¿Se necesita una arquitectura compleja?

**No para este corpus sintético.** El oracle y el MLP bastan. PI-HGAT-T demuestra *recuperabilidad estructural* y sirve de referencia para extensiones (ruido, features adicionales, dominios externos), pero el 100 % no justifica por sí solo la complejidad del modelo sobre datos generados por las mismas reglas que se evalúan.

## Delimitación epistemológica

| Afirmación legítima | Afirmación no legítima |
|---|---|
| «Las relaciones generadas por reglas son recuperables al 100 % a partir de fase y posición bajo LOO.» | «El marco está validado empíricamente en el mundo real.» |
| «La ontología es aprendible a partir de rasgos estructurales mínimos.» | «PI-HGAT-T supera a baselines en datos independientes del generador.» |
| «Las ablaciones cuantifican la contribución de fase y posición.» | «El 100 % demuestra robustez frente a ruido del mundo real.» |

La validación empírica del marco sobre datos **no** derivados de las reglas exige anotación humana ciega (`datasets/independent_eval/`) o candidatos externos (`datasets/external_eval/`).

## Cómo reproducir la auditoría

```bash
python scripts/audit_perfect_metrics.py
python -m unittest tests.test_metrics_audit -v
```

Artefacto: `experiments/results/perfect_metrics_audit.json`.
