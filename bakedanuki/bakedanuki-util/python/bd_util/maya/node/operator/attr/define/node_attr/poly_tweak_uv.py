# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
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


class UvTweakAttrOperator(Float2CompoundBaseAttrOperator[UvTweakPlugOperator]):
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


class NewUVPlugOperator(CompoundPlugOperator["NewUVAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("faceId", "fid"),
        ("vertexId", "vid"),
        ("newUValue", "nu"),
        ("newVValue", "nv"),
    )

    faceId = LongField(default_value=-1)
    fid = faceId

    vertexId = LongField(default_value=0)
    vid = vertexId

    newUValue = FloatField(default_value=0.0)
    nu = newUValue

    newVValue = FloatField(default_value=0.0)
    nv = newVValue


class NewUVAttrOperator(CompoundAttrOperator[NewUVPlugOperator]):
    __slots__ = ()

    faceId = LongField(default_value=-1)
    fid = faceId

    vertexId = LongField(default_value=0)
    vid = vertexId

    newUValue = FloatField(default_value=0.0)
    nu = newUValue

    newVValue = FloatField(default_value=0.0)
    nv = newVValue


class NewUVField(CompoundField[NewUVAttrOperator, NewUVPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NewUVAttrOperator
    PLUG_CLS = NewUVPlugOperator
