# coding: utf-8
from collections.abc import Callable, Sequence

from ... import qt
from .value import Float3, require_float3


class SetFloat3Command(qt.QObject):
    """公開単位で3成分の一括変更を要求する。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(object)

    def __init__(
        self,
        execute: Callable[[Float3], bool],
        parent: qt.QObject | None = None,
    ) -> None:
        """変更要求の実行先とownerを保持する。"""
        super().__init__(parent)
        self._execute = execute
        self._can_execute = False

    @property
    def can_execute(self) -> bool:
        """3成分すべてを変更できるか返す。"""
        return self._can_execute

    def execute(self, value: Sequence[float]) -> bool:
        """3成分を検証して変更を要求し、実値が変わったか返す。"""
        values = require_float3(value)
        if not self._can_execute:
            return False
        changed = self._execute(values)
        if qt.isValid(self):
            self.executed.emit(values)
        return changed
