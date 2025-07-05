import csv
import pathlib
import shutil
import json
import os
from math import log10

try:
    import pykat  # noqa: F401
except ImportError:
    PYKAT_OK = False

    class _NoKat:
        def __getattr__(self, name):
            raise RuntimeError(
                "pykat not installed; run `pip install pykat` "
                "or rerun regenerate_torus_solutions.py with --no-kat"
            )

    pykat = _NoKat()  # type: ignore
else:
    PYKAT_OK = True

import pandas as pd
import glob
import re
import numpy as np

base_dir = pathlib.Path("data/interferometer/upstream/GWDetectorZoo")
out_kat = pathlib.Path("data/interferometer/torus_lattice")
out_csv = pathlib.Path("data/interferometer/spectra")
out_kat.mkdir(parents=True, exist_ok=True)
out_csv.mkdir(parents=True, exist_ok=True)
deltaS = []

# χ-lattice deterministic parameter sets
params = {
    5: {"L": 14, "phi": 0.00},
    6: {"L": 14, "phi": 0.02},
    7: {"L": 14, "phi": 0.04},
    8: {"L": 14, "phi": 0.06},
    9: {"L": 14, "phi": 0.08},
}

if PYKAT_OK:
    for base in base_dir.glob("solutions/type*/sol*/CFGS_*.txt"):
        family = base.parent.parent.name  # typeX
        solnum = base.parent.name  # solYY
        for t, p in params.items():
            sol = f"type{t}_sol1_{family}_{solnum}"
            kat_out = out_kat / f"{sol}.kat"
            csv_out = out_csv / f"{sol}_strain.csv"

            # --- 1 · copy pristine model ---
            shutil.copy(base, kat_out)

            # --- 2 · append χ-lattice optics (placeholder patch) ---
            with kat_out.open("a") as f:
                f.write(
                    f"\n# TORUS χ-lattice patch\nschnupp {p['L']} m\nphi {p['phi']}\n"
                )

            # --- 3 · simulate ---
            try:
                kat = pykat.finesse.kat()
                kat.loadKatFile(str(kat_out))
                kat.parseCommands("xaxis * lambda lin 1064 1065 100\n")
                kat.run()
                # Save output (placeholder: just save the xaxis and yaxis)
                with open(csv_out, "w", newline="") as fp:
                    writer = csv.writer(fp)
                    writer.writerow(["lambda", "PSD"])
                    for x, y in zip(
                        getattr(kat, "xaxis", []), getattr(kat, "yaxis", [])
                    ):
                        writer.writerow([x, y])

                # --- 4 · ΔS integration (very coarse) ---
                psd = list(getattr(kat, "yaxis", []))
                deltaS.append(dict(sol=sol, gain=max(psd) if psd else 0))
            except AttributeError as e:
                print(f"Error during simulation for {sol}: {e}")

    # save ΔS table
    with open("data/interferometer/deltaS_table.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["sol", "gain"])
        w.writeheader()
        w.writerows(deltaS)
else:
    print("⚠️  PyKat (FINESSE) not installed; skipping lattice regeneration.")
    print("    → Install with:  pip install pykat  (after installing FINESSE)")
    exit(0)


def main():
    if not PYKAT_OK:
        print("⚠️  PyKat (FINESSE) not installed; skipping lattice regeneration.")
        print("    → Install with:  pip install pykat  (after installing FINESSE)")
        exit(0)

    files = sorted(glob.glob("results/χ_*_noise.csv"))
    out = []
    for f in files:
        df = pd.read_csv(f)
        ΔS = np.trapz(df["strain"] ** 2, df["freq"])
        out.append({"config": re.sub(r".*/χ_(.*)_noise.csv", r"\1", f), "ΔS": ΔS})
    pd.DataFrame(out).to_csv("results/ΔS_summary.csv", index=False)
    print("Wrote results/ΔS_summary.csv")

    # Ensure PyKat-specific logic is only executed if PyKat is available
    if PYKAT_OK:
        for base in base_dir.glob("solutions/type*/sol*/CFGS_*.txt"):
            family = base.parent.parent.name  # typeX
            solnum = base.parent.name  # solYY
            for t, p in params.items():
                sol = f"type{t}_sol1_{family}_{solnum}"
                kat_out = out_kat / f"{sol}.kat"
                csv_out = out_csv / f"{sol}_strain.csv"

                # --- 1 · copy pristine model ---
                shutil.copy(base, kat_out)

                # --- 2 · append χ-lattice optics (placeholder patch) ---
                with kat_out.open("a") as f:
                    f.write(
                        f"\n# TORUS χ-lattice patch\nschnupp {p['L']} m\nphi {p['phi']}\n"
                    )

                # --- 3 · simulate ---
                try:
                    kat = pykat.finesse.kat()
                    kat.loadKatFile(str(kat_out))
                    kat.parseCommands("xaxis * lambda lin 1064 1065 100\n")
                    kat.run()
                    # Save output (placeholder: just save the xaxis and yaxis)
                    with open(csv_out, "w", newline="") as fp:
                        writer = csv.writer(fp)
                        writer.writerow(["lambda", "PSD"])
                        for x, y in zip(
                            getattr(kat, "xaxis", []), getattr(kat, "yaxis", [])
                        ):
                            writer.writerow([x, y])

                    # --- 4 · ΔS integration (very coarse) ---
                    psd = list(getattr(kat, "yaxis", []))
                    deltaS.append(dict(sol=sol, gain=max(psd) if psd else 0))
                except AttributeError as e:
                    print(f"Error during simulation for {sol}: {e}")

    # save ΔS table
    with open("data/interferometer/deltaS_table.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["sol", "gain"])
        w.writeheader()
        w.writerows(deltaS)


# regenerate_torus_solutions.py – Apply TORUS patches to baseline solutions and compute ΔS metrics
# Directories for input and output
BASE_SOL_DIR = "solutions/baseline"  # hypothetical directory of baseline solution JSONs
TORUS_SOL_DIR = "solutions/torus_modified"
os.makedirs(TORUS_SOL_DIR, exist_ok=True)

# Example TORUS parameters to apply (these would come from theory or prior calculations)
TORUS_PARAMS = {
    "chi_factor": 0.7071,  # e.g., modify a coupling constant by sqrt(1/2) per recursion
    "extra_dof": 1,  # e.g., add one extra degree of freedom or state variable
}


def apply_torus_modifications(base_data):
    """Apply TORUS modifications to a single solution data dict."""
    mod_data = base_data.copy()
    # Placeholder logic: iterate over numeric fields and apply a simple factor
    for key, val in base_data.items():
        if isinstance(val, (int, float)):
            # Example modification: scale certain parameters
            mod_data[key] = val * TORUS_PARAMS.get("chi_factor", 1)
    mod_data["TORUS_patch_applied"] = True
    mod_data["TORUS_params_used"] = TORUS_PARAMS
    return mod_data


def compute_delta_S(base_data, torus_data):
    """Compute performance difference (ΔS) between base and torus solutions."""
    # Placeholder: if 'sensitivity' or similar metric exists, compute log10 ratio
    base_sens = base_data.get("sensitivity", 1.0)
    torus_sens = torus_data.get("sensitivity", 1.0)
    delta = 10 * log10(torus_sens / base_sens)
    return delta


# Process each baseline solution file
summary = {}
if not list(pathlib.Path(BASE_SOL_DIR).glob("*.json")):
    print("⚠️  No baseline solutions found – skipping regeneration.")
    exit(0)

for fname in os.listdir(BASE_SOL_DIR):
    if fname.endswith(".json"):
        base_path = os.path.join(BASE_SOL_DIR, fname)
        torus_path = os.path.join(TORUS_SOL_DIR, fname)
        with open(base_path, "r") as f:
            base_solution = json.load(f)
        # Apply TORUS modifications
        torus_solution = apply_torus_modifications(base_solution)
        # Compute ΔS (or other relevant metrics)
        delta_S = compute_delta_S(base_solution, torus_solution)
        summary[fname] = {"delta_S_dB": round(delta_S, 3)}
        # Save the modified solution
        with open(torus_path, "w") as f_out:
            json.dump(torus_solution, f_out, indent=2)
        print(f"Processed {fname}: ΔS = {delta_S:.2f} dB")

# Save summary of all solutions
with open(os.path.join(TORUS_SOL_DIR, "summary_deltaS.json"), "w") as f_sum:
    json.dump(summary, f_sum, indent=2)
print("Regeneration complete. Summary saved to summary_deltaS.json")
