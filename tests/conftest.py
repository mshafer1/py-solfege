"""Configure pytest."""

import pytest_readme

# pytest_readme.setup creates a test_readme.py that contains the contents
# of the readme for pytest to pick up the doctests
pytest_readme.setup()
