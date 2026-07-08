# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class ObjectGrpToComp(DG):
    __slots__ = ()

    NODE_TYPE = "objectGrpToComp"

    outComponents = TypedField(multi=True)

    outputMesh = DataMeshField()

    inputMesh = DataMeshField()

    generatePlanarUVs = BoolField(default_value=True)
