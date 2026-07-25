# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.wire import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.float_angle import FloatAngleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class _GeneratedWire(DG):
    __slots__ = ()

    NODE_TYPE = "wire"

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

    crossingEffect = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ce = crossingEffect

    tension = FloatField(default_value=1.0, min_value=-10.0, max_value=10.0)
    te = tension

    localInfluence = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    li = localInfluence

    rotation = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ro = rotation

    freezeGeometry = BoolField(default_value=False)
    fg = freezeGeometry

    bindToOriginalGeometry = BoolField(default_value=False)
    bog = bindToOriginalGeometry

    dropoffDistance = FloatField(multi=True, default_value=1.0, min_value=0.0)
    dds = dropoffDistance

    scale = FloatField(multi=True, default_value=1.0, min_value=0.0)
    sc = scale

    wireLocatorPercentage = FloatField(multi=True, default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    wlpc = wireLocatorPercentage

    wireLocatorParameter = FloatField(multi=True, default_value=0.0)
    wlp = wireLocatorParameter

    wireLocatorEnvelope = FloatField(multi=True, default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    wle = wireLocatorEnvelope

    wireLocatorTwist = FloatAngleField(multi=True, default_value=0.0, soft_min_value=-10313.240312354817, soft_max_value=10313.240312354817)
    wlt = wireLocatorTwist

    deformedWire = DataNurbsCurveField(multi=True)
    dw = deformedWire

    baseWire = DataNurbsCurveField(multi=True)
    bw = baseWire

    holder = GenericField(multi=True)
    ho = holder
