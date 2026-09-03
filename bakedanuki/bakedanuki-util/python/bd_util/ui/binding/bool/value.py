# coding: utf-8
from __future__ import annotations

from ... import qt


def _require_bool(value: object, argument_name: str) -> bool:
    """値をboolとして検証して返す。"""
    if not isinstance(value, bool):
        raise TypeError(
            f"{argument_name}にはboolを指定してください: "
            f"{type(value).__name__}"
        )
    return value


class BoolValue(qt.QObject):
    """変更通知を持つ読み取り専用のboolデータ。"""

    changed = qt.Signal(bool)

    def __init__(
        self,
        value: bool = False,
        parent: qt.QObject | None = None,
    ) -> None:
        """初期値と任意のQt ownerを受け取って初期化する。"""
        super().__init__(parent)
        self._value = _require_bool(value, "value")

    @property
    def value(self) -> bool:
        """現在値を返す。"""
        return self._value
