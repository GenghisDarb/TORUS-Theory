
#!/usr/bin/env python3
"""
TORUS D-2  ·  χ‑Phase Modular Time Test
Usage examples:
  python chi_modtime.py --ticks 28 --dt 0.1 --no_sleep
  python chi_modtime.py --ticks 280 --dt 0.1
"""

import argparse, time, hashlib, csv

def main() -> None:
    parser = argparse.ArgumentParser(description="χ‑Phase modular time simulator")
    parser.add_argument("--ticks", type=int, default=140,
                        help="Total number of logical ticks to simulate")
    parser.add_argument("--dt", type=float, default=0.05,
                        help="Nominal period of each tick, in seconds")
    parser.add_argument("--phase_jump", type=int, default=14,
                        help="Interval for χ rotation (extra dt injected)")
    parser.add_argument("--no_sleep", action="store_true",
                        help="Run instantly without real-time delay")
    args = parser.parse_args()

    logical_t = 0.0
    obs = []

    for k in range(args.ticks):
        if k % args.phase_jump == 0 and k != 0:
            logical_t += args.dt     # χ kick
        logical_t += args.dt         # normal tick
        stamp = hashlib.sha1(f"{logical_t:.9f}".encode()).hexdigest()[:16]
        obs.append((k, logical_t, stamp))
        if not args.no_sleep:
            time.sleep(args.dt)

    lsb = [(obs[i+args.phase_jump][1] - obs[i][1] - args.phase_jump*args.dt)*1e9
           for i in range(len(obs) - args.phase_jump)]

    print("χ‑phase LSB offsets (ns) — first 5:", [round(x, 2) for x in lsb[:5]])

    with open("chi_modtime_trace.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["tick", "logical_t_s", "hash", "delta_ns"])
        for i, row in enumerate(obs[:-args.phase_jump]):
            writer.writerow([*row, round(lsb[i], 2)])

    print("Trace written ➜ chi_modtime_trace.csv")

if __name__ == "__main__":
    main()
