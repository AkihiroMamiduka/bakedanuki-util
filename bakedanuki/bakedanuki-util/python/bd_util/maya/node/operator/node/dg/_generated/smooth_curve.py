# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class _GeneratedSmoothCurve(DG):
    __slots__ = ()

    NODE_TYPE = "smoothCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    smoothness = DoubleField(default_value=10.0, min_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    s = smoothness

    index = LongField(multi=True, default_value=0)
    i = index

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
