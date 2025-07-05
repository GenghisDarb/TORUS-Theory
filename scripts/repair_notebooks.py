# TORUS-Theory Repository Reorganization Plan

## Updated Folder Structure

import nbformat
import json
import pathlib
import shutil

root = pathlib.Path(".")
stub = {"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 2}
fixed = []

for p in root.rglob("*.ipynb"):
    try:
        txt = p.read_text(encoding="utf-8")
        if len(txt.strip()) < 300:
            raise ValueError("too small")
        nb = nbformat.reads(txt, as_version=4)
        if len(nb.cells) == 0:
            raise ValueError("zero cells")
    except Exception:
        bak = p.with_suffix(".ipynb.bak")
        shutil.copy2(p, bak)
        p.write_text(json.dumps(stub, indent=1))
        fixed.append(p)

print(f"patched {len(fixed)} notebook(s):")
for f in fixed:
    print(" ", f)
