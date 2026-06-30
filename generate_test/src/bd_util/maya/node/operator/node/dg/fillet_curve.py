# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class FilletCurve(DG):
    __slots__ = ()

    NODE_TYPE = "filletCurve"

    primaryCurve = DataNurbsCurveField()
    pc = primaryCurve

    secondaryCurve = DataNurbsCurveField()
    sc = secondaryCurve

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    detachedCurve1 = DataNurbsCurveField()
    dc1 = detachedCurve1

    detachedCurve2 = DataNurbsCurveField()
    dc2 = detachedCurve2

    radius = DoubleLinearField()
    r = radius

    depth = DoubleLinearField()
    d = depth

    bias = DoubleLinearField()
    b = bias

    curveParameter1 = DoubleField()
    cp1 = curveParameter1

    curveParameter2 = DoubleField()
    cp2 = curveParameter2

    trim = BoolField()
    t = trim

    join = BoolField()
    jn = join

    circular = BoolField()
    cir = circular

    freeformBlend = BoolField()
    fb = freeformBlend

    blendControl = BoolField()
    bc = blendControl
