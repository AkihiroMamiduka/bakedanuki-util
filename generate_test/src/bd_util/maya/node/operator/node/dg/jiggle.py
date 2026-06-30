# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.jiggle import (
    CachedDataListField,
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
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


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


class Jiggle(DG):
    __slots__ = ()

    NODE_TYPE = "jiggle"

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

    diskCache = MessageField()
    dc = diskCache

    currentTime = TimeField()
    cti = currentTime

    enable = EnableEnumField()
    ebl = enable

    ignoreTransform = BoolField()
    it = ignoreTransform

    forceAlongNormal = DoubleField()
    fan = forceAlongNormal

    forceOnTangent = DoubleField()
    fot = forceOnTangent

    motionMultiplier = DoubleField()
    mm = motionMultiplier

    stiffness = DoubleField()
    sf = stiffness

    damping = DoubleField()
    dp = damping

    jiggleWeight = DoubleField()
    jw = jiggleWeight

    cachedDataList = CachedDataListField(multi=True)
    cdl = cachedDataList

    # TODO: cachedDataList.cachedTime (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: cachedDataList.isResting (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: cachedDataList.cachedInputPositionList (attributeType=None, dataType=vectorArray) は未対応のため手動で追加してください

    # TODO: cachedDataList.cachedPositionList (attributeType=None, dataType=vectorArray) は未対応のため手動で追加してください

    # TODO: cachedDataList.cachedVelocityList (attributeType=None, dataType=vectorArray) は未対応のため手動で追加してください

    directionBias = DoubleField()
    bias = directionBias
