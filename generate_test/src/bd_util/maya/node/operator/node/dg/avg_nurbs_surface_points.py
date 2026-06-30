# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.avg_nurbs_surface_points import (
    ResultField,
    SurfacePointField,
)


class AvgNurbsSurfacePoints(DG):
    __slots__ = ()

    NODE_TYPE = "avgNurbsSurfacePoints"

    surfacePoint = SurfacePointField(multi=True)
    sp = surfacePoint

    result = ResultField()
    r = result
    position = result.position
    p = position
    normal = result.normal
    n = normal
