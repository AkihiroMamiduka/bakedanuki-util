# coding: utf-8
from ._core import DG
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField


class DeleteComponent(DG):
    __slots__ = ()

    NODE_TYPE = "deleteComponent"

    inputGeometry = GenericField()
    ig = inputGeometry

    deleteComponents = TypedField()
    dc = deleteComponents

    outputGeometry = GenericField()
    og = outputGeometry

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap
