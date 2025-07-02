#!/usr/bin/env python3
"""
Download a RINEX file from NASA CDDIS to data/gnss/rinex/YYYYMM/ if missing.
Usage: ensure_rinex("AUCK00NZL", "2025-05-05", "30S")
"""
import os, pathlib, requests, datetime

def ensure_rinex(station, date, interval="30S"):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    y, m, d = dt.year, dt.month, dt.day
    y2 = str(y)[2:]
    doy = dt.strftime("%j")
    folder = pathlib.Path(f"data/gnss/rinex/{y}{m:02d}")
    folder.mkdir(parents=True, exist_ok=True)
    fname = f"{station}_{y}{m:02d}{d:02d}_{interval}.rnx.gz"
    out = folder / fname
    if out.exists():
        print(f"[gnss] {fname} already present.")
        return out
    url = f"https://cddis.nasa.gov/archive/gnss/data/daily/{y}/{doy}/{y2}o/{station.lower()}{doy}0.{y2}o.gz"
    print(f"[gnss] Downloading {url}")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    with open(out, "wb") as f:
        f.write(r.content)
    print(f"[gnss] Saved to {out}")
    return out

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--sample", nargs=2, metavar=("STATION", "DATE"))
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()
    if args.sample:
        ensure_rinex(args.sample[0], args.sample[1])
