#!/usr/bin/env python3
"""Autoevaluación del manual de protocolo ciego (no es métrica del marco)."""
from __future__ import annotations
import json, sys
from pathlib import Path

QUIZ = Path(__file__).with_name("quiz_blind_protocol.json")

def main(answers: dict[str, str]) -> int:
    data = json.loads(QUIZ.read_text(encoding="utf-8"))
    correct = 0
    for q in data["questions"]:
        got = answers.get(q["id"], "").lower().strip()
        ok = got == q["answer"]
        correct += int(ok)
        mark = "OK" if ok else "FAIL"
        print(f"{q['id']}: {mark} (esperado={q['answer']}, recibido={got or '—'})")
        if not ok:
            print(f"  → {q['rationale']}")
    total = len(data["questions"])
    print(f"Puntuación: {correct}/{total}")
    print("Nota: este quiz evalúa comprensión del protocolo; no modifica κ ni EXP-A.")
    return 0 if correct == total else 1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        key = {q["id"]: q["answer"] for q in json.loads(QUIZ.read_text(encoding="utf-8"))["questions"]}
        raise SystemExit(main(key))
    print("Uso: python experiments/learning/score_quiz.py Q1=b Q2=b Q3=c Q4=c")
    print("  o: python experiments/learning/score_quiz.py --self-test")
    ans = {}
    for arg in sys.argv[1:]:
        if "=" in arg:
            k, v = arg.split("=", 1)
            ans[k.strip().upper()] = v.strip()
    if ans:
        raise SystemExit(main(ans))
