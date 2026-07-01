# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class FontColorPlugOperator(
    Float3CompoundBasePlugOperator["FontColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fontColorR", "font_colorr"),
        ("fontColorG", "font_colorg"),
        ("fontColorB", "font_colorb"),
    )

    fontColorR = FloatField()
    font_colorr = fontColorR

    fontColorG = FloatField()
    font_colorg = fontColorG

    fontColorB = FloatField()
    font_colorb = fontColorB


class FontColorAttrOperator(
    Float3CompoundBaseAttrOperator[FontColorPlugOperator]
):
    __slots__ = ()

    fontColorR = FloatField()
    font_colorr = fontColorR

    fontColorG = FloatField()
    font_colorg = fontColorG

    fontColorB = FloatField()
    font_colorb = fontColorB


class FontColorField(
    Float3CompoundBaseField[FontColorAttrOperator, FontColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FontColorAttrOperator
    PLUG_CLS = FontColorPlugOperator

    fontColorR = FloatField()
    font_colorr = fontColorR

    fontColorG = FloatField()
    font_colorg = fontColorG

    fontColorB = FloatField()
    font_colorb = fontColorB


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "background_colorr"),
        ("backgroundColorG", "background_colorg"),
        ("backgroundColorB", "background_colorb"),
    )

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField()
    background_colorr = backgroundColorR

    backgroundColorG = FloatField()
    background_colorg = backgroundColorG

    backgroundColorB = FloatField()
    background_colorb = backgroundColorB
