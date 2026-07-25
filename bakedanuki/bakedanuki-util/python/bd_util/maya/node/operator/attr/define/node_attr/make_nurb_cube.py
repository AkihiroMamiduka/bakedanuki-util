# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class PivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "px"),
        ("pivotY", "py"),
        ("pivotZ", "pz"),
    )

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class AxisPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisX", "axx"),
        ("axisY", "axy"),
        ("axisZ", "axz"),
    )

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AxisPlugOperator]
):
    __slots__ = ()

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ


class AxisField(
    DoubleLinear3CompoundBaseField[AxisAttrOperator, AxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisAttrOperator
    PLUG_CLS = AxisPlugOperator

    axisX = DoubleLinearField(default_value=1.0)
    axx = axisX

    axisY = DoubleLinearField(default_value=0.0)
    axy = axisY

    axisZ = DoubleLinearField(default_value=0.0)
    axz = axisZ
