# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedDetachCurve(DG):
    __slots__ = ()

    NODE_TYPE = "detachCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve

    parameter = DoubleField(multi=True, default_value=0.0, soft_min_value=0.0, soft_max_value=1000.0)
    p = parameter

    keep = BoolField(multi=True, default_value=True)
    k = keep
