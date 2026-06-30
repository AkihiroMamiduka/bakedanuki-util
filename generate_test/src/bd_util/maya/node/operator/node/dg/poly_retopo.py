# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_retopo import PivotField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.at.unit_scalar_range.float_linear import FloatLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class AxisPositionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OBJECT = 1
    BOUNDING_BOX = 2
    WORLD = 3


class AxisPositionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OBJECT = 1
    BOUNDING_BOX = 2
    WORLD = 3

    NAME_MAP = {
        OBJECT: "Object",
        BOUNDING_BOX: "Bounding Box",
        WORLD: "World",
    }


class AxisPositionEnumField(
    EnumField[AxisPositionEnumAttrOperator, AxisPositionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisPositionEnumAttrOperator
    PLUG_CLS = AxisPositionEnumPlugOperator


class AxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS_X_TO_MINUS_X = 1
    MINUS_X_TO_PLUS_X = 2
    PLUS_Y_TO_MINUS_Y = 3
    MINUS_Y_TO_PLUS_Y = 4
    PLUS_Z_TO_MINUS_Z = 5
    MINUS_Z_TO_PLUS_Z = 6


class AxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLUS_X_TO_MINUS_X = 1
    MINUS_X_TO_PLUS_X = 2
    PLUS_Y_TO_MINUS_Y = 3
    MINUS_Y_TO_PLUS_Y = 4
    PLUS_Z_TO_MINUS_Z = 5
    MINUS_Z_TO_PLUS_Z = 6

    NAME_MAP = {
        PLUS_X_TO_MINUS_X: "+X to -X",
        MINUS_X_TO_PLUS_X: "-X to +X",
        PLUS_Y_TO_MINUS_Y: "+Y to -Y",
        MINUS_Y_TO_PLUS_Y: "-Y to +Y",
        PLUS_Z_TO_MINUS_Z: "+Z to -Z",
        MINUS_Z_TO_PLUS_Z: "-Z to +Z",
    }


class AxisEnumField(
    EnumField[AxisEnumAttrOperator, AxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisEnumAttrOperator
    PLUG_CLS = AxisEnumPlugOperator


class PolyRetopo(DG):
    __slots__ = ()

    NODE_TYPE = "polyRetopo"

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

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    targetFaceCount = LongField()
    tfc = targetFaceCount

    targetFaceCountTolerance = LongField()
    tft = targetFaceCountTolerance

    topologyRegularity = DoubleField()
    trg = topologyRegularity

    faceUniformity = DoubleField()
    fun = faceUniformity

    anisotropy = DoubleField()
    a = anisotropy

    targetEdgeDeviation = DoubleField()
    ted = targetEdgeDeviation

    curveSingularitySeparation = DoubleField()
    css = curveSingularitySeparation

    curveInfluenceDirection = DoubleField()
    cid = curveInfluenceDirection

    preserveHardEdges = BoolField()
    phe = preserveHardEdges

    edgesByAngle = BoolField()
    eba = edgesByAngle

    angle = DoubleAngleField()
    ang = angle

    useFeatureTags = BoolField()
    uft = useFeatureTags

    featureTags = DataStringField()
    ft = featureTags

    preprocessMesh = BoolField()
    pm = preprocessMesh

    preprocessedMesh = DataMeshField()
    ppm = preprocessedMesh

    symmetryEdges = TypedField()
    sme = symmetryEdges

    symmetry = BoolField()
    sym = symmetry

    axisPosition = AxisPositionEnumField()
    ap = axisPosition

    axisOffset = FloatLinearField()
    ao = axisOffset

    axis = AxisEnumField()
    an = axis

    pivot = PivotField()
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    shortEdgeTolerance = DoubleLinearField()
    se = shortEdgeTolerance

    thinTriangleAngleTolerance = DoubleAngleField()
    tt = thinTriangleAngleTolerance

    interactiveMode = BoolField()
    imd = interactiveMode
