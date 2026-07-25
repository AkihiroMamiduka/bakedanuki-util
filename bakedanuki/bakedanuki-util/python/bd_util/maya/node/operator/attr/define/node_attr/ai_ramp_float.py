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
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class RampPlugOperator(
    CompoundPlugOperator["RampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_Position", "aiRampp"),
        ("ramp_FloatValue", "aiRampfv"),
        ("ramp_Interp", "aiRampi"),
    )

    ramp_Position = FloatField(default_value=0.0)
    aiRampp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    aiRampfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=1)
    aiRampi = ramp_Interp


class RampAttrOperator(
    CompoundAttrOperator[RampPlugOperator]
):
    __slots__ = ()

    ramp_Position = FloatField(default_value=0.0)
    aiRampp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    aiRampfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=1)
    aiRampi = ramp_Interp


class RampField(
    CompoundField[RampAttrOperator, RampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampAttrOperator
    PLUG_CLS = RampPlugOperator
