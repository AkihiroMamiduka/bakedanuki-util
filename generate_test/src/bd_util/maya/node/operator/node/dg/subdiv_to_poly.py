# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subdiv_to_poly import (
    InSubdCVIdField,
    OutSubdCVIdField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class FormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNIFORM = 0
    ADAPTIVE = 1
    POLYGON_COUNT = 2
    VERTICES = 3


class FormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNIFORM = 0
    ADAPTIVE = 1
    POLYGON_COUNT = 2
    VERTICES = 3

    NAME_MAP = {
        UNIFORM: "Uniform",
        ADAPTIVE: "Adaptive",
        POLYGON_COUNT: "Polygon Count",
        VERTICES: "Vertices",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class PolygonTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRIANGLES = 0
    QUADS = 1
    POLYGONS = 2


class PolygonTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRIANGLES = 0
    QUADS = 1
    POLYGONS = 2

    NAME_MAP = {
        TRIANGLES: "triangles",
        QUADS: "quads",
        POLYGONS: "polygons",
    }


class PolygonTypeEnumField(
    EnumField[PolygonTypeEnumAttrOperator, PolygonTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolygonTypeEnumAttrOperator
    PLUG_CLS = PolygonTypeEnumPlugOperator


class SubdivToPoly(DG):
    __slots__ = ()

    NODE_TYPE = "subdivToPoly"

    inSubdiv = TypedField()
    i = inSubdiv

    outMesh = DataMeshField()
    o = outMesh

    format = FormatEnumField()
    f = format

    polygonType = PolygonTypeEnumField()
    pt = polygonType

    extractPointPosition = BoolField()
    epp = extractPointPosition

    sampleCount = LongField()
    sc = sampleCount

    depth = LongField()
    d = depth

    maxPolys = LongField()
    mp = maxPolys

    subdNormals = BoolField()
    un = subdNormals

    copyUVTopology = BoolField()
    cut = copyUVTopology

    shareUVs = BoolField()
    suv = shareUVs

    level = LongField()
    l = level

    convertComp = BoolField()
    cc = convertComp

    outSubdCVId = OutSubdCVIdField(multi=True)
    os = outSubdCVId

    inSubdCVId = InSubdCVIdField(multi=True)
    is_ = inSubdCVId

    preserveVertexOrdering = BoolField()
    pvo = preserveVertexOrdering

    outv = LongField(multi=True)
    ov = outv

    applyMatrixToResult = BoolField()
    amr = applyMatrixToResult
