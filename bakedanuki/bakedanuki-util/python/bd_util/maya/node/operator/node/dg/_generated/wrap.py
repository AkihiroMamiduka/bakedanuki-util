# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.wrap import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
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
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class FalloffModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VOLUME = 0
    SURFACE = 1


class FalloffModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VOLUME = 0
    SURFACE = 1

    NAME_MAP = {
        VOLUME: "Volume",
        SURFACE: "Surface",
    }


class FalloffModeEnumField(
    EnumField[FalloffModeEnumAttrOperator, FalloffModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffModeEnumAttrOperator
    PLUG_CLS = FalloffModeEnumPlugOperator


class _GeneratedWrap(DG):
    __slots__ = ()

    NODE_TYPE = "wrap"

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

    geomMatrix = DataMatrixField()
    gm = geomMatrix

    driverPoints = TypedField(multi=True)
    dp = driverPoints

    basePoints = TypedField(multi=True)
    bp = basePoints

    dropoff = DoubleField(multi=True, default_value=4.0)
    dr = dropoff

    smoothness = DoubleField(multi=True, default_value=0.0)
    smt = smoothness

    inflType = ShortField(multi=True, default_value=2)
    it = inflType

    nurbsSamples = ShortField(multi=True, default_value=10)
    ns = nurbsSamples

    weightThreshold = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    wt = weightThreshold

    maxDistance = DoubleLinearField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=50.0)
    md = maxDistance

    autoWeightThreshold = BoolField(default_value=False)
    awt = autoWeightThreshold

    autoWeightThresholdValue = DoubleField(default_value=0.0, writable=False)
    wtv = autoWeightThresholdValue

    exclusiveBind = BoolField(default_value=False)
    rb = exclusiveBind

    wtDrty = MessageField()
    wtd = wtDrty

    baseDrt = MessageField()
    bsd = baseDrt

    falloffMode = FalloffModeEnumField(default_value=0)
    fom = falloffMode
