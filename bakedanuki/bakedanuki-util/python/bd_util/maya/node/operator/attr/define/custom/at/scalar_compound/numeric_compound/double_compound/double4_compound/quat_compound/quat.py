# coding: utf-8
from collections.abc import Sequence
from typing import Any

from ._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)
from ........std.at.scalar.numeric.range.double import DoubleField


class QuatPlugOperator(QuatCompoundBasePlugOperator["Quat4AttrOperator"]):
    """4 成分の四元数 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleField()
    y = DoubleField()
    z = DoubleField()
    w = DoubleField()


class Quat4AttrOperator(QuatCompoundBaseAttrOperator[QuatPlugOperator]):
    """4 成分の四元数 compound 属性の定義を保持する。"""

    __slots__ = ()

    def __init__(
        self,
        *args: Any,
        default_value: Sequence[int | float] | None = None,
        **kwargs: Any,
    ) -> None:
        if default_value is None:
            default_value = (0.0, 0.0, 0.0, 1.0)
        super().__init__(*args, default_value=default_value, **kwargs)


class Quat4Field(QuatCompoundBaseField[Quat4AttrOperator, QuatPlugOperator]):
    """4 成分の四元数 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = Quat4AttrOperator
    PLUG_CLS = QuatPlugOperator
