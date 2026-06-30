# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "bcr"),
        ("backgroundColorG", "bcg"),
        ("backgroundColorB", "bcb"),
    )

    backgroundColorR = FloatField()
    bcr = backgroundColorR

    backgroundColorG = FloatField()
    bcg = backgroundColorG

    backgroundColorB = FloatField()
    bcb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField()
    bcr = backgroundColorR

    backgroundColorG = FloatField()
    bcg = backgroundColorG

    backgroundColorB = FloatField()
    bcb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField()
    bcr = backgroundColorR

    backgroundColorG = FloatField()
    bcg = backgroundColorG

    backgroundColorB = FloatField()
    bcb = backgroundColorB
