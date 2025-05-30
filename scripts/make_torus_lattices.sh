#!/usr/bin/env bash
set -e

# ensure PyKat & FINESSE 3 are available
pip install pykat==1.2.94 finesse==3.0a32

mkdir -p data/interferometer/torus_lattice data/interferometer/spectra

for base in data/interferometer/upstream/GWDetectorZoo/*/; do
  name=$(basename "$base")               # e.g. Voyager
  for t in {5..9}; do
    kat_out="data/interferometer/torus_lattice/type${t}_${name}.kat"
    csv_out="data/interferometer/spectra/type${t}_${name}_strain.csv"

    # === STEP 1: apply TORUS lattice modifications (placeholder) ===
    # Here you would call a Python script or sed patch that converts
    # the upstream .kat into a type-t χ-lattice variant.
    #
    # For illustration, copy upstream file:
    cp "${base}"/*.kat "$kat_out"

    # === STEP 2: run FINESSE simulation via PyKat ===
    pykat "$kat_out" > /katout.txt
    # Assume pykat writes strain spectrum to katout.txt; convert to CSV
    grep '^PSD' /katout.txt | awk '{print $2","$3}' > "$csv_out"
  done
done

# === STEP 3: compute ΔS table ===
python notebooks/interferometer/gw_run_pipeline.ipynb --to python --stdout | \
  python - > data/interferometer/deltaS_table.csv
