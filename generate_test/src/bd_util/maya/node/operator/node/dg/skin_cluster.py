# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.skin_cluster import (
    DqsScaleField,
    EnvelopeWeightsListField,
    FunctionField,
    InfluenceColorField,
    InputField,
    PerInfluenceWeightsField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.matrix import DataMatrixField


class SkinningMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLASSIC_LINEAR = 0
    DUAL_QUATERNION = 1
    WEIGHT_BLENDED = 2


class SkinningMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLASSIC_LINEAR = 0
    DUAL_QUATERNION = 1
    WEIGHT_BLENDED = 2

    NAME_MAP = {
        CLASSIC_LINEAR: "Classic Linear",
        DUAL_QUATERNION: "Dual Quaternion",
        WEIGHT_BLENDED: "Weight Blended",
    }


class SkinningMethodEnumField(
    EnumField[SkinningMethodEnumAttrOperator, SkinningMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkinningMethodEnumAttrOperator
    PLUG_CLS = SkinningMethodEnumPlugOperator


class RelativeSpaceModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    CUSTOM = 2


class RelativeSpaceModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    CUSTOM = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
        CUSTOM: "Custom",
    }


class RelativeSpaceModeEnumField(
    EnumField[RelativeSpaceModeEnumAttrOperator, RelativeSpaceModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativeSpaceModeEnumAttrOperator
    PLUG_CLS = RelativeSpaceModeEnumPlugOperator


class BindMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST_DISTANCE = 0
    CLOSEST_JOINT_IN_HIERARCHY = 1
    HEAT_MAP = 2
    GEODESIC_VOXEL = 3


class BindMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST_DISTANCE = 0
    CLOSEST_JOINT_IN_HIERARCHY = 1
    HEAT_MAP = 2
    GEODESIC_VOXEL = 3

    NAME_MAP = {
        CLOSEST_DISTANCE: "Closest Distance",
        CLOSEST_JOINT_IN_HIERARCHY: "Closest Joint In Hierarchy",
        HEAT_MAP: "Heat Map",
        GEODESIC_VOXEL: "Geodesic Voxel",
    }


class BindMethodEnumField(
    EnumField[BindMethodEnumAttrOperator, BindMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BindMethodEnumAttrOperator
    PLUG_CLS = BindMethodEnumPlugOperator


class NormalizeWeightsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    INTERACTIVE = 1
    POST = 2


class NormalizeWeightsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    INTERACTIVE = 1
    POST = 2

    NAME_MAP = {
        NONE: "None",
        INTERACTIVE: "Interactive",
        POST: "Post",
    }


class NormalizeWeightsEnumField(
    EnumField[NormalizeWeightsEnumAttrOperator, NormalizeWeightsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalizeWeightsEnumAttrOperator
    PLUG_CLS = NormalizeWeightsEnumPlugOperator


class WeightDistributionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISTANCE = 0
    NEIGHBORS = 1


class WeightDistributionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISTANCE = 0
    NEIGHBORS = 1

    NAME_MAP = {
        DISTANCE: "Distance",
        NEIGHBORS: "Neighbors",
    }


class WeightDistributionEnumField(
    EnumField[WeightDistributionEnumAttrOperator, WeightDistributionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightDistributionEnumAttrOperator
    PLUG_CLS = WeightDistributionEnumPlugOperator


class SkinCluster(DG):
    __slots__ = ()

    NODE_TYPE = "skinCluster"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    skinningMethod = SkinningMethodEnumField()
    skm = skinningMethod

    blendWeights = DoubleField(multi=True)
    bw = blendWeights

    weightList = WeightListField(multi=True)
    wl = weightList

    perInfluenceWeights = PerInfluenceWeightsField(multi=True)
    piw = perInfluenceWeights

    bindPreMatrix = DataMatrixField(multi=True)
    pm = bindPreMatrix

    geomMatrix = DataMatrixField()
    gm = geomMatrix

    matrix = DataMatrixField(multi=True)
    ma = matrix

    dropoffRate = DoubleField()
    dr = dropoffRate

    dropoff = DoubleField(multi=True)
    dpf = dropoff

    smoothness = DoubleField(multi=True)
    smt = smoothness

    lockWeights = BoolField(multi=True)
    lw = lockWeights

    maintainMaxInfluences = BoolField()
    mmi = maintainMaxInfluences

    maxInfluences = LongField()
    mi = maxInfluences

    relativeSpaceMode = RelativeSpaceModeEnumField()
    rsmd = relativeSpaceMode

    relativeSpaceMatrix = MatrixField()
    rsmat = relativeSpaceMatrix

    bindMethod = BindMethodEnumField()
    bm = bindMethod

    driverPoints = TypedField(multi=True)
    drp = driverPoints

    basePoints = TypedField(multi=True)
    bsp = basePoints

    baseDirty = MessageField()
    bsd = baseDirty

    paintWeights = DataDoubleArrayField()
    ptw = paintWeights

    paintTrans = MessageField()
    ptt = paintTrans

    paintArrDirty = MessageField()
    pad = paintArrDirty

    useComponents = BoolField()
    uc = useComponents

    nurbsSamples = LongField(multi=True)
    ns = nurbsSamples

    useComponentsMatrix = BoolField()
    ucm = useComponentsMatrix

    normalizeWeights = NormalizeWeightsEnumField()
    nw = normalizeWeights

    weightDistribution = WeightDistributionEnumField()
    wd = weightDistribution

    deformUserNormals = BoolField()
    dun = deformUserNormals

    wtDrty = MessageField()
    wtd = wtDrty

    bindPose = MessageField()
    bp = bindPose

    bindVolume = MessageField()
    bc = bindVolume

    heatmapFalloff = DoubleField()
    hmf = heatmapFalloff

    influenceColor = InfluenceColorField(multi=True)
    ifcl = influenceColor

    geomBind = MessageField()
    gb = geomBind

    dqsSupportNonRigid = BoolField()
    dsnr = dqsSupportNonRigid

    dqsScale = DqsScaleField()
    dsc = dqsScale
    dqsScaleX = dqsScale.dqsScaleX
    dscx = dqsScaleX
    dqsScaleY = dqsScale.dqsScaleY
    dscy = dqsScaleY
    dqsScaleZ = dqsScale.dqsScaleZ
    dscz = dqsScaleZ
