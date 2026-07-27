# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.jiggle import (
    CachedDataListField,
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
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class EnableEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ENABLE = 0
    DISABLE = 1
    ENABLE_ONLY_AFTER_OBJECT_STOPS = 2


class EnableEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ENABLE = 0
    DISABLE = 1
    ENABLE_ONLY_AFTER_OBJECT_STOPS = 2

    NAME_MAP = {
        ENABLE: "Enable",
        DISABLE: "Disable",
        ENABLE_ONLY_AFTER_OBJECT_STOPS: "Enable Only After Object Stops",
    }


class EnableEnumField(
    EnumField[EnableEnumAttrOperator, EnableEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnableEnumAttrOperator
    PLUG_CLS = EnableEnumPlugOperator


class GeneratedJiggle(DG):
    __slots__ = ()

    NODE_TYPE = "jiggle"

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

    diskCache = MessageField()
    dc = diskCache

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    enable = EnableEnumField(default_value=2)
    ebl = enable

    ignoreTransform = BoolField(default_value=False)
    it = ignoreTransform

    forceAlongNormal = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fan = forceAlongNormal

    forceOnTangent = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fot = forceOnTangent

    motionMultiplier = DoubleField(default_value=1.0)
    mm = motionMultiplier

    stiffness = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    sf = stiffness

    damping = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    dp = damping

    jiggleWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=2.0)
    jw = jiggleWeight

    cachedDataList = CachedDataListField(multi=True)
    cdl = cachedDataList

    cachedTime = TimeField()
    chti = cachedTime

    isResting = BoolField()
    ir = isResting

    cachedInputPositionList = DataVectorArrayField()
    cipl = cachedInputPositionList

    cachedPositionList = DataVectorArrayField()
    cpl = cachedPositionList

    cachedVelocityList = DataVectorArrayField()
    cvl = cachedVelocityList

    directionBias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bias = directionBias
