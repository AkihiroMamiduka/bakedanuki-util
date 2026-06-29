# coding: utf-8

# self
from .._base import (
    AngleCompoundBasePlugOperator,
    AngleCompoundBaseAttrOperator,
    AngleCompoundBaseField,
)
from .......std.at.unit_scalar_range.float_angle import FloatAngleField


class FloatAngle3PlugOperator(
    AngleCompoundBasePlugOperator["FloatAngle3AttrOperator"]
):
    __slots__ = ()

    x = FloatAngleField()
    y = FloatAngleField()
    z = FloatAngleField()


class FloatAngle3AttrOperator(
    AngleCompoundBaseAttrOperator[FloatAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "float3"


class FloatAngle3Field(
    AngleCompoundBaseField[FloatAngle3AttrOperator, FloatAngle3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatAngle3AttrOperator
    PLUG_CLS = FloatAngle3PlugOperator
