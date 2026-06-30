# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class RedScalePlugOperator(
    CompoundPlugOperator["RedScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("redScale_Position", "rp"),
        ("redScale_FloatValue", "rfv"),
        ("redScale_Interp", "ri"),
    )

    redScale_Position = FloatField()
    rp = redScale_Position

    redScale_FloatValue = FloatField()
    rfv = redScale_FloatValue

    redScale_Interp = EnumField()
    ri = redScale_Interp


class RedScaleAttrOperator(
    CompoundAttrOperator[RedScalePlugOperator]
):
    __slots__ = ()

    redScale_Position = FloatField()
    rp = redScale_Position

    redScale_FloatValue = FloatField()
    rfv = redScale_FloatValue

    redScale_Interp = EnumField()
    ri = redScale_Interp


class RedScaleField(
    CompoundField[RedScaleAttrOperator, RedScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RedScaleAttrOperator
    PLUG_CLS = RedScalePlugOperator


class GreenScalePlugOperator(
    CompoundPlugOperator["GreenScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("greenScale_Position", "gp"),
        ("greenScale_FloatValue", "gfv"),
        ("greenScale_Interp", "gi"),
    )

    greenScale_Position = FloatField()
    gp = greenScale_Position

    greenScale_FloatValue = FloatField()
    gfv = greenScale_FloatValue

    greenScale_Interp = EnumField()
    gi = greenScale_Interp


class GreenScaleAttrOperator(
    CompoundAttrOperator[GreenScalePlugOperator]
):
    __slots__ = ()

    greenScale_Position = FloatField()
    gp = greenScale_Position

    greenScale_FloatValue = FloatField()
    gfv = greenScale_FloatValue

    greenScale_Interp = EnumField()
    gi = greenScale_Interp


class GreenScaleField(
    CompoundField[GreenScaleAttrOperator, GreenScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GreenScaleAttrOperator
    PLUG_CLS = GreenScalePlugOperator


class BlueScalePlugOperator(
    CompoundPlugOperator["BlueScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blueScale_Position", "bp"),
        ("blueScale_FloatValue", "bfv"),
        ("blueScale_Interp", "bi"),
    )

    blueScale_Position = FloatField()
    bp = blueScale_Position

    blueScale_FloatValue = FloatField()
    bfv = blueScale_FloatValue

    blueScale_Interp = EnumField()
    bi = blueScale_Interp


class BlueScaleAttrOperator(
    CompoundAttrOperator[BlueScalePlugOperator]
):
    __slots__ = ()

    blueScale_Position = FloatField()
    bp = blueScale_Position

    blueScale_FloatValue = FloatField()
    bfv = blueScale_FloatValue

    blueScale_Interp = EnumField()
    bi = blueScale_Interp


class BlueScaleField(
    CompoundField[BlueScaleAttrOperator, BlueScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlueScaleAttrOperator
    PLUG_CLS = BlueScalePlugOperator


class AlphaScalePlugOperator(
    CompoundPlugOperator["AlphaScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("alphaScale_Position", "ap"),
        ("alphaScale_FloatValue", "afv"),
        ("alphaScale_Interp", "ai"),
    )

    alphaScale_Position = FloatField()
    ap = alphaScale_Position

    alphaScale_FloatValue = FloatField()
    afv = alphaScale_FloatValue

    alphaScale_Interp = EnumField()
    ai = alphaScale_Interp


class AlphaScaleAttrOperator(
    CompoundAttrOperator[AlphaScalePlugOperator]
):
    __slots__ = ()

    alphaScale_Position = FloatField()
    ap = alphaScale_Position

    alphaScale_FloatValue = FloatField()
    afv = alphaScale_FloatValue

    alphaScale_Interp = EnumField()
    ai = alphaScale_Interp


class AlphaScaleField(
    CompoundField[AlphaScaleAttrOperator, AlphaScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaScaleAttrOperator
    PLUG_CLS = AlphaScalePlugOperator


class IntensityScalePlugOperator(
    CompoundPlugOperator["IntensityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("intensityScale_Position", "np"),
        ("intensityScale_FloatValue", "nfv"),
        ("intensityScale_Interp", "ni"),
    )

    intensityScale_Position = FloatField()
    np = intensityScale_Position

    intensityScale_FloatValue = FloatField()
    nfv = intensityScale_FloatValue

    intensityScale_Interp = EnumField()
    ni = intensityScale_Interp


class IntensityScaleAttrOperator(
    CompoundAttrOperator[IntensityScalePlugOperator]
):
    __slots__ = ()

    intensityScale_Position = FloatField()
    np = intensityScale_Position

    intensityScale_FloatValue = FloatField()
    nfv = intensityScale_FloatValue

    intensityScale_Interp = EnumField()
    ni = intensityScale_Interp


class IntensityScaleField(
    CompoundField[IntensityScaleAttrOperator, IntensityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IntensityScaleAttrOperator
    PLUG_CLS = IntensityScalePlugOperator
