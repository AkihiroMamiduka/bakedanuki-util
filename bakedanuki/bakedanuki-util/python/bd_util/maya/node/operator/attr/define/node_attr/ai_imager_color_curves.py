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


class RampRGB_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RampRGB_InterpEnumAttrOperator(EnumAttrOperator):
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


class RampRGB_InterpEnumField(
    EnumField[RampRGB_InterpEnumAttrOperator, RampRGB_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampRGB_InterpEnumAttrOperator
    PLUG_CLS = RampRGB_InterpEnumPlugOperator


class RampR_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RampR_InterpEnumAttrOperator(EnumAttrOperator):
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


class RampR_InterpEnumField(
    EnumField[RampR_InterpEnumAttrOperator, RampR_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampR_InterpEnumAttrOperator
    PLUG_CLS = RampR_InterpEnumPlugOperator


class RampG_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RampG_InterpEnumAttrOperator(EnumAttrOperator):
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


class RampG_InterpEnumField(
    EnumField[RampG_InterpEnumAttrOperator, RampG_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampG_InterpEnumAttrOperator
    PLUG_CLS = RampG_InterpEnumPlugOperator


class RampB_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RampB_InterpEnumAttrOperator(EnumAttrOperator):
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


class RampB_InterpEnumField(
    EnumField[RampB_InterpEnumAttrOperator, RampB_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampB_InterpEnumAttrOperator
    PLUG_CLS = RampB_InterpEnumPlugOperator


class RampRGBPlugOperator(
    CompoundPlugOperator["RampRGBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampRGB_Position", "aiRampRGBp"),
        ("rampRGB_FloatValue", "aiRampRGBfv"),
        ("rampRGB_Interp", "aiRampRGBi"),
    )

    rampRGB_Position = FloatField(default_value=0.0)
    aiRampRGBp = rampRGB_Position

    rampRGB_FloatValue = FloatField(default_value=0.0)
    aiRampRGBfv = rampRGB_FloatValue

    rampRGB_Interp = RampRGB_InterpEnumField(default_value=1)
    aiRampRGBi = rampRGB_Interp


class RampRGBAttrOperator(
    CompoundAttrOperator[RampRGBPlugOperator]
):
    __slots__ = ()

    rampRGB_Position = FloatField(default_value=0.0)
    aiRampRGBp = rampRGB_Position

    rampRGB_FloatValue = FloatField(default_value=0.0)
    aiRampRGBfv = rampRGB_FloatValue

    rampRGB_Interp = RampRGB_InterpEnumField(default_value=1)
    aiRampRGBi = rampRGB_Interp


class RampRGBField(
    CompoundField[RampRGBAttrOperator, RampRGBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampRGBAttrOperator
    PLUG_CLS = RampRGBPlugOperator


class RampRPlugOperator(
    CompoundPlugOperator["RampRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampR_Position", "aiRampRp"),
        ("rampR_FloatValue", "aiRampRfv"),
        ("rampR_Interp", "aiRampRi"),
    )

    rampR_Position = FloatField(default_value=0.0)
    aiRampRp = rampR_Position

    rampR_FloatValue = FloatField(default_value=0.0)
    aiRampRfv = rampR_FloatValue

    rampR_Interp = RampR_InterpEnumField(default_value=1)
    aiRampRi = rampR_Interp


class RampRAttrOperator(
    CompoundAttrOperator[RampRPlugOperator]
):
    __slots__ = ()

    rampR_Position = FloatField(default_value=0.0)
    aiRampRp = rampR_Position

    rampR_FloatValue = FloatField(default_value=0.0)
    aiRampRfv = rampR_FloatValue

    rampR_Interp = RampR_InterpEnumField(default_value=1)
    aiRampRi = rampR_Interp


class RampRField(
    CompoundField[RampRAttrOperator, RampRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampRAttrOperator
    PLUG_CLS = RampRPlugOperator


class RampGPlugOperator(
    CompoundPlugOperator["RampGAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampG_Position", "aiRampGp"),
        ("rampG_FloatValue", "aiRampGfv"),
        ("rampG_Interp", "aiRampGi"),
    )

    rampG_Position = FloatField(default_value=0.0)
    aiRampGp = rampG_Position

    rampG_FloatValue = FloatField(default_value=0.0)
    aiRampGfv = rampG_FloatValue

    rampG_Interp = RampG_InterpEnumField(default_value=1)
    aiRampGi = rampG_Interp


class RampGAttrOperator(
    CompoundAttrOperator[RampGPlugOperator]
):
    __slots__ = ()

    rampG_Position = FloatField(default_value=0.0)
    aiRampGp = rampG_Position

    rampG_FloatValue = FloatField(default_value=0.0)
    aiRampGfv = rampG_FloatValue

    rampG_Interp = RampG_InterpEnumField(default_value=1)
    aiRampGi = rampG_Interp


class RampGField(
    CompoundField[RampGAttrOperator, RampGPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampGAttrOperator
    PLUG_CLS = RampGPlugOperator


class RampBPlugOperator(
    CompoundPlugOperator["RampBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampB_Position", "aiRampBp"),
        ("rampB_FloatValue", "aiRampBfv"),
        ("rampB_Interp", "aiRampBi"),
    )

    rampB_Position = FloatField(default_value=0.0)
    aiRampBp = rampB_Position

    rampB_FloatValue = FloatField(default_value=0.0)
    aiRampBfv = rampB_FloatValue

    rampB_Interp = RampB_InterpEnumField(default_value=1)
    aiRampBi = rampB_Interp


class RampBAttrOperator(
    CompoundAttrOperator[RampBPlugOperator]
):
    __slots__ = ()

    rampB_Position = FloatField(default_value=0.0)
    aiRampBp = rampB_Position

    rampB_FloatValue = FloatField(default_value=0.0)
    aiRampBfv = rampB_FloatValue

    rampB_Interp = RampB_InterpEnumField(default_value=1)
    aiRampBi = rampB_Interp


class RampBField(
    CompoundField[RampBAttrOperator, RampBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampBAttrOperator
    PLUG_CLS = RampBPlugOperator
