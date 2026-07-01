# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.surface_info import ControlPointsField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SurfaceInfo(DG):
    __slots__ = ()

    NODE_TYPE = "surfaceInfo"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    controlPoints = ControlPointsField(multi=True)
    cp = controlPoints

    weights = DoubleField(multi=True)
    wt = weights

    knotsU = DoubleField(multi=True)
    ku = knotsU

    knotsV = DoubleField(multi=True)
    kv = knotsV
