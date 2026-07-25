# coding: utf-8

# self
from ._base import (
    FloatAngle2CompoundBasePlugOperator,
    FloatAngle2CompoundBaseAttrOperator,
    FloatAngle2CompoundBaseField,
)
from .......std.at.scalar.unit.range.float_angle import FloatAngleField


class FloatAngle2PlugOperator(
    FloatAngle2CompoundBasePlugOperator["FloatAngle2AttrOperator"]
):
    __slots__ = ()

    x = FloatAngleField()
    y = FloatAngleField()


class FloatAngle2AttrOperator(
    FloatAngle2CompoundBaseAttrOperator[FloatAngle2PlugOperator]
):
    __slots__ = ()


class FloatAngle2Field(
    FloatAngle2CompoundBaseField[
        FloatAngle2AttrOperator, FloatAngle2PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FloatAngle2AttrOperator
    PLUG_CLS = FloatAngle2PlugOperator
