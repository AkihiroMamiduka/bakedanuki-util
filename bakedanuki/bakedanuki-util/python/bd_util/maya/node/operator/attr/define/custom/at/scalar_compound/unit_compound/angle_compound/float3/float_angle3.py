# coding: utf-8

# self
from ._base import (
    FloatAngle3CompoundBasePlugOperator,
    FloatAngle3CompoundBaseAttrOperator,
    FloatAngle3CompoundBaseField,
)
from .......std.at.scalar.unit.range.float_angle import FloatAngleField


class FloatAngle3PlugOperator(
    FloatAngle3CompoundBasePlugOperator["FloatAngle3AttrOperator"]
):
    __slots__ = ()

    x = FloatAngleField()
    y = FloatAngleField()
    z = FloatAngleField()


class FloatAngle3AttrOperator(
    FloatAngle3CompoundBaseAttrOperator[FloatAngle3PlugOperator]
):
    __slots__ = ()


class FloatAngle3Field(
    FloatAngle3CompoundBaseField[
        FloatAngle3AttrOperator, FloatAngle3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FloatAngle3AttrOperator
    PLUG_CLS = FloatAngle3PlugOperator
