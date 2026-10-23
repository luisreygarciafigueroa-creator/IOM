#!/usr/bin/env python3
"""Escribe SHA-256 de los artefactos fuente/reproducibles incluidos en el paquete.

Exclusiones (no forman parte del punto fijo del manifiesto):
  - MANIFEST.sha256 — evita hash auto-referente
  - AUDITORIA_AUTO.md — regenerable con timestamp
  - ontology/io_ontology.ttl — regenerable; orden de serialización rdflib no es
    estable byte-a-byte entre corridas (CI lo regenera antes de SHACL)
  - __pycache__, .pytest_cache, .venv

Los CSV canónicos (triad_nodes, vector_steps, relation_candidates) SÍ entran:
son el punto fijo de generate_ontology.py.
"""
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE_DIRS = ("IOM", "data", "datasets", "docs", "experiments", "ontology", "scripts", "tests")
INCLUDE_FILES = (
    "IOM.lean", "README.md", "AUDITORIA.md", "EXPERIMENTOS.md", "REPRODUCCION.md", "paper.md",
    "MANIFIESTO.md",
    "requirements.txt", "requirements-lock.txt", "lakefile.lean", "lake-manifest.json", "lean-toolchain",
    "LICENSE", ".gitignore", ".github/workflows/ci.yml",
)
EXCLUDE_NAMES = frozenset({
    "MANIFEST.sha256",
    "AUDITORIA_AUTO.md",
    "io_ontology.ttl",  # regenerable; serialización no determinista
})
EXCLUDE_DIR_PARTS = frozenset({"__pycache__", ".pytest_cache", ".venv", "node_modules"})


def main() -> None:
    files = {ROOT / name for name in INCLUDE_FILES if (ROOT / name).is_file()}
    for dirname in INCLUDE_DIRS:
        folder = ROOT / dirname
        if folder.exists():
            files.update(
                p for p in folder.rglob("*")
                if p.is_file()
                and not any(part in EXCLUDE_DIR_PARTS for part in p.parts)
            )
    files = {p for p in files if p.name not in EXCLUDE_NAMES}
    out = ROOT / "MANIFEST.sha256"
    lines = [
        f"{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}"
        for path in sorted(files)
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"SHA-256: {len(lines)} archivos -> {out}")
    print(f"  excluidos por nombre: {sorted(EXCLUDE_NAMES)}")


if __name__ == "__main__":
    main()
