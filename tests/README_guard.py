import pathlib

def validate_readme():
    for folder in pathlib.Path(".").iterdir():
        if folder.name.startswith("."):
            continue
        if folder.name == "docker":
            continue
        readme_path = folder / "README.md"
        if not readme_path.exists():
            print(f"Missing README in {folder}")

if __name__ == "__main__":
    validate_readme()
