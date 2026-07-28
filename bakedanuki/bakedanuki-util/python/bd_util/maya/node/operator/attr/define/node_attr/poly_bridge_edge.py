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


class TaperCurve_InterpEnumPlugOperator(
    EnumPlugOperator["TaperCurve_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class TaperCurve_InterpEnumAttrOperator(
    EnumAttrOperator[TaperCurve_InterpEnumPlugOperator]
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


class TaperCurve_InterpEnumField(
    EnumField[
        TaperCurve_InterpEnumAttrOperator, TaperCurve_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TaperCurve_InterpEnumAttrOperator
    PLUG_CLS = TaperCurve_InterpEnumPlugOperator


class TaperCurvePlugOperator(CompoundPlugOperator["TaperCurveAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("taperCurve_Position", "cp"),
        ("taperCurve_FloatValue", "cfv"),
        ("taperCurve_Interp", "ci"),
    )

    taperCurve_Position = FloatField(default_value=0.0)
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField(default_value=0.0)
    cfv = taperCurve_FloatValue

    taperCurve_Interp = TaperCurve_InterpEnumField(default_value=0)
    ci = taperCurve_Interp


class TaperCurveAttrOperator(CompoundAttrOperator[TaperCurvePlugOperator]):
    __slots__ = ()

    taperCurve_Position = FloatField(default_value=0.0)
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField(default_value=0.0)
    cfv = taperCurve_FloatValue

    taperCurve_Interp = TaperCurve_InterpEnumField(default_value=0)
    ci = taperCurve_Interp


class TaperCurveField(
    CompoundField[TaperCurveAttrOperator, TaperCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TaperCurveAttrOperator
    PLUG_CLS = TaperCurvePlugOperator
