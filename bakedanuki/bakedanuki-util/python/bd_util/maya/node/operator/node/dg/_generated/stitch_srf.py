# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.stitch_srf import (
    CvPositionField,
    NormalField,
    PositionField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedStitchSrf(DG):
    __slots__ = ()

    NODE_TYPE = "stitchSrf"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    inputCurve = DataNurbsCurveField(multi=True)
    ic = inputCurve

    inputMatchCurve = DataNurbsCurveField(multi=True)
    imc = inputMatchCurve

    inputReferenceCOS = DataNurbsCurveField(multi=True)
    ir = inputReferenceCOS

    positionalContinuity = BoolField(multi=True, default_value=True)
    pc = positionalContinuity

    tangentialContinuity = BoolField(multi=True, default_value=False)
    tc = tangentialContinuity

    toggleTolerance = BoolField(multi=True, default_value=False)
    tt = toggleTolerance

    tolerance = DoubleLinearField(multi=True, default_value=0.1, soft_min_value=0.0001, soft_max_value=0.1)
    tol = tolerance

    stepCount = LongField(multi=True, default_value=20, min_value=6)
    sc = stepCount

    parameterU = DoubleField(multi=True, default_value=-10000.0)
    u = parameterU

    parameterV = DoubleField(multi=True, default_value=-10000.0)
    v = parameterV

    position = PositionField(multi=True, default_value=(0.0, 0.0, 0.0))
    p = position

    normal = NormalField(multi=True, default_value=(0.0, 0.0, 0.0))
    n = normal

    togglePointNormals = BoolField(default_value=False)
    tpn = togglePointNormals

    togglePointPosition = BoolField(default_value=True)
    tpp = togglePointPosition

    cvIthIndex = LongField(multi=True, default_value=-1)
    ci = cvIthIndex

    cvJthIndex = LongField(multi=True, default_value=-1)
    cj = cvJthIndex

    cvPosition = CvPositionField(multi=True, default_value=(-1.0, -1.0, -1.0))
    cv = cvPosition

    bias = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    b = bias

    fixBoundary = BoolField(default_value=False)
    fb = fixBoundary

    shouldBeLast = BoolField(default_value=True, writable=False)
    sbl = shouldBeLast

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
