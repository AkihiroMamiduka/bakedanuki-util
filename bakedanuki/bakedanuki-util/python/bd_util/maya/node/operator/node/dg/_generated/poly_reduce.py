# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.custom import Double4Field
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class VersionEnumPlugOperator(EnumPlugOperator["VersionEnumAttrOperator"]):
    __slots__ = ()

    MAYA = 0
    SOFTIMAGE = 1


class VersionEnumAttrOperator(EnumAttrOperator[VersionEnumPlugOperator]):
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


class TerminationEnumPlugOperator(
    EnumPlugOperator["TerminationEnumAttrOperator"]
):
    __slots__ = ()

    PERCENTAGE = 0
    VERTEX_COUNT = 1
    TRIANGLE_COUNT = 2


class TerminationEnumAttrOperator(
    EnumAttrOperator[TerminationEnumPlugOperator]
):
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


class UseVirtualSymmetryEnumPlugOperator(
    EnumPlugOperator["UseVirtualSymmetryEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    AUTOMATIC = 1
    PLANE = 2


class UseVirtualSymmetryEnumAttrOperator(
    EnumAttrOperator[UseVirtualSymmetryEnumPlugOperator]
):
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
    EnumField[
        UseVirtualSymmetryEnumAttrOperator, UseVirtualSymmetryEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UseVirtualSymmetryEnumAttrOperator
    PLUG_CLS = UseVirtualSymmetryEnumPlugOperator


class GeneratedPolyReduce(DG):
    __slots__ = ()

    NODE_TYPE = "polyReduce"

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

    percentageAchieved = DoubleField(
        default_value=0.0, min_value=0.0, max_value=100.0, writable=False
    )
    pa = percentageAchieved

    vertexCountAchieved = LongField(
        default_value=0, min_value=0, writable=False
    )
    va = vertexCountAchieved

    triangleCountAchieved = LongField(
        default_value=0, min_value=0, writable=False
    )
    ta = triangleCountAchieved

    vertexCountIn = LongField(default_value=0, min_value=0, writable=False)
    ivc = vertexCountIn

    triangleCountIn = LongField(default_value=0, min_value=0, writable=False)
    itc = triangleCountIn

    version = VersionEnumField(default_value=0)
    ver = version

    termination = TerminationEnumField(default_value=0)
    trm = termination

    percentage = DoubleField(default_value=0.0, min_value=0.0, max_value=100.0)
    p = percentage

    vertexCount = LongField(default_value=0, min_value=0)
    vct = vertexCount

    triangleCount = LongField(default_value=0, min_value=0)
    tct = triangleCount

    preserveTopology = BoolField(default_value=True)
    top = preserveTopology

    vertexMapName = DataStringField()
    vmp = vertexMapName

    sharpness = DoubleField(default_value=0.0)
    shp = sharpness

    invertVertexWeights = BoolField(default_value=True)
    iwt = invertVertexWeights

    vertexWeightCoefficient = DoubleField(default_value=1.0, min_value=0.0)
    vwc = vertexWeightCoefficient

    useVirtualSymmetry = UseVirtualSymmetryEnumField(default_value=0)
    uvs = useVirtualSymmetry

    symmetryPlane = Double4Field(default_value=(0.0, 0.0, 0.0, 0.0))
    sym = symmetryPlane

    symmetryTolerance = DoubleField(default_value=0.0, min_value=0.0)
    stl = symmetryTolerance

    keepBorder = BoolField(default_value=True)
    kb = keepBorder

    keepBorderWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    kbw = keepBorderWeight

    keepMapBorder = BoolField(default_value=True)
    kmb = keepMapBorder

    keepMapBorderWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    kmw = keepMapBorderWeight

    keepColorBorder = BoolField(default_value=True)
    kcb = keepColorBorder

    keepColorBorderWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    kcw = keepColorBorderWeight

    keepFaceGroupBorder = BoolField(default_value=True)
    kfb = keepFaceGroupBorder

    keepFaceGroupBorderWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    kfw = keepFaceGroupBorderWeight

    keepHardEdge = BoolField(default_value=True)
    khe = keepHardEdge

    keepHardEdgeWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    khw = keepHardEdgeWeight

    keepCreaseEdge = BoolField(default_value=True)
    kce = keepCreaseEdge

    keepCreaseEdgeWeight = DoubleField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cew = keepCreaseEdgeWeight

    keepQuadsWeight = DoubleField(
        default_value=0.0, min_value=0.0, max_value=10.0, soft_max_value=1.0
    )
    kqw = keepQuadsWeight

    vertexWeights = DataDoubleArrayField()
    vwt = vertexWeights

    cachingReduce = BoolField(default_value=False)
    cr = cachingReduce

    compactness = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    com = compactness

    geomWeights = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    gwt = geomWeights

    uvWeights = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    uwt = uvWeights

    colorWeights = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    cwt = colorWeights

    weightCoefficient = DoubleField(default_value=10000.0, min_value=1.0)
    wc = weightCoefficient

    keepOriginalVertices = BoolField(default_value=False)
    kev = keepOriginalVertices

    triangulate = BoolField(default_value=True)
    t = triangulate

    border = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    b = border

    line = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    l = line

    detail = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    d = detail

    weights = DoubleField(
        multi=True, default_value=0.0, min_value=0.0, max_value=1.0
    )
    wts = weights
