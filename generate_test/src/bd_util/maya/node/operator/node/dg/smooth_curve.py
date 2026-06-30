# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class SmoothCurve(DG):
    __slots__ = ()

    NODE_TYPE = "smoothCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    smoothness = DoubleField()
    s = smoothness

    index = LongField(multi=True)
    i = index

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
