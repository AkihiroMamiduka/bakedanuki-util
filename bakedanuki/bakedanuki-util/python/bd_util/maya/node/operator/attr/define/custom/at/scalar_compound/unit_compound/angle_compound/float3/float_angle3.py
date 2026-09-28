# coding: utf-8

from ._base import (
    FloatAngle3CompoundBasePlugOperator,
    FloatAngle3CompoundBaseAttrOperator,
    FloatAngle3CompoundBaseField,
)
from .......std.at.scalar.unit.range.float_angle import FloatAngleField


class FloatAngle3PlugOperator(
    FloatAngle3CompoundBasePlugOperator["FloatAngle3AttrOperator"]
):
    """3 成分の float 型の角度 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatAngleField()
    y = FloatAngleField()
    z = FloatAngleField()


class FloatAngle3AttrOperator(
    FloatAngle3CompoundBaseAttrOperator[FloatAngle3PlugOperator]
):
    """3 成分の float 型の角度 compound 属性の定義を保持する。"""

    __slots__ = ()


class FloatAngle3Field(
    FloatAngle3CompoundBaseField[
        FloatAngle3AttrOperator, FloatAngle3PlugOperator
    ]
):
    """3 成分の float 型の角度 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatAngle3AttrOperator
    PLUG_CLS = FloatAngle3PlugOperator
