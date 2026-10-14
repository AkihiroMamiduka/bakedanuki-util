# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ... import qt
from ._validation import require_int


class SetIntCommand(qt.QObject):
    """UIとPythonから整数値の変更を要求する。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(object)

    def __init__(
        self,
        execute: Callable[[int], bool],
        parent: qt.QObject | None = None,
    ) -> None:
        """変更要求の処理関数を保持する。"""
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        """現在変更を受け付けられるか返す。"""
        return self._can_execute

    def execute(self, value: int) -> bool:
        """検証済みの値を渡し、正本の実値が変わったか返す。"""
        value = require_int(value)
        if not self._can_execute:
            return False
        changed = self._execute(value)
        if qt.isValid(self):
            self.executed.emit(value)
        return changed
