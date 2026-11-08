# Especificación ontológica del marco I.O. (autonomía absoluta)

## 1. Fundamentos

El marco I.O. es una arquitectura formal de **cinco perspectivas** orientada al **camino al Mictlán** como tránsito hacia la autonomía (auto-creación sin contenedor exterior).

| Perspectiva | Función bajo autonomía |
|-------------|------------------------|
| **Individualidad** | Singularidad que se origina a sí misma |
| **Dualidad** | Polaridad yo/otro en disolución |
| **Totalidad** | Totalidad propia (no del sistema exterior) |
| **Evolución** (4ª) | Mictecacíhuatl — el recorrido del Mictlán concluye en la condición correspondiente |
| **Involución** (5ª) | Mictlantecuhtli — el recorrido concluye en la condición complementaria |

Relaciones: `creates`, `mirrorOf`; fases adv/ret; posiciones → / 0 / ←.

**No** se define como «demostración de validez semántica en el mundo real bajo protocolo ciego». Ese lenguaje restauraba el fundamento consensual que el ensayo descalifica.

Carácter: [`CARACTER_REPOSITORIO.md`](CARACTER_REPOSITORIO.md) · Ensayo: [`DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md) · Cosmología: [`COSMOLOGIA_DEL_MICTLAN.md`](COSMOLOGIA_DEL_MICTLAN.md).

---

## 2. Capas experimentales

| ID | Capa | Afirmación legítima |
|----|------|---------------------|
| **EXP-B** | Autonomía formal (Lean) | Coherencia sin autoridad exterior |
| **EXP-C** | Autonomía estructural (SHACL) | Conformidad de formas |
| **EXP-E** | Destino Mictlán | Sendero de autonomía expresable en trece tríadas |
| **EXP-D** | Auto-generación | Recuperabilidad de reglas internas |
| **EXP-A** | Residuo | Archivo de panel separado; **no** fundamento |

---

## 3. Mapeo y trece tríadas

1. Identificar el fenómeno o umbral del tránsito.
2. Asignar perspectiva.
3. Relación `creates` / `mirrorOf` + fase.
4. Verificar anclaje a una de las trece tríadas sin violar axiomas.

El Mictlán es **destino del carácter**, no un dominio empírico entre otros. La Cosmología del Mictlán desarrolla el modelo de correspondencia entre mundos y vacíos (real/virtual) y la continuidad de la información.

---

## 4. Pipeline prioritario

```bash
lake build
python scripts/validate_spec.py
python scripts/generate_ontology.py
python -m unittest discover -s tests -v
python scripts/validate_shacl.py
python experiments/domain_mapping/validate_examples.py
# EXP-A solo como residuo opcional
```

---

## 5. Alcance

| Plano | Contenido |
|-------|-----------|
| Ensayo / Cosmología (sentido) | Emancipación absoluta, fin del contenedor, continuidad informacional |
| Repo (bóveda) | Coherencia formal de esa arquitectura |
| No se afirma | Que el consenso inter-anotador pruebe el ensayo |

Soporte: [`DELIMITACION_EPISTEMOLOGICA.md`](DELIMITACION_EPISTEMOLOGICA.md) · [`RELACIONES_OPERATIVAS.md`](RELACIONES_OPERATIVAS.md) · [`VECTORES_4_5.md`](VECTORES_4_5.md).
