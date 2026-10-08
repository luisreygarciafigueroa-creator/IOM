# Reproducción de IOM

La cadena ejecutable comprueba el modelo formalizado y reproduce una suite de experimentos estructurales. Los resultados no son validación empírica de las afirmaciones filosóficas, neurocientíficas o físicas del marco.

## Entorno fijado

- Python 3.12 (versión exacta en `experiments/results/software_versions.json`).
- Lean 4.9.0, fijado en `lean-toolchain` mediante Elan.
- Dependencias Python con versiones directas fijadas en `requirements.txt` y lock completo en `requirements-lock.txt`; PyTorch CPU 2.6.0.
- Sistema CI: Ubuntu 24.04.

Instala Elan/Lean si es necesario:

```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
  | sh -s -- -y --default-toolchain leanprover/lean4:v4.9.0
export PATH="$HOME/.elan/bin:$PATH"
```

## Reproducción integral

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python experiments/pi_hgat_t.py
.venv/bin/python scripts/capture_environment.py
.venv/bin/python scripts/create_manifest.py
.venv/bin/python scripts/package_reproducible.py
```

La generación toma `data/iom_spec.json` como fuente única y actualiza `ontology/io_ontology.ttl` y los CSV en `datasets/`. El experimento escribe el resultado JSON y el log. La captura registra versiones reales, el manifiesto genera hashes SHA-256 y el empaquetador crea `dist/IOM-reproducible.zip` con código, Lean, RDF/OWL, SHACL, datasets, configuración, dependencias, resultados, logs y documentación.

## Criterios de comprobación

1. `lake build` compila los cuatro operadores y los teoremas de posiciones/espejos/vectores sin `sorry` ni `admit`.
2. El generador produce 78 nodos, 104 aristas `creates`, 78 aristas dirigidas de espejo, 20 pasos vectoriales y 390 candidatos de relación.
3. Las pruebas comparan literalmente las 26 filas de tríadas y las cuatro secuencias vectoriales; incluyen mutaciones negativas.
4. OWL RL infiere tipos por dominios/rangos y SHACL valida reglas, cardinalidades, direcciones, espejos, enlaces y secuencias vectoriales.
5. La suite ejecuta PI-HGAT-T completo y ablaciones sin fase/sin posición, con 13 folds leave-one-triad-out cada una. No hay umbral estadístico elegido a mano: los scores se vinculan a propiedades ontológicas deterministas y se reportan como métricas descriptivas del dataset suministrado.

## Reproducir etapas individuales

```bash
lake build
.venv/bin/python scripts/generate_ontology.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_shacl.py
.venv/bin/python experiments/pi_hgat_t.py
```

La metodología, las métricas y sus propiedades correspondientes, así como sus límites de interpretación, están en [`EXPERIMENTOS.md`](EXPERIMENTOS.md). La fuente original `docs/MARCOI.O.txt` se conserva sin alteraciones; las aclaraciones actualizadas se registran en `data/iom_spec.json` y los anexos.
