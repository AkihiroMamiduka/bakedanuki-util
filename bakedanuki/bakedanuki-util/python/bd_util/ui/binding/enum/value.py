# coding: utf-8
from ... import qt
from .definition import require_enum_value


class EnumValue(qt.QObject):
    """最後に同期した整数値。選択肢にない実値も保持する。

    Attributes:
        changed: 確定値の変更をPython整数で通知する。
    """

    # Python整数をQtの32bit intへ狭めない。
    changed = qt.Signal(object)

    def __init__(
        self, value: int = 0, parent: qt.QObject | None = None
    ) -> None:
        """初期値を保持する。

        Args:
            value: 初期の整数値。`bool`は受け付けない。
            parent: この値objectを所有するQObject。
        """
        super().__init__(parent)
        self._value = require_enum_value(value)

    @property
    def value(self) -> int:
        """最後に同期した整数値を返す。"""
        return self._value
