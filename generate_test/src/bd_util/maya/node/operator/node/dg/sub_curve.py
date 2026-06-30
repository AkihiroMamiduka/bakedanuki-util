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

    minValue = DoubleField()
    min = minValue

    maxValue = DoubleField()
    max = maxValue

    relative = BoolField()
    r = relative

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
