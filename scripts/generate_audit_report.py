#!/usr/bin/env python3
"""Genera reporte de auditoría que relaciona commit, hashes de datos,
versiones de dependencias y métricas experimentales."""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def git_info() -> dict:
    def run(cmd: list[str]) -> str:
        try:
            return subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            return "unknown"

    return {
        "commit": run(["git", "rev-parse", "HEAD"]),
        "commit_short": run(["git", "rev-parse", "--short", "HEAD"]),
        "branch": run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "status_porcelain": run(["git", "status", "--porcelain"]),
        "describe": run(["git", "describe", "--always", "--dirty"]),
    }


def collect_hashes() -> dict:
    paths = [
        "data/iom_spec.json",
        "data/iom_spec.schema.json",
        "datasets/triad_nodes.csv",
        "datasets/relation_candidates.csv",
        "datasets/vector_steps.csv",
        "ontology/io_ontology.ttl",
        "ontology/io_shapes.ttl",
        "requirements-lock.txt",
        "experiments/config.json",
    ]
    result = {}
    for rel in paths:
        p = ROOT / rel
        if p.exists():
            result[rel] = sha256_file(p)
        else:
            result[rel] = None
    return result


def load_json(rel: str):
    p = ROOT / rel
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> None:
    git = git_info()
    hashes = collect_hashes()
    spec = load_json("data/iom_spec.json") or {}
    metrics = load_json("experiments/results/pi_hgat_t_metrics.json")
    baselines = load_json("experiments/results/baselines_comparison.json")
    versions = load_json("experiments/results/software_versions.json")

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git": git,
        "spec_version": spec.get("spec_version"),
        "schema_version": spec.get("schema_version"),
        "data_hashes_sha256": hashes,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "executable": sys.executable,
        },
        "software_versions_file": versions,
        "primary_metrics": (metrics or {}).get("primary_metrics"),
        "baselines_summary": None,
        "manifest_present": (ROOT / "MANIFEST.sha256").exists(),
    }

    if baselines:
        summary = {}
        for name, block in baselines.get("baselines", {}).items():
            m = block.get("metrics", {})
            summary[name] = {
                "accuracy": m.get("accuracy"),
                "macro_f1": m.get("macro_f1"),
            }
        report["baselines_summary"] = summary

    out_json = ROOT / "experiments" / "results" / "audit_report.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Auditoría automática IOM",
        "",
        f"**Generado:** {report['generated_at']}",
        f"**Commit:** `{git['commit_short']}` (`{git['commit']}`)",
        f"**Rama:** `{git['branch']}`",
        f"**spec_version:** {report['spec_version']}",
        f"**schema_version:** {report['schema_version']}",
        "",
        "## Hashes SHA-256 de artefactos de datos",
        "",
        "| Archivo | SHA-256 |",
        "|---|---|",
    ]
    for path, digest in hashes.items():
        lines.append(f"| `{path}` | `{digest or 'AUSENTE'}` |")

    lines += [
        "",
        "## Entorno",
        "",
        f"- Python: {report['environment']['python']}",
        f"- Platform: {report['environment']['platform']}",
        "",
        "## Métricas primarias PI-HGAT-T",
        "",
    ]
    if report["primary_metrics"]:
        for k, v in report["primary_metrics"].items():
            val = v.get("value") if isinstance(v, dict) else v
            lines.append(f"- **{k}**: {val}")
    else:
        lines.append("_No se encontró pi_hgat_t_metrics.json; ejecutar experiments/pi_hgat_t.py primero._")

    if report["baselines_summary"]:
        lines += ["", "## Resumen de baselines", ""]
        for name, m in report["baselines_summary"].items():
            lines.append(f"- **{name}**: accuracy={m['accuracy']}, macro_f1={m['macro_f1']}")

    lines += [
        "",
        "## Estado del working tree",
        "",
        "```",
        git.get("status_porcelain") or "(limpio)",
        "```",
        "",
        "---",
        "Generado por `scripts/generate_audit_report.py`.",
    ]

    out_md = ROOT / "AUDITORIA_AUTO.md"
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Auditoría JSON: {out_json}")
    print(f"Auditoría MD:   {out_md}")
    print(f"Commit: {git['commit_short']}  spec_version={report['spec_version']}")


if __name__ == "__main__":
    main()
