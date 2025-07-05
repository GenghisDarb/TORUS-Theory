import numpy as np


def test_brot_fft_peak():
    # Mock TORUS-brot data
    torus_brot = np.sin(np.linspace(0, 2 * np.pi, 256))
    fft_peak = np.argmax(np.abs(np.fft.fft(torus_brot)))
    assert fft_peak == 1, "FFT peak not at χ frequency bin"
