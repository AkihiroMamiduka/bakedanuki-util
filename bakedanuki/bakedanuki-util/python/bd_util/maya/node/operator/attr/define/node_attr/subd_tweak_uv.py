# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class UvTweakPlugOperator(
    Float2CompoundBasePlugOperator["UvTweakAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvTweakU", "tu"),
        ("uvTweakV", "tv"),
    )

    uvTweakU = FloatField(default_value=0.0)
    tu = uvTweakU

    uvTweakV = FloatField(default_value=0.0)
    tv = uvTweakV


class UvTweakAttrOperator(
    Float2CompoundBaseAttrOperator[UvTweakPlugOperator]
):
    __slots__ = ()

    uvTweakU = FloatField(default_value=0.0)
    tu = uvTweakU

    uvTweakV = FloatField(default_value=0.0)
    tv = uvTweakV


class UvTweakField(
    Float2CompoundBaseField[UvTweakAttrOperator, UvTweakPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvTweakAttrOperator
    PLUG_CLS = UvTweakPlugOperator
