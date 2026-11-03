# Las cinco perspectivas del marco I.O.

El marco I.O. se articula mediante **cinco perspectivas complementarias**:

| # | Id | Perspectiva | Rol |
|---|-----|-------------|-----|
| 1 | `Ind` | **Individualidad** | Posicional (→ / lateral 0): unidad / singularidad |
| 2 | `D` | **Dualidad** | Posicional (0): relación / diferencia |
| 3 | `Tot` | **Totalidad** | Posicional (→ / lateral 2): integración / sistema |
| 4 | `Evol` | **Evolución** | Vectorial: flujo del vacío hacia la estructura |
| 5 | `Invol` | **Involución** | Vectorial: flujo de la estructura hacia el vacío |

Las tres primeras (Individualidad, Dualidad, Totalidad) describen los *modos de actualización* y se representan como metadatos de posición en cada tríada (→ | 0 | → en avance; ← | 0 | ← en retroceso). Las perspectivas cuarta y quinta (Evolución e Involución) describen las *direcciones de flujo informativo* y se materializan como secuencias vectoriales de cinco pasos, con lecturas de **materia** y de **vacío**, en registro **real** y **virtual**.

Fuente estructurada: [`data/iom_spec.json`](../data/iom_spec.json) (`five_perspectives`, `vectors`).

---

## Cuarta perspectiva

### Evolución · materia real

```
invol | ind | dua | tot | evol
  0   |  1  |  2  |  3  |  4
      |  ⟳  |  ⟳  |  ⟳  |  ⟳
------------------------------------
  ⟲   |  ⟲  |  ⟲  |  ⟲  |
  4   |  3  |  2  |  1  |  0
evol  | tot | dua | ind | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flujo |
|---|---|---|---|
| Avance | `invol · ind · dua · tot · evol` | `0 · 1 · 2 · 3 · 4` | ⟳ |
| Retroceso | `evol · tot · dua · ind · invol` | `4 · 3 · 2 · 1 · 0` | ⟲ |

### Involución · materia virtual

```
invol | tot | dua | ind | evol
  4   |  3  |  2  |  1  |  0
  ⟳   |  ⟳  |  ⟳  |  ⟳  |
----------------------------------
      |  ⟲  |  ⟲  |  ⟲  |  ⟲
  0   |  1  |  2  |  3  |  4
evol  | ind | dua | tot | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flujo |
|---|---|---|---|
| Avance | `invol · tot · dua · ind · evol` | `4 · 3 · 2 · 1 · 0` | ⟳ |
| Retroceso | `evol · ind · dua · tot · invol` | `0 · 1 · 2 · 3 · 4` | ⟲ |

---

## Quinta perspectiva

### Involución · vacío real

```
invol | ind | dua | tot | evol
  0   |  1  |  2  |  3  |  4
      |  ⟳  |  ⟳  |  ⟳  |  ⟳
------------------------------------
  ⟲   |  ⟲  |  ⟲  |  ⟲  |
  4   |  3  |  2  |  1  |  0
evol  | tot | dua | ind | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flujo |
|---|---|---|---|
| Avance | `invol · ind · dua · tot · evol` | `0 · 1 · 2 · 3 · 4` | ⟳ |
| Retroceso | `evol · tot · dua · ind · invol` | `4 · 3 · 2 · 1 · 0` | ⟲ |

### Evolución · vacío virtual

```
invol | tot | dua | ind | evol
  4   |  3  |  2  |  1  |  0
  ⟳   |  ⟳  |  ⟳  |  ⟳  |
----------------------------------
      |  ⟲  |  ⟲  |  ⟲  |  ⟲
  0   |  1  |  2  |  3  |  4
evol  | ind | dua | tot | invol
```

| Fase | Etiquetas en orden de eje | Posiciones del eje | Flujo |
|---|---|---|---|
| Avance | `invol · tot · dua · ind · evol` | `4 · 3 · 2 · 1 · 0` | ⟳ |
| Retroceso | `evol · ind · dua · tot · invol` | `0 · 1 · 2 · 3 · 4` | ⟲ |

---

## Resumen de ejes

| Perspectiva | Lectura | Eje de avance (posiciones) | Eje de retroceso (posiciones) |
|---|---|---|---|
| **4ª** | Evolución · materia real | invol(0)·ind(1)·dua(2)·tot(3)·evol(4) | evol(4)·tot(3)·dua(2)·ind(1)·invol(0) |
| **4ª** | Involución · materia virtual | invol(4)·tot(3)·dua(2)·ind(1)·evol(0) | evol(0)·ind(1)·dua(2)·tot(3)·invol(4) |
| **5ª** | Involución · vacío real | invol(0)·ind(1)·dua(2)·tot(3)·evol(4) | evol(4)·tot(3)·dua(2)·ind(1)·invol(0) |
| **5ª** | Evolución · vacío virtual | invol(4)·tot(3)·dua(2)·ind(1)·evol(0) | evol(0)·ind(1)·dua(2)·tot(3)·invol(4) |

Los dos ejes estructurales se conservan:

1. **Eje A** (materia real / vacío real): `invol · ind · dua · tot · evol` ↔ espejo.
2. **Eje B** (materia virtual / vacío virtual): `invol · tot · dua · ind · evol` ↔ espejo.

La distinción real/virtual y materia/vacío es lectural (semántica de la perspectiva), no un cambio de posiciones del eje.

---

## Representación formal

Cada fila se materializa como cinco instancias `io:VectorStep`. Cada instancia conserva el vector (`Evol` / `Invol`), fase, posición del eje, índice visual, etiqueta y flecha. En conjunto son **20 pasos vectoriales** (los dos ejes × dos fases).

En la ontología, las cinco perspectivas son individuos de `io:Perspective` con etiquetas en español: Individualidad, Dualidad, Totalidad, Evolución e Involución.

`spec_version` ≥ **1.5.0**.
