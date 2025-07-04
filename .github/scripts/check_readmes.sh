#!/bin/bash

# Check for missing README.md files in top-level directories
missing=$(find . -maxdepth 2 -type d \
          -not -path "./.*" -not -path "./.git*" \
          -not -path "./torus_cli*" -exec test ! -e '{}/README.md' ';' -print)

if [ -z "$missing" ]; then
  echo "All directories have README.md files."
  exit 0
else
  echo "Missing READMEs:";
  echo "$missing";
  exit 1
fi
