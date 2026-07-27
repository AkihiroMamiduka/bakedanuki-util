# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedFfBlendSrfObsolete(DG):
    __slots__ = ()

    NODE_TYPE = "ffBlendSrfObsolete"

    leftCurve = DataNurbsCurveField(multi=True)
    lc = leftCurve

    rightCurve = DataNurbsCurveField(multi=True)
    rc = rightCurve

    positionTolerance = DoubleField(default_value=0.1, min_value=1e-05, soft_min_value=0.0001, soft_max_value=0.1)
    pt = positionTolerance

    tangentTolerance = DoubleField(default_value=0.1, min_value=1e-05, soft_min_value=0.0001, soft_max_value=0.1)
    tt = tangentTolerance

    flipLeft = BoolField(default_value=False)
    fl = flipLeft

    flipRight = BoolField(default_value=False)
    fr = flipRight

    autoDirection = BoolField(default_value=True)
    ad = autoDirection

    leftRail = DataNurbsCurveField()
    lr = leftRail

    rightRail = DataNurbsCurveField()
    rr = rightRail

    leftParameter = DoubleField(default_value=123456.0, min_value=-123456.0, max_value=123456.0, soft_min_value=-1.0, soft_max_value=1.0)
    lp = leftParameter

    rightParameter = DoubleField(default_value=123456.0, min_value=-123456.0, max_value=123456.0, soft_min_value=-1.0, soft_max_value=1.0)
    rp = rightParameter

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    multipleKnots = BoolField(default_value=True)
    mk = multipleKnots
