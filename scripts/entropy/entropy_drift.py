#!/usr/bin/env python3
"""Collect 10 MB of entropy from os.urandom and optional CPU‑jitter loops.
Outputs raw binary to entropy_raw.bin and a simple CSV of byte counts."""
import argparse
import csv
import hashlib
import os
import random
import time

parser = argparse.ArgumentParser()
parser.add_argument("--bytes", type=int, default=10_000_000, help="bytes to gather")
args = parser.parse_args()

fname = "data/entropy/entropy_raw.bin"
with open(fname, "wb") as f:
    f.write(os.urandom(args.bytes))

# simple count stats
counts = [0] * 256
with open(fname, "rb") as f:
    for b in f.read():
        counts[b] += 1
with open("data/entropy/entropy_counts.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["byte", "count"])
    for i, c in enumerate(counts):
        w.writerow([i, c])
print(f"Wrote {fname} and entropy_counts.csv")
