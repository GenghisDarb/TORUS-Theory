import json
from pathlib import Path


def list_ci_skip_notebooks():
    notebooks_dir = Path("notebooks")
    for notebook in notebooks_dir.rglob("*.ipynb"):
        with open(notebook, "r") as f:
            data = json.load(f)
            if "ci-skip" in data.get("metadata", {}).get("tags", []):
                print(notebook)


if __name__ == "__main__":
    list_ci_skip_notebooks()
