# Auditoría IOM — auto-fundamentación y encuentros

**Jerarquía canónica:** [`EXPERIMENTOS.md`](EXPERIMENTOS.md)  
**Delimitación:** [`docs/DELIMITACION_EPISTEMOLOGICA.md`](docs/DELIMITACION_EPISTEMOLOGICA.md)

## 1. Capa primaria — autonomía (punto fijo)

El repositorio es **válido como sistema** si:

1. `self_bootstrap.py --passes 2` deja CSV idénticos a HEAD ($S_{n+1}=S_n$).
2. `lake build` incluye `IOM/SelfGenesis.lean` (conteos derivados).
3. SHACL conforme sobre TTL regenerado.
4. `measure_invariance.py` reporta invariancia **no trivial** (control negativo).

`AUDITORIA_AUTO.md` **no se versiona**. Se genera bajo `experiments/results/` (CI/local) y es solo un informe fechado. **No** es prueba de punto fijo ni fundamento.

## 2. Capa secundaria — invariancia

Regeneración de etiquetas desde (fase, pos); LOO por tríada; corrupción de una arista detectada.

## 3. Encuentro — EXP-E y EXP-A (no fundamentan)

| Experimento | Rol |
|-------------|-----|
| EXP-E (dominio / Mictlán) | Expresabilidad; un fallo de anclaje **no** invalida el núcleo |
| EXP-A (κ) | Resonancia provisional **solo** con log de acceso e instrumento ciego |

κ ≈ 0.6871 es registro histórico. Sin `ACCESS_LOG` de exposición previa **no** se declara «demostración provisional completada» en esta auditoría.

## 4. Diagnóstico sintético (circular)

| Método | Accuracy |
|--------|---------:|
| PI-HGAT-T (fase + posición) | 1.0000 |
| MLP / reglas sin grafo | 1.0000 |

Muestran que la regla ya está en las features; no son validez semántica mundana.

## 5. Referencias

- Técnica: [`docs/AUDITORIA_TECNICA.md`](docs/AUDITORIA_TECNICA.md)
- Métricas sintéticas: [`docs/AUDITORIA_METRICAS.md`](docs/AUDITORIA_METRICAS.md)
