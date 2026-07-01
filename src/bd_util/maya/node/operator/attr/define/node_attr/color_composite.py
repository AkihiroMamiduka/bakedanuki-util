# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorAPlugOperator(
    Float3CompoundBasePlugOperator["ColorAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorAR", "_car"),
        ("colorAG", "_cag"),
        ("colorAB", "_cab"),
    )

    colorAR = FloatField()
    car = colorAR

    colorAG = FloatField()
    cag = colorAG

    colorAB = FloatField()
    cab = colorAB


class ColorAAttrOperator(
    Float3CompoundBaseAttrOperator[ColorAPlugOperator]
):
    __slots__ = ()

    colorAR = FloatField()
    car = colorAR

    colorAG = FloatField()
    cag = colorAG

    colorAB = FloatField()
    cab = colorAB


class ColorAField(
    Float3CompoundBaseField[ColorAAttrOperator, ColorAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAAttrOperator
    PLUG_CLS = ColorAPlugOperator

    colorAR = FloatField()
    car = colorAR

    colorAG = FloatField()
    cag = colorAG

    colorAB = FloatField()
    cab = colorAB


class ColorBPlugOperator(
    Float3CompoundBasePlugOperator["ColorBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorBR", "_cbr"),
        ("colorBG", "_cbg"),
        ("colorBB", "_cbb"),
    )

    colorBR = FloatField()
    cbr = colorBR

    colorBG = FloatField()
    cbg = colorBG

    colorBB = FloatField()
    cbb = colorBB


class ColorBAttrOperator(
    Float3CompoundBaseAttrOperator[ColorBPlugOperator]
):
    __slots__ = ()

    colorBR = FloatField()
    cbr = colorBR

    colorBG = FloatField()
    cbg = colorBG

    colorBB = FloatField()
    cbb = colorBB


class ColorBField(
    Float3CompoundBaseField[ColorBAttrOperator, ColorBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorBAttrOperator
    PLUG_CLS = ColorBPlugOperator

    colorBR = FloatField()
    cbr = colorBR

    colorBG = FloatField()
    cbg = colorBG

    colorBB = FloatField()
    cbb = colorBB


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
