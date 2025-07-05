from typing import Tuple
import numpy as np
from scipy.signal import butter as _butter

def _safe_butter(
    low: float,
    high: float,
    fs: float,
    order: int = 4
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return band-pass Butterworth coefficients, validated.

    Raises
    ------
    ValueError
        If low/high band edges are not 0 < low < high < fs/2.
    """
    if not (0 < low < high < fs / 2):
        raise ValueError(
            f"Invalid band: low={low}, high={high}, fs={fs}"
        )
    wn = (low / (fs / 2), high / (fs / 2))
    b, a = _butter(order, wn, btype="band")
    return b, a
