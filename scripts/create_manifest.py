#!/usr/bin/env python3
"""Escribe SHA-256 de los artefactos fuente/reproducibles incluidos en el paquete."""
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE_DIRS = ("IOM", "data", "datasets", "docs", "experiments", "ontology", "scripts", "tests")
INCLUDE_FILES = ("IOM.lean", "README.md", "AUDITORIA.md", "EXPERIMENTOS.md", "REPRODUCCION.md", "paper.md",
                 "requirements.txt", "requirements-lock.txt", "lakefile.lean", "lake-manifest.json", "lean-toolchain",
                 "LICENSE", ".gitignore", ".github/workflows/ci.yml")

def main() -> None:
    files = {ROOT / name for name in INCLUDE_FILES if (ROOT / name).is_file()}
    for dirname in INCLUDE_DIRS:
        folder = ROOT / dirname
        if folder.exists():
            files.update(p for p in folder.rglob("*") if p.is_file() and
                         not any(part in {"__pycache__", ".pytest_cache"} for part in p.parts))
    out = ROOT / "MANIFEST.sha256"
    lines = [f"{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
             for path in sorted(files)]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"SHA-256: {len(lines)} archivos -> {out}")

if __name__ == "__main__":
    main()
