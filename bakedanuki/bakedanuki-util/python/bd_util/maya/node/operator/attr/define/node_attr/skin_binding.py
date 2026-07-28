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


class FalloffCurve_InterpEnumPlugOperator(EnumPlugOperator["FalloffCurve_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FalloffCurve_InterpEnumAttrOperator(EnumAttrOperator[FalloffCurve_InterpEnumPlugOperator]):
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


class FalloffCurve_InterpEnumField(
    EnumField[FalloffCurve_InterpEnumAttrOperator, FalloffCurve_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurve_InterpEnumAttrOperator
    PLUG_CLS = FalloffCurve_InterpEnumPlugOperator


class FalloffCurvePlugOperator(
    CompoundPlugOperator["FalloffCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffCurve_Position", "fcp"),
        ("falloffCurve_FloatValue", "fcfv"),
        ("falloffCurve_Interp", "fci"),
    )

    falloffCurve_Position = FloatField(default_value=0.0)
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField(default_value=0.0)
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = FalloffCurve_InterpEnumField(default_value=0)
    fci = falloffCurve_Interp


class FalloffCurveAttrOperator(
    CompoundAttrOperator[FalloffCurvePlugOperator]
):
    __slots__ = ()

    falloffCurve_Position = FloatField(default_value=0.0)
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField(default_value=0.0)
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = FalloffCurve_InterpEnumField(default_value=0)
    fci = falloffCurve_Interp


class FalloffCurveField(
    CompoundField[FalloffCurveAttrOperator, FalloffCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurveAttrOperator
    PLUG_CLS = FalloffCurvePlugOperator
