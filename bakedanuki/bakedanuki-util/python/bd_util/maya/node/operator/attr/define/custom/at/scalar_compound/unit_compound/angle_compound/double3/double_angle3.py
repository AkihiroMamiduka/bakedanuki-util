# coding: utf-8

# self
from ._base import (
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_angle import DoubleAngleField


class DoubleAngle3PlugOperator(
    DoubleAngle3CompoundBasePlugOperator["DoubleAngle3AttrOperator"]
):
    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()
    z = DoubleAngleField()


class DoubleAngle3AttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[DoubleAngle3PlugOperator]
):
    __slots__ = ()


class DoubleAngle3Field(
    DoubleAngle3CompoundBaseField[
        DoubleAngle3AttrOperator, DoubleAngle3PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngle3AttrOperator
    PLUG_CLS = DoubleAngle3PlugOperator
