import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))       # ensure repo root first

import pytest
from gwd._prep import _safe_butter

def test_safe_butter_ok():
    b, a = _safe_butter(30, 300, fs=4096)
    assert len(b) == len(a)                   # simple shape sanity

def test_safe_butter_bad():
    with pytest.raises(ValueError):
        _safe_butter(0, 300, fs=4096)        # low=0 invalid
