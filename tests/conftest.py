import inspect
from pathlib import Path

import pytest


@pytest.fixture
def test_dir(request):
    """テストコードのディレクトリパスを取得"""
    return Path(request.fpath).parent


@pytest.fixture
def assert_func_output():
    """関数の出力または例外発生をチェックするヘルパー"""

    def _assert_func_output(func, expected, *args, **kwargs):
        if inspect.isclass(expected) and issubclass(expected, BaseException):
            with pytest.raises(expected):
                func(*args, **kwargs)
        elif expected is None:
            assert func(*args, **kwargs) is None
        else:
            assert func(*args, **kwargs) == expected

    return _assert_func_output
