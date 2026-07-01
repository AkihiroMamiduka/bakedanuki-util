# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class MagnitudeScalePlugOperator(
    CompoundPlugOperator["MagnitudeScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("magnitudeScale_Position", "msp"),
        ("magnitudeScale_FloatValue", "msfv"),
        ("magnitudeScale_Interp", "msi"),
    )

    magnitudeScale_Position = FloatField()
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField()
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = EnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleAttrOperator(
    CompoundAttrOperator[MagnitudeScalePlugOperator]
):
    __slots__ = ()

    magnitudeScale_Position = FloatField()
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField()
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = EnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleField(
    CompoundField[MagnitudeScaleAttrOperator, MagnitudeScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScaleAttrOperator
    PLUG_CLS = MagnitudeScalePlugOperator
