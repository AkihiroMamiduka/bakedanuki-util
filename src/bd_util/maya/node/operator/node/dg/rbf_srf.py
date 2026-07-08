# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class RbfSrf(DG):
    __slots__ = ()

    NODE_TYPE = "rbfSrf"

    primarySurface = DataNurbsSurfaceField()
    ps = primarySurface

    secondarySurface = DataNurbsSurfaceField()
    ss = secondarySurface

    primaryRadius = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    pr = primaryRadius

    secondaryRadius = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    sr = secondaryRadius

    positionTolerance = DoubleField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=0.1)
    pt = positionTolerance

    tangentTolerance = DoubleField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=0.1)
    tt = tangentTolerance

    outputSurface = DataNurbsSurfaceField(multi=True, writable=False)
    os = outputSurface

    trimCurveOnPrimary = DataNurbsCurveField(multi=True, writable=False)
    tcp = trimCurveOnPrimary

    trimCurveOnSecondary = DataNurbsCurveField(multi=True, writable=False)
    tcs = trimCurveOnSecondary
