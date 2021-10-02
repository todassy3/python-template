import pytest
from mypackage.cli import sample_func


@pytest.mark.parametrize(
    "val1, val2, expected",
    [(1, 2, 3), (1, None, ValueError)],
)
def test_sample_func(assert_func_output, val1, val2, expected):
    assert_func_output(sample_func, expected, val1, val2=val2)
