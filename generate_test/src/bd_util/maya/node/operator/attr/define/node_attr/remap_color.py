# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class RedPlugOperator(
    CompoundPlugOperator["RedAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("red_Position", "rp"),
        ("red_FloatValue", "rfv"),
        ("red_Interp", "ri"),
    )

    red_Position = FloatField()
    rp = red_Position

    red_FloatValue = FloatField()
    rfv = red_FloatValue

    red_Interp = EnumField()
    ri = red_Interp


class RedAttrOperator(
    CompoundAttrOperator[RedPlugOperator]
):
    __slots__ = ()

    red_Position = FloatField()
    rp = red_Position

    red_FloatValue = FloatField()
    rfv = red_FloatValue

    red_Interp = EnumField()
    ri = red_Interp


class RedField(
    CompoundField[RedAttrOperator, RedPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RedAttrOperator
    PLUG_CLS = RedPlugOperator


class GreenPlugOperator(
    CompoundPlugOperator["GreenAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("green_Position", "gp"),
        ("green_FloatValue", "gfv"),
        ("green_Interp", "gi"),
    )

    green_Position = FloatField()
    gp = green_Position

    green_FloatValue = FloatField()
    gfv = green_FloatValue

    green_Interp = EnumField()
    gi = green_Interp


class GreenAttrOperator(
    CompoundAttrOperator[GreenPlugOperator]
):
    __slots__ = ()

    green_Position = FloatField()
    gp = green_Position

    green_FloatValue = FloatField()
    gfv = green_FloatValue

    green_Interp = EnumField()
    gi = green_Interp


class GreenField(
    CompoundField[GreenAttrOperator, GreenPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GreenAttrOperator
    PLUG_CLS = GreenPlugOperator


class BluePlugOperator(
    CompoundPlugOperator["BlueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blue_Position", "bp"),
        ("blue_FloatValue", "bfv"),
        ("blue_Interp", "bi"),
    )

    blue_Position = FloatField()
    bp = blue_Position

    blue_FloatValue = FloatField()
    bfv = blue_FloatValue

    blue_Interp = EnumField()
    bi = blue_Interp


class BlueAttrOperator(
    CompoundAttrOperator[BluePlugOperator]
):
    __slots__ = ()

    blue_Position = FloatField()
    bp = blue_Position

    blue_FloatValue = FloatField()
    bfv = blue_FloatValue

    blue_Interp = EnumField()
    bi = blue_Interp


class BlueField(
    CompoundField[BlueAttrOperator, BluePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlueAttrOperator
    PLUG_CLS = BluePlugOperator


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB
