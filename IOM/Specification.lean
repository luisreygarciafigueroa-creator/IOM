namespace IOM

/-- Posición discreta de un concepto en una tríada, izquierda-centro-derecha. -/
inductive TriadPosition where
  | left
  | center
  | right
  deriving DecidableEq, Repr

/-- Coordenada ordinal asociada a cada posición de la tríada. -/
def TriadPosition.index : TriadPosition → Nat
  | .left => 0
  | .center => 1
  | .right => 2

/-- Intercambio lateral usado al espejar avance y retroceso. -/
def TriadPosition.mirror : TriadPosition → TriadPosition
  | .left => .right
  | .center => .center
  | .right => .left

theorem mirror_involutive (p : TriadPosition) : p.mirror.mirror = p := by
  cases p <;> rfl

theorem mirror_index (p : TriadPosition) : p.mirror.index = 2 - p.index := by
  cases p <;> rfl

/-- Fase de la tabla de avance/retroceso. -/
inductive TriadPhase where
  | advance
  | retreat
  deriving DecidableEq, Repr

/-- Coordenada permitida en los vectores de cinco pasos. -/
def validVectorIndex (n : Nat) : Prop := n ≤ 4

theorem vector_index_bounds (n : Nat) (h : validVectorIndex n) : n ≤ 4 := h

theorem vector_index_mirror (n : Nat) (h : n ≤ 4) : 4 - (4 - n) = n := by
  omega

end IOM
