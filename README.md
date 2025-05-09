# TORUS Theory 📚

A unified, recursion-based framework that integrates gravity, quantum mechanics, and observer-state dynamics into a single mathematical architecture.  
This repository contains the book manuscript, peer-review papers, validation suites, and laboratory protocols that collectively define and test **TORUS Theory**.

---

## 📂 Folder layout

| Path | Contents |
|------|-----------|
| `docs/book-docx-fixed/` | Canonical DOCX: all edits here; legacy `docs/book/` retained for historical diff only |
| `docs/book/frontmatter/` | `00_Preface.docx`, `Table_of_Contents.docx` |
| `docs/book/chapters/`   | 15 chapter DOCX files (`01_…` – `15_…`) |
| `docs/book/appendices/` | Appendices A–E (`A_…` – `E_…`) |
| `docs/papers/` | Stand-alone research papers & monographs |
| `docs/validation/` | Phase-A/B cross-domain validation `.tex` + detector executive summary |
| `docs/experiments/` | Bench protocols & lab worksheets |
| `.github/workflows/` | CI: slug-rule & structure audit (WIP) |

_All filenames are ASCII-safe “slugs”: spaces → underscores, Unicode letters spelled out (e.g., `χ` → `Chi`)._

---

## 🛠 Getting started

```bash
git clone https://github.com/GenghisDarb/TORUS-Theory.git
cd TORUS-Theory
# optional: run the audit script to verify structure
bash scripts/audit_structure.sh   # (coming soon)
