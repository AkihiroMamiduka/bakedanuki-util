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

    primaryRadius = DoubleLinearField()
    pr = primaryRadius

    secondaryRadius = DoubleLinearField()
    sr = secondaryRadius

    positionTolerance = DoubleField()
    pt = positionTolerance

    tangentTolerance = DoubleField()
    tt = tangentTolerance

    outputSurface = DataNurbsSurfaceField(multi=True)
    os = outputSurface

    trimCurveOnPrimary = DataNurbsCurveField(multi=True)
    tcp = trimCurveOnPrimary

    trimCurveOnSecondary = DataNurbsCurveField(multi=True)
    tcs = trimCurveOnSecondary
