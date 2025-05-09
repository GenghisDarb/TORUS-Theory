#!/usr/bin/env bash
# Convert every DOCX under docs/book/** to a parallel .tex tree in docs/book-latex/
set -euo pipefail
find docs/book -type f -name '*.docx' -print0 |
while IFS= read -r -d '' file; do
  rel=${file#docs/book/}                  # e.g. chapters/01_Intro…
  out="docs/book-latex/${rel%.docx}.tex"
  mkdir -p "$(dirname "$out")"
  pandoc "$file" -o "$out" --standalone
done
