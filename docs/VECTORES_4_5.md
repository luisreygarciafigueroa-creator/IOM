# Las cinco perspectivas del marco I.O.

El marco I.O. se articula mediante **cinco perspectivas complementarias**:

| # | Id | Perspectiva | Rol |
|---|-----|-------------|-----|
| 1 | `Ind` | **Individualidad** | Posicional (→ / lateral 0): unidad / singularidad |
| 2 | `D` | **Dualidad** | Posicional (0): relación / diferencia |
| 3 | `Tot` | **Totalidad** | Posicional (→ / lateral 2): integración / sistema |
| 4 | `Evol` | **Evolución** | Vectorial: flujo del vacío hacia la estructura |
| 5 | `Invol` | **Involución** | Vectorial: flujo de la estructura hacia el vacío |

Las tres primeras (Individualidad, Dualidad, Totalidad) describen los *modos de actualización* y se representan como metadatos de posición en cada tríada (→ | 0 | → en avance; ← | 0 | ← en retroceso). Las perspectivas cuarta y quinta (Evolución e Involución) describen las *direcciones de flujo informativo* y se materializan como secuencias vectoriales de cinco pasos.

Fuente estructurada: [`data/iom_spec.json`](../data/iom_spec.json) (`five_perspectives`, `vectors`).

## Cuarta perspectiva — Evolución

```
invol | ind | dua | tot | evol
  0   |  1  |  2  |  3  |  4
      |  →  |  →  |  →  |  →
  ---------------------
  ←   |  ←  |  ←  |  ←  |
  4   |  3  |  2  |  1  |  0
evol  | tot | dua | ind | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flecha |
|---|---|---|---|
| Avance | `invol · ind · dua · tot · evol` | `0 · 1 · 2 · 3 · 4` | → |
| Retroceso | `evol · tot · dua · ind · invol` | `4 · 3 · 2 · 1 · 0` | ← |

## Quinta perspectiva — Involución

```
invol | tot | dua | ind | evol
  4   |  3  |  2  |  1  |  0
  →   |  →  |  →  |  →  |
  ---------------------
      |  ←  |  ←  |  ←  |  ←
  0   |  1  |  2  |  3  |  4
evol  | ind | dua | tot | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flecha |
|---|---|---|---|
| Avance | `invol · tot · dua · ind · evol` | `4 · 3 · 2 · 1 · 0` | → |
| Retroceso | `evol · ind · dua · tot · invol` | `0 · 1 · 2 · 3 · 4` | ← |

## Representación formal

Cada fila se materializa como cinco instancias `io:VectorStep`. Cada instancia conserva el vector (`Evol` / `Invol`), fase, posición del eje, índice visual, etiqueta y flecha. En conjunto son **20 pasos vectoriales**.

En la ontología, las cinco perspectivas son individuos de `io:Perspective` con etiquetas en español: Individualidad, Dualidad, Totalidad, Evolución e Involución.

`spec_version` ≥ **1.5.0**.
