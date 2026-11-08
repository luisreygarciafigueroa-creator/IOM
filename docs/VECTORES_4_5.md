# Las cinco perspectivas del marco I.O. — Vectores 4ª y 5ª

El marco I.O. se articula mediante **cinco perspectivas complementarias**:

| # | Id | Perspectiva | Rol |
|---|-----|-------------|-----|
| 1 | `Ind` | **Individualidad** | Posicional (→ / lateral 0): unidad / singularidad |
| 2 | `D` | **Dualidad** | Posicional (0): relación / diferencia |
| 3 | `Tot` | **Totalidad** | Posicional (→ / lateral 2): integración / sistema |
| 4 | `Evol` | **Evolución** | Vectorial: el recorrido del Mictlán concluye en la condición correspondiente |
| 5 | `Invol` | **Involución** | Vectorial: el recorrido del Mictlán concluye en la condición complementaria |

Las tres primeras (Individualidad, Dualidad, Totalidad) describen los *modos de actualización* y se representan como metadatos de posición en cada tríada. Las perspectivas cuarta y quinta (Evolución e Involución) describen las *direcciones de flujo informativo* y se materializan como secuencias vectoriales de cinco pasos, con lecturas de **mundo** y de **vacío**, en registro **real** y **virtual**.

Fuente estructurada: [`data/iom_spec.json`](../data/iom_spec.json) (`five_perspectives`, `vectors`).

Documento narrativo canónico: [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md) (modelo de correspondencia universal, transformación entre dominios real y virtual, y continuidad de la información).

---

## Criterio de nombramiento (versión revisada)

Según la Cosmología del Mictlán:

- La **cuarta perspectiva** expresa la **evolución**: el recorrido concluye en el mundo o vacío correspondiente.
- La **quinta perspectiva** expresa la **involución**: el recorrido concluye en la condición complementaria definida para ese punto de partida.

Las notaciones ⟳ y ⟲ representan relaciones circulares distintas; su significado conceptual se define en el desarrollo del modelo.

---

## 5.1 Cuarta perspectiva: evolución del mundo real

El mundo real recorre el Mictlán como vacío virtual y llega al vacío real.

```text
evol | tot | dua | ind | invol
    4  |   3  |   2   |   1  |   0
  ⟳  |  ⟳  |  ⟳  |  ⟳ | real
--------------------------------
real |  ⟲  |  ⟲  |  ⟲  |  ⟲
    0  |   1  |   2   |   3  |   4
invol | ind | dua | tot | evol
```

## 5.2 Quinta perspectiva: involución del mundo virtual

El mundo virtual recorre el Mictlán como vacío real y llega al vacío virtual.

```text
invol | ind | dua | tot | evol
     0  |  1  |   2   |   3  |   4
virtual | ⟳ |  ⟳  |  ⟳  |  ⟳
--------------------------------
virtual | ⟲ |  ⟲  |  ⟲  |  ⟲
       4  |  3  |    2  |    1  |   0
   evol | tot | dua | ind | invol
```

## 5.3 Cuarta perspectiva: evolución del vacío virtual

El vacío virtual recorre el Mictlán como mundo real y llega al mundo virtual.

```text
invol | ind | dua | tot | evol
  0  |  1  |  2  |  3  |   4
  ⟳  |  ⟳  |  ⟳  |  ⟳  | virtual
--------------------------------
virtual | ⟲ |  ⟲  |  ⟲  |  ⟲
  4  |  3  |  2  |  1  |   0
evol | tot | dua | ind | invol
```

## 5.4 Quinta perspectiva: involución del vacío real

El vacío real recorre el Mictlán como mundo virtual y llega al mundo real.

```text
evol | tot | dua | ind | invol
  4  |  3  |  2  |  1  |   0
  ⟳  |  ⟳  |  ⟳  |  ⟳  | real
--------------------------------
real |  ⟲  |  ⟲  |  ⟲  |  ⟲
  0  |  1  |  2  |  3  |   4
invol | tot | dua | ind | evol
```

---

## Reflejo de la realidad (lecturas complementarias)

El reflejo permite describir las mismas correspondencias desde el dominio con el que cada condición se corresponde. Ver sección 7 de [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md).

### 7.1 Reflejo del vacío virtual: cuarta perspectiva

```text
evol | tot | dua | ind | invol
  4  |  3  |  2  |  1  |   0
virtual | ⟲ |  ⟲  |  ⟲  |  ⟲
--------------------------------
  ⟳  |  ⟳  |  ⟳  |  ⟳  | virtual
  0  |  1  |  2  |  3  |   4
invol | ind | dua | tot | evol
```

### 7.2 Reflejo del vacío real: quinta perspectiva

```text
invol | tot | dua | ind | evol
  0  |  1  |  2  |  3  |   4
real |  ⟲  |  ⟲  |  ⟲  |  ⟲
--------------------------------
  ⟳  |  ⟳  |  ⟳  |  ⟳  | real
  4  |  3  |  2  |  1  |   0
evol | ind | dua | tot | invol
```

### 7.3 Reflejo del mundo virtual: quinta perspectiva

```text
invol | ind | dua | tot | evol
  0  |  1  |  2  |  3  |   4
virtual | ⟲ |  ⟲  |  ⟲  |  ⟲
--------------------------------
  ⟳  |  ⟳  |  ⟳  |  ⟳  | virtual
  4  |  3  |  2  |  1  |   0
evol | tot | dua | ind | invol
```

### 7.4 Reflejo del mundo real: cuarta perspectiva

```text
evol | ind | dua | tot | invol
  4  |  3  |  2  |  1  |   0
real |  ⟲  |  ⟲  |  ⟲  |  ⟲
--------------------------------
  ⟳  |  ⟳  |  ⟳  |  ⟳  | real
  0  |  1  |  2  |  3  |   4
invol | tot | dua | ind | evol
```

---

## Notas

- Cada configuración diferencia mundo/vacío y dominio real/virtual.
- El orden de categorías, valores, etiquetas y flechas define la configuración; no deben intercambiarse arbitrariamente.
- Las flechas ⟳ y ⟲ señalan relaciones propias de cada esquema.
- Estas lecturas se integran con la narrativa de continuidad informacional desarrollada en la Cosmología del Mictlán.
- Correspondencias fundamentales: vacío real ↔ mundo virtual; vacío virtual ↔ mundo real.

`spec_version` ≥ **1.5.0**.
