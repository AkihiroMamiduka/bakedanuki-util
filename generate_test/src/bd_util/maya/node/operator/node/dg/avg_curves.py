# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class AvgCurves(DG):
    __slots__ = ()

    NODE_TYPE = "avgCurves"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    weight1 = DoubleField()
    w1 = weight1

    weight2 = DoubleField()
    w2 = weight2

    automaticWeight = BoolField()
    aw = automaticWeight

    normalizeWeights = BoolField()
    nw = normalizeWeights

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
