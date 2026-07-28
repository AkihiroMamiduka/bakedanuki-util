# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField


class WidthRamp_InterpEnumPlugOperator(EnumPlugOperator["WidthRamp_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WidthRamp_InterpEnumAttrOperator(EnumAttrOperator[WidthRamp_InterpEnumPlugOperator]):
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


class WidthRamp_InterpEnumField(
    EnumField[WidthRamp_InterpEnumAttrOperator, WidthRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthRamp_InterpEnumAttrOperator
    PLUG_CLS = WidthRamp_InterpEnumPlugOperator


class WidthRampPlugOperator(
    CompoundPlugOperator["WidthRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("widthRamp_Position", "wdrp"),
        ("widthRamp_FloatValue", "wdrfv"),
        ("widthRamp_Interp", "wdri"),
    )

    widthRamp_Position = FloatField(default_value=0.0)
    wdrp = widthRamp_Position

    widthRamp_FloatValue = FloatField(default_value=0.0)
    wdrfv = widthRamp_FloatValue

    widthRamp_Interp = WidthRamp_InterpEnumField(default_value=1)
    wdri = widthRamp_Interp


class WidthRampAttrOperator(
    CompoundAttrOperator[WidthRampPlugOperator]
):
    __slots__ = ()

    widthRamp_Position = FloatField(default_value=0.0)
    wdrp = widthRamp_Position

    widthRamp_FloatValue = FloatField(default_value=0.0)
    wdrfv = widthRamp_FloatValue

    widthRamp_Interp = WidthRamp_InterpEnumField(default_value=1)
    wdri = widthRamp_Interp


class WidthRampField(
    CompoundField[WidthRampAttrOperator, WidthRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthRampAttrOperator
    PLUG_CLS = WidthRampPlugOperator
