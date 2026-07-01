# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class MASH_PointToCurve(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_PointToCurve"

    outputCurves = DataNurbsCurveField(multi=True)
    oc = outputCurves

    numCurves = LongField()
    nc = numCurves

    curveOffset = DoubleField()
    co = curveOffset

    inputPoints = TypedField()
