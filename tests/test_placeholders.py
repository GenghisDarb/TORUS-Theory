import unittest
from importlib import import_module
import pathlib
import sys
import os

class TestEchoFunctions(unittest.TestCase):
    def test_echo_functions(self):
        # Dynamically resolve the absolute path to the notebooks/gwd directory
        notebooks_gwd_path = pathlib.Path(__file__).parent.parent / "notebooks" / "gwd"
        sys.path.insert(0, str(notebooks_gwd_path))  # Use insert to prioritize this path

        # Debug: Print sys.path to verify paths
        print("Python sys.path:", sys.path)

        # Debug: Print contents of the notebooks/gwd directory
        print("Contents of notebooks/gwd:", os.listdir(notebooks_gwd_path))

        # Verify the resolved path and existence of LIGO_Echo_Torus_vs_T_HET.py
        resolved_path = notebooks_gwd_path / "LIGO_Echo_Torus_vs_T_HET.py"
        print(f"Resolved path to LIGO_Echo_Torus_vs_T_HET.py: {resolved_path}")
        if not resolved_path.exists():
            self.fail(f"LIGO_Echo_Torus_vs_T_HET.py does not exist at {resolved_path}")

        # Ensure notebooks/gwd is treated as a package
        if not (notebooks_gwd_path / "__init__.py").exists():
            self.fail("Missing __init__.py in notebooks/gwd; cannot import as a package.")

        # Debug: Print sys.path after modification
        print("Updated Python sys.path:", sys.path)

        try:
            # Import the module using importlib
            mod = import_module("gwd.LIGO_Echo_Torus_vs_T_HET")

            from gwd import LIGO_Echo_Torus_vs_T_HET as het

            # Example test inputs
            import numpy as np

            strain = np.random.randn(10000)  # Simulated strain data
            fs = 4096  # Sample rate in Hz
            merger_time = 1.0  # Merger peak time in seconds
            tau_base = 0.1  # Example base recursion period
            R_km = 10.0  # Example radius in kilometers

            # Test torus_echo
            torus_result = het.torus_echo(strain, fs, merger_time, tau_base)
            self.assertIn("snr", torus_result)
            self.assertIn("verdict", torus_result)

            # Test thet_echo
            thet_result = het.thet_echo(strain, fs, R_km)
            self.assertIn("snr", thet_result)
            self.assertIn("verdict", thet_result)
        except ImportError as e:
            self.fail(f"Failed to import LIGO_Echo_Torus_vs_T_HET: {e}")

if __name__ == "__main__":
    unittest.main()
