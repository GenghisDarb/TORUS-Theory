"""
gwd package – Gravitational-Wave Detector validation modules
"""
from importlib import import_module

# lazy import so pykat can remain optional
_LIGO = import_module(".LIGO_Echo_Torus_vs_T_HET", package=__name__)

# re-export for `from gwd import LIGO_Echo_Torus_vs_T_HET`
LIGO_Echo_Torus_vs_T_HET = _LIGO
__all__ = ["LIGO_Echo_Torus_vs_T_HET"]
