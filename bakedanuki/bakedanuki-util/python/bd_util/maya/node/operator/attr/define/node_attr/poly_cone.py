# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class AxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "axx"),
        ("axisY", "axy"),
        ("axisZ", "axz"),
    )

    axisX = DoubleLinearField(default_value=0.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=1.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField(default_value=0.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=1.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField(default_value=0.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=1.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ
