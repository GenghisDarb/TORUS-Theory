# Interferometer - Upstream Solutions  
*(TORUS-Theory data bundle)*

This folder is the **home of solved / processed outputs** that originate from
raw interferometer runs stored in  
`data/interferometer/upstream/raw/`.

| Sub-folder | What it contains | Typical file type |
|------------|------------------|-------------------|
| `phase_maps/` | 2-D wrapped phase images (one per frame) | `.npy`, `.tiff` |
| `unwrap/`    | Unwrapped phase maps after Goldstein or PUMA | `.npy` |
| `spectra/`   | 2-D FFT magnitude spectra used in side-band analysis | `.h5`, `.png` |
| `reports/`   | Auto-generated HTML / PDF run summaries | `.html`, `.pdf` |

---

## File-naming convention  

YYYYMMDD_runNNN_<stage>[_descriptor].ext

* **`YYYYMMDD`** – UTC date of acquisition  
* **`runNNN`** – zero-padded run index from the raw folder  
* **`stage`** – `phase`, `unwrap`, `fft`, `report`, …  
* **`descriptor`** – optional (e.g. `hann`, `1over14mask`)  

Example  
20250512_run042_fft_hann.npy

---

## Provenance / reproducibility  

Each file here should have a matching entry in  
`data/interferometer/PROVENANCE.csv` with columns:

file_path, raw_source, pipeline_hash, torus_version, notes

* **`pipeline_hash`** is the first 8 chars of the git commit that produced it.  
* Use `torus-cli provenance add` to append new rows automatically.  

---

## Re-running the pipeline  

From repo root:

```bash
pip install -r requirements.txt      # once
torus-cli interferometer solve \
    --raw data/interferometer/upstream/raw/20250512_run042 \
    --out data/interferometer/upstream/solutions \
    --mask 1over14
```

The tool will:
- Perform Goldstein unwrapping
- Apply Hann window → FFT
- Save outputs into the sub-folders above
- Append a provenance row

---

## Contributing new solutions

- Create a branch named `feat/solution-<date>-<run>`
- Drop processed files into the correct sub-folder(s)
- Run `torus-cli provenance add`
- Commit & open a PR

Please avoid committing raw data (>50 MB) in this tree; keep them under
`upstream/raw/` or link via an external DOI.

