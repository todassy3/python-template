"""CLI"""
from __future__ import annotations


def sample_func(arg: int, kwarg: int | None = None) -> int:
    """サンプル関数"""
    if kwarg is None:
        raise ValueError("Sample value error")

    return arg + kwarg


def _main() -> None:
    """メイン関数"""
    print("hello world")


if __name__ == "__main__":
    _main()
