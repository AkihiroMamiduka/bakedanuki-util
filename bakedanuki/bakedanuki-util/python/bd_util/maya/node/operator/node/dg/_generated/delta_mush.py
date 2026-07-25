# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.delta_mush import (
    CacheField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    ScaleField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


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


class _GeneratedDeltaMush(DG):
    __slots__ = ()

    NODE_TYPE = "deltaMush"

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

    smoothingIterations = LongField(default_value=10, min_value=0)
    si = smoothingIterations

    smoothingAlgorithm = SmoothingAlgorithmEnumField(default_value=0)
    sa = smoothingAlgorithm

    smoothingStep = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    ss = smoothingStep

    inwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    iwc = inwardConstraint

    outwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    owc = outwardConstraint

    distanceWeight = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dwt = distanceWeight

    pinBorderVertices = BoolField(default_value=True)
    pbv = pinBorderVertices

    displacement = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    dsp = displacement

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    s = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    cache = CacheField(multi=True)
    cach = cache
