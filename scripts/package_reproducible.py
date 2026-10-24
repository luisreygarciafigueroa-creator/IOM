#!/usr/bin/env python3
"""Empaqueta los artefactos reproducibles, excluyendo cachés y el checkout Git."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = [
    "README.md", "AUDITORIA.md", "EXPERIMENTOS.md", "REPRODUCCION.md", "paper.md", "LICENSE", "MANIFEST.sha256",
    "IOM.lean", "IOM", "lakefile.lean", "lake-manifest.json", "lean-toolchain", "requirements.txt", "requirements-lock.txt",
    "data", "datasets", "experiments/config.json", "experiments/optional", "experiments/results",
    "experiments/logs", "ontology", "scripts", "tests", ".github/workflows/ci.yml",
]

def files_in(path: Path):
    if path.is_file():
        yield path
    elif path.is_dir():
        for p in path.rglob("*"):
            if p.is_file() and ".git" not in p.parts:
                yield p

def main() -> None:
    out = ROOT / "iom-reproducible.zip"
    with ZipFile(out, "w", ZIP_DEFLATED) as zf:
        for rel in INCLUDE:
            for p in files_in(ROOT / rel):
                zf.write(p, p.relative_to(ROOT).as_posix())
    print(f"Escrito {out}")

if __name__ == "__main__":
    main()
