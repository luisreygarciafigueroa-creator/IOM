/-
  Núcleo mínimo de la unidad informativa.

  No formaliza la metafísica completa: solo propiedades verificables —
  estructura identificable, relaciones derivables, trazabilidad interna.
-/
import IOM.Specification
import IOM.FormalRules

namespace IOM

/-- Núcleo abstracto: nodos con igualdad decidible y relación binaria.
    Instantiable sobre los nodos de una tríada o del grafo completo. -/
structure InformationalUnit (α : Type) where
  /-- Relación estructural entre nodos (p. ej. isMirrorRel ∨ isCreatesRel). -/
  related : α → α → Prop
  /-- Identidad decidible de nodos (trazabilidad de la distinción). -/
  [decEq : DecidableEq α]

/-- Relación canónica IOM sobre nodos de tríada. -/
def triadRelated (a b : TriadNode) : Prop :=
  isMirrorRel a b ∨ isCreatesRel a b

/-- Unidad informativa operativa sobre nodos (tríada + fase + posición). -/
def triadInformationalUnit : InformationalUnit TriadNode where
  related := triadRelated

/-- El espejo de posiciones es involutivo: la transformación es reversible. -/
theorem mirror_traceable (p : TriadPosition) : p.mirror.mirror = p :=
  mirror_involutive p

/-- La fase opuesta es involutiva: ida y vuelta conservan la identidad de fase. -/
theorem phase_traceable (p : TriadPhase) : p.opposite.opposite = p :=
  opposite_involutive p

/-- Misma tríada es condición de dominio de las relaciones operativas. -/
theorem related_same_triad (a b : TriadNode) (h : triadRelated a b) :
    sameTriad a b := by
  cases h with
  | inl hm => exact isMirrorRel_implies_same_triad a b hm
  | inr hc => exact isCreatesRel_implies_same_triad a b hc

end IOM
