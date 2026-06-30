# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class FalloffCurvePlugOperator(
    CompoundPlugOperator["FalloffCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffCurve_Position", "fcp"),
        ("falloffCurve_FloatValue", "fcfv"),
        ("falloffCurve_Interp", "fci"),
    )

    falloffCurve_Position = FloatField()
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField()
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = EnumField()
    fci = falloffCurve_Interp


class FalloffCurveAttrOperator(
    CompoundAttrOperator[FalloffCurvePlugOperator]
):
    __slots__ = ()

    falloffCurve_Position = FloatField()
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField()
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = EnumField()
    fci = falloffCurve_Interp


class FalloffCurveField(
    CompoundField[FalloffCurveAttrOperator, FalloffCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurveAttrOperator
    PLUG_CLS = FalloffCurvePlugOperator
