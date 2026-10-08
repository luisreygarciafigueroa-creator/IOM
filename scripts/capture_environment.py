#!/usr/bin/env python3
"""Captura versiones del entorno de reproducción en un artefacto JSON."""
from __future__ import annotations
import importlib.metadata
import json
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def command_version(command: list[str]) -> str | None:
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=20)
        return (result.stdout or result.stderr).strip().splitlines()[0]
    except (OSError, subprocess.SubprocessError):
        return None

def main() -> None:
    packages = {}
    for name in ("rdflib", "pyshacl", "owlrl", "numpy", "torch"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    data = {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "packages": packages,
        "lean_toolchain_file": (ROOT / "lean-toolchain").read_text(encoding="utf-8").strip(),
        "lean_version": command_version(["lean", "--version"]),
        "lake_version": command_version(["lake", "--version"]),
        "requirements": (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines(),
    }
    out = ROOT / "experiments" / "results" / "software_versions.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
