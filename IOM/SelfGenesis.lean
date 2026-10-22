import IOM.FormalRules

namespace IOM

/-!
# Auto-creación formal (SelfGenesis)

Encarnación Lean de la autonomía: los conteos canónicos y la partición de
relaciones se derivan de los axiomas de `FormalRules` sin semilla exterior.

Correspondencia con el ensayo
[`docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md`](../docs/DEL_ORDEN_UNIVERSAL_A_LA_CREACION_DE_UNO_MISMO.md):

* **Mictecacíhuatl (Evolución)** ↔ fuerza que recombina / expande (fase `advance`, `creates` hacia estructura).
* **Mictlantecuhtli (Involución)** ↔ fuerza que despoja / purifica (fase `retreat`, retorno al vacío).
* **`isMirrorRel`** ↔ polaridad complementaria Evolución/Involución (fase opuesta + posición espejada).
* **`isCreatesRel`** ↔ operación por la cual el sistema distingue y genera su propio orden desde el vacío-matriz.

Lean es la fuente de las reglas; los CSV son derivados verificables
(`scripts/self_bootstrap.py` = punto fijo operativo).
-/

/-- Nodos = 13 tríadas × 2 fases × 3 posiciones. -/
theorem nodes_from_axioms : expectedNodes = 13 * 2 * 3 := expected_nodes_formula

/-- Partición completa de los 390 candidatos dirigidos. -/
theorem partition_complete :
    expectedMirrorDirected + expectedCreatesDirected + expectedNoneDirected = 390 :=
  expected_partition

/-- Pasos vectoriales = 4 secuencias × 5 ejes. -/
theorem vectors_from_axioms : expectedVectorSteps = 4 * 5 := expected_vector_steps_formula

/-- La fase opuesta es involutiva: advance↔retreat (díada Evolución/Involución). -/
theorem dual_phase_involutive (p : TriadPhase) : p.opposite.opposite = p :=
  opposite_involutive p

/-- Ninguna fase es fija bajo oposición (no hay punto medio exterior). -/
theorem dual_phase_no_fixed_point (p : TriadPhase) : p.opposite ≠ p :=
  opposite_ne p

/-- Espejo implica fases distintas (complementariedad Mictecacíhuatl/Mictlantecuhtli). -/
theorem mirror_requires_dual_phase (a b : TriadNode) (h : isMirror a b) :
    a.phase ≠ b.phase :=
  isMirror_implies_opposite_phase a b h

end IOM
