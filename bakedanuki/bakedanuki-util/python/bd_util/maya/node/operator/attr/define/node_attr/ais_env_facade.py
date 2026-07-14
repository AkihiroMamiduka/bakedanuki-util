# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.short import ShortField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "bcr"),
        ("backgroundColorG", "bcg"),
        ("backgroundColorB", "bcb"),
    )

    backgroundColorR = FloatField(default_value=0.699999988079071)
    bcr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.699999988079071)
    bcg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.699999988079071)
    bcb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField(default_value=0.699999988079071)
    bcr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.699999988079071)
    bcg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.699999988079071)
    bcb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField(default_value=0.699999988079071)
    bcr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.699999988079071)
    bcg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.699999988079071)
    bcb = backgroundColorB


class ExtraLightInfoPlugOperator(
    CompoundPlugOperator["ExtraLightInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extraLightShape", "elsh"),
        ("extraLightShadows", "elsd"),
        ("extraLightOnOff", "eloo"),
        ("extraLightIntensity", "elin"),
        ("extraLightColor", "elc"),
        ("extraLightShadowColor", "elsc"),
        ("extraLightShadowSmoothness", "elss"),
        ("extraLightShadowWidth", "elsw"),
    )

    extraLightShape = MessageField()
    elsh = extraLightShape

    extraLightShadows = BoolField(default_value=False)
    elsd = extraLightShadows

    extraLightOnOff = BoolField(default_value=False)
    eloo = extraLightOnOff

    extraLightIntensity = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    elin = extraLightIntensity

    extraLightColor = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    elc = extraLightColor

    extraLightShadowColor = Float3Field(default_value=(0.0, 0.0, 0.0))
    elsc = extraLightShadowColor

    extraLightShadowSmoothness = ShortField(default_value=1, min_value=1, max_value=40)
    elss = extraLightShadowSmoothness

    extraLightShadowWidth = DoubleField(default_value=0.0, min_value=0.0, max_value=10.0)
    elsw = extraLightShadowWidth


class ExtraLightInfoAttrOperator(
    CompoundAttrOperator[ExtraLightInfoPlugOperator]
):
    __slots__ = ()

    extraLightShape = MessageField()
    elsh = extraLightShape

    extraLightShadows = BoolField(default_value=False)
    elsd = extraLightShadows

    extraLightOnOff = BoolField(default_value=False)
    eloo = extraLightOnOff

    extraLightIntensity = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    elin = extraLightIntensity

    extraLightColor = Float3Field(default_value=(1.0, 1.0, 1.0), readable=False)
    elc = extraLightColor

    extraLightShadowColor = Float3Field(default_value=(0.0, 0.0, 0.0))
    elsc = extraLightShadowColor

    extraLightShadowSmoothness = ShortField(default_value=1, min_value=1, max_value=40)
    elss = extraLightShadowSmoothness

    extraLightShadowWidth = DoubleField(default_value=0.0, min_value=0.0, max_value=10.0)
    elsw = extraLightShadowWidth


class ExtraLightInfoField(
    CompoundField[ExtraLightInfoAttrOperator, ExtraLightInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtraLightInfoAttrOperator
    PLUG_CLS = ExtraLightInfoPlugOperator
