# Protocolo preregistrado para evaluación independiente

Este protocolo separa tres cosas que no deben confundirse: (1) las métricas sintéticas de recuperación del gold determinista; (2) la revisión de reglas por expertos; y (3) el juicio humano de pares conceptuales. Solo (3) aporta observaciones independientes de los autores/reglas; la evaluación externa actualmente almacenada es una anotación basada en reglas y **no** se presenta como consenso humano empírico.

## Plan antes de recolectar

1. Congelar versión de la especificación, protocolo, pares visibles y hash SHA-256; publicar fecha y commit/tag en el registro de estudio antes de abrir anotaciones.
2. Reclutar al menos tres anotadores que no hayan creado el gold. El custodio de datos prepara una copia ciega con IDs aleatorios; no entrega `rule_reference.json`, `relation_candidates.csv`, predicciones ni métricas.
3. Mostrar solo pares, contexto mínimo y definiciones operativas; ocultar gold y orden de clases aleatorizado. Cada anotador etiqueta independientemente `none`, `mirrorOf`, `creates` o `unsure`, añade justificación breve y no consulta a otros hasta cierre.
4. No se adjudican respuestas antes del cálculo de acuerdo. Publicar conteo unánime/mayoritario, tabla anonimizadas de desacuerdos, tasa `unsure`, Fleiss' kappa con definición de casos/manejo de faltantes e intervalos si el tamaño lo permite.
5. Comparar con reglas/gold únicamente post hoc. Informar por separado acuerdo entre anotadores y coincidencia con gold; desacuerdo no se resuelve silenciosamente. Un panel de adjudicación puede añadir una etiqueta final, conservando originales y justificación.

## Criterios operativos

- **Acuerdo unánime**: los tres o más anotadores eligieron exactamente la misma etiqueta, incluida la categoría `unsure`.
- **Acuerdo mayoritario**: una etiqueta recibe más de la mitad de votos; si no, se reporta empate/sin mayoría.
- **Acuerdo interanotador**: estadístico de concordancia corregido por azar calculado sobre las etiquetas individuales, no sobre anotaciones de reglas. Es descriptivo, no prueba de verdad del marco.
- **Gold/reglas**: comparación posterior contra referencia versionada; se reportan confusiones y discrepancias sin convertirla en objetivo primario.

## Estado actual y archivos

`datasets/independent_eval/PROTOCOL.json` contiene la versión operativa; `independent_pairs.csv` es la vista de anotación y `rule_reference.json` se mantiene separada. No afirmar que hay datos independientes humanos hasta documentar reclutamiento, procedencia anonimizada y anotaciones crudas. `datasets/external_eval/annotations.json` se describe como evaluación basada en reglas con evaluadores E1–E3; su kappa no es evidencia de anotación humana independiente.

Antes de un estudio real, registrar el hash/commit y la fecha de congelación en el protocolo y en el informe. Cualquier cambio del conjunto/protocolo después de iniciada la anotación requiere una nueva versión y debe declararse.
