# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.wrap import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
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
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


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


class Wrap(DG):
    __slots__ = ()

    NODE_TYPE = "wrap"

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

    geomMatrix = DataMatrixField()
    gm = geomMatrix

    driverPoints = TypedField(multi=True)
    dp = driverPoints

    basePoints = TypedField(multi=True)
    bp = basePoints

    dropoff = DoubleField(multi=True)
    dr = dropoff

    smoothness = DoubleField(multi=True)
    smt = smoothness

    inflType = ShortField(multi=True)
    it = inflType

    nurbsSamples = ShortField(multi=True)
    ns = nurbsSamples

    weightThreshold = DoubleField()
    wt = weightThreshold

    maxDistance = DoubleLinearField()
    md = maxDistance

    autoWeightThreshold = BoolField()
    awt = autoWeightThreshold

    autoWeightThresholdValue = DoubleField()
    wtv = autoWeightThresholdValue

    exclusiveBind = BoolField()
    rb = exclusiveBind

    wtDrty = MessageField()
    wtd = wtDrty

    baseDrt = MessageField()
    bsd = baseDrt

    falloffMode = FalloffModeEnumField()
    fom = falloffMode
