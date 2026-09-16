# coding: utf-8
from collections.abc import Callable

from ... import qt
from .definition import require_enum_value


class SetEnumCommand(qt.QObject):
    """整数値による選択要求をViewModelへ渡す。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(object)

    def __init__(
        self, execute: Callable[[int], bool], parent: qt.QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        return self._can_execute

    def execute(self, value: int) -> bool:
        value = require_enum_value(value)
        if not self._can_execute:
            return False
        changed = self._execute(value)
        self.executed.emit(value)
        return changed
