# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class DirectionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("directionX", "dx"),
        ("directionY", "dy"),
        ("directionZ", "dz"),
    )

    directionX = DoubleLinearField(default_value=0.0)
    dx = directionX

    directionY = DoubleLinearField(default_value=0.0)
    dy = directionY

    directionZ = DoubleLinearField(default_value=1.0)
    dz = directionZ


class DirectionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[DirectionPlugOperator]
):
    __slots__ = ()

    directionX = DoubleLinearField(default_value=0.0)
    dx = directionX

    directionY = DoubleLinearField(default_value=0.0)
    dy = directionY

    directionZ = DoubleLinearField(default_value=1.0)
    dz = directionZ


class DirectionField(
    DoubleLinear3CompoundBaseField[DirectionAttrOperator, DirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionAttrOperator
    PLUG_CLS = DirectionPlugOperator

    directionX = DoubleLinearField(default_value=0.0)
    dx = directionX

    directionY = DoubleLinearField(default_value=0.0)
    dy = directionY

    directionZ = DoubleLinearField(default_value=1.0)
    dz = directionZ
