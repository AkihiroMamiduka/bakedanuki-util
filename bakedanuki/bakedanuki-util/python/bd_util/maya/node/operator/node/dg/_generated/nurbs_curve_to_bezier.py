# coding: utf-8
from .._core import DG
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedNurbsCurveToBezier(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsCurveToBezier"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
