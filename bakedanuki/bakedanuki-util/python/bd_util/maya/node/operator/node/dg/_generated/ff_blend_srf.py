# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedFfBlendSrf(DG):
    __slots__ = ()

    NODE_TYPE = "ffBlendSrf"

    leftCurve = DataNurbsCurveField(multi=True)
    lc = leftCurve

    rightCurve = DataNurbsCurveField(multi=True)
    rc = rightCurve

    leftRail = DataNurbsCurveField()
    lr = leftRail

    rightRail = DataNurbsCurveField()
    rr = rightRail

    multipleKnots = BoolField(default_value=True)
    mk = multipleKnots

    positionTolerance = DoubleField(default_value=0.1, min_value=1e-05, soft_min_value=0.0001, soft_max_value=0.1)
    pt = positionTolerance

    tangentTolerance = DoubleField(default_value=0.1, min_value=1e-05, soft_min_value=0.0001, soft_max_value=0.1)
    tt = tangentTolerance

    autoNormal = BoolField(default_value=True)
    an = autoNormal

    flipLeftNormal = BoolField(default_value=False)
    fln = flipLeftNormal

    flipRightNormal = BoolField(default_value=False)
    frn = flipRightNormal

    autoAnchor = BoolField(default_value=True)
    aa = autoAnchor

    leftAnchor = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    la = leftAnchor

    leftStart = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    ls = leftStart

    leftEnd = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    le = leftEnd

    reverseLeft = BoolField(default_value=False)
    rvl = reverseLeft

    rightAnchor = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    ra = rightAnchor

    rightStart = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    rs = rightStart

    rightEnd = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    re = rightEnd

    reverseRight = BoolField(default_value=False)
    rvr = reverseRight

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
