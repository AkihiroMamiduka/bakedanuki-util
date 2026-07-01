# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InColorPlugOperator(
    Float3CompoundBasePlugOperator["InColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inColorR", "_cr"),
        ("inColorG", "_cg"),
        ("inColorB", "_cb"),
    )

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


class InColorAttrOperator(
    Float3CompoundBaseAttrOperator[InColorPlugOperator]
):
    __slots__ = ()

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


class InColorField(
    Float3CompoundBaseField[InColorAttrOperator, InColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InColorAttrOperator
    PLUG_CLS = InColorPlugOperator

    inColorR = FloatField()
    cr = inColorR

    inColorG = FloatField()
    cg = inColorG

    inColorB = FloatField()
    cb = inColorB


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
