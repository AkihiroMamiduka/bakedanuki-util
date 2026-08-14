# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.pxr_usd_point_based_deformer_node import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class GeneratedPxrUsdPointBasedDeformerNode(DG):
    __slots__ = ()

    NODE_TYPE = "pxrUsdPointBasedDeformerNode"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(
        multi=True, default_value=1.0, writable=False
    )
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(
        default_value=1.0,
        min_value=-2.0,
        max_value=2.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
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

    inUsdStage = TypedField(readable=False)
    is_ = inUsdStage

    primPath = DataStringField()
    pp = primPath

    time = TimeField(default_value=0.0)
    tm = time
