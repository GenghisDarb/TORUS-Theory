# Notebooks Overview

This folder contains Jupyter notebooks for TORUS Theory simulations and validations. They are organized into subdirectories:

- **validation/synthetic/** – Synthetic data tests and benchmarks (e.g., side-band injection tests, noise robustness).
- **validation/realdata/** – Notebooks for real experimental or observational datasets (e.g., pair-correlation analysis on real data).
- **validation/constants/** – Phase B notebooks testing fundamental constant relationships (ladder precision, multi-probe seed constant).
- **validation/optics/** – Phase B notebooks for optical/interferometric tests (Talbot carpet side-band analysis, etc.).
- **validation/bicycle/** – Bicycle and controller recursion validation (e.g., recursive controller, pair-correlation)
- **validation/audio/** – Audio side-band and FFT validation
- **validation/entropy/** – Entropy drift and related experiments

Most notebooks include a standard setup cell (imports and helper functions) and print a **TORUS-POSITIVE** or **TORUS-NEGATIVE** result indicating whether TORUS-theoretic signatures are detected.

**Usage:** To run a notebook, ensure you have installed the required libraries (`requirements.txt`) and have the necessary data files. Some notebooks will attempt to download large data (e.g., `.h5` files) when run – an internet connection or prior data setup is required for those.

For headless or CI execution, interactive notebooks (like those prompting file selection) may need modifications (or use provided default data paths).

# Bicycle Balance Mystery Validation Suite

This section documents the new validation notebooks and tests for the Bicycle Balance Mystery resolution:

- **recursive_controller_validation.ipynb**: Monte-Carlo recursive controller lean/steer test. Simulates a 14-cycle lean–steer correction loop and validates the controller dimension concept in a classical mechanical setting.
- **constant_ladder_residuals.ipynb**: Linearized stability and eigen-plot placeholder. Computes χ–β ladder residuals using CODATA constants.
- **audio_fft.ipynb**: Audio harmonics χ analysis using PSD of recursion14.wav.
- **shannon_bound_compression.ipynb**: Recursive Shannon-bound compression test.
- **timing_stats.ipynb**: Stack timing analysis from timing.csv.

All notebooks are now located in `notebooks/bicycle/`.

> **Note:** For full reproducibility, ensure `recursion14.wav` and `timing.csv` are present in the repo root or update paths as needed.
