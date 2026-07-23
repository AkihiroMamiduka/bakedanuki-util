# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class _GeneratedDeleteComponent(DG):
    __slots__ = ()

    NODE_TYPE = "deleteComponent"

    inputGeometry = GenericField()
    ig = inputGeometry

    deleteComponents = TypedField()
    dc = deleteComponents

    outputGeometry = GenericField(writable=False)
    og = outputGeometry

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap
