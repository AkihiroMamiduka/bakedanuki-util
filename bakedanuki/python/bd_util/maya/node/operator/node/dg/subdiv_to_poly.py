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

    inSubdiv = TypedField(readable=False)
    i = inSubdiv

    outMesh = DataMeshField(writable=False)
    o = outMesh

    format = FormatEnumField(default_value=0)
    f = format

    polygonType = PolygonTypeEnumField(default_value=2)
    pt = polygonType

    extractPointPosition = BoolField(default_value=False)
    epp = extractPointPosition

    sampleCount = LongField(default_value=1, min_value=1, max_value=20, soft_min_value=1, soft_max_value=12)
    sc = sampleCount

    depth = LongField(default_value=0, min_value=0, max_value=12, soft_min_value=0, soft_max_value=12)
    d = depth

    maxPolys = LongField(default_value=0, min_value=0)
    mp = maxPolys

    subdNormals = BoolField(default_value=False)
    un = subdNormals

    copyUVTopology = BoolField(default_value=False)
    cut = copyUVTopology

    shareUVs = BoolField(default_value=False)
    suv = shareUVs

    level = LongField(default_value=0, min_value=0, max_value=12, soft_min_value=0, soft_max_value=12)
    l = level

    convertComp = BoolField(default_value=False)
    cc = convertComp

    outSubdCVId = OutSubdCVIdField(multi=True, default_value=(0, 0))
    os = outSubdCVId

    inSubdCVId = InSubdCVIdField(multi=True, default_value=(0, 0))
    is_ = inSubdCVId

    preserveVertexOrdering = BoolField(default_value=True)
    pvo = preserveVertexOrdering

    outv = LongField(multi=True, default_value=0)
    ov = outv

    applyMatrixToResult = BoolField(default_value=True)
    amr = applyMatrixToResult
