#!/usr/bin/env python
import pathlib

SKIP_DIRS = {"PhaseA", ".ipynb_checkpoints"}

for nb in pathlib.Path("notebooks").rglob("*.ipynb"):
    if any(part in SKIP_DIRS for part in nb.parts):
        continue
    print(nb)
