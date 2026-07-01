# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.tension import (
    CacheField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class Tension(DG):
    __slots__ = ()

    NODE_TYPE = "tension"

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

    smoothingIterations = LongField()
    si = smoothingIterations

    smoothingStep = FloatField()
    ss = smoothingStep

    inwardConstraint = FloatField()
    iwc = inwardConstraint

    outwardConstraint = FloatField()
    owc = outwardConstraint

    squashConstraint = FloatField()
    sqc = squashConstraint

    stretchConstraint = FloatField()
    stc = stretchConstraint

    relative = FloatField()
    rel = relative

    shearStrength = FloatField()
    shr = shearStrength

    bendStrength = FloatField()
    bnd = bendStrength

    pinBorderVertices = BoolField()
    pbv = pinBorderVertices

    cache = CacheField(multi=True)
    cach = cache
