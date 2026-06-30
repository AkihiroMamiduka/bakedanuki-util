# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ
