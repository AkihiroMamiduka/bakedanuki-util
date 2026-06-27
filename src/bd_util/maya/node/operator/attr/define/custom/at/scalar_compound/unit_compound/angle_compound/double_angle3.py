# coding: utf-8

# self
from ._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)
from ......std.at.unit_scalar_range.double_angle import DoubleAngleField


class DoubleAngle3PlugOperator(
    AngleCompoundBasePlugOperator["DoubleAngle3AttrOperator"]
):
    __slots__ = ()

    x = DoubleAngleField()
    y = DoubleAngleField()
    z = DoubleAngleField()


class DoubleAngle3AttrOperator(
    AngleCompoundBaseAttrOperator[DoubleAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "double3"


class DoubleAngle3Field(
    AngleCompoundBaseField[DoubleAngle3AttrOperator, DoubleAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngle3AttrOperator
    PLUG_CLS = DoubleAngle3PlugOperator
