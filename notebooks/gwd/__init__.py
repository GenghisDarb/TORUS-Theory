"""
gwd package – Gravitational-Wave validation modules
Exports:
    LIGO_Echo_Torus_vs_T_HET
"""

from importlib import import_module

LIGO_Echo_Torus_vs_T_HET = import_module(".LIGO_Echo_Torus_vs_T_HET", package=__name__)
__all__ = ["LIGO_Echo_Torus_vs_T_HET"]
