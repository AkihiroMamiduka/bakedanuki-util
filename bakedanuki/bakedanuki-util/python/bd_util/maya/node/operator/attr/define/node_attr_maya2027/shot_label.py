# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cb = colorB
