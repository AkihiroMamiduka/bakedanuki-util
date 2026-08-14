# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.point_on_surface_info import ResultField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedPointOnSurfaceInfo(DG):
    __slots__ = ()

    NODE_TYPE = "pointOnSurfaceInfo"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    parameterU = DoubleField(default_value=0.0)
    u = parameterU

    parameterV = DoubleField(default_value=0.0)
    v = parameterV

    turnOnPercentage = BoolField(default_value=False)
    top = turnOnPercentage

    result = ResultField(writable=False)
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
