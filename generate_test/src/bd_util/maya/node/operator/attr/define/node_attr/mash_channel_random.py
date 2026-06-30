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


class StartVectorPlugOperator(
    Float3CompoundBasePlugOperator["StartVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("startVector0", "startVector0"),
        ("startVector1", "startVector1"),
        ("startVector2", "startVector2"),
    )

    startVector0 = FloatField()

    startVector1 = FloatField()

    startVector2 = FloatField()


class StartVectorAttrOperator(
    Float3CompoundBaseAttrOperator[StartVectorPlugOperator]
):
    __slots__ = ()

    startVector0 = FloatField()

    startVector1 = FloatField()

    startVector2 = FloatField()


class StartVectorField(
    Float3CompoundBaseField[StartVectorAttrOperator, StartVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartVectorAttrOperator
    PLUG_CLS = StartVectorPlugOperator

    startVector0 = FloatField()

    startVector1 = FloatField()

    startVector2 = FloatField()


class VarianceVectorMinPlugOperator(
    Float3CompoundBasePlugOperator["VarianceVectorMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("varianceVectorMin0", "varianceVectorMin0"),
        ("varianceVectorMin1", "varianceVectorMin1"),
        ("varianceVectorMin2", "varianceVectorMin2"),
    )

    varianceVectorMin0 = FloatField()

    varianceVectorMin1 = FloatField()

    varianceVectorMin2 = FloatField()


class VarianceVectorMinAttrOperator(
    Float3CompoundBaseAttrOperator[VarianceVectorMinPlugOperator]
):
    __slots__ = ()

    varianceVectorMin0 = FloatField()

    varianceVectorMin1 = FloatField()

    varianceVectorMin2 = FloatField()


class VarianceVectorMinField(
    Float3CompoundBaseField[VarianceVectorMinAttrOperator, VarianceVectorMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VarianceVectorMinAttrOperator
    PLUG_CLS = VarianceVectorMinPlugOperator

    varianceVectorMin0 = FloatField()

    varianceVectorMin1 = FloatField()

    varianceVectorMin2 = FloatField()


class VarianceVectorMaxPlugOperator(
    Float3CompoundBasePlugOperator["VarianceVectorMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("varianceVectorMax0", "varianceVectorMax0"),
        ("varianceVectorMax1", "varianceVectorMax1"),
        ("varianceVectorMax2", "varianceVectorMax2"),
    )

    varianceVectorMax0 = FloatField()

    varianceVectorMax1 = FloatField()

    varianceVectorMax2 = FloatField()


class VarianceVectorMaxAttrOperator(
    Float3CompoundBaseAttrOperator[VarianceVectorMaxPlugOperator]
):
    __slots__ = ()

    varianceVectorMax0 = FloatField()

    varianceVectorMax1 = FloatField()

    varianceVectorMax2 = FloatField()


class VarianceVectorMaxField(
    Float3CompoundBaseField[VarianceVectorMaxAttrOperator, VarianceVectorMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VarianceVectorMaxAttrOperator
    PLUG_CLS = VarianceVectorMaxPlugOperator

    varianceVectorMax0 = FloatField()

    varianceVectorMax1 = FloatField()

    varianceVectorMax2 = FloatField()
