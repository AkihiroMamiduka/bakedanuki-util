# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ... import qt
from ._validation import require_float


class SetFloatCommand(qt.QObject):
    """UIとPythonから公開単位の値変更を要求する。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(float)

    def __init__(
        self,
        execute: Callable[[float], bool],
        parent: qt.QObject | None = None,
    ) -> None:
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        return self._can_execute

    def execute(self, value: float) -> bool:
        """変更要求を渡し、正本の実値が変わったか返す。"""
        value = require_float(value)
        if not self._can_execute:
            return False
        changed = self._execute(value)
        if qt.isValid(self):
            self.executed.emit(value)
        return changed
