# coding: utf-8
from __future__ import annotations

from ... import qt
from ._validation import require_int


class IntValue(qt.QObject):
    """変更通知を持つ読み取り専用の整数値。"""

    changed = qt.Signal(object)

    def __init__(
        self, value: int = 0, parent: qt.QObject | None = None
    ) -> None:
        """符号付き32-bit整数で初期化する。"""
        super().__init__(parent)
        self._value = require_int(value)

    @property
    def value(self) -> int:
        """最後に確定した整数値を返す。"""
        return self._value
