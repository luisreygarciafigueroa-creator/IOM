# TODO — IOM Flow

## 1. Explorar IOM y sus capas de fundamento
- [x] La aplicación móvil está en español, funciona en orientación vertical y ofrece navegación inferior y controles aptos para una mano.
- [x] La app permite explorar unidades informativas, trece tríadas, cinco perspectivas y relaciones `mirrorOf` / `creates` / `none`; se seleccionan los nodos de origen y objetivo, la fase y la posición, se calcula su relación con la regla IOM y se conserva la trazabilidad de identidad.
- [x] La app presenta la cadena operativa «vacío informativo → distinción → relación → integración → transformación → unidad informativa autocontenida».
- [x] La ficha de fundamentos distingue la especificación canónica, las pruebas en Lean, la validación SHACL y la validación semántica externa; aclara que la app muestra las reglas, pero no ejecuta Lean/SHACL ni valida dominios externos.

## 2. Describir, mapear y diagnosticar un proceso
- [x] Se puede describir el proceso que se desea optimizar, su contexto, entradas, actores, restricciones, resultados esperados, evidencia disponible, métrica de éxito, línea base actual y meta esperada; sin una base y una meta no se afirma que el resultado haya mejorado.
- [x] El usuario puede mapear interactivamente elementos del proceso a Individualidad, Dualidad, Totalidad, Evolución e Involución, escoger fase de Avance o Retroceso, con ayuda contextual y detección de vacíos.
- [x] El diagnóstico IOM muestra correspondencias, relaciones calculadas entre mapeos posicionales, supuestos, conflictos y nivel de cobertura de forma explicable; para vectores Evolución/Involución no fuerza posiciones, y no presenta inferencias circulares como aprendizaje generalizado.
- [x] La propuesta se desglosa en reglas, transformaciones, decisiones y puntos de intervención humana; cada elemento se vincula al mapeo, la arista o la meta de resultado de origen, incluye antes/después y confianza con justificación.
- [x] Cada resultado lleva un estado distinguible: demostración de reglas, hipótesis, evidencia de encuentro o aprendizaje entrenado. Las sugerencias de proceso se etiquetan «Hipótesis»; la demo no presenta evidencia de encuentro; el estado «aprendizaje entrenado» solo se usa para datos, entrenamiento y evaluación documentados.

## 3. Revisar propuestas y automatizar con control humano
- [x] El flujo de revisión previa muestra comparación antes/después y advertencias; permite editar, aceptar o rechazar por separado cada transformación propuesta.
- [x] La app solicita confirmación explícita antes de registrar cambios aceptados; ninguna sugerencia se aplica automáticamente ni ejecuta acciones en sistemas externos.

## 4. Entrenar una referencia IOM y comunicar sus límites
- [x] La app permite ejecutar un entrenamiento local reproducible sobre el corpus sintético interno (78 nodos derivados de 13 tríadas × dos fases × tres posiciones) y presenta el esquema de partición dejando una tríada fuera por turno.
- [x] El resultado del corpus interno se identifica como diagnóstico sintético/circular de recuperación de etiquetas, no como prueba de generalización, validez semántica externa o mejora de procesos del mundo real.
- [x] Cuando no existan datos de proceso reales, entrenamiento y evaluación documentados, la app no afirma haber entrenado ni validado un modelo empírico de optimización.

## 5. Accesibilidad y persistencia
- [x] La experiencia usa objetivos táctiles amplios, texto legible, señales de estado que no dependen solo del color y etiquetas accesibles para tecnologías de asistencia.
- [x] El borrador activo del proceso, los mapeos y el estado de revisión se conservan localmente en el dispositivo; la app advierte antes de reemplazar el borrador único y no presenta datos sintéticos como datos reales del usuario.
