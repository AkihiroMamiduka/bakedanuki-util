# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
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

    offsetValues0 = FloatField()
    ofVal0 = offsetValues0

    offsetValues1 = FloatField()
    ofVal1 = offsetValues1

    offsetValues2 = FloatField()
    ofVal2 = offsetValues2


class OffsetValuesAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetValuesPlugOperator]
):
    __slots__ = ()

    offsetValues0 = FloatField()
    ofVal0 = offsetValues0

    offsetValues1 = FloatField()
    ofVal1 = offsetValues1

    offsetValues2 = FloatField()
    ofVal2 = offsetValues2


class OffsetValuesField(
    Float3CompoundBaseField[OffsetValuesAttrOperator, OffsetValuesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetValuesAttrOperator
    PLUG_CLS = OffsetValuesPlugOperator

    offsetValues0 = FloatField()
    ofVal0 = offsetValues0

    offsetValues1 = FloatField()
    ofVal1 = offsetValues1

    offsetValues2 = FloatField()
    ofVal2 = offsetValues2
