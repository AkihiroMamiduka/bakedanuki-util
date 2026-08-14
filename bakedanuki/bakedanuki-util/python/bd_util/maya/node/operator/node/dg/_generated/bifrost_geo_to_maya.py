# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class GeneratedBifrostGeoToMaya(DG):
    __slots__ = ()

    NODE_TYPE = "bifrostGeoToMaya"

    transferNormals = BoolField(default_value=False)
    tn = transferNormals

    properties = DataStringField()
    pr = properties

    bifrostGeo = TypedField()
    bg = bifrostGeo

    componentTags = DataStringField()
    ct = componentTags

    mayaMesh = DataMeshField(multi=True, writable=False)
    mm = mayaMesh
