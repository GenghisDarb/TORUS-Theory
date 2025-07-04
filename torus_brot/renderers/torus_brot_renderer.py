#!/usr/bin/env python3
"""
torus_brot_renderer.py – minimal renderer for the TORUS-brot fractal.
Usage:
    python torus_brot_renderer.py --out img.png
"""
import json, argparse, numpy as np, matplotlib.pyplot as plt, pathlib, hashlib
PARAMS = json.loads((pathlib.Path(__file__).parents[1] / 'data/sample_params.json').read_text())

def torus_brot(z0, max_iter=512, escape=4.0):
    z = complex(z0)
    for n in range(max_iter):
        z = (abs(z.real) + 1j*abs(z.imag))**2 + z0  # simple “brot on torus” toy map
        if abs(z) > escape:
            return n
    return max_iter

def render_grid(n=400):
    xs = np.linspace(-2, 2, n)
    ys = np.linspace(-2, 2, n)
    img = np.zeros((n, n), dtype=np.uint16)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            img[j, i] = torus_brot(complex(x, y),
                                   max_iter=PARAMS["max_iter"],
                                   escape=PARAMS["escape_radius"])
    return img

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="torus_brot.png")
    args = ap.parse_args()

    pic = render_grid()
    plt.imshow(pic, cmap="inferno", extent=[-2, 2, -2, 2])
    plt.title("TORUS-brot demo")
    plt.axis("off")
    plt.savefig(args.out, dpi=300, bbox_inches="tight")
    h = hashlib.sha256(open(args.out, "rb").read()).hexdigest()[:8]
    print(f"✓ saved {args.out}  sha256:{h}")
