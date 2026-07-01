# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class FfBlendSrf(DG):
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

    multipleKnots = BoolField()
    mk = multipleKnots

    positionTolerance = DoubleField()
    pt = positionTolerance

    tangentTolerance = DoubleField()
    tt = tangentTolerance

    autoNormal = BoolField()
    an = autoNormal

    flipLeftNormal = BoolField()
    fln = flipLeftNormal

    flipRightNormal = BoolField()
    frn = flipRightNormal

    autoAnchor = BoolField()
    aa = autoAnchor

    leftAnchor = DoubleField()
    la = leftAnchor

    leftStart = DoubleField()
    ls = leftStart

    leftEnd = DoubleField()
    le = leftEnd

    reverseLeft = BoolField()
    rvl = reverseLeft

    rightAnchor = DoubleField()
    ra = rightAnchor

    rightStart = DoubleField()
    rs = rightStart

    rightEnd = DoubleField()
    re = rightEnd

    reverseRight = BoolField()
    rvr = reverseRight

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
