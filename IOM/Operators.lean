import IOM.Core

namespace IOM

/-- Evolución: avanza un instante y conserva la carga informativa. -/
def E (s : State) : State := ⟨s.time + 1, s.payload⟩

/-- Supresión directa: elimina redundancias sin cambiar el instante. -/
def S_fwd (s : State) : State := ⟨s.time, red s.payload⟩

/-- Involución: retrocede un instante e invierte la orientación categorial. -/
def Ivo (s : State) : State := ⟨s.time - 1, invert s.payload⟩

/-- Supresión retroactiva: conserva exactamente un estado vacío y, en otro
caso, retrocede con el contenido reducido e invertido. -/
def S_rev (s : State) : State :=
  if s.payload = [] then ⟨s.time, []⟩ else ⟨s.time - 1, red (invert s.payload)⟩

theorem E_vacuum (t : Int) : E (vacuum t) = vacuum (t + 1) := by rfl
theorem S_fwd_vacuum (t : Int) : S_fwd (vacuum t) = vacuum t := by rfl
theorem Ivo_vacuum (t : Int) : Ivo (vacuum t) = vacuum (t - 1) := by rfl
theorem S_rev_vacuum (t : Int) : S_rev (vacuum t) = vacuum t := by rfl

/-- La composición temporal restaura exactamente cualquier vacío. -/
theorem strict_fixed_point (t : Int) : S_rev (Ivo (E (vacuum t))) = vacuum t := by
  simp [E, Ivo, S_rev, vacuum, red, invert]

theorem E_preserves_payload (s : State) : (E s).payload = s.payload := by rfl
theorem S_fwd_preserves_time (s : State) : (S_fwd s).time = s.time := by rfl
theorem S_fwd_applies_red (s : State) : (S_fwd s).payload = red s.payload := by rfl
theorem Ivo_preserves_time_rule (s : State) : (Ivo s).time = s.time - 1 := by rfl
theorem Ivo_applies_inversion (s : State) : (Ivo s).payload = invert s.payload := by rfl
theorem S_rev_empty_payload (s : State) : (S_rev s).payload = red (invert s.payload) := by
  by_cases h : s.payload = [] <;>
    simp [S_rev, h, red, invert, List.eraseDups, List.eraseDups.loop]
theorem S_rev_empty_time (t : Int) : (S_rev (vacuum t)).time = t := by rfl
theorem E_then_Ivo_time (s : State) : (Ivo (E s)).time = s.time := by simp [E, Ivo]
theorem Ivo_then_E_time (s : State) : (E (Ivo s)).time = s.time := by simp [E, Ivo]
theorem invert_involutive (σ : List String) : invert (invert σ) = σ := by simp [invert]

theorem no_repetition (σ : List String) (h : σ ≠ []) :
    S_rev (Ivo (E (⟨0, σ⟩ : State))) ≠ ⟨0, σ⟩ := by
  have hr : invert σ ≠ [] := by simpa [invert] using h
  simp [E, Ivo, S_rev, hr]

end IOM
