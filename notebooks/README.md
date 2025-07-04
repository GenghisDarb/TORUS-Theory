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

# Notebooks Directory

This directory contains Jupyter notebooks for validating various aspects of the TORUS Theory framework. The notebooks are organized into subdirectories based on their focus areas, such as entropy analysis, pair-correlation studies, and gravitational wave detection.

## Subdirectories
- `validation/`: Contains notebooks for validating theoretical predictions against experimental or synthetic data.
- `gwd/`: Focuses on gravitational wave detection and analysis.
- `bicycle/`: Includes notebooks related to the Bicycle Balance Mystery and its resolution.

## Running the Notebooks
To run a notebook, ensure you have Python 3 and Jupyter installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

Then, open the desired notebook in Jupyter and execute the cells sequentially.

# notebooks
**Role in TORUS:** Contains Jupyter notebooks for validation and exploration.
**Key files:**
- `validation/`: Phase A and Phase B suites.
- `gwd/`: Gravitational wave detection analysis.
**Try it:** `jupyter nbopen validation/PhaseA.ipynb`.
**Upstream data:** Linked datasets in `data/`.
**Next steps:** Explore `docs/` for theory and CLI tools.

# Bicycle Balance Mystery Validation Suite

This section documents the new validation notebooks and tests for the Bicycle Balance Mystery resolution:

- **recursive_controller_validation.ipynb**: Monte-Carlo recursive controller lean/steer test. Simulates a 14-cycle lean–steer correction loop and validates the controller dimension concept in a classical mechanical setting.
- **constant_ladder_residuals.ipynb**: Linearized stability and eigen-plot placeholder. Computes χ–β ladder residuals using CODATA constants.
- **audio_fft.ipynb**: Audio harmonics χ analysis using PSD of data/audio/recursion14.wav.
- **shannon_bound_compression.ipynb**: Recursive Shannon-bound compression test.
- **timing_stats.ipynb**: Stack timing analysis from data/bicycle/timing.csv.

All notebooks are now located in `notebooks/bicycle/`.

> **Note:** For full reproducibility, ensure `data/audio/recursion14.wav` and `data/bicycle/timing.csv` are present, or update paths as needed.
