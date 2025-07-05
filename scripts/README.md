# Scripts

## Why this folder matters for TORUS
This folder contains various standalone scripts that support data handling and analysis in the TORUS project. These are Python (and occasionally Bash) tools intended to be run from the command line.

## What it contains
- **fetch_gnss.py**: Downloads GNSS timing data (RINEX files) needed for the GPS satellite clock drift test.
- **fetch_optics.py**: Helper to pull the optics experiment HDF5 from Zenodo.
- **stack_timing.py**: Processes data/bicycle/timing.csv and computes aggregate statistics for analysis in notebooks.
- **update_import_paths.py**: Scans notebooks and fixes import or data file path references after any reorganization.

## How to use
Each script can be executed from the repository root. For example:
- To fetch GNSS data: `python scripts/fetch_gnss.py --date 2025-05-05`
- To fetch optics data: `python scripts/fetch_optics.py`

Many scripts print usage instructions if run with `-h`. Run them before corresponding notebooks if you don’t already have the required data files.

## Next steps
Developers can add new scripts here for any repetitive task. Please document any new script by adding a bullet to this README, including what it does and how to run it.

# Scripts Directory

This directory contains utility scripts for generating data, running simulations, and validating TORUS Theory predictions.

## Key Scripts
- `make_torus_lattices.sh`: Generates TORUS-modified interferometer lattices and spectra. Requires FINESSE and PyKat.
- `regenerate_torus_solutions.py`: Applies TORUS patches to baseline solutions and computes performance metrics.
- `audio_harmonics.py`: Generates audio test tones for sideband analysis.
- `entropy_drift.py`: Simulates entropy drift and generates data for analysis.

## Usage
To run a script, ensure the required dependencies are installed. For example, to run `regenerate_torus_solutions.py`, you may need to install PyKat:

```bash
pip install pykat
```

Refer to individual script comments for specific usage instructions.

# scripts
**Role in TORUS:** Helper scripts for data processing and validation.
**Key files:**
- `make_torus_lattices.sh`: Generates lattice structures.
- `regenerate_torus_solutions.py`: Recomputes solutions.
**Try it:** Run `bash make_torus_lattices.sh`.
**Upstream data:** Uses `data/` for inputs.
**Next steps:** Explore `notebooks/` for validation.
