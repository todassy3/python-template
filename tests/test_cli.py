import pytest

from mypackage.cli import sample_func


@pytest.mark.parametrize(
    "val1, val2, expected",
    [(1, 2, 3), (2, 3, 5)],
)
def test_sample_func_success(val1, val2, expected):
    assert sample_func(val1, val2=val2) == expected


@pytest.mark.parametrize(
    "val1, val2, expected",
    [(1, None, ValueError)],
)
def test_sample_func_fail(val1, val2, expected):
    with pytest.raises(expected):
        sample_func(val1, val2=val2)
