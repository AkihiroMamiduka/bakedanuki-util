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


class HuePlugOperator(
    CompoundPlugOperator["HueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hue_Position", "hp"),
        ("hue_FloatValue", "hfv"),
        ("hue_Interp", "hi"),
    )

    hue_Position = FloatField()
    hp = hue_Position

    hue_FloatValue = FloatField()
    hfv = hue_FloatValue

    hue_Interp = EnumField()
    hi = hue_Interp


class HueAttrOperator(
    CompoundAttrOperator[HuePlugOperator]
):
    __slots__ = ()

    hue_Position = FloatField()
    hp = hue_Position

    hue_FloatValue = FloatField()
    hfv = hue_FloatValue

    hue_Interp = EnumField()
    hi = hue_Interp


class HueField(
    CompoundField[HueAttrOperator, HuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HueAttrOperator
    PLUG_CLS = HuePlugOperator


class SaturationPlugOperator(
    CompoundPlugOperator["SaturationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("saturation_Position", "sp"),
        ("saturation_FloatValue", "sfv"),
        ("saturation_Interp", "si"),
    )

    saturation_Position = FloatField()
    sp = saturation_Position

    saturation_FloatValue = FloatField()
    sfv = saturation_FloatValue

    saturation_Interp = EnumField()
    si = saturation_Interp


class SaturationAttrOperator(
    CompoundAttrOperator[SaturationPlugOperator]
):
    __slots__ = ()

    saturation_Position = FloatField()
    sp = saturation_Position

    saturation_FloatValue = FloatField()
    sfv = saturation_FloatValue

    saturation_Interp = EnumField()
    si = saturation_Interp


class SaturationField(
    CompoundField[SaturationAttrOperator, SaturationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SaturationAttrOperator
    PLUG_CLS = SaturationPlugOperator


class ValuePlugOperator(
    CompoundPlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value_Position", "vp"),
        ("value_FloatValue", "vfv"),
        ("value_Interp", "vi"),
    )

    value_Position = FloatField()
    vp = value_Position

    value_FloatValue = FloatField()
    vfv = value_FloatValue

    value_Interp = EnumField()
    vi = value_Interp


class ValueAttrOperator(
    CompoundAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    value_Position = FloatField()
    vp = value_Position

    value_FloatValue = FloatField()
    vfv = value_FloatValue

    value_Interp = EnumField()
    vi = value_Interp


class ValueField(
    CompoundField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator


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
