# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class InsertKnotCurve(DG):
    __slots__ = ()

    NODE_TYPE = "insertKnotCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    parameter = DoubleField(multi=True, default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    p = parameter

    numberOfKnots = LongField(multi=True, default_value=1, min_value=0, soft_min_value=0, soft_max_value=3)
    nk = numberOfKnots

    addKnots = BoolField(default_value=True)
    add = addKnots

    insertBetween = BoolField(default_value=False)
    ib = insertBetween

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
