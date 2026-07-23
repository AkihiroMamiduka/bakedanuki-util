# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.tension import (
    CacheField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField


class _GeneratedTension(DG):
    __slots__ = ()

    NODE_TYPE = "tension"

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

    smoothingIterations = LongField(default_value=10, min_value=0)
    si = smoothingIterations

    smoothingStep = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ss = smoothingStep

    inwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    iwc = inwardConstraint

    outwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    owc = outwardConstraint

    squashConstraint = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    sqc = squashConstraint

    stretchConstraint = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    stc = stretchConstraint

    relative = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rel = relative

    shearStrength = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    shr = shearStrength

    bendStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bnd = bendStrength

    pinBorderVertices = BoolField(default_value=True)
    pbv = pinBorderVertices

    cache = CacheField(multi=True)
    cach = cache
