#!/usr/bin/env python3
"""Plantilla de ingesta guiada: alinea un CSV de conceptos externos a la ontología IOM de 78 nodos.

No modifica data/iom_spec.json ni la ontología core. Valida que los mapped_node_id
existen, comprueba consistencia de perspectiva/fase/posición y genera un CSV alineado
más un informe de validación.

Uso:
  python scripts/importar_datos_personalizados.py \
      --input datasets/ingestion/templates/biologia_depredador_presa.csv \
      --output datasets/ingestion/aligned/biologia_aligned.csv

Opciones:
  --input PATH     CSV de entrada (obligatorio)
  --output PATH    CSV alineado de salida (por defecto: datasets/ingestion/aligned/<stem>_aligned.csv)
  --strict         Fallar si hay cualquier warning (por defecto solo error en mapped_node_id inválido)
  --report PATH    Ruta del informe JSON (por defecto junto al output)
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NODES_CSV = ROOT / "datasets" / "triad_nodes.csv"
VALID_PERSPECTIVES = {"Ind", "D", "Tot", "Evol", "Invol"}
VALID_PHASES = {"adv", "ret"}
VALID_POSITIONS = {"left", "center", "right"}
VALID_RELATIONS = {"none", "mirrorOf", "creates"}
REQUIRED_COLUMNS = {"external_id", "external_label"}


def load_canonical_nodes() -> dict[str, dict[str, Any]]:
    """Carga los 78 nodos canónicos indexados por node_id."""
    if not NODES_CSV.is_file():
        print(
            f"ERROR: no se encuentra {NODES_CSV}. "
            "Ejecuta primero: python scripts/generate_ontology.py",
            file=sys.stderr,
        )
        raise SystemExit(1)
    nodes: dict[str, dict[str, Any]] = {}
    with NODES_CSV.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            nodes[row["node_id"]] = row
    if len(nodes) != 78:
        print(
            f"ADVERTENCIA: se esperaban 78 nodos, se cargaron {len(nodes)}. "
            "Regenera los datasets con generate_ontology.py.",
            file=sys.stderr,
        )
    return nodes


def read_input_csv(path: Path) -> list[dict[str, str]]:
    """Lee el CSV de entrada ignorando líneas de comentario que empiezan por #."""
    rows: list[dict[str, str]] = []
    with path.open(encoding="utf-8", newline="") as fh:
        # Filtrar comentarios antes de pasar al DictReader
        lines = [ln for ln in fh if not ln.strip().startswith("#")]
    from io import StringIO

    reader = csv.DictReader(StringIO("".join(lines)))
    if reader.fieldnames is None:
        print("ERROR: el CSV no tiene cabecera.", file=sys.stderr)
        raise SystemExit(1)
    missing = REQUIRED_COLUMNS - set(reader.fieldnames)
    if missing:
        print(f"ERROR: faltan columnas obligatorias: {sorted(missing)}", file=sys.stderr)
        raise SystemExit(1)
    for row in reader:
        # Normalizar claves
        cleaned = {k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
        if not cleaned.get("external_id"):
            continue
        rows.append(cleaned)
    return rows


def validate_row(
    row: dict[str, str],
    nodes: dict[str, dict[str, Any]],
    row_num: int,
) -> tuple[dict[str, Any], list[str], list[str]]:
    """Valida una fila y devuelve (fila_alineada, errores, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []
    aligned: dict[str, Any] = {
        "external_id": row["external_id"],
        "external_label": row.get("external_label", ""),
        "mapped_node_id": row.get("mapped_node_id", ""),
        "perspective": row.get("perspective", ""),
        "phase": row.get("phase", ""),
        "position": row.get("position", ""),
        "relation_candidate": row.get("relation_candidate", "none") or "none",
        "notes": row.get("notes", ""),
        "canonical_label": "",
        "canonical_perspective": "",
        "canonical_phase": "",
        "canonical_position": "",
        "status": "ok",
    }

    node_id = aligned["mapped_node_id"]
    if not node_id:
        errors.append(f"fila {row_num}: mapped_node_id vacío")
        aligned["status"] = "error"
        return aligned, errors, warnings

    if node_id not in nodes:
        errors.append(
            f"fila {row_num}: mapped_node_id '{node_id}' no existe en los 78 nodos canónicos"
        )
        aligned["status"] = "error"
        return aligned, errors, warnings

    canon = nodes[node_id]
    aligned["canonical_label"] = canon.get("label", "")
    aligned["canonical_perspective"] = canon.get("perspective", "")
    aligned["canonical_phase"] = canon.get("phase", "")
    aligned["canonical_position"] = canon.get("position", "")

    # Consistencia opcional de perspectiva / fase / posición
    if aligned["perspective"] and aligned["perspective"] not in VALID_PERSPECTIVES:
        warnings.append(
            f"fila {row_num}: perspective '{aligned['perspective']}' no es canónica "
            f"({sorted(VALID_PERSPECTIVES)})"
        )
    elif aligned["perspective"] and aligned["perspective"] != canon.get("perspective"):
        # Solo advertir si el usuario forzó un valor distinto del nodo
        if aligned["perspective"] in {"Ind", "D", "Tot"}:
            warnings.append(
                f"fila {row_num}: perspective declarada '{aligned['perspective']}' "
                f"≠ perspectiva del nodo '{canon.get('perspective')}'"
            )

    if aligned["phase"] and aligned["phase"] not in VALID_PHASES:
        warnings.append(
            f"fila {row_num}: phase '{aligned['phase']}' no es canónica ({sorted(VALID_PHASES)})"
        )
    elif aligned["phase"] and aligned["phase"] != canon.get("phase"):
        warnings.append(
            f"fila {row_num}: phase declarada '{aligned['phase']}' ≠ fase del nodo '{canon.get('phase')}'"
        )

    if aligned["position"] and aligned["position"] not in VALID_POSITIONS:
        warnings.append(
            f"fila {row_num}: position '{aligned['position']}' no es canónica "
            f"({sorted(VALID_POSITIONS)})"
        )
    elif aligned["position"] and aligned["position"] != canon.get("position"):
        warnings.append(
            f"fila {row_num}: position declarada '{aligned['position']}' "
            f"≠ posición del nodo '{canon.get('position')}'"
        )

    if aligned["relation_candidate"] not in VALID_RELATIONS:
        warnings.append(
            f"fila {row_num}: relation_candidate '{aligned['relation_candidate']}' "
            f"no es válida ({sorted(VALID_RELATIONS)}); se fuerza a 'none'"
        )
        aligned["relation_candidate"] = "none"

    if warnings and aligned["status"] == "ok":
        aligned["status"] = "warning"

    return aligned, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Alinea un CSV de conceptos externos a la ontología IOM de 78 nodos."
    )
    parser.add_argument("--input", "-i", required=True, type=Path, help="CSV de entrada")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="CSV alineado de salida",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Tratar warnings como errores (exit code 1)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Ruta del informe JSON de validación",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"ERROR: no existe el archivo de entrada: {args.input}", file=sys.stderr)
        return 1

    nodes = load_canonical_nodes()
    rows = read_input_csv(args.input)
    if not rows:
        print("ERROR: el CSV de entrada no contiene filas de datos.", file=sys.stderr)
        return 1

    aligned_rows: list[dict[str, Any]] = []
    all_errors: list[str] = []
    all_warnings: list[str] = []

    for i, row in enumerate(rows, start=2):  # +2 por cabecera y 1-index
        aligned, errors, warnings = validate_row(row, nodes, i)
        aligned_rows.append(aligned)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    # Determinar rutas de salida
    if args.output is None:
        out_dir = ROOT / "datasets" / "ingestion" / "aligned"
        out_dir.mkdir(parents=True, exist_ok=True)
        args.output = out_dir / f"{args.input.stem}_aligned.csv"
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)

    if args.report is None:
        args.report = args.output.with_suffix(".report.json")

    # Escribir CSV alineado
    fieldnames = [
        "external_id",
        "external_label",
        "mapped_node_id",
        "canonical_label",
        "canonical_perspective",
        "canonical_phase",
        "canonical_position",
        "perspective",
        "phase",
        "position",
        "relation_candidate",
        "status",
        "notes",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(aligned_rows)

    report = {
        "input": str(args.input),
        "output": str(args.output),
        "canonical_nodes": len(nodes),
        "rows_processed": len(aligned_rows),
        "errors": all_errors,
        "warnings": all_warnings,
        "ok_count": sum(1 for r in aligned_rows if r["status"] == "ok"),
        "warning_count": sum(1 for r in aligned_rows if r["status"] == "warning"),
        "error_count": sum(1 for r in aligned_rows if r["status"] == "error"),
    }
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Resumen en consola
    print(f"Entrada:   {args.input}")
    print(f"Salida:    {args.output}")
    print(f"Informe:   {args.report}")
    print(f"Filas:     {report['rows_processed']}  "
          f"(ok={report['ok_count']}, warning={report['warning_count']}, error={report['error_count']})")
    if all_errors:
        print("\nERRORES:")
        for e in all_errors:
            print(f"  - {e}")
    if all_warnings:
        print("\nADVERTENCIAS:")
        for w in all_warnings:
            print(f"  - {w}")

    if all_errors:
        print("\nResultado: FALLO (hay errores de mapeo)")
        return 1
    if args.strict and all_warnings:
        print("\nResultado: FALLO (--strict y hay advertencias)")
        return 1
    print("\nResultado: OK — los conceptos se alinearon a la ontología canónica sin romper la bóveda.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
