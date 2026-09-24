# coding: utf-8
from collections.abc import Callable

from ... import qt
from .definition import require_enum_value


class SetEnumCommand(qt.QObject):
    """整数値による選択要求をViewModelへ渡す。

    Attributes:
        can_execute_changed: 実行可否の変化を`bool`で通知する。
        executed: 受理した要求値を`int`で通知する。
    """

    can_execute_changed = qt.Signal(bool)
    executed = qt.Signal(object)

    def __init__(
        self, execute: Callable[[int], bool], parent: qt.QObject | None = None
    ) -> None:
        """値の設定処理を指定する。

        Args:
            execute: 整数値を受け、実値が変わったか返す関数。
            parent: このCommandを所有するQObject。
        """
        super().__init__(parent)
        self._execute = execute
        self._can_execute = True

    @property
    def can_execute(self) -> bool:
        """変更要求を受け付ける状態なら`True`。"""
        return self._can_execute

    def execute(self, value: int) -> bool:
        """整数値の変更を要求する。

        Args:
            value: 設定する整数値。`bool`は受け付けない。

        Returns:
            正本の実値が変わった場合は`True`。実行不可なら`False`。

        Raises:
            TypeError: valueが整数でない場合。
        """
        value = require_enum_value(value)
        if not self._can_execute:
            return False
        changed = self._execute(value)
        self.executed.emit(value)
        return changed
