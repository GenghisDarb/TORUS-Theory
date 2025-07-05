from gwd._prep import _safe_butter
import pytest


def test_safe_bandpass():
    b, a = _safe_butter(30, 300, fs=4096)
    assert b.size == a.size and b.ndim == 1


def test_invalid_band():
    with pytest.raises(ValueError):
        _safe_butter(0, 300, fs=4096)
