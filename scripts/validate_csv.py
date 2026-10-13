#!/usr/bin/env python3
"""Valida contratos Draft 2020-12, encabezados y coherencia de CSV canónicos."""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
SCHEMA_PATH=ROOT/"data/csv_schemas.json"

def main() -> int:
    schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors=[]
    for filename in schema["properties"]["datasets"]["properties"]:
        item_schema=schema["properties"]["datasets"]["properties"][filename]["items"]
        row_schema=schema["$defs"][item_schema["$ref"].split("/")[-1]]
        expected=row_schema["required"]
        path=ROOT/"datasets"/filename
        seen=set(); rows=[]
        with path.open(encoding="utf-8",newline="") as fh:
            reader=csv.DictReader(fh)
            if reader.fieldnames != expected:
                errors.append(f"{filename}: encabezado debe ser exactamente {expected}, recibido {reader.fieldnames}")
                continue
            for line,row in enumerate(reader,start=2):
                typed={}
                for col,value in row.items():
                    prop=row_schema["properties"][col]
                    if prop.get("type")=="integer":
                        try: typed[col]=int(value)
                        except (TypeError,ValueError): typed[col]=value
                    else: typed[col]=value
                for err in Draft202012Validator(row_schema).iter_errors(typed):
                    errors.append(f"{filename}:{line}: {'.'.join(map(str,err.absolute_path)) or '<row>'}: {err.message}")
                rows.append(typed)
                if filename=="triad_nodes.csv":
                    if typed.get("node_id") in seen: errors.append(f"{filename}:{line}: node_id duplicado {typed.get('node_id')}")
                    seen.add(typed.get("node_id"))
                    if isinstance(typed.get("position_index"),int) and typed["position_index"] in range(3) and typed.get("position") != ("left","center","right")[typed["position_index"]]:
                        errors.append(f"{filename}:{line}: position e index no corresponden")
                if filename=="relation_candidates.csv":
                    pair=(typed.get("source"),typed.get("target"))
                    if pair in seen: errors.append(f"{filename}:{line}: par duplicado {pair}")
                    seen.add(pair)
                    if pair[0]==pair[1]: errors.append(f"{filename}:{line}: par reflexivo no permitido")
        if not any(e.startswith(filename+":") for e in errors): print(f"OK {filename}: {len(rows)} filas")
    if errors: print("\n".join(errors),file=sys.stderr); return 1
    return 0
if __name__=="__main__": sys.exit(main())
