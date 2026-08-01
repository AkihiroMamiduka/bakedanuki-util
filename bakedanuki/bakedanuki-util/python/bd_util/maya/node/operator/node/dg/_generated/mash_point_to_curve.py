# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedMASHPointToCurve(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_PointToCurve"

    outputCurves = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurves

    numCurves = LongField(default_value=5)
    nc = numCurves

    curveOffset = DoubleField(default_value=1.0)
    co = curveOffset

    inputPoints = TypedField()
