# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4 import Double4Field
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class VersionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MAYA = 0
    SOFTIMAGE = 1


class VersionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MAYA = 0
    SOFTIMAGE = 1

    NAME_MAP = {
        MAYA: "Maya",
        SOFTIMAGE: "Softimage",
    }


class VersionEnumField(
    EnumField[VersionEnumAttrOperator, VersionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VersionEnumAttrOperator
    PLUG_CLS = VersionEnumPlugOperator


class TerminationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERCENTAGE = 0
    VERTEX_COUNT = 1
    TRIANGLE_COUNT = 2


class TerminationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERCENTAGE = 0
    VERTEX_COUNT = 1
    TRIANGLE_COUNT = 2

    NAME_MAP = {
        PERCENTAGE: "Percentage",
        VERTEX_COUNT: "Vertex Count",
        TRIANGLE_COUNT: "Triangle Count",
    }


class TerminationEnumField(
    EnumField[TerminationEnumAttrOperator, TerminationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TerminationEnumAttrOperator
    PLUG_CLS = TerminationEnumPlugOperator


class UseVirtualSymmetryEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    AUTOMATIC = 1
    PLANE = 2


class UseVirtualSymmetryEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    AUTOMATIC = 1
    PLANE = 2

    NAME_MAP = {
        NONE: "None",
        AUTOMATIC: "Automatic",
        PLANE: "Plane",
    }


class UseVirtualSymmetryEnumField(
    EnumField[UseVirtualSymmetryEnumAttrOperator, UseVirtualSymmetryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseVirtualSymmetryEnumAttrOperator
    PLUG_CLS = UseVirtualSymmetryEnumPlugOperator


class PolyReduce(DG):
    __slots__ = ()

    NODE_TYPE = "polyReduce"

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

    percentageAchieved = DoubleField()
    pa = percentageAchieved

    vertexCountAchieved = LongField()
    va = vertexCountAchieved

    triangleCountAchieved = LongField()
    ta = triangleCountAchieved

    vertexCountIn = LongField()
    ivc = vertexCountIn

    triangleCountIn = LongField()
    itc = triangleCountIn

    version = VersionEnumField()
    ver = version

    termination = TerminationEnumField()
    trm = termination

    percentage = DoubleField()
    p = percentage

    vertexCount = LongField()
    vct = vertexCount

    triangleCount = LongField()
    tct = triangleCount

    preserveTopology = BoolField()
    top = preserveTopology

    vertexMapName = DataStringField()
    vmp = vertexMapName

    sharpness = DoubleField()
    shp = sharpness

    invertVertexWeights = BoolField()
    iwt = invertVertexWeights

    vertexWeightCoefficient = DoubleField()
    vwc = vertexWeightCoefficient

    useVirtualSymmetry = UseVirtualSymmetryEnumField()
    uvs = useVirtualSymmetry

    symmetryPlane = Double4Field()
    sym = symmetryPlane

    symmetryTolerance = DoubleField()
    stl = symmetryTolerance

    keepBorder = BoolField()
    kb = keepBorder

    keepBorderWeight = DoubleField()
    kbw = keepBorderWeight

    keepMapBorder = BoolField()
    kmb = keepMapBorder

    keepMapBorderWeight = DoubleField()
    kmw = keepMapBorderWeight

    keepColorBorder = BoolField()
    kcb = keepColorBorder

    keepColorBorderWeight = DoubleField()
    kcw = keepColorBorderWeight

    keepFaceGroupBorder = BoolField()
    kfb = keepFaceGroupBorder

    keepFaceGroupBorderWeight = DoubleField()
    kfw = keepFaceGroupBorderWeight

    keepHardEdge = BoolField()
    khe = keepHardEdge

    keepHardEdgeWeight = DoubleField()
    khw = keepHardEdgeWeight

    keepCreaseEdge = BoolField()
    kce = keepCreaseEdge

    keepCreaseEdgeWeight = DoubleField()
    cew = keepCreaseEdgeWeight

    keepQuadsWeight = DoubleField()
    kqw = keepQuadsWeight

    vertexWeights = DataDoubleArrayField()
    vwt = vertexWeights

    cachingReduce = BoolField()
    cr = cachingReduce

    compactness = DoubleField()
    com = compactness

    geomWeights = DoubleField()
    gwt = geomWeights

    uvWeights = DoubleField()
    uwt = uvWeights

    colorWeights = DoubleField()
    cwt = colorWeights

    weightCoefficient = DoubleField()
    wc = weightCoefficient

    keepOriginalVertices = BoolField()
    kev = keepOriginalVertices

    triangulate = BoolField()
    t = triangulate

    border = DoubleField()
    b = border

    line = DoubleField()
    l = line

    detail = DoubleField()
    d = detail

    weights = DoubleField(multi=True)
    wts = weights
