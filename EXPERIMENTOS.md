# Experimentos computacionales PI-HGAT-T

## Definición operativa

En este repositorio, **PI-HGAT-T** significa *Perspective-Informed Heterogeneous Graph Attention Network for Triads*. Es la implementación de referencia del clasificador estructural de relaciones entre nodos de tríada del marco I.O.

El modelo codifica cada nodo con vectores one-hot de fase (`adv`/`ret`) y posición (`left`/`center`/`right`); aplica dos capas de atención multi-cabeza sobre los seis nodos de cada pareja de tríadas; y clasifica cada par dirigido como `none`, `mirrorOf` o `creates`. Se implementa en PyTorch puro, sin PyTorch Geometric. Se excluyen etiquetas léxicas y el índice de tríada para forzar generalización estructural y permitir validación por tríada completa.

La suite compara tres variantes con la misma partición y semilla: modelo completo, ablación sin fase y ablación sin posición. Cada variante se entrena desde cero en cada fold.

## Justificación metodológica: por qué validar con aprendizaje automático

La Fase 1 del repositorio (Lean, RDF/OWL, SHACL, datasets regenerados de forma determinista) demuestra **corrección estructural** en un universo sin ruido: las relaciones `mirrorOf` y `creates` son deducibles de las reglas y verificables formalmente.

La Fase 2 responde a una pregunta distinta y complementaria:

> ¿Esas mismas relaciones siguen siendo **recuperables** cuando un modelo inductivo solo observa atributos parciales (fase, posición) bajo partición leave-one-triad-out?

Esta prueba de **recuperabilidad estructural** (no de validez semántica en el mundo real) es útil por cuatro razones. Las cifras siguientes **no** se interpretan como validación del marco sobre datos independientes:

1. **Aprendibilidad de la ontología.** La recuperación perfecta (accuracy = 1.0, F1 = 1.0) demuestra que la estructura no es un artefacto ad hoc: un modelo puede reconstruir las relaciones generadas por reglas a partir de rasgos mínimos.
2. **Robustez ante información incompleta.** Las ablaciones cuantifican la contribución de cada factor: sin fase la accuracy cae a 0.60; sin posición a ~0.64. Esto revela puntos de fragilidad estructural ante perturbaciones controladas.
3. **Puente explícito entre lo determinista y lo probabilístico.** Fase 1 produce el gold determinista; Fase 2 mide si un modelo generaliza ese gold. El mismo pipeline admite, en extensiones, CSV de dominios externos (biología, economía, etc.) alineados vía `scripts/importar_datos_personalizados.py`, permitiendo evaluar robustez frente al ruido del mundo real **sin modificar** la bóveda formal.
4. **Límite de interpretación.** Las métricas miden recuperabilidad de relaciones *generadas por reglas*, no la verdad del marco sobre datos independientes del generador. Para validación humana independiente véase `datasets/independent_eval/`; para evaluación externa de reglas, `datasets/external_eval/`.
