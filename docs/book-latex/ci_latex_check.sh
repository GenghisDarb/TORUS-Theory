#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
#  CI helper: enumerate ALL undefined macros & tab-mark errors
# ─────────────────────────────────────────────────────────────
# (Run this in the LaTeX build step before latexmk -pdf)

set -euo pipefail

LATEX_FILE="docs/book-latex/torus_book.tex"
LOG="docs/book-latex/torus_book_first.log"

# 1) first pass, stop on first error
echo "[CI] Running first-pass LaTeX dry compile (error-stop mode)..."
latexmk -pdf -interaction=errorstopmode -file-line-error -halt-on-error -jobname=torus_book_first "$LATEX_FILE" || true

# 2) collect undefined macros & tab-mark errors
missing=$(grep -oP "(?<=Undefined control sequence\\)\\\\[A-Za-z@]+" "$LOG" | sort -u || true)
tabs=$(grep -n -E "Illegal unit of measure|tab mark here|Misplaced alignment tab character &" "$LOG" || true)

echo "::group::LaTeX error summary"
if [ -n "$missing" ]; then
  echo "❌ **Undefined macros**"
  echo "$missing" | sed 's/^/  - /'
else
  echo "✅ No undefined macros found."
fi
if [ -n "$tabs" ]; then
  echo -e "\n❌ **Stray & or \\ outside alignment**"
  echo "$tabs" | sed 's/^/  - /'
else
  echo "✅ No stray tab marks found."
fi
echo "::endgroup::"

# 3) fail the job if any errors
if [ -n "$missing" ] || [ -n "$tabs" ]; then
  echo "::error::LaTeX fatal errors detected. See summary above."
  exit 1
fi

# 4) otherwise continue to full build
echo "[CI] No fatal errors found. Proceeding to full LaTeX build..."
latexmk -pdf -interaction=nonstopmode -file-line-error "$LATEX_FILE"
