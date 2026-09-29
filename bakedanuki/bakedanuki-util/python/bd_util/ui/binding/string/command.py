# coding: utf-8
from collections.abc import Callable

from ... import qt
from ._validation import require_string


class SetStringCommand(qt.QObject):
    """文字列の変更要求をViewModelへ渡す。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(str)

    def __init__(
        self, execute: Callable[[str], bool], parent: qt.QObject | None = None
    ) -> None:
        """確定値が変わったか返す変更処理を指定する。"""
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        """変更要求を受け付けられる場合は`True`。"""
        return self._can_execute

    def execute(self, value: str) -> bool:
        """要求を処理し、正本の実値が変わったか返す。"""
        value = require_string(value)
        if not self._can_execute:
            return False
        changed = self._execute(value)
        self.executed.emit(value)
        return changed
