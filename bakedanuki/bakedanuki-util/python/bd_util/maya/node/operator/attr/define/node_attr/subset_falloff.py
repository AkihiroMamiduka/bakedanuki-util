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


class Ramp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Ramp_InterpEnumAttrOperator(EnumAttrOperator):
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


class Ramp_InterpEnumField(
    EnumField[Ramp_InterpEnumAttrOperator, Ramp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Ramp_InterpEnumAttrOperator
    PLUG_CLS = Ramp_InterpEnumPlugOperator


class RampPlugOperator(
    CompoundPlugOperator["RampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_Position", "rmpp"),
        ("ramp_FloatValue", "rmpfv"),
        ("ramp_Interp", "rmpi"),
    )

    ramp_Position = FloatField(default_value=0.0)
    rmpp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    rmpfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=0)
    rmpi = ramp_Interp


class RampAttrOperator(
    CompoundAttrOperator[RampPlugOperator]
):
    __slots__ = ()

    ramp_Position = FloatField(default_value=0.0)
    rmpp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    rmpfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=0)
    rmpi = ramp_Interp


class RampField(
    CompoundField[RampAttrOperator, RampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampAttrOperator
    PLUG_CLS = RampPlugOperator
