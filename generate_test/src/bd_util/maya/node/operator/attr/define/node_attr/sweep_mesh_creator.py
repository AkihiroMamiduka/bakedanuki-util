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
        ("taperCurve_Position", "taperCurvep"),
        ("taperCurve_FloatValue", "taperCurvefv"),
        ("taperCurve_Interp", "taperCurvei"),
    )

    taperCurve_Position = FloatField()
    taperCurvep = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    taperCurvefv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    taperCurvei = taperCurve_Interp


class TaperCurveAttrOperator(
    CompoundAttrOperator[TaperCurvePlugOperator]
):
    __slots__ = ()

    taperCurve_Position = FloatField()
    taperCurvep = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    taperCurvefv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    taperCurvei = taperCurve_Interp


class TaperCurveField(
    CompoundField[TaperCurveAttrOperator, TaperCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TaperCurveAttrOperator
    PLUG_CLS = TaperCurvePlugOperator
