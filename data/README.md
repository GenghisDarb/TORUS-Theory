# Data Directory Overview

This directory contains all data assets used in the TORUS Theory project. Subfolders:

- **interferometer/** – Raw and processed data from interferometer experiments. See `interferometer/README.md` for details.
- **ladder/** – CODATA ladder fit CSVs and RMS results. See `ladder/README.md` for format and usage.
- **structured_light/** – Structured-light experiment data (HDF5, TIFF). Large files are fetched on-demand via Zenodo DOI:10.5281/zenodo.14002229. See `structured_light/README.md`.
- **gnss/** – GNSS (Global Navigation Satellite System) data, including RINEX files. See `gnss/README.md` for fetch instructions and file structure.

Each subfolder may contain its own README with more details and data provenance. For large datasets, see the relevant Zenodo DOI or fetch helper script in `scripts/`.
