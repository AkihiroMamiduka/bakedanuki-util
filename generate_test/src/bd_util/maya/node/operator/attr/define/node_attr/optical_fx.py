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


class FogColorPlugOperator(
    Float3CompoundBasePlugOperator["FogColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fogColorR", "fr"),
        ("fogColorG", "fg"),
        ("fogColorB", "fb"),
    )

    fogColorR = FloatField()
    fr = fogColorR

    fogColorG = FloatField()
    fg = fogColorG

    fogColorB = FloatField()
    fb = fogColorB


class FogColorAttrOperator(
    Float3CompoundBaseAttrOperator[FogColorPlugOperator]
):
    __slots__ = ()

    fogColorR = FloatField()
    fr = fogColorR

    fogColorG = FloatField()
    fg = fogColorG

    fogColorB = FloatField()
    fb = fogColorB


class FogColorField(
    Float3CompoundBaseField[FogColorAttrOperator, FogColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogColorAttrOperator
    PLUG_CLS = FogColorPlugOperator

    fogColorR = FloatField()
    fr = fogColorR

    fogColorG = FloatField()
    fg = fogColorG

    fogColorB = FloatField()
    fb = fogColorB


class FlareColorPlugOperator(
    Float3CompoundBasePlugOperator["FlareColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("flareColorR", "rr"),
        ("flareColorG", "rg"),
        ("flareColorB", "rb"),
    )

    flareColorR = FloatField()
    rr = flareColorR

    flareColorG = FloatField()
    rg = flareColorG

    flareColorB = FloatField()
    rb = flareColorB


class FlareColorAttrOperator(
    Float3CompoundBaseAttrOperator[FlareColorPlugOperator]
):
    __slots__ = ()

    flareColorR = FloatField()
    rr = flareColorR

    flareColorG = FloatField()
    rg = flareColorG

    flareColorB = FloatField()
    rb = flareColorB


class FlareColorField(
    Float3CompoundBaseField[FlareColorAttrOperator, FlareColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlareColorAttrOperator
    PLUG_CLS = FlareColorPlugOperator

    flareColorR = FloatField()
    rr = flareColorR

    flareColorG = FloatField()
    rg = flareColorG

    flareColorB = FloatField()
    rb = flareColorB


class LightColorPlugOperator(
    Float3CompoundBasePlugOperator["LightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightColorR", "lcr"),
        ("lightColorG", "lcg"),
        ("lightColorB", "lgb"),
    )

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lgb = lightColorB


class LightColorAttrOperator(
    Float3CompoundBaseAttrOperator[LightColorPlugOperator]
):
    __slots__ = ()

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lgb = lightColorB


class LightColorField(
    Float3CompoundBaseField[LightColorAttrOperator, LightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightColorAttrOperator
    PLUG_CLS = LightColorPlugOperator

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lgb = lightColorB


class VisibilityPlugOperator(
    Float3CompoundBasePlugOperator["VisibilityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("visibilityR", "vbr"),
        ("visibilityG", "vbg"),
        ("visibilityB", "vbb"),
    )

    visibilityR = FloatField()
    vbr = visibilityR

    visibilityG = FloatField()
    vbg = visibilityG

    visibilityB = FloatField()
    vbb = visibilityB


class VisibilityAttrOperator(
    Float3CompoundBaseAttrOperator[VisibilityPlugOperator]
):
    __slots__ = ()

    visibilityR = FloatField()
    vbr = visibilityR

    visibilityG = FloatField()
    vbg = visibilityG

    visibilityB = FloatField()
    vbb = visibilityB


class VisibilityField(
    Float3CompoundBaseField[VisibilityAttrOperator, VisibilityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VisibilityAttrOperator
    PLUG_CLS = VisibilityPlugOperator

    visibilityR = FloatField()
    vbr = visibilityR

    visibilityG = FloatField()
    vbg = visibilityG

    visibilityB = FloatField()
    vbb = visibilityB
