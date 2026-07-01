# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.cluster import (
    ClusterXformsField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
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


class Cluster(DG):
    __slots__ = ()

    NODE_TYPE = "cluster"

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
