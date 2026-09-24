# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
import functools
import statistics
import time
from typing import ParamSpec, TypeVar, cast

# self
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

P = ParamSpec("P")
R = TypeVar("R")


def log_elapsed(label: str, elapsed: float) -> None:
    logger.debug(f"[timer] {label}: {elapsed:.6f} 秒")


def run_timed(
    func: Callable[..., R],
    *args: object,
    label: str | None = None,
    log: bool = True,
    **kwargs: object,
) -> tuple[R, float]:
    """関数を1回実行し、実行結果と経過秒数を返す。

    Args:
        func: 計測対象の関数。
        *args: 関数へ渡す位置引数。
        label: ログに表示する名前。省略時は関数の修飾名。
        log: 経過時間をログへ出力するか。
        **kwargs: 関数へ渡すキーワード引数。

    Returns:
        関数の戻り値と経過秒数の組。
    """
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
    func: Callable[..., object],
    *args: object,
    repeat_count: int = 3,
    log_each: bool = True,
    unwrap: bool = True,
    **kwargs: object,
) -> list[float]:
    """関数を指定回数実行し、各回の経過秒数を返す。

    Args:
        func: 計測対象の関数。
        *args: 関数へ渡す位置引数。
        repeat_count: 実行回数。1以上を指定する。
        log_each: 各回の経過時間もログへ出力するか。
        unwrap: デコレーターが付いた関数を1段展開するか。
        **kwargs: 関数へ渡すキーワード引数。

    Returns:
        実行順の経過秒数。

    Raises:
        ValueError: ``repeat_count`` が1未満の場合。
    """
    if repeat_count < 1:
        raise ValueError("repeat_count must be greater than 0.")

    raw_func = (
        cast(Callable[..., object], getattr(func, "__wrapped__", func))
        if unwrap
        else func
    )
    label = raw_func.__qualname__
    results: list[float] = []
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
    """関数の経過時間をログへ出力するデコレーター。

    Args:
        func: 計測対象の関数。

    Returns:
        元の戻り値を保つラッパー関数。

    Examples:
        @timer
        def heavy_process():
            ...
    """

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        result, _ = run_timed(func, *args, **kwargs)
        return result

    return wrapper
