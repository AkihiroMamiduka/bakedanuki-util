# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.avg_surface_points import ResultField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class AvgSurfacePoints(DG):
    __slots__ = ()

    NODE_TYPE = "avgSurfacePoints"

    inputSurfaces = DataNurbsSurfaceField(multi=True)
    is_ = inputSurfaces

    weight = DoubleField(multi=True)
    wt = weight

    parameterU = DoubleField(multi=True)
    u = parameterU

    parameterV = DoubleField(multi=True)
    v = parameterV

    turnOnPercentage = BoolField()
    top = turnOnPercentage

    result = ResultField()
    r = result
    position = result.position
    p = position
    normal = result.normal
    n = normal
