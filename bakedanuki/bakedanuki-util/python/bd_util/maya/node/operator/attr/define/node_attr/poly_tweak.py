# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class TweakPlugOperator(Float3CompoundBasePlugOperator["TweakAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweakX", "tx"),
        ("tweakY", "ty"),
        ("tweakZ", "tz"),
    )

    tweakX = FloatField(default_value=0.0)
    tx = tweakX

    tweakY = FloatField(default_value=0.0)
    ty = tweakY

    tweakZ = FloatField(default_value=0.0)
    tz = tweakZ


class TweakAttrOperator(Float3CompoundBaseAttrOperator[TweakPlugOperator]):
    __slots__ = ()

    tweakX = FloatField(default_value=0.0)
    tx = tweakX

    tweakY = FloatField(default_value=0.0)
    ty = tweakY

    tweakZ = FloatField(default_value=0.0)
    tz = tweakZ


class TweakField(
    Float3CompoundBaseField[TweakAttrOperator, TweakPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweakAttrOperator
    PLUG_CLS = TweakPlugOperator
