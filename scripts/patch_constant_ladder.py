import nbformat as nbf
from pathlib import Path

NB = Path("notebooks/validation/ladder/Validation_ConstantLadder_PrecisionReTest.ipynb")
nb = nbf.read(NB, as_version=4)

# ----- 1. prepend CODATA-2022 cell -----
cell = nbf.v4.new_code_cell(
    """
# Fetch CODATA-2022 constants and compute residual vector δ = M·C.
import urllib.request, pandas as pd, numpy as np, pathlib, json

CODATA_URL = "https://physics.nist.gov/cuu/Constants/Table/allascii.txt"
txt = urllib.request.urlopen(CODATA_URL, timeout=10).read().decode().splitlines()
wanted = {"alpha": "alpha", "h": "h", "c": "c", "G": "G", "k": "k"}
const = {}
for line in txt:
    fields = line.split()
    if fields and fields[0] in wanted:
        const[wanted[fields[0]]] = float(fields[1])

# assume matrix M and label list already defined later in notebook
print("[INFO] CODATA 2022 constants loaded:", const)
"""
)
nb.cells.insert(0, cell)

# ----- 2. append residual + verdict cell -----
residual_cell = nbf.v4.new_code_cell(
    """
# Compute residual vector once M and labels are defined (they appear below).
try:
    delta = M @ np.array([const[s] for s in symbols])  # symbols ordered same as C
    verdict = "TORUS PASSES" if np.all(np.abs(delta) < 3e-6) else "TORUS FAILS"
    print("Residuals:", delta)
    print("Verdict:", verdict)
    out = pd.DataFrame({"relation": labels, "residual": delta})
    out.to_csv("data/ladder/ladder_resid_2022.csv", index=False)
except NameError:
    print("[WARN] Run this cell after the matrix M is defined below.")
"""
)
nb.cells.append(residual_cell)

nbf.write(nb, NB)
print("Patched notebook ✔")
