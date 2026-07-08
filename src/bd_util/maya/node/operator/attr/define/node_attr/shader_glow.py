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

    glowColorR = FloatField(default_value=1.0)
    gr = glowColorR

    glowColorG = FloatField(default_value=1.0)
    gg = glowColorG

    glowColorB = FloatField(default_value=1.0)
    gb = glowColorB


class GlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[GlowColorPlugOperator]
):
    __slots__ = ()

    glowColorR = FloatField(default_value=1.0)
    gr = glowColorR

    glowColorG = FloatField(default_value=1.0)
    gg = glowColorG

    glowColorB = FloatField(default_value=1.0)
    gb = glowColorB


class GlowColorField(
    Float3CompoundBaseField[GlowColorAttrOperator, GlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GlowColorAttrOperator
    PLUG_CLS = GlowColorPlugOperator

    glowColorR = FloatField(default_value=1.0)
    gr = glowColorR

    glowColorG = FloatField(default_value=1.0)
    gg = glowColorG

    glowColorB = FloatField(default_value=1.0)
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

    haloColorR = FloatField(default_value=1.0)
    hr = haloColorR

    haloColorG = FloatField(default_value=1.0)
    hg = haloColorG

    haloColorB = FloatField(default_value=1.0)
    hb = haloColorB


class HaloColorAttrOperator(
    Float3CompoundBaseAttrOperator[HaloColorPlugOperator]
):
    __slots__ = ()

    haloColorR = FloatField(default_value=1.0)
    hr = haloColorR

    haloColorG = FloatField(default_value=1.0)
    hg = haloColorG

    haloColorB = FloatField(default_value=1.0)
    hb = haloColorB


class HaloColorField(
    Float3CompoundBaseField[HaloColorAttrOperator, HaloColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HaloColorAttrOperator
    PLUG_CLS = HaloColorPlugOperator

    haloColorR = FloatField(default_value=1.0)
    hr = haloColorR

    haloColorG = FloatField(default_value=1.0)
    hg = haloColorG

    haloColorB = FloatField(default_value=1.0)
    hb = haloColorB
