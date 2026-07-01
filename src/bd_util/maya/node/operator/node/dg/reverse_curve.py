# coding: utf-8
from ._core import DG
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class ReverseCurve(DG):
    __slots__ = ()

    NODE_TYPE = "reverseCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
