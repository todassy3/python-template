import pytest
from mypackage.cli import sample_func


@pytest.mark.parametrize(
    "arg, kwarg, expected",
    [(1, 2, 3), (1, None, ValueError)],
)
def test_sample_func(assert_func_output, arg, kwarg, expected):
    assert_func_output(sample_func, expected, arg, kwarg=kwarg)
