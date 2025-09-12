import pytest

from mypackage.main import _main


@pytest.mark.parametrize(
    "arg, expected",
    [(1, 1), (2, 2), (3, 3)],
)
def test__main(arg, expected):
    assert _main(arg) == expected
