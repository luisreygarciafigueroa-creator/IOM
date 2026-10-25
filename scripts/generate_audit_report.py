#!/usr/bin/env python3
"""Informe de auditoría regenerable (encuentro). No se versiona como fundamento."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    path = ROOT / rel
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    out_dir = ROOT / "experiments" / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    metrics = load_json("experiments/results/pi_hgat_t_metrics.json")
    baselines = load_json("experiments/results/baselines_comparison.json")
    versions = load_json("experiments/results/software_versions.json")

    lines = [
        "# AUDITORIA_AUTO",
        "",
        f"Generado: {datetime.now(timezone.utc).isoformat()}",
        "",
        "> Informe fechado. **No** es prueba de punto fijo ni fundamento del marco.",
        "",
        "## Capas",
        "",
        "- Núcleo: `self_bootstrap.py`, Lean, SHACL, invariancia",
        "- Encuentro: EXP-A/E, PI-HGAT-T/baselines (opcionales)",
        "",
    ]
    if metrics is None:
        lines.append(
            "_No se encontró pi_hgat_t_metrics.json; "
            "ejecutar experiments/optional/pi_hgat_t.py primero._"
        )
    else:
        lines.append("## PI-HGAT-T (diagnóstico)")
        lines.append("```json")
        lines.append(json.dumps(metrics.get("primary_metrics", metrics), indent=2)[:2000])
        lines.append("```")
    if baselines:
        lines.append("## Baselines")
        lines.append("```json")
        lines.append(json.dumps(baselines.get("baselines", baselines), indent=2)[:2000])
        lines.append("```")
    if versions:
        lines.append("## Software")
        lines.append(json.dumps(versions, indent=2))

    out_md = out_dir / "AUDITORIA_AUTO.md"
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Escrito {out_md}")


if __name__ == "__main__":
    main()
