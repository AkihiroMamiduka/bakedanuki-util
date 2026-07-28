# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.joint_cluster import (
    ChildJointClusterXformsField,
    ChildJointMidplaneAxisField,
    ClusterXformsField,
    DistanceListField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    JointMidplaneAxisField,
    NextJointClusterXformsField,
    NextJointMidplaneAxisField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class AngleInterpolationEnumPlugOperator(
    EnumPlugOperator["AngleInterpolationEnumAttrOperator"]
):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2
    SHORTEST = 3


class AngleInterpolationEnumAttrOperator(
    EnumAttrOperator[AngleInterpolationEnumPlugOperator]
):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2
    SHORTEST = 3

    NAME_MAP = {
        CLOSEST: "Closest",
        POSITIVE: "Positive",
        NEGATIVE: "Negative",
        SHORTEST: "Shortest",
    }


class AngleInterpolationEnumField(
    EnumField[
        AngleInterpolationEnumAttrOperator, AngleInterpolationEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AngleInterpolationEnumAttrOperator
    PLUG_CLS = AngleInterpolationEnumPlugOperator


class UpperDropoffTypeEnumPlugOperator(
    EnumPlugOperator["UpperDropoffTypeEnumAttrOperator"]
):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3


class UpperDropoffTypeEnumAttrOperator(
    EnumAttrOperator[UpperDropoffTypeEnumPlugOperator]
):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3

    NAME_MAP = {
        LINEAR: "linear",
        SINE: "sine",
        EXPONENTIAL: "exponential",
        NONE: "none",
    }


class UpperDropoffTypeEnumField(
    EnumField[
        UpperDropoffTypeEnumAttrOperator, UpperDropoffTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UpperDropoffTypeEnumAttrOperator
    PLUG_CLS = UpperDropoffTypeEnumPlugOperator


class LowerDropoffTypeEnumPlugOperator(
    EnumPlugOperator["LowerDropoffTypeEnumAttrOperator"]
):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3


class LowerDropoffTypeEnumAttrOperator(
    EnumAttrOperator[LowerDropoffTypeEnumPlugOperator]
):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3

    NAME_MAP = {
        LINEAR: "linear",
        SINE: "sine",
        EXPONENTIAL: "exponential",
        NONE: "none",
    }


class LowerDropoffTypeEnumField(
    EnumField[
        LowerDropoffTypeEnumAttrOperator, LowerDropoffTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LowerDropoffTypeEnumAttrOperator
    PLUG_CLS = LowerDropoffTypeEnumPlugOperator


class GeneratedJointCluster(DG):
    __slots__ = ()

    NODE_TYPE = "jointCluster"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(
        multi=True, default_value=1.0, writable=False
    )
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(
        default_value=1.0,
        min_value=-2.0,
        max_value=2.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
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

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    relative = BoolField(default_value=False)
    rel = relative

    clusterXforms = ClusterXformsField()
    x = clusterXforms
    preMatrix = clusterXforms.preMatrix
    pre = preMatrix
    weightedMatrix = clusterXforms.weightedMatrix
    wt = weightedMatrix
    postMatrix = clusterXforms.postMatrix
    post = postMatrix

    weightedCompensationMatrix = DataMatrixField()
    wcm = weightedCompensationMatrix

    geomMatrix = DataMatrixField(multi=True)
    gm = geomMatrix

    matrix = DataMatrixField()
    ma = matrix

    bindPreMatrix = DataMatrixField()
    pm = bindPreMatrix

    angleInterpolation = AngleInterpolationEnumField(default_value=3)
    ait = angleInterpolation

    redoLowerWeights = MessageField(writable=False)
    rlw = redoLowerWeights

    redoUpperWeights = MessageField(writable=False)
    ruw = redoUpperWeights

    childJointClusterXforms = ChildJointClusterXformsField(multi=True)
    cjx = childJointClusterXforms

    childJointPreCompensationMatrix = DataMatrixField(multi=True)
    cjpr = childJointPreCompensationMatrix

    childJointWeightedCompensationMatrix = DataMatrixField(multi=True)
    cjwc = childJointWeightedCompensationMatrix

    childJointPostCompensationMatrix = DataMatrixField(multi=True)
    cjps = childJointPostCompensationMatrix

    bindPose = DataMatrixField()
    bp = bindPose

    nextJointBindPose = DataMatrixField()
    njb = nextJointBindPose

    childJointBindPose = DataMatrixField(multi=True)
    cjb = childJointBindPose

    childEnabled = BoolField(multi=True, default_value=False)
    che = childEnabled

    jointMidplaneAxis = JointMidplaneAxisField(default_value=(0.0, 0.0, 0.0))
    jma = jointMidplaneAxis
    jointMidplaneAxisX = jointMidplaneAxis.jointMidplaneAxisX
    jmx = jointMidplaneAxisX
    jointMidplaneAxisY = jointMidplaneAxis.jointMidplaneAxisY
    jmy = jointMidplaneAxisY
    jointMidplaneAxisZ = jointMidplaneAxis.jointMidplaneAxisZ
    jmz = jointMidplaneAxisZ

    nextJointClusterXforms = NextJointClusterXformsField()
    njx = nextJointClusterXforms
    nextJointPreMatrix = nextJointClusterXforms.nextJointPreMatrix
    npr = nextJointPreMatrix
    nextJointWeightedMatrix = nextJointClusterXforms.nextJointWeightedMatrix
    njw = nextJointWeightedMatrix
    nextJointPostMatrix = nextJointClusterXforms.nextJointPostMatrix
    npo = nextJointPostMatrix

    nextJointPreCompensationMatrix = DataMatrixField()
    njpr = nextJointPreCompensationMatrix

    nextJointWeightedCompensationMatrix = DataMatrixField()
    njwc = nextJointWeightedCompensationMatrix

    nextJointPostCompensationMatrix = DataMatrixField()
    njps = nextJointPostCompensationMatrix

    nextJointMidplaneAxis = NextJointMidplaneAxisField(
        default_value=(0.0, 0.0, 0.0)
    )
    njm = nextJointMidplaneAxis
    nextjointMidplaneAxisX = nextJointMidplaneAxis.nextjointMidplaneAxisX
    nmx = nextjointMidplaneAxisX
    nextjointMidplaneAxisY = nextJointMidplaneAxis.nextjointMidplaneAxisY
    nmy = nextjointMidplaneAxisY
    nextjointMidplaneAxisZ = nextJointMidplaneAxis.nextjointMidplaneAxisZ
    nmz = nextjointMidplaneAxisZ

    childJointMidplaneAxis = ChildJointMidplaneAxisField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    cjm = childJointMidplaneAxis

    distanceList = DistanceListField(multi=True, default_value=0.0)
    dl = distanceList

    boneLength = FloatField(default_value=0.0)
    bl = boneLength

    upperBound = FloatField(default_value=10.0, min_value=0.0, max_value=100.0)
    ub = upperBound

    lastUpperBound = FloatField(default_value=0.0)
    lub = lastUpperBound

    upperValue = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    uv = upperValue

    lowerBound = FloatField(default_value=10.0, min_value=0.0, max_value=100.0)
    lb = lowerBound

    lastLowerBound = FloatField(default_value=0.0)
    llb = lastLowerBound

    lowerValue = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    lv = lowerValue

    upperDropoffType = UpperDropoffTypeEnumField(default_value=0)
    udt = upperDropoffType

    lowerDropoffType = LowerDropoffTypeEnumField(default_value=0)
    ldt = lowerDropoffType

    upperEnabled = BoolField(default_value=False)
    upe = upperEnabled

    lowerEnabled = BoolField(default_value=False)
    lwe = lowerEnabled

    clusterFlexorSet = MessageField()
    cfs = clusterFlexorSet

    enableAutoPercentUpdate = BoolField(default_value=False, writable=False)
    epu = enableAutoPercentUpdate

    convertedTo2 = BoolField(default_value=False)
    ct2 = convertedTo2
