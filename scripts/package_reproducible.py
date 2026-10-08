#!/usr/bin/env python3
"""Empaqueta los artefactos reproducibles, excluyendo cachés y el checkout Git."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = [
    "README.md", "AUDITORIA.md", "EXPERIMENTOS.md", "REPRODUCCION.md", "paper.md", "LICENSE", "MANIFEST.sha256",
    "IOM.lean", "IOM", "lakefile.lean", "lake-manifest.json", "lean-toolchain", "requirements.txt", "requirements-lock.txt",
    "data", "datasets", "experiments/config.json", "experiments/pi_hgat_t.py", "experiments/results",
    "experiments/logs", "ontology", "scripts", "tests", ".github/workflows/ci.yml",
]

def files_in(path: Path):
    if path.is_file():
        yield path
    elif path.is_dir():
        for child in sorted(path.rglob("*")):
            if child.is_file() and not any(part in {"__pycache__", ".pytest_cache"} for part in child.parts):
                yield child

def main() -> None:
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / "IOM-reproducible.zip"
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in INCLUDE:
            path = ROOT / rel
            for file in files_in(path):
                archive.write(file, file.relative_to(ROOT).as_posix())
    print(f"Paquete creado: {target} ({target.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
