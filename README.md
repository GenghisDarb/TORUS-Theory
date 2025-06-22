# TORUS Theory 📚

[![Notebook CI](https://github.com/GenghisDarb/TORUS-Theory/actions/workflows/execute_notebooks.yml/badge.svg)](https://github.com/GenghisDarb/TORUS-Theory/actions/workflows/execute_notebooks.yml)

TORUS Theory extends standard gauge theory by embedding every field and interaction inside a 14-dimensional \(\chi\)-\(\beta\) harmonic lattice; the resulting closure matrix forces each recursion loop to return to unity, simultaneously resolving black-hole entropy, measurement paradoxes, and the unification of all four fundamental forces. From this single topological move flow predictive links between quantum amplitudes, gravitational curvature, large-scale cosmology, and observer-state dynamics—yielding testable signatures in gravitational-wave spectra, particle-decay branching ratios, and recursive-intelligence architectures.

---

## 📂 Folder layout

| Path | Contents |
|------|-----------|
| `docs/book-docx-fixed/` | Canonical DOCX: all edits here; legacy `docs/book/` retained for historical diff only |
| `docs/book/frontmatter/` | `00_Preface.docx`, `Table_of_Contents.docx` |
| `docs/book/chapters/` | 15 chapter DOCX files (`01_…` – `15_…`) |
| `docs/book/appendices/` | Appendices A–E (`A_…` – `E_…`) |
| `docs/papers/` | Stand-alone research papers & monographs |
| `docs/validation/` | Phase-A/B cross-domain validation `.tex` + detector executive summary |
| `docs/experiments/` | Bench protocols & lab worksheets |
| `.github/workflows/` | CI: slug-rule & structure audit (WIP) |

_All filenames are ASCII-safe “slugs”: spaces → underscores, Unicode letters spelled out (e.g., `\chi` → `Chi`)._

### Data availability
Raw structured-light data are archived on Zenodo  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14002229.svg)](https://doi.org/10.5281/zenodo.14002229)

Only the lightweight `.h5` bundles are pulled automatically at run-time;  
the multi-GB TIFF stacks remain on Zenodo to keep this repo lean.

---

## Canonical Documents

The following canonical documents are available in DOCX, TEX, and PDF formats:

### Book
- [TORUS Book (DOCX)](docs/book/torus_book.docx)
- [TORUS Book (TEX)](docs/book-latex/torus_book.tex)
- [TORUS Book (PDF)](docs/book-latex/torus_book.pdf)

### Supplements
- [Dimensional Constants Interrelation in TORUS Theory (0D–13D) – Formal Derivation and Closure (PDF,DOCX,TEX)](docs/supplements/Dimensional%20Constants%20Interrelation%20in%20TORUS%20Theory%20(0D%E2%80%9313D)%20%E2%80%93%20Formal%20Derivation%20and%20Closure.pdf)
- [Gravitational-Wave-Detector Validation – Executive Summary (v1.0) (PDF,DOCX,TEX)](docs/supplements/Gravitational-Wave-Detector%20Validation%20%E2%80%93%20Executive%20Summary%20(v1.0).pdf)
- [Hyper-Recursive Algebra in TORUS Theory (PDF,DOCX,TEX)](docs/supplements/Hyper-Recursive%20Algebra%20in%20TORUS%20Theory.pdf)
- [Resolving the Black Hole Entropy and Information Paradox via TORUS Structured Recursion (PDF,DOCX,TEX)](docs/supplements/Resolving%20the%20Black%20Hole%20Entropy%20and%20Information%20Paradox%20via%20TORUS%20Structured%20Recursion.pdf)
- [Topology of the Torus‑of‑Tori, chi-beta‑Function, and the Projection‑Angle Theorem (PDF,DOCX,TEX)](docs/supplements/Topology%20of%20the%20Torus%E2%80%91of%E2%80%91Tori,%20chi-beta%E2%80%91Function,%20and%20the%20Projection%E2%80%91Angle%20Theorem.pdf)

### Validation Data
- Ladder fit data (CODATA): [`data/ladder/ladder_fit_multiCODATA.csv`](data/ladder/ladder_fit_multiCODATA.csv)
- RMS fit results: [`data/ladder/ladder_fit_rms_multi.txt`](data/ladder/ladder_fit_rms_multi.txt)

### Validation
- [Universal Recursion - A 12 Sigma Cross-Domain Validation (Phase A) (PDF,DOCX,TEX)](docs/validation/Universal%20Recursion%20-%20A%2012%20Sigma%20Cross-Domain%20Validation%20(Phase%20A).pdf)
- [Universal Recursion - A 14 Sigma Cross-Domain Validation (Phase B) (PDF,DOCX,TEX)](docs/validation/Universal%20Recursion%20-%20A%2014%20Sigma%20Cross-Domain%20Validation%20(Phase%20B).pdf)
See notebooks/validation/ladder/ for precision re-test of Stationary-Action ladder with CODATA 2022.

### Experiments
- [OSQN Drift in a Quartz-Oscillator Loop Lab Worksheet (PDF,DOCX,TEX)](docs/experiments/OSQN%20Drift%20in%20a%20Quartz-Oscillator%20Loop%20Lab%20Worksheet.pdf)

---

## 🛠️ Getting started

```bash
git clone https://github.com/GenghisDarb/TORUS-Theory.git
cd TORUS-Theory
# optional: run the audit script to verify structure
bash scripts/audit_structure.sh   # (coming soon)
pip install -r requirements.txt   # now includes mpmath, scipy, etc.
```

---

## Quick start

```bash
# run SimLab locally
docker run -it --rm ghcr.io/genghisdarb/torus-simlab:latest torus-cli --help
```

---

## Validation Suite

- [Side-Band Primer](docs/SideBand_Primer.md)
- [Synthetic Benchmark (PairCorr_SideBand_Benchmark.ipynb)](notebooks/validation/synthetic/PairCorr_SideBand_Benchmark.ipynb)
- [Real-Data Template (PairCorr_Fourier_SideBand.ipynb)](notebooks/validation/realdata/PairCorr_Fourier_SideBand.ipynb)
- [Noise-Sweep ROC (Noise_Sweep_ROC.ipynb)](notebooks/validation/synthetic/Noise_Sweep_ROC.ipynb)

**Phase B**
- B1 – [Constant Ladder Precision Re-Test](notebooks/validation/constants/Validation_ConstantLadder_PrecisionReTest.ipynb)
- B2 – [Seed-Constant Multi-Probe](notebooks/validation/constants/Validation_SeedConstant_MultiProbe.ipynb)
- B4 – [Talbot Side-Band Multiframe](notebooks/validation/optics/Validation_Talbot_SideBand_Multiframe.ipynb)

---

## Bicycle Balance Mystery Resolution

A new suite of validation notebooks has been added to resolve the Bicycle Balance Mystery:

- **recursive_controller_validation.ipynb**: Monte-Carlo recursive controller lean/steer test.
- **constant_ladder_residuals.ipynb**: Linearized stability and eigen-plot placeholder.
- **audio_fft.ipynb**: Audio harmonics χ analysis.
- **shannon_bound_compression.ipynb**: Recursive Shannon-bound compression test.
- **timing_stats.ipynb**: Stack timing analysis.

All are located in `notebooks/bicycle/`. See that folder's README for details.

> **Note:** If you have a publication draft (e.g., `docs/papers/bicycle_balance_TORUS.pdf`), link it here for reference.

---

## Data
Processed interferometer outputs and provenance live in
[data/interferometer/upstream/solutions/](data/interferometer/upstream/solutions/) – see its README for details.

---

## License & Contact
MIT License
Maintainer: Genghis Darb <genghis.darb@gmail.com>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GenghisDarb/TORUS-Theory/main?labpath=README.ipynb)
