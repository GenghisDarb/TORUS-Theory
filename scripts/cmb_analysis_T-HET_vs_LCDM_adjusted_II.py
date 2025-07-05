import os
import urllib.request

try:
    import numpy as np  # noqa: F401
except ImportError as exc:
    raise SystemExit(
        "numpy not installed – CI env must install requirements-ci.txt"
    ) from exc

from entropic_spectrum import thet_tt  # scripts package now on path


def ensure_planck_tt_data():
    """Ensure Planck TT spectrum file exists, download if missing."""
    planck_path = "data/cmb/COM_PowerSpect_CMB-TT-full_R3.01.txt"
    url = "https://pla.esac.esa.int/pla-sl/data-action?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-TT-full_R3.01.txt"
    if not os.path.exists(planck_path):
        os.makedirs(os.path.dirname(planck_path), exist_ok=True)
        print(f"Downloading Planck TT data to {planck_path} ...", end=" ", flush=True)

        def reporthook(blocknum, blocksize, totalsize):
            downloaded = blocknum * blocksize
            percent = (
                min(100, int(downloaded * 100 / totalsize)) if totalsize > 0 else 0
            )
            print(f"{percent}%", end="\r", flush=True)

        urllib.request.urlretrieve(url, planck_path, reporthook)
        print("Download complete.")
    return planck_path


# --- Real entropic-modal T-HET TT curve ---
ell_array = np.arange(2, 2508)
Cl_TT_Thet = thet_tt(ell_array)

# After computing Cl_TT_Thet and ell_array, export to file:
output_path = "data/cmb/Cl_TT_T-HET_model.txt"
if not os.path.exists(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    np.savetxt(output_path, np.column_stack([ell_array, Cl_TT_Thet]))
    print("Saved T-HET spectrum to data/cmb/Cl_TT_T-HET_model.txt")
