# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.joint_cluster import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField


class AngleInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2
    SHORTEST = 3


class AngleInterpolationEnumAttrOperator(EnumAttrOperator):
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
    EnumField[AngleInterpolationEnumAttrOperator, AngleInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AngleInterpolationEnumAttrOperator
    PLUG_CLS = AngleInterpolationEnumPlugOperator


class UpperDropoffTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3


class UpperDropoffTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[UpperDropoffTypeEnumAttrOperator, UpperDropoffTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpperDropoffTypeEnumAttrOperator
    PLUG_CLS = UpperDropoffTypeEnumPlugOperator


class LowerDropoffTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    SINE = 1
    EXPONENTIAL = 2
    NONE = 3


class LowerDropoffTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[LowerDropoffTypeEnumAttrOperator, LowerDropoffTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LowerDropoffTypeEnumAttrOperator
    PLUG_CLS = LowerDropoffTypeEnumPlugOperator


class JointCluster(DG):
    __slots__ = ()

    NODE_TYPE = "jointCluster"

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

    weightList = WeightListField(multi=True)
    wl = weightList

    relative = BoolField()
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

    angleInterpolation = AngleInterpolationEnumField()
    ait = angleInterpolation

    redoLowerWeights = MessageField()
    rlw = redoLowerWeights

    redoUpperWeights = MessageField()
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

    childEnabled = BoolField(multi=True)
    che = childEnabled

    jointMidplaneAxis = JointMidplaneAxisField()
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

    nextJointMidplaneAxis = NextJointMidplaneAxisField()
    njm = nextJointMidplaneAxis
    nextjointMidplaneAxisX = nextJointMidplaneAxis.nextjointMidplaneAxisX
    nmx = nextjointMidplaneAxisX
    nextjointMidplaneAxisY = nextJointMidplaneAxis.nextjointMidplaneAxisY
    nmy = nextjointMidplaneAxisY
    nextjointMidplaneAxisZ = nextJointMidplaneAxis.nextjointMidplaneAxisZ
    nmz = nextjointMidplaneAxisZ

    childJointMidplaneAxis = ChildJointMidplaneAxisField(multi=True)
    cjm = childJointMidplaneAxis

    distanceList = DistanceListField(multi=True)
    dl = distanceList

    boneLength = FloatField()
    bl = boneLength

    upperBound = FloatField()
    ub = upperBound

    lastUpperBound = FloatField()
    lub = lastUpperBound

    upperValue = FloatField()
    uv = upperValue

    lowerBound = FloatField()
    lb = lowerBound

    lastLowerBound = FloatField()
    llb = lastLowerBound

    lowerValue = FloatField()
    lv = lowerValue

    upperDropoffType = UpperDropoffTypeEnumField()
    udt = upperDropoffType

    lowerDropoffType = LowerDropoffTypeEnumField()
    ldt = lowerDropoffType

    upperEnabled = BoolField()
    upe = upperEnabled

    lowerEnabled = BoolField()
    lwe = lowerEnabled

    clusterFlexorSet = MessageField()
    cfs = clusterFlexorSet

    enableAutoPercentUpdate = BoolField()
    epu = enableAutoPercentUpdate

    convertedTo2 = BoolField()
    ct2 = convertedTo2
