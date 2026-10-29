# Plan — IOM Flow

## Propósito y alcance
Aplicación móvil en español para explorar y aplicar el marco IOM a procesos candidatos a automatización. La app ayuda a estructurar entradas, actores, restricciones, resultados y evidencia; permite registrar una métrica de éxito, su línea base y su meta; mapea cada elemento a una perspectiva y fase; calcula aristas `mirrorOf`/`creates` entre elementos posicionales; produce propuestas explicables por cada elemento, relación y meta medida; y exige revisión humana antes de aceptar transformaciones. Incluye un entrenamiento local de referencia que recupera reglas desde el corpus sintético interno del adjunto. Distingue claramente la verificación formal de IOM, los diagnósticos sintéticos, las hipótesis de dominio y el aprendizaje empírico entrenado. No afirma generalización ni mejoras sin datos/evaluación apropiados.

## Implementación y componentes
- Conservar el starter Expo Router / React Native / TypeScript / NativeWind y los runtimes móviles fijos (Metro 8081 y API 3000). No introducir otro framework.
- App vertical y local-first: cuatro pestañas inferiores —Inicio, Explorar, Analizar y Método— con formularios, tarjetas y pasos que funcionan con controles táctiles amplios y respetan safe-area.
- `app/(tabs)/`: Inicio resume IOM; Explorar presenta las 13 tríadas, cinco perspectivas y una herramienta interactiva que invoca `formalRelation` para pares de nodos; Analizar captura procesos y proyecta relaciones y propuestas desde su grafo; Método explica límites y ejecuta la referencia k-NN.
- `lib/iom-spec.ts`: catálogo de cinco perspectivas, 13 tríadas canónicas, fases, posiciones, secuencia operacional y reglas formales de relación.
- `lib/iom-engine.ts`: asigna mapeos por perspectiva/fase; calcula cobertura, vacíos, supuestos, conflictos y relaciones `mirrorOf`/`creates`/`none`; genera propuestas trazables al elemento, arista o criterio de resultado que les da origen.
- `lib/iom-training.ts`: conjunto reproducible de 78 nodos (13 tríadas × dos fases × tres posiciones) y clasificador k-NN sencillo que se ajusta localmente y evalúa dejando una tríada fuera por turno. Mostrar el resultado como recuperación circular de etiquetas derivables de fase/posición, no como evidencia de aprendizaje generalizado.
- `lib/storage.ts`: persistencia local con AsyncStorage para un borrador activo, sus mapeos, propuestas, decisiones y reporte; avisa antes de reemplazarlo; no se envían procesos a terceros.
- `components/`: componentes reutilizables y accesibles para tarjetas, etiquetas de estado, barras de progreso, controles de perspectiva y confirmación.
- `app.config.ts` y `assets/images/`: identidad coherente de la aplicación e iconografía móvil; conservar slug, esquema e identificadores generados.

## Límites técnicos y de evidencia
El adjunto describe especificación IOM 1.9.0, cinco perspectivas, 13 tríadas (78 nodos), reglas de relaciones `mirrorOf`/`creates`, verificación mediante Lean/SHACL y experimentos sintéticos opcionales. El bundle aportado es documentación/datos textuales, no un conjunto de procesos reales etiquetados. El corpus sintético solo permite una demostración de recuperación interna: las etiquetas se derivan de las características fase/posición y una puntuación perfecta es circular. La app muestra un simulador de reglas documentadas y sus fuentes, pero no ejecuta el pipeline formal Lean/SHACL ni certifica validez semántica externa. Las propuestas de proceso son hipótesis deterministas a partir de los mapeos del usuario; la validación de dominios y el entrenamiento empírico requieren datos apropiados, procedencia, separación de evaluación y documentación, por lo que no se atribuyen aquí. Las puntuaciones de cobertura/confianza del diagnóstico son heurísticas visibles, no probabilidades calibradas. Se conserva un borrador activo por dispositivo; antes de reemplazarlo se advierte al usuario.

## Diseño
### Exploración de estilos
- Cartografía editorial de precisión: **0.07** (elegido).
- Brutalismo operativo de taller: **0.05**.
- Cibernética neo-folclórica: **0.03**.

### Estilo elegido: cartografía editorial de precisión
- **Movimiento:** cartografía científica editorial con señales de instrumentos contemporáneos; no es una consola técnica genérica.
- **Principios:** estructura antes que decoración; trazabilidad siempre visible; diferenciación por color, texto e icono (no por color únicamente); profundidad progresiva para uso en pantalla pequeña.
- **Filosofía cromática:** tinta verde profunda para estabilidad, fondo hueso para lectura serena, turquesa para flujo/progreso, lima suave para distinciones emergentes y terracota para advertencias o revisión pendiente.
- **Paradigma de layout:** paneles verticales como una hoja de campo; el proceso aparece como una línea de flujo que guía la mirada de lo incompleto hacia la unidad, con el contenido principal alineado a la izquierda y la navegación accesible con el pulgar.
- **Elementos distintivos:** línea de flujo que conecta etapas; cápsulas geométricas para las cinco perspectivas; anotaciones laterales de fuente/estado para cada inferencia.
- **Interacción:** explorar posiciones y pares con controles explícitos; cada diagnóstico se inspecciona por pieza; propuestas editables permanecen en borrador hasta aceptar o rechazar una por una y confirmar expresamente el registro local.
- **Animación:** transiciones cortas de opacidad/desplazamiento al abrir detalle, progreso discreto entre pasos y confirmación visual no cromática al guardar; sin movimiento continuo, parallax ni animaciones que ralenticen formularios.
- **Tipografía:** system sans de React Native para interfaz; jerarquía con títulos semibold, cuerpo regular y etiquetas compactas de espaciado amplio; cifras de cobertura con estilo tabular si el sistema lo permite.
- **Esencia de marca:** “IOM Flow convierte procesos complejos en automatizaciones revisables y trazables”; precisa, reflexiva, responsable.
- **Voz:** concreta, explicativa y prudente; CTAs en infinitivo o verbo directo. Ejemplos: “Mapea lo que ya sabes.” / “Revisa cada cambio antes de aplicarlo.”
- **Wordmark y símbolo:** marca abstracta de tres nodos que convergen y continúan en un trazo abierto, aludiendo a distinción, relación e integración sin pretender representar personas o un producto existente.
- **Color de marca propio:** turquesa mineral `#26B7A4`.

## Estructura del proyecto
```text
app/(tabs)/                 Inicio, exploración de tríadas y relaciones, análisis y método
components/                 Controles accesibles y tarjetas de producto
lib/iom-spec.ts             Fuente local del vocabulario IOM y relaciones formales
lib/iom-engine.ts           Mapeo, cobertura, grafo, diagnóstico y propuestas trazables
lib/iom-training.ts         Ajuste reproducible y diagnóstico del corpus interno
lib/storage.ts              Guardado local del borrador y revisiones
assets/images/              Icono, splash y adaptaciones de marca Expo
plan.md                     Decisiones de implementación y diseño
TODO.md                     Entregables y criterios de alcance
```
