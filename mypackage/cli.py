"""CLI"""
from __future__ import annotations


def sample_func(val1: int, val2: int | None = None) -> int:
    """sample function"""
    if val2 is None:
        raise ValueError("value error")

    return val1 + val2


def _main() -> None:
    """main"""
    print("hello world")


if __name__ == "__main__":
    _main()
