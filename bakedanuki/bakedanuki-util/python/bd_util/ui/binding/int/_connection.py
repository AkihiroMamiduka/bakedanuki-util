# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from ... import qt


class _QueuedSignal(Protocol):
    """Qtの遅延接続に必要なsignal境界。"""

    def connect(
        self,
        slot: Callable[[], None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """指定方式でslotへ接続する。"""
        raise NotImplementedError


def connect_queued(
    signal: object, slot: Callable[[], None]
) -> qt.QtCore.QMetaObject.Connection:
    """Qt stubの差を局所化して破棄signalを遅延接続する。"""
    return cast(_QueuedSignal, signal).connect(
        slot, qt.Qt.ConnectionType.QueuedConnection
    )


def disconnect(
    connection: qt.QtCore.QMetaObject.Connection | None,
) -> None:
    """保持した接続だけを安全に解除する。"""
    if connection is None:
        return
    try:
        method = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QtCore.QObject, "disconnect"),
        )
        method(connection)
    except (RuntimeError, TypeError):
        pass
