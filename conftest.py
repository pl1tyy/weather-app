import sys
import pathlib
root_dir = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, str(root_dir))
import pytest
pytest_plugins = ['pytest_asyncio']