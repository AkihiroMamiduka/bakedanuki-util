# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
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

    lightDirectionX = DoubleField(default_value=0.2)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=-0.9)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ


class LightDirectionAttrOperator(
    Double3CompoundBaseAttrOperator[LightDirectionPlugOperator]
):
    __slots__ = ()

    lightDirectionX = DoubleField(default_value=0.2)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=-0.9)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ


class LightDirectionField(
    Double3CompoundBaseField[LightDirectionAttrOperator, LightDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDirectionAttrOperator
    PLUG_CLS = LightDirectionPlugOperator

    lightDirectionX = DoubleField(default_value=0.2)
    ldx = lightDirectionX

    lightDirectionY = DoubleField(default_value=-0.9)
    ldy = lightDirectionY

    lightDirectionZ = DoubleField(default_value=-0.5)
    ldz = lightDirectionZ
