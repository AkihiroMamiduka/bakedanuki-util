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


class AmplitudeColourPlugOperator(
    Float3CompoundBasePlugOperator["AmplitudeColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("amplitudeColourR", "amplitudeColourR"),
        ("amplitudeColourG", "amplitudeColourG"),
        ("amplitudeColourB", "amplitudeColourB"),
    )

    amplitudeColourR = FloatField(default_value=1.0)

    amplitudeColourG = FloatField(default_value=1.0)

    amplitudeColourB = FloatField(default_value=1.0)


class AmplitudeColourAttrOperator(
    Float3CompoundBaseAttrOperator[AmplitudeColourPlugOperator]
):
    __slots__ = ()

    amplitudeColourR = FloatField(default_value=1.0)

    amplitudeColourG = FloatField(default_value=1.0)

    amplitudeColourB = FloatField(default_value=1.0)


class AmplitudeColourField(
    Float3CompoundBaseField[
        AmplitudeColourAttrOperator, AmplitudeColourPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AmplitudeColourAttrOperator
    PLUG_CLS = AmplitudeColourPlugOperator

    amplitudeColourR = FloatField(default_value=1.0)

    amplitudeColourG = FloatField(default_value=1.0)

    amplitudeColourB = FloatField(default_value=1.0)
