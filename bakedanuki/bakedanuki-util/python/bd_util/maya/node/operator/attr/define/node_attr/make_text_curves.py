# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class PositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "px"),
        ("positionY", "py"),
        ("positionZ", "pz"),
    )

    positionX = DoubleLinearField(default_value=0.0, writable=False)
    px = positionX

    positionY = DoubleLinearField(default_value=0.0, writable=False)
    py = positionY

    positionZ = DoubleLinearField(default_value=0.0, writable=False)
    pz = positionZ


class PositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleLinearField(default_value=0.0, writable=False)
    px = positionX

    positionY = DoubleLinearField(default_value=0.0, writable=False)
    py = positionY

    positionZ = DoubleLinearField(default_value=0.0, writable=False)
    pz = positionZ


class PositionField(
    DoubleLinear3CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator
