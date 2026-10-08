#!/usr/bin/env python3
"""Clasificadores base para comparar con PI-HGAT-T.

Incluye:
  - reglas deterministas (oracle de la especificación)
  - regresión logística sobre features one-hot de fase+posición
  - MLP sin estructura de grafo
"""
from __future__ import annotations

import csv
import json
import random
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.nn import functional as F

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ("none", "mirrorOf", "creates")
CLASS_ID = {n: i for i, n in enumerate(CLASSES)}


def seed_everything(seed: int = 20261008) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(1)


def features_for_node(node_id: str) -> list[float]:
    parts = node_id.split("_")
    phase, position = parts[1], int(parts[2][1:])
    return [float(phase == "adv"), float(phase == "ret"),
            float(position == 0), float(position == 1), float(position == 2)]


def parse_pair_index(node_id: str) -> int:
    phase = node_id.split("_")[1]
    position = int(node_id.split("_")[2][1:])
    return position if phase == "adv" else 3 + position


def read_pairs():
    pairs: dict[int, list[tuple[str, str, int]]] = {i: [] for i in range(13)}
    with (ROOT / "datasets" / "relation_candidates.csv").open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            pairs[int(row["triad_index"])].append(
                (row["source"], row["target"], CLASS_ID[row["relation"]])
            )
    return pairs


def admissible(label: str, source: int, target: int) -> bool:
    source_phase, source_pos = (0 if source < 3 else 1), source % 3
    target_phase, target_pos = (0 if target < 3 else 1), target % 3
    if source_phase == target_phase:
        return False
    if label == "mirrorOf":
        return target_pos == 2 - source_pos
    if label == "creates":
        return (source_pos in (0, 2) and target_pos == 1) or (source_pos == 1 and target_pos in (0, 2))
    return True


def deterministic_rule_predict(src_idx: int, tgt_idx: int) -> int:
    if admissible("mirrorOf", src_idx, tgt_idx):
        return CLASS_ID["mirrorOf"]
    if admissible("creates", src_idx, tgt_idx):
        return CLASS_ID["creates"]
    return CLASS_ID["none"]


def pair_feature(src_id: str, tgt_id: str) -> list[float]:
    return features_for_node(src_id) + features_for_node(tgt_id)


def scores(gold: list[int], pred: list[int]) -> dict:
    matrix = [[0] * 3 for _ in range(3)]
    for a, b in zip(gold, pred):
        matrix[a][b] += 1
    per_class = {}
    f1s = []
    for i, name in enumerate(CLASSES):
        tp = matrix[i][i]
        fp = sum(matrix[r][i] for r in range(3) if r != i)
        fn = sum(matrix[i][c] for c in range(3) if c != i)
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
        per_class[name] = {"precision": prec, "recall": rec, "f1": f1, "support": tp + fn}
        f1s.append(f1)
    acc = sum(a == b for a, b in zip(gold, pred)) / max(len(gold), 1)
    return {
        "accuracy": round(acc, 6),
        "macro_f1": round(sum(f1s) / 3, 6),
        "per_class": per_class,
        "confusion_matrix": matrix,
    }


class SoftmaxRegression(nn.Module):
    def __init__(self, in_dim: int, n_classes: int = 3):
        super().__init__()
        self.linear = nn.Linear(in_dim, n_classes)

    def forward(self, x):
        return self.linear(x)


class SimpleMLP(nn.Module):
    def __init__(self, in_dim: int, hidden: int = 32, n_classes: int = 3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.GELU(),
            nn.Linear(hidden, hidden),
            nn.GELU(),
            nn.Linear(hidden, n_classes),
        )

    def forward(self, x):
        return self.net(x)


def train_sklearn_like(model: nn.Module, X: torch.Tensor, y: torch.Tensor,
                       epochs: int = 200, lr: float = 0.01) -> None:
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    for _ in range(epochs):
        opt.zero_grad()
        logits = model(X)
        loss = F.cross_entropy(logits, y)
        loss.backward()
        opt.step()


def leave_one_triad_out(pairs: dict, model_factory, epochs: int = 200) -> dict:
    all_gold, all_pred = [], []
    fold_accs = []
    for held in sorted(pairs):
        seed_everything(20261008 + held)
        train_X, train_y = [], []
        test_X, test_y, test_meta = [], [], []
        for tid, plist in pairs.items():
            for src, tgt, label in plist:
                feat = pair_feature(src, tgt)
                if tid == held:
                    test_X.append(feat)
                    test_y.append(label)
                    test_meta.append((src, tgt))
                else:
                    train_X.append(feat)
                    train_y.append(label)
        Xtr = torch.tensor(train_X, dtype=torch.float32)
        ytr = torch.tensor(train_y, dtype=torch.long)
        Xte = torch.tensor(test_X, dtype=torch.float32)
        model = model_factory(Xtr.shape[1])
        train_sklearn_like(model, Xtr, ytr, epochs=epochs)
        with torch.no_grad():
            pred = model(Xte).argmax(dim=-1).tolist()
        all_gold.extend(test_y)
        all_pred.extend(pred)
        fold_accs.append(sum(a == b for a, b in zip(test_y, pred)) / max(len(test_y), 1))
    result = scores(all_gold, all_pred)
    result["fold_accuracies"] = fold_accs
    result["fold_accuracy_mean"] = round(float(np.mean(fold_accs)), 6)
    result["fold_accuracy_std"] = round(float(np.std(fold_accs)), 6)
    return result


def run_deterministic(pairs: dict) -> dict:
    gold, pred = [], []
    for plist in pairs.values():
        for src, tgt, label in plist:
            gold.append(label)
            s_idx = parse_pair_index(src)
            t_idx = parse_pair_index(tgt)
            pred.append(deterministic_rule_predict(s_idx, t_idx))
    return scores(gold, pred)


def run() -> dict:
    seed_everything()
    pairs = read_pairs()
    report = {
        "description": "Comparación de PI-HGAT-T con clasificadores base sobre el mismo leave-one-triad-out",
        "baselines": {},
    }
    report["baselines"]["deterministic_rules"] = {
        "description": "Oracle que aplica exactamente las reglas SHACL de mirrorOf/creates",
        "metrics": run_deterministic(pairs),
    }
    report["baselines"]["logistic_regression"] = {
        "description": "Softmax linear sobre concatenación de one-hot fase+posición (10 dim)",
        "metrics": leave_one_triad_out(pairs, lambda d: SoftmaxRegression(d), epochs=300),
    }
    report["baselines"]["mlp_no_graph"] = {
        "description": "MLP de dos capas ocultas sin mensaje-passing ni atención",
        "metrics": leave_one_triad_out(pairs, lambda d: SimpleMLP(d, hidden=32), epochs=200),
    }
    out = ROOT / "experiments" / "results" / "baselines_comparison.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Baselines escritos en", out)
    for name, block in report["baselines"].items():
        m = block["metrics"]
        print(f"  {name}: accuracy={m['accuracy']:.4f}  macro_f1={m['macro_f1']:.4f}")
    return report


if __name__ == "__main__":
    run()
