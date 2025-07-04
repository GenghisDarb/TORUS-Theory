#!/bin/bash

# Create missing directories and placeholder files
echo "Creating missing directories and placeholder files..."
mkdir -p data/interferometer/upstream/GWDetectorZoo/dummy
mkdir -p solutions/baseline

# Add placeholder files
echo "Adding placeholder files..."
echo "delta_ns\n100000\n105000\n98000" > data/bicycle/timing.csv
echo "entropy_counts\n1\n2\n3" > data/entropy/entropy_counts.csv
echo "paircorr_raw_MIT\n0.1\n0.2\n0.3" > data/realdata/paircorr_raw_MIT.csv
echo "dummy kat file" > data/interferometer/upstream/GWDetectorZoo/dummy/dummy.kat
echo "{\"example_key\": \"example_value\"}" > solutions/baseline/example_solution.json

# Ensure scripts are executable
echo "Ensuring scripts are executable..."
chmod +x scripts/*.sh

# Notify completion
echo "Placeholder population complete."

# ensure all stubs carry a python3 kernelspec
python3 - <<'PY'
import nbformat, pathlib
for nb_path in pathlib.Path("notebooks").rglob("*.ipynb"):
    nb = nbformat.read(nb_path, as_version=4)
    ks = nb["metadata"].setdefault("kernelspec", {"name": "python3",
                                                  "display_name": "Python 3",
                                                  "language": "python"})
    if ks["name"] != "python3":
        ks.update(name="python3", display_name="Python 3", language="python")
        nbformat.write(nb, nb_path)
PY
