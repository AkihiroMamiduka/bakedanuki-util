# coding: utf-8

from ._base import (
    DoubleAngle2CompoundBasePlugOperator,
    DoubleAngle2CompoundBaseAttrOperator,
    DoubleAngle2CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_angle import DoubleAngleField


class DoubleAngle2PlugOperator(
    DoubleAngle2CompoundBasePlugOperator["DoubleAngle2AttrOperator"]
):
    """2 成分の double 型の角度 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()


class DoubleAngle2AttrOperator(
    DoubleAngle2CompoundBaseAttrOperator[DoubleAngle2PlugOperator]
):
    """2 成分の double 型の角度 compound 属性の定義を保持する。"""

    __slots__ = ()


class DoubleAngle2Field(
    DoubleAngle2CompoundBaseField[
        DoubleAngle2AttrOperator, DoubleAngle2PlugOperator
    ]
):
    """2 成分の double 型の角度 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleAngle2AttrOperator
    PLUG_CLS = DoubleAngle2PlugOperator
