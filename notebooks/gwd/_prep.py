from typing import Tuple
import numpy as np
from scipy.signal import butter as _butter


def _safe_butter(
    low: float, high: float, fs: float, order: int = 4
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Validated band-pass Butterworth coefficients (b, a).
    Raises ValueError on invalid band edges.
    """
    if not (0 < low < high < fs / 2):
        raise ValueError(f"Invalid band: low={low}, high={high}, fs={fs}")
    wn = (low / (fs / 2), high / (fs / 2))
    result = _butter(order, wn, btype="band", output="ba")
    if not isinstance(result, tuple) or len(result) != 2:
        raise ValueError("Butterworth filter did not return a valid 2-tuple")
    b, a = result
    return b, a
