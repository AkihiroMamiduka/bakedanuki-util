# coding: utf-8
from ... import qt
from .definition import require_enum_value


class EnumValue(qt.QObject):
    """最後に同期した整数値。選択肢にない実値も保持する。"""

    # Python整数をQtの32bit intへ狭めない。
    changed = qt.Signal(object)

    def __init__(
        self, value: int = 0, parent: qt.QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._value = require_enum_value(value)

    @property
    def value(self) -> int:
        return self._value
