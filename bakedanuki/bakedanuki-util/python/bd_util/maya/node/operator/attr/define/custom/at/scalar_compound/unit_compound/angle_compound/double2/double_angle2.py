# coding: utf-8

# self
from ._base import (
    DoubleAngle2CompoundBasePlugOperator,
    DoubleAngle2CompoundBaseAttrOperator,
    DoubleAngle2CompoundBaseField,
)
from .......std.at.scalar.unit.range.double_angle import DoubleAngleField


class DoubleAngle2PlugOperator(
    DoubleAngle2CompoundBasePlugOperator["DoubleAngle2AttrOperator"]
):
    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()


class DoubleAngle2AttrOperator(
    DoubleAngle2CompoundBaseAttrOperator[DoubleAngle2PlugOperator]
):
    __slots__ = ()


class DoubleAngle2Field(
    DoubleAngle2CompoundBaseField[
        DoubleAngle2AttrOperator, DoubleAngle2PlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngle2AttrOperator
    PLUG_CLS = DoubleAngle2PlugOperator
