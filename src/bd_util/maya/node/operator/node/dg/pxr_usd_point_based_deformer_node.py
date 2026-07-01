# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.pxr_usd_point_based_deformer_node import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class PxrUsdPointBasedDeformerNode(DG):
    __slots__ = ()

    NODE_TYPE = "pxrUsdPointBasedDeformerNode"

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

    inUsdStage = TypedField()
    is_ = inUsdStage

    primPath = DataStringField()
    pp = primPath

    time = TimeField()
    tm = time
