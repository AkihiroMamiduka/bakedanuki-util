# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "backgroundColorr"),
        ("backgroundColorG", "backgroundColorg"),
        ("backgroundColorB", "backgroundColorb"),
    )

    backgroundColorR = FloatField()
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField()
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField()
    backgroundColorb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField()
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField()
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField()
    backgroundColorb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField()
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField()
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField()
    backgroundColorb = backgroundColorB
