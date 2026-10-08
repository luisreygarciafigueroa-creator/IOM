namespace IOM

/-- Estado informativo discreto: instante entero y secuencia de unidades. -/
structure State where
  time : Int
  payload : List String
  deriving Repr, DecidableEq

/-- Vacío ontológico en el instante indicado. -/
def vacuum (t : Int) : State := ⟨t, []⟩

/-- Eliminación estable de elementos repetidos. -/
def red (σ : List String) : List String := σ.eraseDups

/-- Inversión lateral de una secuencia categorial. -/
def invert (σ : List String) : List String := σ.reverse

end IOM
