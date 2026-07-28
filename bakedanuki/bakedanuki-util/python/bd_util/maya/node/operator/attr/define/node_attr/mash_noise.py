# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class OffsetValuesPlugOperator(
    Float3CompoundBasePlugOperator["OffsetValuesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetValues0", "ofVal0"),
        ("offsetValues1", "ofVal1"),
        ("offsetValues2", "ofVal2"),
    )

    offsetValues0 = FloatField(default_value=0.0)
    ofVal0 = offsetValues0

    offsetValues1 = FloatField(default_value=0.0)
    ofVal1 = offsetValues1

    offsetValues2 = FloatField(default_value=0.0)
    ofVal2 = offsetValues2


class OffsetValuesAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetValuesPlugOperator]
):
    __slots__ = ()

    offsetValues0 = FloatField(default_value=0.0)
    ofVal0 = offsetValues0

    offsetValues1 = FloatField(default_value=0.0)
    ofVal1 = offsetValues1

    offsetValues2 = FloatField(default_value=0.0)
    ofVal2 = offsetValues2


class OffsetValuesField(
    Float3CompoundBaseField[OffsetValuesAttrOperator, OffsetValuesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetValuesAttrOperator
    PLUG_CLS = OffsetValuesPlugOperator

    offsetValues0 = FloatField(default_value=0.0)
    ofVal0 = offsetValues0

    offsetValues1 = FloatField(default_value=0.0)
    ofVal1 = offsetValues1

    offsetValues2 = FloatField(default_value=0.0)
    ofVal2 = offsetValues2
