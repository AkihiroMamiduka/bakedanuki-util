# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_jiggle import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    MColourField,
    PerGeometryField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField


class MapDirectionEnumPlugOperator(
    EnumPlugOperator["MapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(
    EnumAttrOperator[MapDirectionEnumPlugOperator]
):
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


class FalloffAffectsEnumPlugOperator(
    EnumPlugOperator["FalloffAffectsEnumAttrOperator"]
):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class FalloffAffectsEnumAttrOperator(
    EnumAttrOperator[FalloffAffectsEnumPlugOperator]
):
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


class MapAffectsEnumPlugOperator(
    EnumPlugOperator["MapAffectsEnumAttrOperator"]
):
    __slots__ = ()

    ALL = 1
    BLEND_ONLY = 2


class MapAffectsEnumAttrOperator(EnumAttrOperator[MapAffectsEnumPlugOperator]):
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


class GeneratedMASH_Jiggle(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Jiggle"

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

    time = TimeField(default_value=0.0)

    mColour = MColourField(default_value=(1.0, 1.0, 1.0))
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField(default_value=2)

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    StEnv = StepEnvelope

    falloffAffects = FalloffAffectsEnumField(default_value=1)

    mapAffects = MapAffectsEnumField(default_value=1)

    directionBias = FloatField(
        default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0
    )

    normalStrength = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )

    maxVelocity = FloatField(
        default_value=3.0, soft_min_value=0.0, soft_max_value=4.0
    )

    stiffness = FloatField(
        default_value=0.20000000298023224, min_value=0.0, max_value=1.0
    )

    damping = FloatField(
        default_value=0.20000000298023224, min_value=0.0, max_value=1.0
    )

    strengthPP = TypedField(multi=True)

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    perGeometry = PerGeometryField(multi=True)
