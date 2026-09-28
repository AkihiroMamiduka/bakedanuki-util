# coding: utf-8

from ._base import (
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_angle import DoubleAngleField


class DoubleAngle3PlugOperator(
    DoubleAngle3CompoundBasePlugOperator["DoubleAngle3AttrOperator"]
):
    """3 成分の double 型の角度 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()
    z = DoubleAngleField()


class DoubleAngle3AttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[DoubleAngle3PlugOperator]
):
    """3 成分の double 型の角度 compound 属性の定義を保持する。"""

    __slots__ = ()


class DoubleAngle3Field(
    DoubleAngle3CompoundBaseField[
        DoubleAngle3AttrOperator, DoubleAngle3PlugOperator
    ]
):
    """3 成分の double 型の角度 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DoubleAngle3AttrOperator
    PLUG_CLS = DoubleAngle3PlugOperator
