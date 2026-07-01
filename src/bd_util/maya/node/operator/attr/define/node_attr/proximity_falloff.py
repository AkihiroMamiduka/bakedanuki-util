# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class RampPlugOperator(
    CompoundPlugOperator["RampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_Position", "rmpp"),
        ("ramp_FloatValue", "rmpfv"),
        ("ramp_Interp", "rmpi"),
    )

    ramp_Position = FloatField()
    rmpp = ramp_Position

    ramp_FloatValue = FloatField()
    rmpfv = ramp_FloatValue

    ramp_Interp = EnumField()
    rmpi = ramp_Interp


class RampAttrOperator(
    CompoundAttrOperator[RampPlugOperator]
):
    __slots__ = ()

    ramp_Position = FloatField()
    rmpp = ramp_Position

    ramp_FloatValue = FloatField()
    rmpfv = ramp_FloatValue

    ramp_Interp = EnumField()
    rmpi = ramp_Interp


class RampField(
    CompoundField[RampAttrOperator, RampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampAttrOperator
    PLUG_CLS = RampPlugOperator
