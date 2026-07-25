# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_retopo import PivotField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.scalar.unit.range.float_linear import FloatLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedPolyRetopo(DG):
    __slots__ = ()

    NODE_TYPE = "polyRetopo"

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

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    targetFaceCount = LongField(default_value=0, min_value=0, soft_max_value=100000)
    tfc = targetFaceCount

    targetFaceCountTolerance = LongField(default_value=10, min_value=1, max_value=100)
    tft = targetFaceCountTolerance

    topologyRegularity = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    trg = topologyRegularity

    faceUniformity = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    fun = faceUniformity

    anisotropy = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    a = anisotropy

    targetEdgeDeviation = DoubleField(default_value=0.2929, min_value=0.0001, max_value=1.0)
    ted = targetEdgeDeviation

    curveSingularitySeparation = DoubleField(default_value=0.1, min_value=0.0, max_value=100.0)
    css = curveSingularitySeparation

    curveInfluenceDirection = DoubleField(default_value=0.01, min_value=0.0, max_value=100.0)
    cid = curveInfluenceDirection

    preserveHardEdges = BoolField(default_value=False)
    phe = preserveHardEdges

    edgesByAngle = BoolField(default_value=False)
    eba = edgesByAngle

    angle = DoubleAngleField(default_value=29.999999999999996, min_value=0.0, max_value=180.0)
    ang = angle

    useFeatureTags = BoolField(default_value=False)
    uft = useFeatureTags

    featureTags = DataStringField()
    ft = featureTags

    preprocessMesh = BoolField(default_value=True)
    pm = preprocessMesh

    preprocessedMesh = DataMeshField()
    ppm = preprocessedMesh

    symmetryEdges = TypedField()
    sme = symmetryEdges

    symmetry = BoolField(default_value=False)
    sym = symmetry

    axisPosition = AxisPositionEnumField(default_value=1)
    ap = axisPosition

    axisOffset = FloatLinearField(default_value=0.0)
    ao = axisOffset

    axis = AxisEnumField(default_value=1)
    an = axis

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    shortEdgeTolerance = DoubleLinearField(default_value=0.0001, min_value=0.0)
    se = shortEdgeTolerance

    thinTriangleAngleTolerance = DoubleAngleField(default_value=0.9740282517223996)
    tt = thinTriangleAngleTolerance

    interactiveMode = BoolField(default_value=False)
    imd = interactiveMode
