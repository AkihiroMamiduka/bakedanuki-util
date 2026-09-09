# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast

from .... import qt


class _QueuedSignal(Protocol):
    """QueuedConnectionを指定できるQt signalの型境界。"""

    def connect(
        self,
        slot: Callable[[], None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """slotを指定した接続方式で接続する。"""
        raise NotImplementedError


def connect_queued_qt_signal(
    signal: object,
    slot: Callable[[], None],
) -> qt.QtCore.QMetaObject.Connection:
    """PySide6 6.5のstub差分を閉じ込めてqueued接続する。"""
    queued_signal = cast(_QueuedSignal, signal)
    return queued_signal.connect(
        slot,
        qt.Qt.ConnectionType.QueuedConnection,
    )


def disconnect_qt_connection(
    connection: qt.QtCore.QMetaObject.Connection | None,
) -> None:
    """保持しているQt signal接続を安全に解除する。"""
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
