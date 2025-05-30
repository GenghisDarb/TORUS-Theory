### Validation-repo tasks
1. Copy upstream GWDetectorZoo models (tag 94d3c01) into data/interferometer/upstream/.
2. Add TORUS lattice .kat files & spectra CSVs into data/interferometer/torus_lattice/ and data/interferometer/spectra/.
3. Add notebooks:
   • notebooks/interferometer/gw_run_pipeline.ipynb
   • notebooks/PhaseA/chi_beta_ladder_fit.nb
   • …
4. Export ladder_fit_results.csv & ladder_fit_rms.txt next to the notebook.
5. Commit all files with message: “Add validation datasets & notebooks (v1.0)”.
6. Create a Git tag v1.0.
7. Trigger GitHub Release & Zenodo DOI via the CI workflow.

Copilot Chat (in VS Code or the browser) will take each numbered instruction, generate the git commands, and even draft the copy-paste code snippets you need.

2 · One-shot GitHub Actions workflow (auto-release & Zenodo)
Add .github/workflows/release.yml:

```yaml
name: Build validation release
on:
  push:
    tags: ["v*"]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0   # gets the tag commit
      - name: Create GitHub release
        uses: ncipollo/release-action@v1
        with:
          allowUpdates: true
          draft: false
          generatesReleaseNotes: true
          artifacts: |
            data/**/*
            notebooks/**/*.{ipynb,nb}
      - name: Upload Zenodo metadata
        if: ${{ secrets.ZENODO_TOKEN != '' }}
        uses: openjournals/zenodo-action@v1
        with:
          token: ${{ secrets.ZENODO_TOKEN }}
```

What this does: whenever you push/tag v1.0 Copilot (or you) the workflow packages the repo, publishes a GitHub Release, and (if you drop your encrypted Zenodo token into repository → Settings → Secrets) deposits the same archive at Zenodo, returning a DOI. (See <attachments> above for file contents. You may not need to search or read the file again.)
