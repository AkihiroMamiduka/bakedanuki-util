# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.wire import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.float_angle import FloatAngleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class Wire(DG):
    __slots__ = ()

    NODE_TYPE = "wire"

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

    crossingEffect = FloatField()
    ce = crossingEffect

    tension = FloatField()
    te = tension

    localInfluence = FloatField()
    li = localInfluence

    rotation = FloatField()
    ro = rotation

    freezeGeometry = BoolField()
    fg = freezeGeometry

    bindToOriginalGeometry = BoolField()
    bog = bindToOriginalGeometry

    dropoffDistance = FloatField(multi=True)
    dds = dropoffDistance

    scale = FloatField(multi=True)
    sc = scale

    wireLocatorPercentage = FloatField(multi=True)
    wlpc = wireLocatorPercentage

    wireLocatorParameter = FloatField(multi=True)
    wlp = wireLocatorParameter

    wireLocatorEnvelope = FloatField(multi=True)
    wle = wireLocatorEnvelope

    wireLocatorTwist = FloatAngleField(multi=True)
    wlt = wireLocatorTwist

    deformedWire = DataNurbsCurveField(multi=True)
    dw = deformedWire

    baseWire = DataNurbsCurveField(multi=True)
    bw = baseWire

    holder = GenericField(multi=True)
    ho = holder
