# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputPointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointX", "px"),
        ("pointY", "py"),
        ("pointZ", "pz"),
    )

    pointX = DoubleLinearField()
    px = pointX

    pointY = DoubleLinearField()
    py = pointY

    pointZ = DoubleLinearField()
    pz = pointZ


class InputPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPointPlugOperator]
):
    __slots__ = ()

    pointX = DoubleLinearField()
    px = pointX

    pointY = DoubleLinearField()
    py = pointY

    pointZ = DoubleLinearField()
    pz = pointZ


class InputPointField(
    DoubleLinear3CompoundBaseField[InputPointAttrOperator, InputPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputPointAttrOperator
    PLUG_CLS = InputPointPlugOperator

    pointX = DoubleLinearField()
    px = pointX

    pointY = DoubleLinearField()
    py = pointY

    pointZ = DoubleLinearField()
    pz = pointZ
