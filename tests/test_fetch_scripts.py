import os
from pathlib import Path

EXPECTED = Path.home() / ".torus_cache/optics/talbot_processed.h5"

def test_fetch_script():
    # Mock fetch script output
    expected_files = ["data/optics/mock_file.h5"]
    for file in expected_files:
        assert os.path.exists(file), f"File {file} not found"
    assert EXPECTED.exists()
