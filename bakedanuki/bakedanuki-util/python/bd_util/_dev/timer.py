# coding: utf-8
from __future__ import annotations
import functools
import statistics
import time
from typing import Callable, TypeVar, ParamSpec

# self
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

P = ParamSpec("P")
R = TypeVar("R")


def log_elapsed(label: str, elapsed: float):
    logger.debug(f"[timer] {label}: {elapsed:.6f} 秒")


def run_timed(
    func: Callable[P, R],
    *args: P.args,
    label: str | None = None,
    log: bool = True,
    **kwargs: P.kwargs,
) -> tuple[R, float]:
    label = label or func.__qualname__
    start = time.perf_counter()
    try:
        result = func(*args, **kwargs)
    finally:
        elapsed = time.perf_counter() - start
        if log:
            log_elapsed(label, elapsed)
    return result, elapsed


def run_timed_repeat(
    func: Callable[P, R],
    *args: P.args,
    repeat_count: int = 3,
    log_each: bool = True,
    unwrap: bool = True,
    **kwargs: P.kwargs,
) -> list[float]:
    if repeat_count < 1:
        raise ValueError("repeat_count must be greater than 0.")

    raw_func = getattr(func, "__wrapped__", func) if unwrap else func
    label = raw_func.__qualname__
    results = []
    for i in range(repeat_count):
        _, elapsed = run_timed(
            raw_func,
            *args,
            label=f"{label} ({i + 1}/{repeat_count})",
            log=log_each,
            **kwargs,
        )
        results.append(elapsed)

    logger.debug(
        "[timer] {}: median={:.6f} 秒 min={:.6f} 秒 max={:.6f} 秒 runs={}".format(
            label,
            statistics.median(results),
            min(results),
            max(results),
            repeat_count,
        )
    )
    return results


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
        result, _ = run_timed(func, *args, **kwargs)
        return result

    return wrapper
