# coding: utf-8
from ._core import DG
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class Untrim(DG):
    __slots__ = ()

    NODE_TYPE = "untrim"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve
