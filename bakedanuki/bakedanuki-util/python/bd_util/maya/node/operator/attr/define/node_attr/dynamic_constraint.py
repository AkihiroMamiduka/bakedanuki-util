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


class ConnectionDensityRange_connectionDensityRange_InterpEnumPlugOperator(
    EnumPlugOperator[
        "ConnectionDensityRange_connectionDensityRange_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ConnectionDensityRange_connectionDensityRange_InterpEnumAttrOperator(
    EnumAttrOperator[
        ConnectionDensityRange_connectionDensityRange_InterpEnumPlugOperator
    ]
):
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


class ConnectionDensityRange_connectionDensityRange_InterpEnumField(
    EnumField[
        ConnectionDensityRange_connectionDensityRange_InterpEnumAttrOperator,
        ConnectionDensityRange_connectionDensityRange_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = (
        ConnectionDensityRange_connectionDensityRange_InterpEnumAttrOperator
    )
    PLUG_CLS = (
        ConnectionDensityRange_connectionDensityRange_InterpEnumPlugOperator
    )


class StrengthDropoff_strengthDropoff_InterpEnumPlugOperator(
    EnumPlugOperator["StrengthDropoff_strengthDropoff_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class StrengthDropoff_strengthDropoff_InterpEnumAttrOperator(
    EnumAttrOperator[StrengthDropoff_strengthDropoff_InterpEnumPlugOperator]
):
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


class StrengthDropoff_strengthDropoff_InterpEnumField(
    EnumField[
        StrengthDropoff_strengthDropoff_InterpEnumAttrOperator,
        StrengthDropoff_strengthDropoff_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = StrengthDropoff_strengthDropoff_InterpEnumAttrOperator
    PLUG_CLS = StrengthDropoff_strengthDropoff_InterpEnumPlugOperator


class ConnectionDensityRangePlugOperator(
    CompoundPlugOperator["ConnectionDensityRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("connectionDensityRange_Position", "cdnrp"),
        ("connectionDensityRange_FloatValue", "cdnrfv"),
        ("connectionDensityRange_Interp", "cdnri"),
    )

    connectionDensityRange_Position = FloatField(default_value=0.0)
    cdnrp = connectionDensityRange_Position

    connectionDensityRange_FloatValue = FloatField(default_value=0.0)
    cdnrfv = connectionDensityRange_FloatValue

    connectionDensityRange_Interp = (
        ConnectionDensityRange_connectionDensityRange_InterpEnumField(
            default_value=0
        )
    )
    cdnri = connectionDensityRange_Interp


class ConnectionDensityRangeAttrOperator(
    CompoundAttrOperator[ConnectionDensityRangePlugOperator]
):
    __slots__ = ()

    connectionDensityRange_Position = FloatField(default_value=0.0)
    cdnrp = connectionDensityRange_Position

    connectionDensityRange_FloatValue = FloatField(default_value=0.0)
    cdnrfv = connectionDensityRange_FloatValue

    connectionDensityRange_Interp = (
        ConnectionDensityRange_connectionDensityRange_InterpEnumField(
            default_value=0
        )
    )
    cdnri = connectionDensityRange_Interp


class ConnectionDensityRangeField(
    CompoundField[
        ConnectionDensityRangeAttrOperator, ConnectionDensityRangePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConnectionDensityRangeAttrOperator
    PLUG_CLS = ConnectionDensityRangePlugOperator


class StrengthDropoffPlugOperator(
    CompoundPlugOperator["StrengthDropoffAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("strengthDropoff_Position", "sdpp"),
        ("strengthDropoff_FloatValue", "sdpfv"),
        ("strengthDropoff_Interp", "sdpi"),
    )

    strengthDropoff_Position = FloatField(default_value=0.0)
    sdpp = strengthDropoff_Position

    strengthDropoff_FloatValue = FloatField(default_value=0.0)
    sdpfv = strengthDropoff_FloatValue

    strengthDropoff_Interp = StrengthDropoff_strengthDropoff_InterpEnumField(
        default_value=0
    )
    sdpi = strengthDropoff_Interp


class StrengthDropoffAttrOperator(
    CompoundAttrOperator[StrengthDropoffPlugOperator]
):
    __slots__ = ()

    strengthDropoff_Position = FloatField(default_value=0.0)
    sdpp = strengthDropoff_Position

    strengthDropoff_FloatValue = FloatField(default_value=0.0)
    sdpfv = strengthDropoff_FloatValue

    strengthDropoff_Interp = StrengthDropoff_strengthDropoff_InterpEnumField(
        default_value=0
    )
    sdpi = strengthDropoff_Interp


class StrengthDropoffField(
    CompoundField[StrengthDropoffAttrOperator, StrengthDropoffPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StrengthDropoffAttrOperator
    PLUG_CLS = StrengthDropoffPlugOperator
