#!/usr/bin/env python3
"""
Scan every *.ipynb in the repo, make sure it is valid JSON,
inject a kernelspec if missing, and drop in a universal bootstrap cell
(imports, RNG seed, safe-sigma helper, etc.).  Idempotent: re-running
won’t duplicate cells.
"""
import json, pathlib, uuid, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOT_CELL_TAG = "TORUS-BOOTSTRAP-CELL"

BOOT_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "id": str(uuid.uuid4()),
    "metadata": {"tags": [BOOT_CELL_TAG]},
    "outputs": [],
    "source": [
        "# --- 🚀 TORUS universal imports / helpers ---\n",
        "import os, json, math, numpy as np, pandas as pd, matplotlib.pyplot as plt\n",
        "from scipy.stats import chi2, pearsonr\n",
        "from scipy.special import erfcinv\n",
        "np.random.seed(42)\n",
        "\n",
        "# Safe σ helper – never let σ==0 blow up χ²\n",
        "def safe_sigma(sig, floor=1e-12):\n",
        "    sig = np.asarray(sig, dtype=float)\n",
        "    bad = sig < floor\n",
        "    if bad.any():\n",
        "        print(f'[boot] σ floor applied to {bad.sum()} cells')\n",
        "        sig[bad] = floor\n",
        "    return sig\n",
    ],
}

def patch_notebook(path: pathlib.Path):
    raw = path.read_text(encoding='utf-8')
    if not raw.strip():                   # empty file → leave for user to fill
        print(f"[skip] {path} is empty")
        return
    try:
        nb = json.loads(raw)
    except json.JSONDecodeError:
        print(f"[warn] {path} is corrupted JSON – open & fix manually")
        return

    # 1. kernelspec
    meta = nb.setdefault("metadata", {})
    if "kernelspec" not in meta:
        meta["kernelspec"] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        }
        print(f"[fix] kernelspec added → {path}")

    # 2. bootstrap cell
    if not any(c.get("metadata", {}).get("tags") == [BOOT_CELL_TAG] for c in nb["cells"]):
        nb["cells"].insert(0, BOOT_CELL)
        print(f"[fix] bootstrap cell injected → {path}")

    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')

def main():
    for ipynb in ROOT.rglob("*.ipynb"):
        patch_notebook(ipynb)

if __name__ == "__main__":
    main() or sys.exit(0)
