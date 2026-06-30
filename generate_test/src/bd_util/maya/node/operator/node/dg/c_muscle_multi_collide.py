# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_multi_collide import (
    CollisionDataField,
    EnvelopeWeightsListField,
    FunctionField,
    GeoDataField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class CMuscleMultiCollide(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleMultiCollide"

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

    geoData = GeoDataField(multi=True)
    gdata = geoData

    collisionData = CollisionDataField()
    clldata = collisionData
    tolerance = collisionData.tolerance
    tol = tolerance
    falloff = collisionData.falloff
    fal = falloff
    volumize = collisionData.volumize
    vol = volumize
    blurIterations = collisionData.blurIterations
    blrit = blurIterations
    relaxIterations = collisionData.relaxIterations
    rxi = relaxIterations
    relaxStrength = collisionData.relaxStrength
    rxstr = relaxStrength
    smoothIterations = collisionData.smoothIterations
    smi = smoothIterations
    smoothStrength = collisionData.smoothStrength
    smstr = smoothStrength
    smoothHold = collisionData.smoothHold
    hld = smoothHold

    inTime = DoubleField()
    it = inTime

    inMesh = GenericField(multi=True)
    imsh = inMesh
