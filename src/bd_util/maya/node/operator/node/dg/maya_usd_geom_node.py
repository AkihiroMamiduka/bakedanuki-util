# coding: utf-8
from ._core import DG
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class MayaUsdGeomNode(DG):
    __slots__ = ()

    NODE_TYPE = "mayaUsdGeomNode"

    filePath = DataStringField()
    fp = filePath

    rootPrim = DataStringField()
    rp = rootPrim

    geometry = DataMeshField(multi=True)
    geo = geometry

    matrix = DataMatrixField(multi=True)
    tra = matrix
