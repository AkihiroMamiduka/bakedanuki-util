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


class SignalScaleMultiplierPlugOperator(
    Float3CompoundBasePlugOperator["SignalScaleMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("signalScaleMultiplier0", "signalScaleMultiplier0"),
        ("signalScaleMultiplier1", "signalScaleMultiplier1"),
        ("signalScaleMultiplier2", "signalScaleMultiplier2"),
    )

    signalScaleMultiplier0 = FloatField()

    signalScaleMultiplier1 = FloatField()

    signalScaleMultiplier2 = FloatField()


class SignalScaleMultiplierAttrOperator(
    Float3CompoundBaseAttrOperator[SignalScaleMultiplierPlugOperator]
):
    __slots__ = ()

    signalScaleMultiplier0 = FloatField()

    signalScaleMultiplier1 = FloatField()

    signalScaleMultiplier2 = FloatField()


class SignalScaleMultiplierField(
    Float3CompoundBaseField[SignalScaleMultiplierAttrOperator, SignalScaleMultiplierPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SignalScaleMultiplierAttrOperator
    PLUG_CLS = SignalScaleMultiplierPlugOperator

    signalScaleMultiplier0 = FloatField()

    signalScaleMultiplier1 = FloatField()

    signalScaleMultiplier2 = FloatField()
