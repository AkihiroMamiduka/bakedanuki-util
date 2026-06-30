# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InitDirectionPlugOperator(
    Float3CompoundBasePlugOperator["InitDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initDirectionX", "dx"),
        ("initDirectionY", "dy"),
        ("initDirectionZ", "dz"),
    )

    initDirectionX = FloatField()
    dx = initDirectionX

    initDirectionY = FloatField()
    dy = initDirectionY

    initDirectionZ = FloatField()
    dz = initDirectionZ


class InitDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[InitDirectionPlugOperator]
):
    __slots__ = ()

    initDirectionX = FloatField()
    dx = initDirectionX

    initDirectionY = FloatField()
    dy = initDirectionY

    initDirectionZ = FloatField()
    dz = initDirectionZ


class InitDirectionField(
    Float3CompoundBaseField[InitDirectionAttrOperator, InitDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitDirectionAttrOperator
    PLUG_CLS = InitDirectionPlugOperator

    initDirectionX = FloatField()
    dx = initDirectionX

    initDirectionY = FloatField()
    dy = initDirectionY

    initDirectionZ = FloatField()
    dz = initDirectionZ
