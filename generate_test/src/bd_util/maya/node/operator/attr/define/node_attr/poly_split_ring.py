# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class ProfileCurvePlugOperator(
    CompoundPlugOperator["ProfileCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("profileCurve_Position", "pp"),
        ("profileCurve_FloatValue", "pfv"),
        ("profileCurve_Interp", "pi"),
    )

    profileCurve_Position = FloatField()
    pp = profileCurve_Position

    profileCurve_FloatValue = FloatField()
    pfv = profileCurve_FloatValue

    profileCurve_Interp = EnumField()
    pi = profileCurve_Interp


class ProfileCurveAttrOperator(
    CompoundAttrOperator[ProfileCurvePlugOperator]
):
    __slots__ = ()

    profileCurve_Position = FloatField()
    pp = profileCurve_Position

    profileCurve_FloatValue = FloatField()
    pfv = profileCurve_FloatValue

    profileCurve_Interp = EnumField()
    pi = profileCurve_Interp


class ProfileCurveField(
    CompoundField[ProfileCurveAttrOperator, ProfileCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfileCurveAttrOperator
    PLUG_CLS = ProfileCurvePlugOperator
