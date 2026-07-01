# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.delta_mush import (
    CacheField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    ScaleField,
    WeightListField,
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


class SmoothingAlgorithmEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AVERAGE = 0


class SmoothingAlgorithmEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AVERAGE = 0

    NAME_MAP = {
        AVERAGE: "Average",
    }


class SmoothingAlgorithmEnumField(
    EnumField[SmoothingAlgorithmEnumAttrOperator, SmoothingAlgorithmEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothingAlgorithmEnumAttrOperator
    PLUG_CLS = SmoothingAlgorithmEnumPlugOperator


class DeltaMush(DG):
    __slots__ = ()

    NODE_TYPE = "deltaMush"

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

    smoothingIterations = LongField()
    si = smoothingIterations

    smoothingAlgorithm = SmoothingAlgorithmEnumField()
    sa = smoothingAlgorithm

    smoothingStep = FloatField()
    ss = smoothingStep

    inwardConstraint = FloatField()
    iwc = inwardConstraint

    outwardConstraint = FloatField()
    owc = outwardConstraint

    distanceWeight = FloatField()
    dwt = distanceWeight

    pinBorderVertices = BoolField()
    pbv = pinBorderVertices

    displacement = FloatField()
    dsp = displacement

    scale = ScaleField()
    s = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    cache = CacheField(multi=True)
    cach = cache
