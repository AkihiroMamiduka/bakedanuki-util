# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class MergeUVSetsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_MERGE = 0
    MERGE_BY_NAME = 1
    MERGE_BY_UV_LINKS = 2


class MergeUVSetsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_MERGE = 0
    MERGE_BY_NAME = 1
    MERGE_BY_UV_LINKS = 2

    NAME_MAP = {
        NO_MERGE: "No Merge",
        MERGE_BY_NAME: "Merge By Name",
        MERGE_BY_UV_LINKS: "Merge By UV Links",
    }


class MergeUVSetsEnumField(
    EnumField[MergeUVSetsEnumAttrOperator, MergeUVSetsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeUVSetsEnumAttrOperator
    PLUG_CLS = MergeUVSetsEnumPlugOperator


class NewInputOperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNION = 1
    DIFFERENCE_A_MINUS_B = 2
    INTERSECTION = 3
    DIFFERENCE_B_MINUS_A = 4
    SLICE = 5
    HOLE_PUNCH = 6
    CUT_OUT = 7
    SPLIT_EDGE = 8


class NewInputOperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNION = 1
    DIFFERENCE_A_MINUS_B = 2
    INTERSECTION = 3
    DIFFERENCE_B_MINUS_A = 4
    SLICE = 5
    HOLE_PUNCH = 6
    CUT_OUT = 7
    SPLIT_EDGE = 8

    NAME_MAP = {
        UNION: "Union",
        DIFFERENCE_A_MINUS_B: "Difference (A-B)",
        INTERSECTION: "Intersection",
        DIFFERENCE_B_MINUS_A: "Difference (B-A)",
        SLICE: "Slice",
        HOLE_PUNCH: "Hole Punch",
        CUT_OUT: "Cut Out",
        SPLIT_EDGE: "Split Edge",
    }


class NewInputOperationEnumField(
    EnumField[NewInputOperationEnumAttrOperator, NewInputOperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NewInputOperationEnumAttrOperator
    PLUG_CLS = NewInputOperationEnumPlugOperator


class NewInputDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WIREFRAME = 0
    SHADED = 1
    BOUNDING_BOX = 2
    X_MINUS_RAY = 3
    HIDDEN = 4


class NewInputDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WIREFRAME = 0
    SHADED = 1
    BOUNDING_BOX = 2
    X_MINUS_RAY = 3
    HIDDEN = 4

    NAME_MAP = {
        WIREFRAME: "Wireframe",
        SHADED: "Shaded",
        BOUNDING_BOX: "Bounding Box",
        X_MINUS_RAY: "X-Ray",
        HIDDEN: "Hidden",
    }


class NewInputDisplayEnumField(
    EnumField[NewInputDisplayEnumAttrOperator, NewInputDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NewInputDisplayEnumAttrOperator
    PLUG_CLS = NewInputDisplayEnumPlugOperator


class ClassificationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EDGE = 1
    NORMAL = 2
    AUTO = 3


class ClassificationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EDGE = 1
    NORMAL = 2
    AUTO = 3

    NAME_MAP = {
        EDGE: "Edge",
        NORMAL: "Normal",
        AUTO: "Auto",
    }


class ClassificationEnumField(
    EnumField[ClassificationEnumAttrOperator, ClassificationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClassificationEnumAttrOperator
    PLUG_CLS = ClassificationEnumPlugOperator


class GeometryModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MESH = 0
    OPENVDB = 1


class GeometryModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MESH = 0
    OPENVDB = 1

    NAME_MAP = {
        MESH: "Mesh",
        OPENVDB: "OpenVDB",
    }


class GeometryModeEnumField(
    EnumField[GeometryModeEnumAttrOperator, GeometryModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeometryModeEnumAttrOperator
    PLUG_CLS = GeometryModeEnumPlugOperator


class PolyBoolean(DG):
    __slots__ = ()

    NODE_TYPE = "polyBoolean"

    output = DataMeshField()
    out = output

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    inputPoly = DataMeshField(multi=True)
    ip = inputPoly

    inputMat = DataMatrixField(multi=True)
    im = inputMat

    componentTagName = DataStringField(multi=True)
    ctg = componentTagName

    mergeUVSets = MergeUVSetsEnumField()
    muv = mergeUVSets

    outputUVSetName = DataStringField(multi=True)
    ouv = outputUVSetName

    intersectionEdges = TypedField()
    ied = intersectionEdges

    interactiveUpdate = BoolField()
    iu = interactiveUpdate

    operation = TypedField()
    op = operation

    newInputOperation = NewInputOperationEnumField()
    nio = newInputOperation

    newInputDisplay = NewInputDisplayEnumField()
    nid = newInputDisplay

    elementEnabled = TypedField()
    ee = elementEnabled

    classification = ClassificationEnumField()
    cls = classification

    geometryMode = GeometryModeEnumField()
    gm = geometryMode

    voxelSize = FloatField()
    vs = voxelSize

    booleanMode = BoolField()
    bm = booleanMode

    preserveColor = BoolField()
    pcr = preserveColor

    mergeGroups = TypedField()
    mg = mergeGroups

    tagIntersection = BoolField()
    ti = tagIntersection

    planarTolerance = DoubleField()
    ptl = planarTolerance

    sortOutput = BoolField()
    sop = sortOutput

    edgeInterpolation = BoolField()
    eit = edgeInterpolation

    useThresholds = BoolField()
    uth = useThresholds

    vertexDistanceThreshold = DoubleLinearField()
    vdt = vertexDistanceThreshold

    maya2025 = BoolField()
    m25 = maya2025
