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
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class ValuePlugOperator(
    CompoundPlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value_Position", "vlp"),
        ("value_FloatValue", "vlfv"),
        ("value_Interp", "vli"),
    )

    value_Position = FloatField()
    vlp = value_Position

    value_FloatValue = FloatField()
    vlfv = value_FloatValue

    value_Interp = EnumField()
    vli = value_Interp


class ValueAttrOperator(
    CompoundAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    value_Position = FloatField()
    vlp = value_Position

    value_FloatValue = FloatField()
    vlfv = value_FloatValue

    value_Interp = EnumField()
    vli = value_Interp


class ValueField(
    CompoundField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator


class ColorPlugOperator(
    CompoundPlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color_Position", "clp"),
        ("color_Color", "clc"),
        ("color_Interp", "cli"),
    )

    color_Position = FloatField()
    clp = color_Position

    color_Color = Float3Field()
    clc = color_Color

    color_Interp = EnumField()
    cli = color_Interp


class ColorAttrOperator(
    CompoundAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    color_Position = FloatField()
    clp = color_Position

    color_Color = Float3Field()
    clc = color_Color

    color_Interp = EnumField()
    cli = color_Interp


class ColorField(
    CompoundField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator


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
