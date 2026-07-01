# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_mirror import (
    MirrorPlaneCenterField,
    MirrorPlaneRotateField,
    PivotField,
    ScalePivotField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.at.unit_scalar_range.float_linear import FloatLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class DirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class AxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class AxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class AxisEnumField(
    EnumField[AxisEnumAttrOperator, AxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisEnumAttrOperator
    PLUG_CLS = AxisEnumPlugOperator


class AxisDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS = 0
    MINUS = 1


class AxisDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLUS = 0
    MINUS = 1

    NAME_MAP = {
        PLUS: "+",
        MINUS: "-",
    }


class AxisDirectionEnumField(
    EnumField[AxisDirectionEnumAttrOperator, AxisDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisDirectionEnumAttrOperator
    PLUG_CLS = AxisDirectionEnumPlugOperator


class MirrorAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOUNDING_BOX = 0
    OBJECT = 1
    WORLD = 2


class MirrorAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOUNDING_BOX = 0
    OBJECT = 1
    WORLD = 2

    NAME_MAP = {
        BOUNDING_BOX: "Bounding box",
        OBJECT: "Object",
        WORLD: "World",
    }


class MirrorAxisEnumField(
    EnumField[MirrorAxisEnumAttrOperator, MirrorAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorAxisEnumAttrOperator
    PLUG_CLS = MirrorAxisEnumPlugOperator


class MergeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MERGE_BORDER_VERTICES = 1
    BRIDGE_BORDER_EDGES = 2
    DO_NOT_MERGE_BORDERS = 3


class MergeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MERGE_BORDER_VERTICES = 1
    BRIDGE_BORDER_EDGES = 2
    DO_NOT_MERGE_BORDERS = 3

    NAME_MAP = {
        MERGE_BORDER_VERTICES: "Merge border vertices",
        BRIDGE_BORDER_EDGES: "Bridge border edges",
        DO_NOT_MERGE_BORDERS: "Do not merge borders",
    }


class MergeModeEnumField(
    EnumField[MergeModeEnumAttrOperator, MergeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeModeEnumAttrOperator
    PLUG_CLS = MergeModeEnumPlugOperator


class MergeThresholdTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1


class MergeThresholdTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        CUSTOM: "Custom",
    }


class MergeThresholdTypeEnumField(
    EnumField[MergeThresholdTypeEnumAttrOperator, MergeThresholdTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeThresholdTypeEnumAttrOperator
    PLUG_CLS = MergeThresholdTypeEnumPlugOperator


class FlipUVsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    LOCAL_U = 1
    LOCAL_V = 2
    WORLD_U = 3
    WORLD_V = 4


class FlipUVsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    LOCAL_U = 1
    LOCAL_V = 2
    WORLD_U = 3
    WORLD_V = 4

    NAME_MAP = {
        OFF: "Off",
        LOCAL_U: "Local U",
        LOCAL_V: "Local V",
        WORLD_U: "World U",
        WORLD_V: "World V",
    }


class FlipUVsEnumField(
    EnumField[FlipUVsEnumAttrOperator, FlipUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlipUVsEnumAttrOperator
    PLUG_CLS = FlipUVsEnumPlugOperator


class PolyMirror(DG):
    __slots__ = ()

    NODE_TYPE = "polyMirror"

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

    pivot = PivotField()
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    userSpecifiedPivot = BoolField()
    pu = userSpecifiedPivot

    direction = DirectionEnumField()
    d = direction

    axis = AxisEnumField()
    a = axis

    axisDirection = AxisDirectionEnumField()
    ad = axisDirection

    mirrorAxis = MirrorAxisEnumField()
    ma = mirrorAxis

    mirrorPosition = FloatLinearField()
    mps = mirrorPosition

    mergeMode = MergeModeEnumField()
    mm = mergeMode

    mergeThresholdType = MergeThresholdTypeEnumField()
    mtt = mergeThresholdType

    mergeThreshold = DoubleLinearField()
    mt = mergeThreshold

    smoothingAngle = FloatField()
    sa = smoothingAngle

    scalePivot = ScalePivotField()
    sp = scalePivot
    scalePivotX = scalePivot.scalePivotX
    spx = scalePivotX
    scalePivotY = scalePivot.scalePivotY
    spy = scalePivotY
    scalePivotZ = scalePivot.scalePivotZ
    spz = scalePivotZ

    cutMesh = BoolField()
    cm = cutMesh

    firstNewFace = LongField()
    fnf = firstNewFace

    lastNewFace = LongField()
    lnf = lastNewFace

    flipUVs = FlipUVsEnumField()
    fuv = flipUVs

    compId = LongField()
    cid = compId

    mirrorPlaneCenter = MirrorPlaneCenterField()
    pc = mirrorPlaneCenter
    mirrorPlaneCenterX = mirrorPlaneCenter.mirrorPlaneCenterX
    pcx = mirrorPlaneCenterX
    mirrorPlaneCenterY = mirrorPlaneCenter.mirrorPlaneCenterY
    pcy = mirrorPlaneCenterY
    mirrorPlaneCenterZ = mirrorPlaneCenter.mirrorPlaneCenterZ
    pcz = mirrorPlaneCenterZ

    mirrorPlaneRotate = MirrorPlaneRotateField()
    ro = mirrorPlaneRotate
    mirrorPlaneRotateX = mirrorPlaneRotate.mirrorPlaneRotateX
    rx = mirrorPlaneRotateX
    mirrorPlaneRotateY = mirrorPlaneRotate.mirrorPlaneRotateY
    ry = mirrorPlaneRotateY
    mirrorPlaneRotateZ = mirrorPlaneRotate.mirrorPlaneRotateZ
    rz = mirrorPlaneRotateZ

    maya2017 = BoolField()
    m17 = maya2017

    keepVertexIDs = BoolField()
    kv = keepVertexIDs
