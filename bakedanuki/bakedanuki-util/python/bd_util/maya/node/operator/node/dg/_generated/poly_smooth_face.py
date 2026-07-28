# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class MethodEnumPlugOperator(EnumPlugOperator["MethodEnumAttrOperator"]):
    __slots__ = ()

    EXPONENTIAL = 0
    LINEAR = 1


class MethodEnumAttrOperator(EnumAttrOperator[MethodEnumPlugOperator]):
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


class SubdivisionTypeEnumPlugOperator(EnumPlugOperator["SubdivisionTypeEnumAttrOperator"]):
    __slots__ = ()

    MAYA_CATMULL_MINUS_CLARK = 0
    OPENSUBDIV_CATMULL_MINUS_CLARK = 2
    OPENSUBDIV_CATMULL_MINUS_CLARK_ADAPTIVE = 3


class SubdivisionTypeEnumAttrOperator(EnumAttrOperator[SubdivisionTypeEnumPlugOperator]):
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


class OsdVertBoundaryEnumPlugOperator(EnumPlugOperator["OsdVertBoundaryEnumAttrOperator"]):
    __slots__ = ()

    SHARP_EDGES_AND_CORNERS = 1
    SHARP_EDGES = 2


class OsdVertBoundaryEnumAttrOperator(EnumAttrOperator[OsdVertBoundaryEnumPlugOperator]):
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


class OsdFvarBoundaryEnumPlugOperator(EnumPlugOperator["OsdFvarBoundaryEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    PRESERVE_EDGES_AND_CORNERS = 1
    PRESERVE_EDGES = 2
    MAYA_CATMULL_MINUS_CLARK = 3


class OsdFvarBoundaryEnumAttrOperator(EnumAttrOperator[OsdFvarBoundaryEnumPlugOperator]):
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


class OsdCreaseMethodEnumPlugOperator(EnumPlugOperator["OsdCreaseMethodEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    CHAIKIN = 1


class OsdCreaseMethodEnumAttrOperator(EnumAttrOperator[OsdCreaseMethodEnumPlugOperator]):
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


class BoundaryRuleEnumPlugOperator(EnumPlugOperator["BoundaryRuleEnumAttrOperator"]):
    __slots__ = ()

    LEGACY = 0
    CREASE_ALL = 1
    CREASE_EDGES = 2


class BoundaryRuleEnumAttrOperator(EnumAttrOperator[BoundaryRuleEnumPlugOperator]):
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


class KeepMapBordersEnumPlugOperator(EnumPlugOperator["KeepMapBordersEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    INTERNAL = 1
    ALL = 2


class KeepMapBordersEnumAttrOperator(EnumAttrOperator[KeepMapBordersEnumPlugOperator]):
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


class GeneratedPolySmoothFace(DG):
    __slots__ = ()

    NODE_TYPE = "polySmoothFace"

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

    method = MethodEnumField(default_value=0)
    mth = method

    subdivisionType = SubdivisionTypeEnumField(default_value=0)
    sdt = subdivisionType

    useOsdBoundaryMethods = BoolField(default_value=True)
    uob = useOsdBoundaryMethods

    osdVertBoundary = OsdVertBoundaryEnumField(default_value=1)
    ovb = osdVertBoundary

    osdFvarBoundary = OsdFvarBoundaryEnumField(default_value=3)
    ofb = osdFvarBoundary

    osdFvarPropagateCorners = BoolField(default_value=False)
    ofc = osdFvarPropagateCorners

    osdSmoothTriangles = BoolField(default_value=False)
    ost = osdSmoothTriangles

    osdCreaseMethod = OsdCreaseMethodEnumField(default_value=0)
    ocr = osdCreaseMethod

    osdIndependentUVChannels = BoolField(default_value=True)
    iuv = osdIndependentUVChannels

    continuity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c = continuity

    divisions = ShortField(default_value=1, min_value=0, max_value=15, soft_min_value=0, soft_max_value=4)
    dv = divisions

    smoothUVs = BoolField(default_value=False)
    suv = smoothUVs

    keepBorder = BoolField(default_value=True)
    kb = keepBorder

    keepSelectionBorder = BoolField(default_value=True)
    ksb = keepSelectionBorder

    boundaryRule = BoundaryRuleEnumField(default_value=1)
    bnr = boundaryRule

    keepHardEdge = BoolField(default_value=False)
    khe = keepHardEdge

    propagateEdgeHardness = BoolField(default_value=False)
    peh = propagateEdgeHardness

    keepMapBorders = KeepMapBordersEnumField(default_value=1)
    kmb = keepMapBorders

    keepTessellation = BoolField(default_value=True)
    kt = keepTessellation

    subdivisionLevels = LongField(default_value=1, min_value=0, max_value=10, soft_min_value=0, soft_max_value=4)
    sl = subdivisionLevels

    divisionsPerEdge = LongField(default_value=1, min_value=0, max_value=10, soft_min_value=0, soft_max_value=4)
    dpe = divisionsPerEdge

    degree = LongField(default_value=3)
    deg = degree

    pushStrength = FloatField(default_value=0.0, min_value=-1.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    ps = pushStrength

    roundness = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0, soft_min_value=-2.0, soft_max_value=2.0)
    ro = roundness

    maya65Above = BoolField(default_value=False)
    ma = maya65Above

    maya2008Above = BoolField(default_value=False)
    m08 = maya2008Above

    orderVerticesFromFacesFirst = BoolField(default_value=False)
    ovf = orderVerticesFromFacesFirst
