# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedFfFilletSrf(DG):
    __slots__ = ()

    NODE_TYPE = "ffFilletSrf"

    leftCurve = DataNurbsCurveField()
    lc = leftCurve

    rightCurve = DataNurbsCurveField()
    rc = rightCurve

    positionTolerance = DoubleField(default_value=0.1, soft_min_value=0.0001, soft_max_value=0.1)
    pt = positionTolerance

    tangentTolerance = DoubleField(default_value=0.1, soft_min_value=0.0001, soft_max_value=0.1)
    tt = tangentTolerance

    depth = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    d = depth

    bias = DoubleField(default_value=0.5, min_value=-1.0, max_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    b = bias

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
