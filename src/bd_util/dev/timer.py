# coding: utf-8

# builtin
import functools
import time
from collections.abc import Callable
from typing import Any

# self
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.LogLevel.INFO)


def measure_time(func: Callable) -> Callable:
    """
    関数の処理速度を計測するデコレーター

    計測結果は INFO レベルのログとして出力される。
    一時的に付与・取り外しができる。

    Args:
        func (Callable): 計測対象の関数

    Returns:
        Callable: ラップされた関数

    Example:
        @measure_time
        def heavy_process():
            ...
    """

    @functools.wraps(func)
    def _wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("[measure_time] %s: %.6f 秒", func.__qualname__, elapsed)
        return result

    return _wrapper
