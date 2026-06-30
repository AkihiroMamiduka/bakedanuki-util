# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class CenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerX", "ctx"),
        ("centerY", "cty"),
        ("centerZ", "ctz"),
    )

    centerX = DoubleLinearField()
    ctx = centerX

    centerY = DoubleLinearField()
    cty = centerY

    centerZ = DoubleLinearField()
    ctz = centerZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerX = DoubleLinearField()
    ctx = centerX

    centerY = DoubleLinearField()
    cty = centerY

    centerZ = DoubleLinearField()
    ctz = centerZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    centerX = DoubleLinearField()
    ctx = centerX

    centerY = DoubleLinearField()
    cty = centerY

    centerZ = DoubleLinearField()
    ctz = centerZ


class AxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "asx"),
        ("axisY", "asy"),
        ("axisZ", "asz"),
    )

    axisX = DoubleLinearField()
    asx = axisX

    axisY = DoubleLinearField()
    asy = axisY

    axisZ = DoubleLinearField()
    asz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField()
    asx = axisX

    axisY = DoubleLinearField()
    asy = axisY

    axisZ = DoubleLinearField()
    asz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField()
    asx = axisX

    axisY = DoubleLinearField()
    asy = axisY

    axisZ = DoubleLinearField()
    asz = axisZ
