# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class MethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EXPONENTIAL = 0
    LINEAR = 1


class MethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EXPONENTIAL = 0
    LINEAR = 1

    NAME_MAP = {
        EXPONENTIAL: "Exponential",
        LINEAR: "Linear",
    }


class MethodEnumField(
    EnumField[MethodEnumAttrOperator, MethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MethodEnumAttrOperator
    PLUG_CLS = MethodEnumPlugOperator


class SubdivisionTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MAYA_CATMULL_MINUS_CLARK = 0
    OPENSUBDIV_CATMULL_MINUS_CLARK = 2
    OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE = 3


class SubdivisionTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MAYA_CATMULL_MINUS_CLARK = 0
    OPENSUBDIV_CATMULL_MINUS_CLARK = 2
    OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE = 3

    NAME_MAP = {
        MAYA_CATMULL_MINUS_CLARK: "Maya Catmull-Clark",
        OPENSUBDIV_CATMULL_MINUS_CLARK: "OpenSubdiv Catmull-Clark",
        OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE: "OpenSubdiv Catmull-Clark Adaptive",
    }


class SubdivisionTypeEnumField(
    EnumField[SubdivisionTypeEnumAttrOperator, SubdivisionTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubdivisionTypeEnumAttrOperator
    PLUG_CLS = SubdivisionTypeEnumPlugOperator


class OsdVertBoundaryEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHARP_EDGES_AND_CORNERS = 1
    SHARP_EDGES = 2


class OsdVertBoundaryEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SHARP_EDGES_AND_CORNERS = 1
    SHARP_EDGES = 2

    NAME_MAP = {
        SHARP_EDGES_AND_CORNERS: "Sharp edges and corners",
        SHARP_EDGES: "Sharp edges",
    }


class OsdVertBoundaryEnumField(
    EnumField[OsdVertBoundaryEnumAttrOperator, OsdVertBoundaryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdVertBoundaryEnumAttrOperator
    PLUG_CLS = OsdVertBoundaryEnumPlugOperator


class OsdFvarBoundaryEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PRESERVE_EDGES_AND_CORNERS = 1
    PRESERVE_EDGES = 2
    MAYA_CATMULL_MINUS_CLARK = 3


class OsdFvarBoundaryEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    PRESERVE_EDGES_AND_CORNERS = 1
    PRESERVE_EDGES = 2
    MAYA_CATMULL_MINUS_CLARK = 3

    NAME_MAP = {
        NONE: "None",
        PRESERVE_EDGES_AND_CORNERS: "Preserve Edges and Corners",
        PRESERVE_EDGES: "Preserve Edges",
        MAYA_CATMULL_MINUS_CLARK: "Maya Catmull-Clark",
    }


class OsdFvarBoundaryEnumField(
    EnumField[OsdFvarBoundaryEnumAttrOperator, OsdFvarBoundaryEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdFvarBoundaryEnumAttrOperator
    PLUG_CLS = OsdFvarBoundaryEnumPlugOperator


class OsdCreaseMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    CHAIKIN = 1


class OsdCreaseMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    CHAIKIN = 1

    NAME_MAP = {
        NORMAL: "Normal",
        CHAIKIN: "Chaikin",
    }


class OsdCreaseMethodEnumField(
    EnumField[OsdCreaseMethodEnumAttrOperator, OsdCreaseMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OsdCreaseMethodEnumAttrOperator
    PLUG_CLS = OsdCreaseMethodEnumPlugOperator


class BoundaryRuleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2


class BoundaryRuleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2

    NAME_MAP = {
        LEGACY: "Legacy",
        CREASE_ALL: "Crease All",
        CREASE_EDGES: "Crease Edges",
    }


class BoundaryRuleEnumField(
    EnumField[BoundaryRuleEnumAttrOperator, BoundaryRuleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundaryRuleEnumAttrOperator
    PLUG_CLS = BoundaryRuleEnumPlugOperator


class KeepMapBordersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2


class KeepMapBordersEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2

    NAME_MAP = {
        NONE: "None",
        INTERNAL: "Internal",
        ALL: "All",
    }


class KeepMapBordersEnumField(
    EnumField[KeepMapBordersEnumAttrOperator, KeepMapBordersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeepMapBordersEnumAttrOperator
    PLUG_CLS = KeepMapBordersEnumPlugOperator


class PolySmoothFace(DG):
    __slots__ = ()

    NODE_TYPE = "polySmoothFace"

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

    method = MethodEnumField()
    mth = method

    subdivisionType = SubdivisionTypeEnumField()
    sdt = subdivisionType

    useOsdBoundaryMethods = BoolField()
    uob = useOsdBoundaryMethods

    osdVertBoundary = OsdVertBoundaryEnumField()
    ovb = osdVertBoundary

    osdFvarBoundary = OsdFvarBoundaryEnumField()
    ofb = osdFvarBoundary

    osdFvarPropagateCorners = BoolField()
    ofc = osdFvarPropagateCorners

    osdSmoothTriangles = BoolField()
    ost = osdSmoothTriangles

    osdCreaseMethod = OsdCreaseMethodEnumField()
    ocr = osdCreaseMethod

    osdIndependentUVChannels = BoolField()
    iuv = osdIndependentUVChannels

    continuity = FloatField()
    c = continuity

    divisions = ShortField()
    dv = divisions

    smoothUVs = BoolField()
    suv = smoothUVs

    keepBorder = BoolField()
    kb = keepBorder

    keepSelectionBorder = BoolField()
    ksb = keepSelectionBorder

    boundaryRule = BoundaryRuleEnumField()
    bnr = boundaryRule

    keepHardEdge = BoolField()
    khe = keepHardEdge

    propagateEdgeHardness = BoolField()
    peh = propagateEdgeHardness

    keepMapBorders = KeepMapBordersEnumField()
    kmb = keepMapBorders

    keepTessellation = BoolField()
    kt = keepTessellation

    subdivisionLevels = LongField()
    sl = subdivisionLevels

    divisionsPerEdge = LongField()
    dpe = divisionsPerEdge

    degree = LongField()
    deg = degree

    pushStrength = FloatField()
    ps = pushStrength

    roundness = FloatField()
    ro = roundness

    maya65Above = BoolField()
    ma = maya65Above

    maya2008Above = BoolField()
    m08 = maya2008Above

    orderVerticesFromFacesFirst = BoolField()
    ovf = orderVerticesFromFacesFirst
