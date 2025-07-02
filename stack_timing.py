#!/usr/bin/env python3
"""14-deep call-stack timing test.
Usage:  python stack_timing.py --iters 20000 --trace latent --csv timing.csv
"""
import time, argparse, csv, statistics, sys
p = argparse.ArgumentParser()
p.add_argument("--iters", type=int, default=20000)
p.add_argument("--trace", choices=["latent","none"], default="latent")
p.add_argument("--csv",  default=None, help="write raw Δt to CSV")
args = p.parse_args()

sys.setrecursionlimit(1000)
def recurse(n):
    if n == 0:
        return
    recurse(n-1)

deltas = []
for _ in range(args.iters):
    t0 = time.perf_counter_ns()
    recurse(14 if args.trace=="latent" else 0)
    deltas.append(time.perf_counter_ns() - t0)

μ, σ = statistics.mean(deltas), statistics.stdev(deltas)
print(f"mean {μ:.0f} ns   σ {σ:.0f} ns   sample {args.iters}")

if args.csv:
    with open(args.csv, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["delta_ns"]); w.writerows([[d] for d in deltas])
    print(f"wrote {args.csv}")
