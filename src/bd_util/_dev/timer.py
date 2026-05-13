# coding: utf-8
from __future__ import annotations
import time
import functools
from typing import Callable, TypeVar, ParamSpec

# self
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

P = ParamSpec("P")
R = TypeVar("R")


def timer(func: Callable[P, R]) -> Callable[P, R]:
    """
    関数の処理時間を計測するデコレーター。
    関数の実行前後の時刻を記録し、経過時間をログに出力する。

    Args:
        func (Callable): 計測対象の関数

    Returns:
        Callable: ラップされた関数

    Example:
        @timer
        def heavy_process():
            ...
    """

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logger.debug(f"[timer] {func.__qualname__}: {elapsed:.6f} 秒")
        return result

    return wrapper
