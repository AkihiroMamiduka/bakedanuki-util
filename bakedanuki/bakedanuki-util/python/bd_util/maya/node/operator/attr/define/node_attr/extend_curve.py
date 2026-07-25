# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    pointX = DoubleLinearField(default_value=0.0)
    px = pointX

    pointY = DoubleLinearField(default_value=0.0)
    py = pointY

    pointZ = DoubleLinearField(default_value=0.0)
    pz = pointZ


class InputPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPointPlugOperator]
):
    __slots__ = ()

    pointX = DoubleLinearField(default_value=0.0)
    px = pointX

    pointY = DoubleLinearField(default_value=0.0)
    py = pointY

    pointZ = DoubleLinearField(default_value=0.0)
    pz = pointZ


class InputPointField(
    DoubleLinear3CompoundBaseField[InputPointAttrOperator, InputPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputPointAttrOperator
    PLUG_CLS = InputPointPlugOperator

    pointX = DoubleLinearField(default_value=0.0)
    px = pointX

    pointY = DoubleLinearField(default_value=0.0)
    py = pointY

    pointZ = DoubleLinearField(default_value=0.0)
    pz = pointZ
