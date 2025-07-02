#!/usr/bin/env python3
"""
audio_harmonics.py  –  TORUS χ-phase demo
Generates a 5-second mono WAV (44.1 kHz) of a 440 Hz sine fed through a
14-tap delay-feedback loop.  χ-prediction: PSD shoulders at ± f₀/14
(≈ 407 Hz and 472 Hz).
Usage:  python audio_harmonics.py
"""
import argparse
import math
import struct
import wave


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--f0", type=float, default=440, help="carrier freq (Hz)")
    p.add_argument("--dur", type=float, default=5.0, help="seconds")
    p.add_argument("--rate", type=int, default=44100, help="sample rate")
    args = p.parse_args()

    fs, dur, f0 = args.rate, args.dur, args.f0
    delay, taps = 400, 14  # 200-sample tap ×14
    buf = [0.0] * (delay * taps)
    out = []

    for n in range(int(fs * dur)):
        x = math.sin(2 * math.pi * f0 * n / fs)
        y = x + 0.8 * buf[n % len(buf)]  # feedback
        buf[n % len(buf)] = y
        out.append(int(max(min(y, 1), -1) * 32767))

    with wave.open("recursion14.wav", "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(fs)
        w.writeframes(b"".join(struct.pack("<h", s) for s in out))

    print("Wrote recursion14.wav  ({} samples)".format(len(out)))


if __name__ == "__main__":
    main()
