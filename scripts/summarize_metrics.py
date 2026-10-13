#!/usr/bin/env python3
"""Renderiza métricas principales de los artefactos experimentales como Markdown."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    pi=json.loads((ROOT/"experiments/results/pi_hgat_t_metrics.json").read_text())
    base=json.loads((ROOT/"experiments/results/baselines_comparison.json").read_text())
    lines=["## Métricas reproducibles — IOM", "", "### PI-HGAT-T y ablaciones", "", "| Variante | Accuracy | Macro-F1 | F1 mirrorOf | F1 creates |", "|---|---:|---:|---:|---:|"]
    for exp in pi["experiments"]:
        m=exp["metrics"]; lines.append(f"| {exp['variant']} | {m['candidate_relation_accuracy']['value']:.4f} | {m['relation_macro_f1']['value']:.4f} | {m['mirrorOf_f1']['value']:.4f} | {m['creates_f1']['value']:.4f} |")
    lines += ["", "### Baselines", "", "| Método | Accuracy | Macro-F1 |", "|---|---:|---:|"]
    for name,entry in base["baselines"].items():
        m=entry["metrics"]; lines.append(f"| {name} | {m['accuracy']:.4f} | {m['macro_f1']:.4f} |")
    lines += ["", f"Semilla: `{pi.get('configuration',{}).get('seed','n/d')}` · Validación: `{pi.get('validation','n/d')}` · Dataset: {pi.get('dataset',{}).get('directed_relation_candidates','n/d')} candidatos.", "", "Estas métricas reflejan recuperación de relaciones generadas por reglas; no son validación independiente de la teoría."]
    text="\n".join(lines)+"\n"
    print(text, end="")
if __name__=="__main__": main()
