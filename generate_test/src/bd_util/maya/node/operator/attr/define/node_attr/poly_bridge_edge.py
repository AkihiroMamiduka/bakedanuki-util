# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class TaperCurvePlugOperator(
    CompoundPlugOperator["TaperCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("taperCurve_Position", "cp"),
        ("taperCurve_FloatValue", "cfv"),
        ("taperCurve_Interp", "ci"),
    )

    taperCurve_Position = FloatField()
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    cfv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    ci = taperCurve_Interp


class TaperCurveAttrOperator(
    CompoundAttrOperator[TaperCurvePlugOperator]
):
    __slots__ = ()

    taperCurve_Position = FloatField()
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    cfv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    ci = taperCurve_Interp


class TaperCurveField(
    CompoundField[TaperCurveAttrOperator, TaperCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TaperCurveAttrOperator
    PLUG_CLS = TaperCurvePlugOperator
