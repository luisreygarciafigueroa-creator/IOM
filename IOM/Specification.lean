namespace IOM

/-- Posición discreta de un concepto en una tríada.
    Etiquetas canónicas: avance → | 0 | → ; retroceso ← | 0 | ← .
    Constructores formales: → / ₀ / ← (índice 0/1/2). El espejo intercambia laterales. -/
inductive TriadPosition where
  /-- Lateral de avance (etiqueta →). -/
  | «→»
  /-- Centro (etiqueta 0). -/
  | «₀»
  /-- Lateral de retroceso (etiqueta ←). -/
  | «←»
  deriving DecidableEq, Repr

/-- Coordenada ordinal asociada a cada posición de la tríada. -/
def TriadPosition.index : TriadPosition → Nat
  | .«→» => 0
  | .«₀» => 1
  | .«←» => 2

/-- Intercambio lateral usado al espejar avance y retroceso. -/
def TriadPosition.mirror : TriadPosition → TriadPosition
  | .«→» => .«←»
  | .«₀» => .«₀»
  | .«←» => .«→»

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
