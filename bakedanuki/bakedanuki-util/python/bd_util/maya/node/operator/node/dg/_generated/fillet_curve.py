# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class _GeneratedFilletCurve(DG):
    __slots__ = ()

    NODE_TYPE = "filletCurve"

    primaryCurve = DataNurbsCurveField()
    pc = primaryCurve

    secondaryCurve = DataNurbsCurveField()
    sc = secondaryCurve

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    detachedCurve1 = DataNurbsCurveField(writable=False)
    dc1 = detachedCurve1

    detachedCurve2 = DataNurbsCurveField(writable=False)
    dc2 = detachedCurve2

    radius = DoubleLinearField(default_value=1.0)
    r = radius

    depth = DoubleLinearField(default_value=0.5, min_value=0.0, max_value=1.0)
    d = depth

    bias = DoubleLinearField(default_value=0.0, min_value=-1.0, max_value=1.0)
    b = bias

    curveParameter1 = DoubleField(default_value=0.0)
    cp1 = curveParameter1

    curveParameter2 = DoubleField(default_value=0.0)
    cp2 = curveParameter2

    trim = BoolField(default_value=False)
    t = trim

    join = BoolField(default_value=False)
    jn = join

    circular = BoolField(default_value=True)
    cir = circular

    freeformBlend = BoolField(default_value=False)
    fb = freeformBlend

    blendControl = BoolField(default_value=False)
    bc = blendControl
