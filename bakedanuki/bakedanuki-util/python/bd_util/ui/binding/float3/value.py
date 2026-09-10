# coding: utf-8
from collections.abc import Sequence
from typing import TypeAlias, cast

from ... import qt
from ..float._validation import require_float

Float3: TypeAlias = tuple[float, float, float]


def require_float3(value: object) -> Float3:
    """有限の数値3成分を検証し、immutableなtupleへ変換する。"""
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise TypeError("valueには数値3成分のsequenceを指定してください")
    value = cast(Sequence[object], value)
    if len(value) != 3:
        raise ValueError("valueにはちょうど3成分を指定してください")
    return (
        require_float(value[0], "value[0]"),
        require_float(value[1], "value[1]"),
        require_float(value[2], "value[2]"),
    )


class Float3Value(qt.QObject):
    """変更通知を持つ読み取り専用の3成分値。"""

    changed = qt.Signal(object)

    def __init__(self, parent: qt.QObject | None = None) -> None:
        """初期値を0の3成分として生成する。"""
        super().__init__(parent)
        self._value: Float3 = (0.0, 0.0, 0.0)

    @property
    def value(self) -> Float3:
        """最後に同期した確定値をtupleで返す。"""
        return self._value
