# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
    colorb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
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

    backgroundColorR = FloatField(default_value=0.0)
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    backgroundColorb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField(default_value=0.0)
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    backgroundColorb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[
        BackgroundColorAttrOperator, BackgroundColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField(default_value=0.0)
    backgroundColorr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    backgroundColorg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    backgroundColorb = backgroundColorB
