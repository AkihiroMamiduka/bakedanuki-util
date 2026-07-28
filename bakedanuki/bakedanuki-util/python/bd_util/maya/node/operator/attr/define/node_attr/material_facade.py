# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=1.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.6000000238418579)
    ocg = outColorG

    outColorB = FloatField(default_value=0.4000000059604645)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=1.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.6000000238418579)
    ocg = outColorG

    outColorB = FloatField(default_value=0.4000000059604645)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=1.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.6000000238418579)
    ocg = outColorG

    outColorB = FloatField(default_value=0.4000000059604645)
    ocb = outColorB
