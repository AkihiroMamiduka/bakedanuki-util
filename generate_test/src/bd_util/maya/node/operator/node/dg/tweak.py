# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.tweak import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    PlistField,
    VlistField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class Tweak(DG):
    __slots__ = ()

    NODE_TYPE = "tweak"

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

    relativeTweak = BoolField()
    rtw = relativeTweak

    plist = PlistField(multi=True)
    pl = plist

    vlist = VlistField(multi=True)
    vl = vlist
