#!/usr/bin/env python3
"""
Download individual .h5 assets from Zenodo record 14002229.
Keeps a tiny local cache; avoids pulling 1.9-GB Data.tar.gz unless --all.
"""
import argparse
import pathlib
import sys

import requests
import tqdm

RECORD = "14002229"
API = f"https://zenodo.org/api/records/{RECORD}"
CACHE = pathlib.Path("data/optics")
CACHE.mkdir(parents=True, exist_ok=True)


def _zenodo_file_map():
    meta = requests.get(API, timeout=30).json()
    return {f["key"].lstrip("./"): f["links"]["self"] for f in meta["files"]}


FILES = _zenodo_file_map()


def download(name):
    url = FILES[name]
    out = CACHE / name
    if out.exists():
        return out
    print(f"[fetch] {name} …")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        with (
            open(out, "wb") as fh,
            tqdm.tqdm(total=total, unit="B", unit_scale=True) as bar,
        ):
            for chunk in r.iter_content(chunk_size=8192):
                fh.write(chunk)
                bar.update(len(chunk))
    return out


def ensure_h5(name):
    if not (CACHE / name).exists():
        download(name)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("files", nargs="*")
    args = p.parse_args()

    targets = FILES.keys() if args.all else args.files
    if not targets:
        print("Specify --all or filenames.")
        sys.exit(0)
    for f in targets:
        if not args.quiet:
            print("→", f)
        ensure_h5(f)
