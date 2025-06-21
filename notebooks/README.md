# Notebooks Overview

This folder contains Jupyter notebooks for TORUS Theory simulations and validations. They are organized into subdirectories:

- **validation/synthetic/** – Synthetic data tests and benchmarks (e.g., side-band injection tests, noise robustness).
- **validation/realdata/** – Notebooks for real experimental or observational datasets (e.g., pair-correlation analysis on real data).
- **validation/constants/** – Phase B notebooks testing fundamental constant relationships (ladder precision, multi-probe seed constant).
- **validation/optics/** – Phase B notebooks for optical/interferometric tests (Talbot carpet side-band analysis, etc.).

Most notebooks include a standard setup cell (imports and helper functions) and print a **TORUS-POSITIVE** or **TORUS-NEGATIVE** result indicating whether TORUS-theoretic signatures are detected.

**Usage:** To run a notebook, ensure you have installed the required libraries (`requirements.txt`) and have the necessary data files. Some notebooks will attempt to download large data (e.g., `.h5` files) when run – an internet connection or prior data setup is required for those.

For headless or CI execution, interactive notebooks (like those prompting file selection) may need modifications (or use provided default data paths).
