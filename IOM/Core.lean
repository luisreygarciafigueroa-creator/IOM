namespace IOM
structure State where time : Int; payload : List String
def vacuum (t : Int) : State := ⟨t, []⟩
end IOM
