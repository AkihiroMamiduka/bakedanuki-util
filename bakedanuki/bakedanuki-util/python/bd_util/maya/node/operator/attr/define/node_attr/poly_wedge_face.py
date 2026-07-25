# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    centerX = DoubleLinearField(default_value=0.0)
    ctx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cty = centerY

    centerZ = DoubleLinearField(default_value=0.0)
    ctz = centerZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerX = DoubleLinearField(default_value=0.0)
    ctx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cty = centerY

    centerZ = DoubleLinearField(default_value=0.0)
    ctz = centerZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    centerX = DoubleLinearField(default_value=0.0)
    ctx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cty = centerY

    centerZ = DoubleLinearField(default_value=0.0)
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

    axisX = DoubleLinearField(default_value=0.0)
    asx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    asy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    asz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField(default_value=0.0)
    asx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    asy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    asz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField(default_value=0.0)
    asx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    asy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    asz = axisZ
