# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
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

    colorIfTrueR = FloatField()
    ctr = colorIfTrueR

    colorIfTrueG = FloatField()
    ctg = colorIfTrueG

    colorIfTrueB = FloatField()
    ctb = colorIfTrueB


class ColorIfTrueAttrOperator(
    Float3CompoundBaseAttrOperator[ColorIfTruePlugOperator]
):
    __slots__ = ()

    colorIfTrueR = FloatField()
    ctr = colorIfTrueR

    colorIfTrueG = FloatField()
    ctg = colorIfTrueG

    colorIfTrueB = FloatField()
    ctb = colorIfTrueB


class ColorIfTrueField(
    Float3CompoundBaseField[ColorIfTrueAttrOperator, ColorIfTruePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorIfTrueAttrOperator
    PLUG_CLS = ColorIfTruePlugOperator

    colorIfTrueR = FloatField()
    ctr = colorIfTrueR

    colorIfTrueG = FloatField()
    ctg = colorIfTrueG

    colorIfTrueB = FloatField()
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

    colorIfFalseR = FloatField()
    cfr = colorIfFalseR

    colorIfFalseG = FloatField()
    cfg = colorIfFalseG

    colorIfFalseB = FloatField()
    cfb = colorIfFalseB


class ColorIfFalseAttrOperator(
    Float3CompoundBaseAttrOperator[ColorIfFalsePlugOperator]
):
    __slots__ = ()

    colorIfFalseR = FloatField()
    cfr = colorIfFalseR

    colorIfFalseG = FloatField()
    cfg = colorIfFalseG

    colorIfFalseB = FloatField()
    cfb = colorIfFalseB


class ColorIfFalseField(
    Float3CompoundBaseField[ColorIfFalseAttrOperator, ColorIfFalsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorIfFalseAttrOperator
    PLUG_CLS = ColorIfFalsePlugOperator

    colorIfFalseR = FloatField()
    cfr = colorIfFalseR

    colorIfFalseG = FloatField()
    cfg = colorIfFalseG

    colorIfFalseB = FloatField()
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
