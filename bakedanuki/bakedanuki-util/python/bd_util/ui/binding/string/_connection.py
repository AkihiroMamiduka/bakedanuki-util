# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from ... import qt


class _QueuedSignal(Protocol):
    """Qt signalのqueued接続に必要な型境界。"""

    def connect(
        self,
        slot: Callable[[], None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """指定した接続方式でslotを登録する。"""
        raise NotImplementedError


def connect_queued_qt_signal(
    signal: object, slot: Callable[[], None]
) -> qt.QtCore.QMetaObject.Connection:
    """PySide stub差分を閉じ込めてqueued接続する。"""
    return cast(_QueuedSignal, signal).connect(
        slot, qt.Qt.ConnectionType.QueuedConnection
    )


def disconnect_qt_connection(
    connection: qt.QtCore.QMetaObject.Connection | None,
) -> None:
    """保持しているQt signal接続を解除する。"""
    if connection is None:
        return
    try:
        disconnect = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QtCore.QObject, "disconnect"),
        )
        disconnect(connection)
    except (RuntimeError, TypeError):
        pass
