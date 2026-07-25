# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_color_per_vertex import ColorPerVertexField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field
from ....attr.define.std.at.compound import CompoundField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedPolyColorPerVertex(DG):
    __slots__ = ()

    NODE_TYPE = "polyColorPerVertex"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    colorPerVertex = ColorPerVertexField()
    cpvx = colorPerVertex
    vertexColor = colorPerVertex.vertexColor
    vclr = vertexColor

    vertexColorRGB = Float3Field()
    vrgb = vertexColorRGB

    vertexColorR = FloatField()
    vxcr = vertexColorR

    vertexColorG = FloatField()
    vxcg = vertexColorG

    vertexColorB = FloatField()
    vxcb = vertexColorB

    vertexAlpha = FloatField()
    vxal = vertexAlpha

    vertexFaceColor = CompoundField()
    vfcl = vertexFaceColor

    vertexFaceColorRGB = Float3Field()
    frgb = vertexFaceColorRGB

    vertexFaceColorR = FloatField()
    vfcr = vertexFaceColorR

    vertexFaceColorG = FloatField()
    vfcg = vertexFaceColorG

    vertexFaceColorB = FloatField()
    vfcb = vertexFaceColorB

    vertexFaceAlpha = FloatField()
    vfal = vertexFaceAlpha

    colorSetName = DataStringField()
    cn = colorSetName

    clamped = BoolField(default_value=True)
    clam = clamped

    representation = RepresentationEnumField(default_value=4)
    rprt = representation
