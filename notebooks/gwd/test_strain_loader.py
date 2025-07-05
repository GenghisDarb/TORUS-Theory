import numpy as np
from LIGO_Echo_Torus_vs_T_HET import _prep


def generate_synthetic_strain(fs, duration):
    """Generate synthetic strain data for testing."""
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    strain = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    return strain


if __name__ == "__main__":
    fs = 4096  # Sampling frequency in Hz
    duration = 10  # Duration in seconds
    strain = generate_synthetic_strain(fs, duration)

    print("Testing _prep function with synthetic strain data...")
    whitened_strain = _prep(strain, fs)
    print("Whitened strain shape:", whitened_strain.shape)
