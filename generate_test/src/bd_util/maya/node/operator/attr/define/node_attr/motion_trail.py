# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class LocalPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localPositionX", "lpx"),
        ("localPositionY", "lpy"),
        ("localPositionZ", "lpz"),
    )

    localPositionX = DoubleLinearField()
    lpx = localPositionX

    localPositionY = DoubleLinearField()
    lpy = localPositionY

    localPositionZ = DoubleLinearField()
    lpz = localPositionZ


class LocalPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalPositionPlugOperator]
):
    __slots__ = ()

    localPositionX = DoubleLinearField()
    lpx = localPositionX

    localPositionY = DoubleLinearField()
    lpy = localPositionY

    localPositionZ = DoubleLinearField()
    lpz = localPositionZ


class LocalPositionField(
    DoubleLinear3CompoundBaseField[LocalPositionAttrOperator, LocalPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalPositionAttrOperator
    PLUG_CLS = LocalPositionPlugOperator

    localPositionX = DoubleLinearField()
    lpx = localPositionX

    localPositionY = DoubleLinearField()
    lpy = localPositionY

    localPositionZ = DoubleLinearField()
    lpz = localPositionZ
