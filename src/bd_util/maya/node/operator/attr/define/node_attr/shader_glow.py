# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class GlowColorPlugOperator(
    Float3CompoundBasePlugOperator["GlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("glowColorR", "gr"),
        ("glowColorG", "gg"),
        ("glowColorB", "gb"),
    )

    glowColorR = FloatField()
    gr = glowColorR

    glowColorG = FloatField()
    gg = glowColorG

    glowColorB = FloatField()
    gb = glowColorB


class GlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[GlowColorPlugOperator]
):
    __slots__ = ()

    glowColorR = FloatField()
    gr = glowColorR

    glowColorG = FloatField()
    gg = glowColorG

    glowColorB = FloatField()
    gb = glowColorB


class GlowColorField(
    Float3CompoundBaseField[GlowColorAttrOperator, GlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GlowColorAttrOperator
    PLUG_CLS = GlowColorPlugOperator

    glowColorR = FloatField()
    gr = glowColorR

    glowColorG = FloatField()
    gg = glowColorG

    glowColorB = FloatField()
    gb = glowColorB


class HaloColorPlugOperator(
    Float3CompoundBasePlugOperator["HaloColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("haloColorR", "hr"),
        ("haloColorG", "hg"),
        ("haloColorB", "hb"),
    )

    haloColorR = FloatField()
    hr = haloColorR

    haloColorG = FloatField()
    hg = haloColorG

    haloColorB = FloatField()
    hb = haloColorB


class HaloColorAttrOperator(
    Float3CompoundBaseAttrOperator[HaloColorPlugOperator]
):
    __slots__ = ()

    haloColorR = FloatField()
    hr = haloColorR

    haloColorG = FloatField()
    hg = haloColorG

    haloColorB = FloatField()
    hb = haloColorB


class HaloColorField(
    Float3CompoundBaseField[HaloColorAttrOperator, HaloColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HaloColorAttrOperator
    PLUG_CLS = HaloColorPlugOperator

    haloColorR = FloatField()
    hr = haloColorR

    haloColorG = FloatField()
    hg = haloColorG

    haloColorB = FloatField()
    hb = haloColorB
