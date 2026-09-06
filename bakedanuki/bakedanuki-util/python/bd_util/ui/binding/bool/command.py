# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ... import qt


def _require_bool(value: object, argument_name: str) -> bool:
    """値をboolとして検証して返す。"""
    if not isinstance(value, bool):
        raise TypeError(
            f"{argument_name}にはboolを指定してください: "
            f"{type(value).__name__}"
        )
    return value


class SetBoolCommand(qt.QObject):
    """UIとPythonからboolの変更を要求するCommand。"""

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(bool)

    def __init__(
        self,
        execute: Callable[[bool], bool],
        parent: qt.QObject | None = None,
    ) -> None:
        """ViewModelの変更要求処理を受け取って初期化する。"""
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        """現在Commandを実行できるか返す。"""
        return self._can_execute

    def execute(self, value: bool) -> bool:
        """値の変更を要求し、実値が変化したか返す。"""
        value = _require_bool(value, "value")
        if not self._can_execute:
            return False
        changed = self._execute(value)
        self.executed.emit(value)
        return changed
