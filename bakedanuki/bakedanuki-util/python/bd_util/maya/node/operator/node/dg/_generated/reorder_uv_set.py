# coding: utf-8
from .._core import DG
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class GeneratedReorderUVSet(DG):
    __slots__ = ()

    NODE_TYPE = "reorderUVSet"

    inputGeometry = TypedField()
    ig = inputGeometry

    outputGeometry = TypedField()
    og = outputGeometry

    uvSetName = DataStringField()
    uvs = uvSetName

    uvSetName2 = DataStringField()
    uv2 = uvSetName2
