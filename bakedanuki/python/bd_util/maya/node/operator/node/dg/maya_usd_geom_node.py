# coding: utf-8
from ._core import DG
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class MayaUsdGeomNode(DG):
    __slots__ = ()

    NODE_TYPE = "mayaUsdGeomNode"

    filePath = DataStringField(readable=False)
    fp = filePath

    rootPrim = DataStringField(readable=False)
    rp = rootPrim

    geometry = DataMeshField(multi=True, writable=False)
    geo = geometry

    matrix = DataMatrixField(multi=True, writable=False)
    tra = matrix
