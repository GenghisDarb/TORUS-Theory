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

    # Redirect output to a writable directory
    output_dir="torus_brot/output"
    mkdir -p "$output_dir"
    katout_path="$output_dir/katout.txt"

    # === STEP 2: run FINESSE simulation via PyKat ===
    pykat "$kat_out" > "$katout_path"
    # Assume pykat writes strain spectrum to katout.txt; convert to CSV
    grep '^PSD' "$katout_path" | awk '{print $2","$3}' > "$csv_out"
  done
done

# === STEP 3: compute ΔS table ===
python notebooks/interferometer/gw_run_pipeline.ipynb --to python --stdout | \
  python - > data/interferometer/deltaS_table.csv

for cfg in interferometers/*.kat; do
    base=$(basename "$cfg" .kat)
    # inject χ-mass-aging: finesse param mass -> mass*(1+1/14)
    sed -E 's/^Mass *= *([0-9.]+)/Mass = \1*1.0714286/' "$cfg" \
      > "interferometers/χ_${base}.kat"
done
echo "χ-lattice configs regenerated ✔"

# --- TORUS MODIFICATION SCRIPT ---

# Requirements: FINESSE/PyKat installed, base .kat files present in docs/ or a known directory.
# This script will loop over base interferometer configurations and apply TORUS theory adjustments.

BASE_DIR="docs/finesse_models"   # hypothetical directory with base .kat files
OUTPUT_DIR="torus_brot/output"   # directory to save modified lattices and results
mkdir -p "$OUTPUT_DIR"

# TORUS parameters (example values; in practice, determine from TORUS theory)
CHI_PHASE_SHIFT=1e-15    # e.g., slight refractive index shift equivalent
EXTRA_POLARIZATION=0.001 # e.g., introduce a small scalar polarization component

echo "Generating TORUS-modified interferometer lattices..."
DRY_RUN=false
command -v finesse >/dev/null 2>&1 || { echo "⚠️  FINESSE not installed – running in dry-run mode."; DRY_RUN=true; }

for katfile in "$BASE_DIR"/*.kat; do
  fname=$(basename "$katfile")
  torus_kat="$OUTPUT_DIR/torus_${fname}"
  cp "$katfile" "$torus_kat"
  echo "# TORUS modifications:" >> "$torus_kat"
  echo "param chi_phase $CHI_PHASE_SHIFT" >> "$torus_kat"    # placeholder: an example global parameter
  echo "## (Placeholder for actual TORUS lattice modifications)" >> "$torus_kat"
  # For example, we might tweak mirror masses, add a thin lens, or adjust a cavity length to simulate recursion effects.

  if [ "$DRY_RUN" = true ]; then continue; fi
  # Run FINESSE on the modified .kat file to get output (assuming `kat` CLI available)
  finesse "$torus_kat" "$OUTPUT_DIR/${fname%.kat}_torus.out" || echo "FINESSE run failed for $fname"
done

echo "Done. Modified lattice files and outputs are in $OUTPUT_DIR."
