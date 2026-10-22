# Instrumento EXP-A (entrega al anotador)

Paquete **autocontenido** para el protocolo ciego. Se entrega **fuera** del
clon del repositorio (zip, carpeta separada, o mensaje con solo estos archivos).

| Archivo | Rol |
|---------|-----|
| `INSTRUCTIONS.md` | Definiciones neutras de etiquetas; sin tesis del proyecto |
| `pairs.csv` | 14 pares (id, etiquetas, contexto genérico) |
| `ACCESS_LOG.template.json` | Plantilla para el **coordinador** (no se envía al anotador como tarea) |

## Flujo del coordinador

1. Copiar solo `INSTRUCTIONS.md` + `pairs.csv` al anotador.
2. Rellenar una entrada en el log de acceso (copia de la plantilla) **antes** de la entrega.
3. Al recibir anotaciones, completar `annotations_received_at` y `declared_prior_exposure_*`.
4. Archivar el log junto a `annotations.json` en el repo (post-hoc).

La ceguera es un **estado del anotador**, no del repo público. Este instrumento
existe para no obligar al anotador a abrir el repo.
