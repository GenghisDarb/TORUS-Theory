import csv
import pathlib
import shutil

import pykat

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
            f.write(f"\n# TORUS χ-lattice patch\nschnupp {p['L']} m\nphi {p['phi']}\n")

        # --- 3 · simulate ---
        kat = pykat.finesse.kat()
        kat.loadKatFile(str(kat_out))
        kat.parseCommands("xaxis * lambda lin 1064 1065 100\n")
        kat.run(printout=False)
        # Save output (placeholder: just save the xaxis and yaxis)
        with open(csv_out, "w", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(["lambda", "PSD"])
            for x, y in zip(kat.xaxis, kat.yaxis):
                writer.writerow([x, y])

        # --- 4 · ΔS integration (very coarse) ---
        psd = list(kat.yaxis)
        deltaS.append(dict(sol=sol, gain=max(psd) if psd else 0))

# save ΔS table
with open("data/interferometer/deltaS_table.csv", "w", newline="") as fp:
    w = csv.DictWriter(fp, fieldnames=["sol", "gain"])
    w.writeheader()
    w.writerows(deltaS)
