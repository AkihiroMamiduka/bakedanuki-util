# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class TweakPlugOperator(
    Double3CompoundBasePlugOperator["TweakAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweakX", "tx"),
        ("tweakY", "ty"),
        ("tweakZ", "tz"),
    )

    tweakX = DoubleField(default_value=0.0)
    tx = tweakX

    tweakY = DoubleField(default_value=0.0)
    ty = tweakY

    tweakZ = DoubleField(default_value=0.0)
    tz = tweakZ


class TweakAttrOperator(
    Double3CompoundBaseAttrOperator[TweakPlugOperator]
):
    __slots__ = ()

    tweakX = DoubleField(default_value=0.0)
    tx = tweakX

    tweakY = DoubleField(default_value=0.0)
    ty = tweakY

    tweakZ = DoubleField(default_value=0.0)
    tz = tweakZ


class TweakField(
    Double3CompoundBaseField[TweakAttrOperator, TweakPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweakAttrOperator
    PLUG_CLS = TweakPlugOperator
