# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.closest_point_on_surface import (
    InPositionField,
    ResultField,
)
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedClosestPointOnSurface(DG):
    __slots__ = ()

    NODE_TYPE = "closestPointOnSurface"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    inPosition = InPositionField(default_value=(0.0, 0.0, 0.0))
    ip = inPosition
    inPositionX = inPosition.inPositionX
    ipx = inPositionX
    inPositionY = inPosition.inPositionY
    ipy = inPositionY
    inPositionZ = inPosition.inPositionZ
    ipz = inPositionZ

    result = ResultField(writable=False)
    r = result
    position = result.position
    p = position
    parameterU = result.parameterU
    u = parameterU
    parameterV = result.parameterV
    v = parameterV
