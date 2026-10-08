# Auditoría de correspondencia con la especificación IOM

**Fuentes:** [`docs/MARCOI.O.txt`](docs/MARCOI.O.txt), que conserva byte a byte el original, y la tabla actualizada aportada por el usuario el 8 de octubre de 2026, normalizada como datos estructurados en [`data/iom_spec.json`](data/iom_spec.json). La especificación JSON alimenta generador, ontología, CSV y pruebas.

## Correspondencia y comprobación

| Especificación | Representación | Verificación |
|---|---|---|
| Estado temporal y vacío | `State(time, payload)`; `vacuum` | Lean 4.9.0 |
| Cuatro operadores temporales | `E`, `S_fwd`, `Ivo`, `S_rev` | Teoremas Lean compilados |
| Posiciones de tríada | izquierda=0/`Ind`; centro=1/`D`; derecha=2/`Tot` | RDF/OWL, SHACL, pruebas y `TriadPosition` Lean |
| Avance/retroceso actualizados | 13 filas por fase; 78 nodos | CSV, RDF, SHACL, pruebas literales |
| Extremos actualizados | avance comienza `involución | vacio | evolución`; retroceso termina `evolución | vacio | involución` | Fuente JSON, RDF y pruebas |
| Espejos laterales | misma fila, fase opuesta, `pos_ret = 2 - pos_adv` | OWL `mirrorOf` simétrica, SHACL y Lean |
| Dinámicas `creates` | cuatro reglas, 8 aristas por fila = 104 | Generador, SHACL y comparación exacta |
| Perspectivas vectoriales 4–5 | cuatro secuencias de 5 pasos = 20 | RDF, SHACL semántico y pruebas |
| Axiomas de ontología | clases, dominios, rangos, simetría y funcionalidad | Aserciones OWL más expansión OWL RL |
| PI-HGAT-T | clasificación de relación estructural en 13 folds | JSON de métricas, logs, configuración y CI |

## Decisiones de transcripción

- Se usa la última tabla del usuario. La tríada `individualidad | dualidad | totalidad` que formaba la primera fila de una versión anterior deja de ser una etiqueta de las 13 filas categoriales; `Ind`, `D`, `Tot` permanecen como metadatos posicionales de perspectiva, distintos del rótulo categorial.
- Se conserva la diferencia literal del usuario entre `vacio` (fila extrema de evolución/involución) y `vacío` (fila Universo/Espacio y otras filas). Los rótulos se guardan en minúscula, manteniendo los acentos.
- Los vectores de retroceso se actualizan a `evol · tot · dua · ind · vacio` y `vacio · ind · dua · tot · invol`. La orientación visible y el índice del eje son campos diferentes.
- El archivo original `docs/MARCOI.O.txt` no se modifica; las tablas posteriores se documentan como versión suplementaria del usuario.

## Métricas y límites

Las métricas de aristas de PI-HGAT-T están ligadas a `io:mirrorOf` y `io:creates` y a sus reglas SHACL. No se fija un umbral estadístico independiente: la referencia formal es la igualdad exacta (1.0) con la estructura ontológica determinista. El score observado del modelo no se presenta como prueba del marco.

El dataset se construye únicamente de la especificación proporcionada (13 tríadas; 78 nodos). Por ello, los experimentos prueban la capacidad del código de reconstruir propiedades estructurales de una especificación pequeña; no estiman generalización a datos del mundo real ni validan afirmaciones empíricas. Véase [`EXPERIMENTOS.md`](EXPERIMENTOS.md).

OWL RL expande inferencias de dominios/rangos; SHACL valida restricciones cerradas y reglas de estructura. Ninguno de estos pasos demuestra verdad empírica. El modelo Lean formaliza ecuaciones concretas y no interpreta automáticamente su significado filosófico.
