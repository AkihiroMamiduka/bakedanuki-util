# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class TweakPlugOperator(
    Float3CompoundBasePlugOperator["TweakAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweakX", "tx"),
        ("tweakY", "ty"),
        ("tweakZ", "tz"),
    )

    tweakX = FloatField()
    tx = tweakX

    tweakY = FloatField()
    ty = tweakY

    tweakZ = FloatField()
    tz = tweakZ


class TweakAttrOperator(
    Float3CompoundBaseAttrOperator[TweakPlugOperator]
):
    __slots__ = ()

    tweakX = FloatField()
    tx = tweakX

    tweakY = FloatField()
    ty = tweakY

    tweakZ = FloatField()
    tz = tweakZ


class TweakField(
    Float3CompoundBaseField[TweakAttrOperator, TweakPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweakAttrOperator
    PLUG_CLS = TweakPlugOperator
