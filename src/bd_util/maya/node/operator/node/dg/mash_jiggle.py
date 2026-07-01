# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_jiggle import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    MColourField,
    PerGeometryField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


class MapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class MapDirectionEnumField(
    EnumField[MapDirectionEnumAttrOperator, MapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapDirectionEnumAttrOperator
    PLUG_CLS = MapDirectionEnumPlugOperator


class FalloffAffectsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class FalloffAffectsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2

    NAME_MAP = {
        ALL: "All",
        BLEND_ONLY: "Blend Only",
    }


class FalloffAffectsEnumField(
    EnumField[FalloffAffectsEnumAttrOperator, FalloffAffectsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffAffectsEnumAttrOperator
    PLUG_CLS = FalloffAffectsEnumPlugOperator


class MapAffectsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class MapAffectsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2

    NAME_MAP = {
        ALL: "All",
        BLEND_ONLY: "Blend Only",
    }


class MapAffectsEnumField(
    EnumField[MapAffectsEnumAttrOperator, MapAffectsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapAffectsEnumAttrOperator
    PLUG_CLS = MapAffectsEnumPlugOperator


class MASH_Jiggle(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Jiggle"

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

    time = TimeField()

    mColour = MColourField()
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField()

    randEnvelope = FloatField()
    raEn = randEnvelope

    StepEnvelope = FloatField()
    StEnv = StepEnvelope

    falloffAffects = FalloffAffectsEnumField()

    mapAffects = MapAffectsEnumField()

    directionBias = FloatField()

    normalStrength = FloatField()

    maxVelocity = FloatField()

    stiffness = FloatField()

    damping = FloatField()

    strengthPP = TypedField(multi=True)

    Envelope = FloatField()
    env = Envelope

    perGeometry = PerGeometryField(multi=True)
