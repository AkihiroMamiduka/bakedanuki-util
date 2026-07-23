# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class _GeneratedAvgCurves(DG):
    __slots__ = ()

    NODE_TYPE = "avgCurves"

    inputCurve1 = DataNurbsCurveField()
    ic1 = inputCurve1

    inputCurve2 = DataNurbsCurveField()
    ic2 = inputCurve2

    weight1 = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    w1 = weight1

    weight2 = DoubleField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    w2 = weight2

    automaticWeight = BoolField(default_value=True)
    aw = automaticWeight

    normalizeWeights = BoolField(default_value=True)
    nw = normalizeWeights

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
