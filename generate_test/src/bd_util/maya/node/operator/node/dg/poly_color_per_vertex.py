# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_color_per_vertex import ColorPerVertexField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class RepresentationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class RepresentationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4

    NAME_MAP = {
        A: "A",
        LA: "LA",
        RGB: "RGB",
        RGBA: "RGBA",
    }


class RepresentationEnumField(
    EnumField[RepresentationEnumAttrOperator, RepresentationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepresentationEnumAttrOperator
    PLUG_CLS = RepresentationEnumPlugOperator


class PolyColorPerVertex(DG):
    __slots__ = ()

    NODE_TYPE = "polyColorPerVertex"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    colorPerVertex = ColorPerVertexField()
    cpvx = colorPerVertex
    vertexColor = colorPerVertex.vertexColor
    vclr = vertexColor

    # TODO: vertexColor.vertexColorRGB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexAlpha (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor.vertexFaceColorRGB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor.vertexFaceColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor.vertexFaceColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor.vertexFaceColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexColor.vertexFaceColor.vertexFaceAlpha (attributeType=None, dataType=None) は未対応のため手動で追加してください

    colorSetName = DataStringField()
    cn = colorSetName

    clamped = BoolField()
    clam = clamped

    representation = RepresentationEnumField()
    rprt = representation
