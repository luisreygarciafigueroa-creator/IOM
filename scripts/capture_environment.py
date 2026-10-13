#!/usr/bin/env python3
"""Captura versiones del entorno; no reemplaza la referencia si Python difiere."""
from __future__ import annotations
import importlib.metadata, json, platform, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def command_version(command: list[str]) -> str | None:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=20)
        return (result.stdout or result.stderr).strip().splitlines()[0]
    except (OSError, subprocess.SubprocessError): return None

def main() -> int:
    out = ROOT / "experiments/results/software_versions.json"
    reference = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
    current_python = platform.python_version()
    expected_python = reference.get("python")
    if expected_python and platform.python_version_tuple()[:2] != tuple(expected_python.split(".")[:2]):
        print(f"ADVERTENCIA: Python activo {current_python} no coincide con referencia {expected_python} (se exige misma versión major.minor). Referencia preservada; no se escribe sobre software_versions.json.", file=sys.stderr)
        return 1
    packages = {}
    for name in ("rdflib", "pyshacl", "owlrl", "numpy", "torch"):
        try: packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: packages[name] = None
    data = {"python": current_python, "implementation": platform.python_implementation(), "platform": platform.platform(),
            "packages": packages, "lean_toolchain_file": (ROOT / "lean-toolchain").read_text(encoding="utf-8").strip(),
            "lean_version": command_version(["lean", "--version"]), "lake_version": command_version(["lake", "--version"]),
            "requirements": (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out); print(json.dumps(data, ensure_ascii=False, indent=2)); return 0
if __name__ == "__main__": sys.exit(main())
