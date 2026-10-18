# Auditoría de las métricas perfectas (100 %)

## Pregunta

¿Por qué PI-HGAT-T y el MLP alcanzan accuracy y macro-F1 = 1.0 bajo leave-one-triad-out?

## Respuesta breve

Porque el gold de `relation_candidates.csv` es una **función determinista de fase y posición**. Cualquier modelo que vea esas dos features (y solo ellas) puede recuperar la partición exacta. El leave-one-triad-out no oculta la regla: oculta identidades de nodos e índices de tríada, no la estructura posicional.

## Partición

La partición leave-one-triad-out garantiza que **ninguna pareja** cuya `triad_index` es la held-out aparece en el conjunto de entrenamiento. No hay fuga de identidad de nodo ni de índice de tríada: el modelo solo recibe one-hot de fase y posición.

## Función determinista

Para un par dirigido $(s, t)$ con fases $p_s, p_t$ y posiciones $i_s, i_t$:

- `mirrorOf` si y solo si fase opuesta y $i_t = 2 - i_s$;
- `creates` si y solo si fase opuesta y una de las cuatro reglas laterales/centro;
- `none` en cualquier otro caso.

según las mismas reglas SHACL / FormalRules.lean. El script `scripts/audit_perfect_metrics.py` comprueba mismatches = 0.

## Ablaciones

| Variante | Accuracy | Interpretación |
|---|---:|---|
| Completo (fase + posición) | 1.0000 | Regla recuperable |
| Sin fase | 0.6000 | La fase es necesaria |
| Sin posición | 0.6359 | La posición es necesaria |

## Límites de interpretación

Las métricas 100 % demuestran **recuperabilidad de relaciones generadas por reglas**, no validez semántica en el mundo real. La prueba de validez semántica del marco sobre datos **no** derivados de las reglas exige anotación humana ciega (`datasets/independent_eval/`) o candidatos externos (`datasets/external_eval/`).
