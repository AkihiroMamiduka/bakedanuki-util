# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class ControlPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ControlPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xValue", "xv"),
        ("yValue", "yv"),
        ("zValue", "zv"),
    )

    xValue = DoubleLinearField()
    xv = xValue

    yValue = DoubleLinearField()
    yv = yValue

    zValue = DoubleLinearField()
    zv = zValue


class ControlPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ControlPointsPlugOperator]
):
    __slots__ = ()

    xValue = DoubleLinearField()
    xv = xValue

    yValue = DoubleLinearField()
    yv = yValue

    zValue = DoubleLinearField()
    zv = zValue


class ControlPointsField(
    DoubleLinear3CompoundBaseField[ControlPointsAttrOperator, ControlPointsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ControlPointsAttrOperator
    PLUG_CLS = ControlPointsPlugOperator
