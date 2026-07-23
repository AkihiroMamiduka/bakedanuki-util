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


class ProfileCurve_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ProfileCurve_InterpEnumAttrOperator(EnumAttrOperator):
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


class ProfileCurve_InterpEnumField(
    EnumField[ProfileCurve_InterpEnumAttrOperator, ProfileCurve_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfileCurve_InterpEnumAttrOperator
    PLUG_CLS = ProfileCurve_InterpEnumPlugOperator


class ProfileCurvePlugOperator(
    CompoundPlugOperator["ProfileCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("profileCurve_Position", "pp"),
        ("profileCurve_FloatValue", "pfv"),
        ("profileCurve_Interp", "pi"),
    )

    profileCurve_Position = FloatField(default_value=0.0)
    pp = profileCurve_Position

    profileCurve_FloatValue = FloatField(default_value=0.0)
    pfv = profileCurve_FloatValue

    profileCurve_Interp = ProfileCurve_InterpEnumField(default_value=0)
    pi = profileCurve_Interp


class ProfileCurveAttrOperator(
    CompoundAttrOperator[ProfileCurvePlugOperator]
):
    __slots__ = ()

    profileCurve_Position = FloatField(default_value=0.0)
    pp = profileCurve_Position

    profileCurve_FloatValue = FloatField(default_value=0.0)
    pfv = profileCurve_FloatValue

    profileCurve_Interp = ProfileCurve_InterpEnumField(default_value=0)
    pi = profileCurve_Interp


class ProfileCurveField(
    CompoundField[ProfileCurveAttrOperator, ProfileCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfileCurveAttrOperator
    PLUG_CLS = ProfileCurvePlugOperator
