# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class HardenPoint(DG):
    __slots__ = ()

    NODE_TYPE = "hardenPoint"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    index = LongField(multi=True)
    i = index

    multiplicity = LongField()
    m = multiplicity

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
