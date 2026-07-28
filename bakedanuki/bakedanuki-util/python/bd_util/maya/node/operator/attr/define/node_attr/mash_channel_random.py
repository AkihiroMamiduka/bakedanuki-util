# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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


class StartVectorPlugOperator(
    Float3CompoundBasePlugOperator["StartVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("startVector0", "startVector0"),
        ("startVector1", "startVector1"),
        ("startVector2", "startVector2"),
    )

    startVector0 = FloatField(default_value=0.0)

    startVector1 = FloatField(default_value=0.0)

    startVector2 = FloatField(default_value=0.0)


class StartVectorAttrOperator(
    Float3CompoundBaseAttrOperator[StartVectorPlugOperator]
):
    __slots__ = ()

    startVector0 = FloatField(default_value=0.0)

    startVector1 = FloatField(default_value=0.0)

    startVector2 = FloatField(default_value=0.0)


class StartVectorField(
    Float3CompoundBaseField[StartVectorAttrOperator, StartVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StartVectorAttrOperator
    PLUG_CLS = StartVectorPlugOperator

    startVector0 = FloatField(default_value=0.0)

    startVector1 = FloatField(default_value=0.0)

    startVector2 = FloatField(default_value=0.0)


class VarianceVectorMinPlugOperator(
    Float3CompoundBasePlugOperator["VarianceVectorMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("varianceVectorMin0", "varianceVectorMin0"),
        ("varianceVectorMin1", "varianceVectorMin1"),
        ("varianceVectorMin2", "varianceVectorMin2"),
    )

    varianceVectorMin0 = FloatField(default_value=0.0)

    varianceVectorMin1 = FloatField(default_value=0.0)

    varianceVectorMin2 = FloatField(default_value=0.0)


class VarianceVectorMinAttrOperator(
    Float3CompoundBaseAttrOperator[VarianceVectorMinPlugOperator]
):
    __slots__ = ()

    varianceVectorMin0 = FloatField(default_value=0.0)

    varianceVectorMin1 = FloatField(default_value=0.0)

    varianceVectorMin2 = FloatField(default_value=0.0)


class VarianceVectorMinField(
    Float3CompoundBaseField[
        VarianceVectorMinAttrOperator, VarianceVectorMinPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VarianceVectorMinAttrOperator
    PLUG_CLS = VarianceVectorMinPlugOperator

    varianceVectorMin0 = FloatField(default_value=0.0)

    varianceVectorMin1 = FloatField(default_value=0.0)

    varianceVectorMin2 = FloatField(default_value=0.0)


class VarianceVectorMaxPlugOperator(
    Float3CompoundBasePlugOperator["VarianceVectorMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("varianceVectorMax0", "varianceVectorMax0"),
        ("varianceVectorMax1", "varianceVectorMax1"),
        ("varianceVectorMax2", "varianceVectorMax2"),
    )

    varianceVectorMax0 = FloatField(default_value=0.0)

    varianceVectorMax1 = FloatField(default_value=0.0)

    varianceVectorMax2 = FloatField(default_value=0.0)


class VarianceVectorMaxAttrOperator(
    Float3CompoundBaseAttrOperator[VarianceVectorMaxPlugOperator]
):
    __slots__ = ()

    varianceVectorMax0 = FloatField(default_value=0.0)

    varianceVectorMax1 = FloatField(default_value=0.0)

    varianceVectorMax2 = FloatField(default_value=0.0)


class VarianceVectorMaxField(
    Float3CompoundBaseField[
        VarianceVectorMaxAttrOperator, VarianceVectorMaxPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VarianceVectorMaxAttrOperator
    PLUG_CLS = VarianceVectorMaxPlugOperator

    varianceVectorMax0 = FloatField(default_value=0.0)

    varianceVectorMax1 = FloatField(default_value=0.0)

    varianceVectorMax2 = FloatField(default_value=0.0)
