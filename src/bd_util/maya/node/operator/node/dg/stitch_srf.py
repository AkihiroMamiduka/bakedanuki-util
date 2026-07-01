# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.stitch_srf import (
    CvPositionField,
    NormalField,
    PositionField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class StitchSrf(DG):
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

    positionalContinuity = BoolField(multi=True)
    pc = positionalContinuity

    tangentialContinuity = BoolField(multi=True)
    tc = tangentialContinuity

    toggleTolerance = BoolField(multi=True)
    tt = toggleTolerance

    tolerance = DoubleLinearField(multi=True)
    tol = tolerance

    stepCount = LongField(multi=True)
    sc = stepCount

    parameterU = DoubleField(multi=True)
    u = parameterU

    parameterV = DoubleField(multi=True)
    v = parameterV

    position = PositionField(multi=True)
    p = position

    normal = NormalField(multi=True)
    n = normal

    togglePointNormals = BoolField()
    tpn = togglePointNormals

    togglePointPosition = BoolField()
    tpp = togglePointPosition

    cvIthIndex = LongField(multi=True)
    ci = cvIthIndex

    cvJthIndex = LongField(multi=True)
    cj = cvJthIndex

    cvPosition = CvPositionField(multi=True)
    cv = cvPosition

    bias = DoubleField()
    b = bias

    fixBoundary = BoolField()
    fb = fixBoundary

    shouldBeLast = BoolField()
    sbl = shouldBeLast

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
