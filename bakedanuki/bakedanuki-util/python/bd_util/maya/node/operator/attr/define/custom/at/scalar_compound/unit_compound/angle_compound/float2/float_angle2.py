# coding: utf-8

from ._base import (
    FloatAngle2CompoundBasePlugOperator,
    FloatAngle2CompoundBaseAttrOperator,
    FloatAngle2CompoundBaseField,
)
from .......std.at.scalar.unit.range.float_angle import FloatAngleField


class FloatAngle2PlugOperator(
    FloatAngle2CompoundBasePlugOperator["FloatAngle2AttrOperator"]
):
    """2 成分の float 型の角度 compound 属性の値を読み書きするプラグ操作。"""

    __slots__ = ()

    x = FloatAngleField()
    y = FloatAngleField()


class FloatAngle2AttrOperator(
    FloatAngle2CompoundBaseAttrOperator[FloatAngle2PlugOperator]
):
    """2 成分の float 型の角度 compound 属性の定義を保持する。"""

    __slots__ = ()


class FloatAngle2Field(
    FloatAngle2CompoundBaseField[
        FloatAngle2AttrOperator, FloatAngle2PlugOperator
    ]
):
    """2 成分の float 型の角度 compound 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatAngle2AttrOperator
    PLUG_CLS = FloatAngle2PlugOperator
