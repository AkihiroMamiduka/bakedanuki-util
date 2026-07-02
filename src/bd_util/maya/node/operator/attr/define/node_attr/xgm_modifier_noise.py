# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class MagnitudeScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class MagnitudeScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class MagnitudeScale_InterpEnumField(
    EnumField[MagnitudeScale_InterpEnumAttrOperator, MagnitudeScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScale_InterpEnumAttrOperator
    PLUG_CLS = MagnitudeScale_InterpEnumPlugOperator


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

    magnitudeScale_Interp = MagnitudeScale_InterpEnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleAttrOperator(
    CompoundAttrOperator[MagnitudeScalePlugOperator]
):
    __slots__ = ()

    magnitudeScale_Position = FloatField()
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField()
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = MagnitudeScale_InterpEnumField()
    msi = magnitudeScale_Interp


class MagnitudeScaleField(
    CompoundField[MagnitudeScaleAttrOperator, MagnitudeScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScaleAttrOperator
    PLUG_CLS = MagnitudeScalePlugOperator
