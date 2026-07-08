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

    controlPoints = ControlPointsField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    cp = controlPoints

    weights = DoubleField(multi=True, default_value=1.0, writable=False)
    wt = weights

    knotsU = DoubleField(multi=True, default_value=0.0, writable=False)
    ku = knotsU

    knotsV = DoubleField(multi=True, default_value=0.0, writable=False)
    kv = knotsV
