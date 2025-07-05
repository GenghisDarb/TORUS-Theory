# TORUS-Theory — Repository Plan (v0.9 “Phase-B ready”)

## Folder Structure (post-sweep)

TORUS-Theory/
├── notebooks/
│   └── validation/
│       ├── audio/ # χ-audio validation notebooks
│       ├── bicycle/ # Bicycle dynamics validation
│       ├── entropy/ # Entropy drift validation
│       ├── ladder/ # Constant-ladder validation
│       ├── realdata/ # Real-world pair-corr data
│       ├── tests/ # Small, repeatable synthetic tests ← add README
│       └── … # Future domains (optics, gw, etc.)
├── data/
│   ├── audio/ # Audio data (recursion14.wav, timing.csv)
│   ├── entropy/ # Entropy counts + raw bin
│   ├── gnss/ # FLRS00… RINEX data
│   └── … # Other data domains
├── scripts/ # Analysis & utility scripts
├── docs/
│   ├── figures/ # All images / figs for papers
│   ├── papers/ # Stand-alone PDFs / DOCX
│   └── visualization/ # Visualization prompts / outputs
├── torus_brot/ # Fractal renderer + validation logic
└── tests/ # pytest / doctest unit tests (fast)

## README Checklist
* **Add or update README.md** in every new folder above.  
  – Purpose · Contents · How it links to TORUS validation  
  – Naming conventions (`YYYY-MM-DD_topic.ipynb` vs `guide_*.ipynb`)

## `.gitattributes`
```gitattributes
*.ipynb filter=nbstripout diff=ipynb
*.bin filter=lfs diff=lfs
*.wav filter=lfs diff=lfs
```