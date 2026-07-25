# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.history_switch import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class _GeneratedHistorySwitch(DG):
    __slots__ = ()

    NODE_TYPE = "historySwitch"

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

    undeformedGeometry = TypedField(multi=True)
    ug = undeformedGeometry

    playFromCache = BoolField(default_value=False)
    pfc = playFromCache

    inPositions = GenericField(multi=True)
    inp = inPositions

    outPositions = DataVectorArrayField(multi=True)
    op = outPositions
