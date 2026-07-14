# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class HardenPoint(DG):
    __slots__ = ()

    NODE_TYPE = "hardenPoint"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    index = LongField(multi=True, default_value=0)
    i = index

    multiplicity = LongField(default_value=-1, soft_min_value=1, soft_max_value=3)
    m = multiplicity

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
