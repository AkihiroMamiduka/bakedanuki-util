# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.history_switch import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class HistorySwitch(DG):
    __slots__ = ()

    NODE_TYPE = "historySwitch"

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

    undeformedGeometry = TypedField(multi=True)
    ug = undeformedGeometry

    playFromCache = BoolField()
    pfc = playFromCache

    inPositions = GenericField(multi=True)
    inp = inPositions

    outPositions = DataVectorArrayField(multi=True)
    op = outPositions
