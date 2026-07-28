# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorIfTruePlugOperator(
    Float3CompoundBasePlugOperator["ColorIfTrueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorIfTrueR", "ctr"),
        ("colorIfTrueG", "ctg"),
        ("colorIfTrueB", "ctb"),
    )

    colorIfTrueR = FloatField(default_value=0.0)
    ctr = colorIfTrueR

    colorIfTrueG = FloatField(default_value=0.0)
    ctg = colorIfTrueG

    colorIfTrueB = FloatField(default_value=0.0)
    ctb = colorIfTrueB


class ColorIfTrueAttrOperator(
    Float3CompoundBaseAttrOperator[ColorIfTruePlugOperator]
):
    __slots__ = ()

    colorIfTrueR = FloatField(default_value=0.0)
    ctr = colorIfTrueR

    colorIfTrueG = FloatField(default_value=0.0)
    ctg = colorIfTrueG

    colorIfTrueB = FloatField(default_value=0.0)
    ctb = colorIfTrueB


class ColorIfTrueField(
    Float3CompoundBaseField[ColorIfTrueAttrOperator, ColorIfTruePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorIfTrueAttrOperator
    PLUG_CLS = ColorIfTruePlugOperator

    colorIfTrueR = FloatField(default_value=0.0)
    ctr = colorIfTrueR

    colorIfTrueG = FloatField(default_value=0.0)
    ctg = colorIfTrueG

    colorIfTrueB = FloatField(default_value=0.0)
    ctb = colorIfTrueB


class ColorIfFalsePlugOperator(
    Float3CompoundBasePlugOperator["ColorIfFalseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorIfFalseR", "cfr"),
        ("colorIfFalseG", "cfg"),
        ("colorIfFalseB", "cfb"),
    )

    colorIfFalseR = FloatField(default_value=1.0)
    cfr = colorIfFalseR

    colorIfFalseG = FloatField(default_value=1.0)
    cfg = colorIfFalseG

    colorIfFalseB = FloatField(default_value=1.0)
    cfb = colorIfFalseB


class ColorIfFalseAttrOperator(
    Float3CompoundBaseAttrOperator[ColorIfFalsePlugOperator]
):
    __slots__ = ()

    colorIfFalseR = FloatField(default_value=1.0)
    cfr = colorIfFalseR

    colorIfFalseG = FloatField(default_value=1.0)
    cfg = colorIfFalseG

    colorIfFalseB = FloatField(default_value=1.0)
    cfb = colorIfFalseB


class ColorIfFalseField(
    Float3CompoundBaseField[ColorIfFalseAttrOperator, ColorIfFalsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorIfFalseAttrOperator
    PLUG_CLS = ColorIfFalsePlugOperator

    colorIfFalseR = FloatField(default_value=1.0)
    cfr = colorIfFalseR

    colorIfFalseG = FloatField(default_value=1.0)
    cfg = colorIfFalseG

    colorIfFalseB = FloatField(default_value=1.0)
    cfb = colorIfFalseB


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
