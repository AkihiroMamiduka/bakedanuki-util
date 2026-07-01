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

    parameter = DoubleField(multi=True)
    p = parameter

    numberOfKnots = LongField(multi=True)
    nk = numberOfKnots

    addKnots = BoolField()
    add = addKnots

    insertBetween = BoolField()
    ib = insertBetween

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
