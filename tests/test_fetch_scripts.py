import os

def test_fetch_script():
    # Mock fetch script output
    expected_files = ["data/optics/mock_file.h5"]
    for file in expected_files:
        assert os.path.exists(file), f"File {file} not found"
