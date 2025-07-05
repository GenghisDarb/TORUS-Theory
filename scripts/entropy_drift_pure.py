#!/usr/bin/env python3
"""
entropy_drift_pure.py  –  raw CPU-jitter entropy (no C extension)
Collects 10 MB of entropy via perf_counter_ns jitter.
Outputs:
  entropy_raw.bin     (10 MB)
  entropy_counts.csv  (256-byte histogram)
"""
import time, csv, argparse
p = argparse.ArgumentParser(); p.add_argument('--bytes', type=int, default=10_000_000)
args = p.parse_args()

buf = bytearray()
print(f'Collecting {args.bytes/1e6:.1f} MB of jitter …')
while len(buf) < args.bytes:
    t1 = time.perf_counter_ns()
    t2 = time.perf_counter_ns()
    buf.append((t2 - t1) & 0xFF)        # take 8 LSBs of timing jitter

open('entropy_raw.bin', 'wb').write(buf)
print('Wrote entropy_raw.bin')

counts = [0]*256
for b in buf:
    counts[b] += 1
with open('entropy_counts.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['byte','count'])
    w.writerows(enumerate(counts))
print('Wrote entropy_counts.csv')
