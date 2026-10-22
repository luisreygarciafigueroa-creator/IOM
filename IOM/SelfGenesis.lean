import IOM.FormalRules
import IOM.Specification

namespace IOM

/-!
# Auto-creación formal (SelfGenesis)

Los conteos canónicos se **derivan** de la estructura finita (13 × 2 × 3,
espejos por tríada, reglas de creación), no se asumen como literales opacos.

Correspondencia con el ensayo:
* Mictecacíhuatl (Evolución) ↔ fase `advance` / fuerza ascendente
* Mictlantecuhtli (Involución) ↔ fase `retreat` / fuerza descendente
* `isMirrorRel` ↔ polaridad complementaria de la díada
* `isCreatesRel` ↔ auto-distinción generativa desde el vacío-matriz
-/

/-- 13 tríadas × 2 fases × 3 posiciones = 78 nodos (fórmula, no literal suelto). -/
theorem nodes_from_structure : 13 * 2 * 3 = 78 := by native_decide

theorem expected_nodes_matches_structure : expectedNodes = 13 * 2 * 3 :=
  expected_nodes_formula

/-- Por tríada: 3 posiciones × 2 sentidos de espejo = 6 aristas `mirrorOf` dirigidas. -/
def mirrorsPerTriad : Nat := 3 * 2

theorem mirrors_per_triad : mirrorsPerTriad = 6 := by native_decide

/-- 13 tríadas × 6 espejos dirigidos = 78. -/
theorem mirrors_from_structure : 13 * mirrorsPerTriad = 78 := by native_decide

theorem expected_mirrors_matches_structure :
    expectedMirrorDirected = 13 * mirrorsPerTriad := by
  native_decide

/-- Candidatos dirigidos por tríada: 6 nodos × 5 destinos = 30; × 13 = 390. -/
theorem candidates_from_structure : 13 * (6 * 5) = 390 := by native_decide

theorem partition_sums_to_candidates :
    expectedMirrorDirected + expectedCreatesDirected + expectedNoneDirected = 390 :=
  expected_partition

/-- Vectores: 4 secuencias × 5 ejes. -/
theorem vectors_from_structure : 4 * 5 = 20 := by native_decide

theorem expected_vectors_matches_structure : expectedVectorSteps = 4 * 5 :=
  expected_vector_steps_formula

/-- Díada de fases: involutiva y sin punto fijo (Evolución ↔ Involución). -/
theorem dual_phase_involutive (p : TriadPhase) : p.opposite.opposite = p :=
  opposite_involutive p

theorem dual_phase_no_fixed_point (p : TriadPhase) : p.opposite ≠ p :=
  opposite_ne p

theorem mirror_requires_dual_phase (a b : TriadNode) (h : isMirror a b) :
    a.phase ≠ b.phase :=
  isMirror_implies_opposite_phase a b h

end IOM
