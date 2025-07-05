# Data Directory Overview

This directory contains all data assets used in the TORUS Theory project. Subfolders:

- **interferometer/** – Raw and processed data from interferometer experiments. See `interferometer/README.md` for details.
- **ladder/** – CODATA ladder fit CSVs and RMS results. See `ladder/README.md` for format and usage.
- **optics/** – Optical experiment data (HDF5, TIFF). Large files are fetched on-demand via Zenodo DOI:10.5281/zenodo.14002229. See `optics/README.md`.
- **gnss/** – GNSS (Global Navigation Satellite System) data, including RINEX files. See `gnss/README.md` for fetch instructions and file structure.

Each subfolder may contain its own README with more details and data provenance. For large datasets, see the relevant Zenodo DOI or fetch helper script in `scripts/`.

# Data
This directory contains domain-specific data files used in TORUS Theory analyses.

## Subdirectories
- **audio/**: Audio data for harmonic recursion experiments.
- **bicycle/**: Timing and chi-modtime trace data.
- **entropy/**: Entropy drift and spectrum data.
- **ladder/**: CODATA ladder fit CSVs and RMS results.
- **optics/**: Optical experiment data (HDF5, TIFF).

## Notes
Large binary files are fetched on-demand via scripts or Zenodo links. See individual subdirectory README files for details.
