#!/usr/bin/env bash
# Convert every DOCX under docs/book/** to a parallel .tex tree in docs/book-latex/
set -euo pipefail
find docs/book -type f -name '*.docx' -print0 |
while IFS= read -r -d '' file; do
  rel=${file#docs/book/}                  # e.g. chapters/01_Intro…
  out="docs/book-latex/${rel%.docx}.tex"
  mkdir -p "$(dirname "$out")"
  pandoc "$file" -o "$out" --standalone
  # Sanitize problematic Unicode characters for LaTeX compatibility
  sed -i 's/Λ/\\Lambda/g' "$out"
  sed -i 's/ħ/\\hbar/g' "$out"
  sed -i 's/α/\\alpha/g' "$out"
  sed -i 's/≈/\\approx/g' "$out"
  sed -i 's/−/-/g' "$out"
  sed -i 's/ℓ/\\ell/g' "$out"
done
