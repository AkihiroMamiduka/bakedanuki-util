# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class FfFilletSrf(DG):
    __slots__ = ()

    NODE_TYPE = "ffFilletSrf"

    leftCurve = DataNurbsCurveField()
    lc = leftCurve

    rightCurve = DataNurbsCurveField()
    rc = rightCurve

    positionTolerance = DoubleField()
    pt = positionTolerance

    tangentTolerance = DoubleField()
    tt = tangentTolerance

    depth = DoubleField()
    d = depth

    bias = DoubleField()
    b = bias

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
