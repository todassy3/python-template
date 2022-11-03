from pathlib import Path

import pytest


@pytest.fixture
def test_dir(request):
    """Get test directory path"""
    return Path(request.fpath).parent
