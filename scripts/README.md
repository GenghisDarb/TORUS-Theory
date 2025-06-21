# Scripts

This directory contains utility scripts for maintenance and data processing in the TORUS Theory project:

- **restore_structure.sh** – Reorganizes the repository file structure to the canonical layout (moves and renames files to their proper folders). Typically used after major document imports or merges.
- **audit_structure.sh** – *(Planned)* Script to verify that all files and filenames conform to the expected slug rules and directory layout (mentioned in README; to be implemented).
- **make_torus_lattices.sh** – Uses FINESSE (via PyKat) to generate TORUS-modified interferometer models and their strain spectra. *(Currently uses placeholder logic for lattice modifications.)*
- **regenerate_torus_solutions.py** – Python version of lattice generation: copies base solutions and applies χ-lattice parameter patches, then runs simulations to produce updated spectra and a summary table of ΔS gains. *(Contains placeholder steps to be improved.)*
- **fetch_structured_light.py** – Downloads structured-light experiment data from Zenodo (DOI:10.5281/zenodo.14002229) on-demand. Used by notebooks to retrieve large `.h5` files at runtime instead of storing them in the repo.

These scripts are typically run from the repository root. Ensure required dependencies (e.g., `pykat`, `finesse`) are installed for the interferometer scripts.
