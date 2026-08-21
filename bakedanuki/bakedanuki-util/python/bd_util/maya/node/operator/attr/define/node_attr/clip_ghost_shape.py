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
        ("colorR", "colr"),
        ("colorG", "colg"),
        ("colorB", "colb"),
    )

    colorR = FloatField(default_value=0.06700000166893005)
    colr = colorR

    colorG = FloatField(default_value=0.0860000029206276)
    colg = colorG

    colorB = FloatField(default_value=0.3799999952316284)
    colb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.06700000166893005)
    colr = colorR

    colorG = FloatField(default_value=0.0860000029206276)
    colg = colorG

    colorB = FloatField(default_value=0.3799999952316284)
    colb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.06700000166893005)
    colr = colorR

    colorG = FloatField(default_value=0.0860000029206276)
    colg = colorG

    colorB = FloatField(default_value=0.3799999952316284)
    colb = colorB
