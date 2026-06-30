# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class LightDirectionPlugOperator(
    Double3CompoundBasePlugOperator["LightDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirectionX", "ldx"),
        ("lightDirectionY", "ldy"),
        ("lightDirectionZ", "ldz"),
    )

    lightDirectionX = DoubleField()
    ldx = lightDirectionX

    lightDirectionY = DoubleField()
    ldy = lightDirectionY

    lightDirectionZ = DoubleField()
    ldz = lightDirectionZ


class LightDirectionAttrOperator(
    Double3CompoundBaseAttrOperator[LightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = DoubleField()
    ldx = lightDirectionX

    lightDirectionY = DoubleField()
    ldy = lightDirectionY

    lightDirectionZ = DoubleField()
    ldz = lightDirectionZ


class LightDirectionField(
    Double3CompoundBaseField[LightDirectionAttrOperator, LightDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDirectionAttrOperator
    PLUG_CLS = LightDirectionPlugOperator

    lightDirectionX = DoubleField()
    ldx = lightDirectionX

    lightDirectionY = DoubleField()
    ldy = lightDirectionY

    lightDirectionZ = DoubleField()
    ldz = lightDirectionZ
