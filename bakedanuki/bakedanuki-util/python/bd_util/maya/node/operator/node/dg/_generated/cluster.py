# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.cluster import (
    ClusterXformsField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class AngleInterpolationEnumPlugOperator(EnumPlugOperator["AngleInterpolationEnumAttrOperator"]):
    __slots__ = ()

    CLOSEST = 0
    POSITIVE = 1
    NEGATIVE = 2
    SHORTEST = 3


class AngleInterpolationEnumAttrOperator(EnumAttrOperator[AngleInterpolationEnumPlugOperator]):
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


class GeneratedCluster(DG):
    __slots__ = ()

    NODE_TYPE = "cluster"

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
