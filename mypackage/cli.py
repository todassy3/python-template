"""CLI"""
from __future__ import annotations


def sample_func(val1: int, val2: int | None = None) -> int:
    """サンプル関数"""
    if val2 is None:
        raise ValueError("Sample value error")

    return val1 + val2


def _main() -> None:
    """メイン関数"""
    print("hello world")


if __name__ == "__main__":
    _main()
