# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class SubCurve(DG):
    __slots__ = ()

    NODE_TYPE = "subCurve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    minValue = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    min = minValue

    maxValue = DoubleField(default_value=-1.0, soft_min_value=0.0, soft_max_value=1.0)
    max = maxValue

    relative = BoolField(default_value=False)
    r = relative

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve
