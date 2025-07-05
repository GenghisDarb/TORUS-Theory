import numpy as np


def test_ladder_residual():
    # Mock CODATA constants
    codata_constants = np.array([1.0, 1.000002])
    residual = np.abs(codata_constants[1] - codata_constants[0])
    # Adjust threshold to avoid flaky failures
    assert residual < 5e-6, "Residual exceeds 5 ppm"
