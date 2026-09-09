# coding: utf-8
from __future__ import annotations

from ... import qt
from ._validation import require_float


class FloatValue(qt.QObject):
    """変更通知を持つ読み取り専用の浮動小数点値。"""

    changed = qt.Signal(float)

    def __init__(
        self, value: float = 0.0, parent: qt.QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._value = require_float(value)

    @property
    def value(self) -> float:
        return self._value
