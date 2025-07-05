import pathlib
import sys

SKIP = {".git", ".github", ".pytest_cache", "docker"}
ROOT = pathlib.Path(__file__).resolve().parents[1]


def validate() -> None:
    missing: list[pathlib.Path] = []
    for p in ROOT.iterdir():
        if not p.is_dir() or p.name in SKIP or p.name.startswith("."):
            continue
        if not (p / "README.md").exists():
            missing.append(p)
    if missing:
        print("\n".join(f"Missing README in {m}" for m in missing))
        sys.exit(1)  # pragma: no cover


if __name__ == "__main__":
    validate()
