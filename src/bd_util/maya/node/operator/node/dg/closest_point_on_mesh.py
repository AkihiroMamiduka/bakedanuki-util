# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.closest_point_on_mesh import (
    InPositionField,
    ResultField,
)
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class ClosestPointOnMesh(DG):
    __slots__ = ()

    NODE_TYPE = "closestPointOnMesh"

    inMesh = DataMeshField()
    im = inMesh

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    inPosition = InPositionField()
    ip = inPosition
    inPositionX = inPosition.inPositionX
    ipx = inPositionX
    inPositionY = inPosition.inPositionY
    ipy = inPositionY
    inPositionZ = inPosition.inPositionZ
    ipz = inPositionZ

    result = ResultField()
    r = result
    position = result.position
    p = position
    parameterU = result.parameterU
    u = parameterU
    parameterV = result.parameterV
    v = parameterV
    normal = result.normal
    n = normal
    closestFaceIndex = result.closestFaceIndex
    f = closestFaceIndex
    closestVertexIndex = result.closestVertexIndex
    vt = closestVertexIndex
