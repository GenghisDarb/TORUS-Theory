import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))           # repo root first

NOTEBOOKS = ROOT / "notebooks"
sys.path.insert(0, str(NOTEBOOKS))       # ensure notebooks directory is discoverable

GWD = NOTEBOOKS / "gwd"
sys.path.insert(0, str(GWD))       # ensure gwd directory is discoverable
