# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.point_on_surface_info import ResultField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class PointOnSurfaceInfo(DG):
    __slots__ = ()

    NODE_TYPE = "pointOnSurfaceInfo"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    parameterU = DoubleField()
    u = parameterU

    parameterV = DoubleField()
    v = parameterV

    turnOnPercentage = BoolField()
    top = turnOnPercentage

    result = ResultField()
    r = result
    position = result.position
    p = position
    normal = result.normal
    n = normal
    normalizedNormal = result.normalizedNormal
    nn = normalizedNormal
    tangentU = result.tangentU
    tu = tangentU
    normalizedTangentU = result.normalizedTangentU
    ntu = normalizedTangentU
    tangentV = result.tangentV
    tv = tangentV
    normalizedTangentV = result.normalizedTangentV
    ntv = normalizedTangentV
