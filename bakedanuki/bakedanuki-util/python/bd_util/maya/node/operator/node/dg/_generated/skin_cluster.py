# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.skin_cluster import (
    DqsScaleField,
    EnvelopeWeightsListField,
    FunctionField,
    InfluenceColorField,
    InputField,
    PerInfluenceWeightsField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField


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


class GeneratedSkinCluster(DG):
    __slots__ = ()

    NODE_TYPE = "skinCluster"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    skinningMethod = SkinningMethodEnumField(default_value=0)
    skm = skinningMethod

    blendWeights = DoubleField(multi=True, default_value=0.0)
    bw = blendWeights

    weightList = WeightListField(multi=True, default_value=0.0)
    wl = weightList

    perInfluenceWeights = PerInfluenceWeightsField(multi=True, default_value=0.0, writable=False)
    piw = perInfluenceWeights

    bindPreMatrix = DataMatrixField(multi=True)
    pm = bindPreMatrix

    geomMatrix = DataMatrixField()
    gm = geomMatrix

    matrix = DataMatrixField(multi=True)
    ma = matrix

    dropoffRate = DoubleField(default_value=4.0, min_value=0.1, max_value=10.0)
    dr = dropoffRate

    dropoff = DoubleField(multi=True, default_value=4.0, min_value=0.1, max_value=100.0)
    dpf = dropoff

    smoothness = DoubleField(multi=True, default_value=0.0)
    smt = smoothness

    lockWeights = BoolField(multi=True, default_value=False)
    lw = lockWeights

    maintainMaxInfluences = BoolField(default_value=False)
    mmi = maintainMaxInfluences

    maxInfluences = LongField(default_value=2, min_value=0)
    mi = maxInfluences

    relativeSpaceMode = RelativeSpaceModeEnumField(default_value=0)
    rsmd = relativeSpaceMode

    relativeSpaceMatrix = MatrixField()
    rsmat = relativeSpaceMatrix

    bindMethod = BindMethodEnumField(default_value=0)
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

    useComponents = BoolField(default_value=False)
    uc = useComponents

    nurbsSamples = LongField(multi=True, default_value=10)
    ns = nurbsSamples

    useComponentsMatrix = BoolField(default_value=False)
    ucm = useComponentsMatrix

    normalizeWeights = NormalizeWeightsEnumField(default_value=1)
    nw = normalizeWeights

    weightDistribution = WeightDistributionEnumField(default_value=0)
    wd = weightDistribution

    deformUserNormals = BoolField(default_value=True)
    dun = deformUserNormals

    wtDrty = MessageField()
    wtd = wtDrty

    bindPose = MessageField()
    bp = bindPose

    bindVolume = MessageField()
    bc = bindVolume

    heatmapFalloff = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    hmf = heatmapFalloff

    influenceColor = InfluenceColorField(multi=True, default_value=(0.0, 0.0, 0.0))
    ifcl = influenceColor

    geomBind = MessageField()
    gb = geomBind

    dqsSupportNonRigid = BoolField(default_value=False)
    dsnr = dqsSupportNonRigid

    dqsScale = DqsScaleField(default_value=(1.0, 1.0, 1.0))
    dsc = dqsScale
    dqsScaleX = dqsScale.dqsScaleX
    dscx = dqsScaleX
    dqsScaleY = dqsScale.dqsScaleY
    dscy = dqsScaleY
    dqsScaleZ = dqsScale.dqsScaleZ
    dscz = dqsScaleZ
