# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorAPlugOperator(Float3CompoundBasePlugOperator["ColorAAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorAR", "_car"),
        ("colorAG", "_cag"),
        ("colorAB", "_cab"),
    )

    colorAR = FloatField(default_value=1.0)
    car = colorAR

    colorAG = FloatField(default_value=0.0)
    cag = colorAG

    colorAB = FloatField(default_value=0.0)
    cab = colorAB


class ColorAAttrOperator(Float3CompoundBaseAttrOperator[ColorAPlugOperator]):
    __slots__ = ()

    colorAR = FloatField(default_value=1.0)
    car = colorAR

    colorAG = FloatField(default_value=0.0)
    cag = colorAG

    colorAB = FloatField(default_value=0.0)
    cab = colorAB


class ColorAField(
    Float3CompoundBaseField[ColorAAttrOperator, ColorAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAAttrOperator
    PLUG_CLS = ColorAPlugOperator

    colorAR = FloatField(default_value=1.0)
    car = colorAR

    colorAG = FloatField(default_value=0.0)
    cag = colorAG

    colorAB = FloatField(default_value=0.0)
    cab = colorAB


class ColorBPlugOperator(Float3CompoundBasePlugOperator["ColorBAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorBR", "_cbr"),
        ("colorBG", "_cbg"),
        ("colorBB", "_cbb"),
    )

    colorBR = FloatField(default_value=0.0)
    cbr = colorBR

    colorBG = FloatField(default_value=1.0)
    cbg = colorBG

    colorBB = FloatField(default_value=0.0)
    cbb = colorBB


class ColorBAttrOperator(Float3CompoundBaseAttrOperator[ColorBPlugOperator]):
    __slots__ = ()

    colorBR = FloatField(default_value=0.0)
    cbr = colorBR

    colorBG = FloatField(default_value=1.0)
    cbg = colorBG

    colorBB = FloatField(default_value=0.0)
    cbb = colorBB


class ColorBField(
    Float3CompoundBaseField[ColorBAttrOperator, ColorBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorBAttrOperator
    PLUG_CLS = ColorBPlugOperator

    colorBR = FloatField(default_value=0.0)
    cbr = colorBR

    colorBG = FloatField(default_value=1.0)
    cbg = colorBG

    colorBB = FloatField(default_value=0.0)
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

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB
