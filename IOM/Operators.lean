import IOM.Core
namespace IOM
def E (s : State) : State := ⟨s.time + 1, s.payload⟩
def Ivo (s : State) : State := ⟨s.time - 1, s.payload⟩
def S_rev (s : State) : State := if s.payload = [] then ⟨s.time, []⟩ else ⟨s.time - 1, []⟩
theorem strict_fixed_point (t : Int) : S_rev (Ivo (E (vacuum t))) = vacuum t := by rfl
end IOM
