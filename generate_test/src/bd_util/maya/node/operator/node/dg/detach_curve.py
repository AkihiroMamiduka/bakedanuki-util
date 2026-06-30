# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DetachCurve(DG):
    __slots__ = ()

    NODE_TYPE = "detachCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve

    parameter = DoubleField(multi=True)
    p = parameter

    keep = BoolField(multi=True)
    k = keep
