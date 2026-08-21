# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class PositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "tpx"),
        ("positionY", "tpy"),
        ("positionZ", "tpz"),
    )

    positionX = DoubleLinearField(default_value=0.0)
    tpx = positionX

    positionY = DoubleLinearField(default_value=0.0)
    tpy = positionY

    positionZ = DoubleLinearField(default_value=0.0)
    tpz = positionZ


class PositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleLinearField(default_value=0.0)
    tpx = positionX

    positionY = DoubleLinearField(default_value=0.0)
    tpy = positionY

    positionZ = DoubleLinearField(default_value=0.0)
    tpz = positionZ


class PositionField(
    DoubleLinear3CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator

    positionX = DoubleLinearField(default_value=0.0)
    tpx = positionX

    positionY = DoubleLinearField(default_value=0.0)
    tpy = positionY

    positionZ = DoubleLinearField(default_value=0.0)
    tpz = positionZ
