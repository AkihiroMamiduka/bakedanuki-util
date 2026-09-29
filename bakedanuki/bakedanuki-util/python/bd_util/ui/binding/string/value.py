# coding: utf-8
from ... import qt
from ._validation import require_string


class StringValue(qt.QObject):
    """最後に同期した確定文字列を読み取り専用で公開する。"""

    changed = qt.Signal(str)

    def __init__(
        self, value: str = "", parent: qt.QObject | None = None
    ) -> None:
        """初期の確定文字列を保持する。"""
        super().__init__(parent)
        self._value = require_string(value)

    @property
    def value(self) -> str:
        """最後に同期した文字列を返す。"""
        return self._value
