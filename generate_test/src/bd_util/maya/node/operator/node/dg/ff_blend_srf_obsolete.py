# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class FfBlendSrfObsolete(DG):
    __slots__ = ()

    NODE_TYPE = "ffBlendSrfObsolete"

    leftCurve = DataNurbsCurveField(multi=True)
    lc = leftCurve

    rightCurve = DataNurbsCurveField(multi=True)
    rc = rightCurve

    positionTolerance = DoubleField()
    pt = positionTolerance

    tangentTolerance = DoubleField()
    tt = tangentTolerance

    flipLeft = BoolField()
    fl = flipLeft

    flipRight = BoolField()
    fr = flipRight

    autoDirection = BoolField()
    ad = autoDirection

    leftRail = DataNurbsCurveField()
    lr = leftRail

    rightRail = DataNurbsCurveField()
    rr = rightRail

    leftParameter = DoubleField()
    lp = leftParameter

    rightParameter = DoubleField()
    rp = rightParameter

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    multipleKnots = BoolField()
    mk = multipleKnots
