# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_trig import (
    AmplitudeColourField,
    MColourField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


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


class TransformationSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[TransformationSpaceEnumAttrOperator, TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class GeneratedMASH_Trig(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Trig"

    savedData = TypedField()

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

    Envelope = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField(default_value=True)

    enableStrengthY = BoolField(default_value=True)

    enableStrengthZ = BoolField(default_value=True)

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField(default_value=1)

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    outputArray = DataVectorArrayField()
    outArray = outputArray

    inputArray = DataVectorArrayField()
    inArray = inputArray

    inUtilityPositions = DataVectorArrayField()

    time = TimeField(default_value=1.0)
    ti = time

    xAxis = LongField(default_value=1)
    xAx = xAxis

    yAxis = LongField(default_value=1)
    yAx = yAxis

    zAxis = LongField(default_value=1)
    zAx = zAxis

    positiveNoise = BoolField(default_value=False)
    posNoi = positiveNoise

    strengthAffectsAmplitude = BoolField(default_value=True)

    strengthAffectsFrequency = BoolField(default_value=False)

    strengthAffectsStep = BoolField(default_value=False)

    modular = LongField(default_value=1, min_value=1, soft_max_value=20)
    mod = modular

    amplitudeX = FloatField(default_value=5.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampX = amplitudeX

    frequencyX = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=2.0)
    freqX = frequencyX

    amplitudeY = FloatField(default_value=5.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampY = amplitudeY

    frequencyY = FloatField(default_value=0.20000000298023224, soft_min_value=0.0, soft_max_value=2.0)
    freqY = frequencyY

    amplitudeZ = FloatField(default_value=5.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampZ = amplitudeZ

    frequencyZ = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=2.0)
    freqZ = frequencyZ

    step = FloatField(default_value=2.0, soft_min_value=0.0, soft_max_value=100.0)
    st = step

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    amplitudeColour = AmplitudeColourField(default_value=(1.0, 1.0, 1.0))
    amplitudeColourR = amplitudeColour.amplitudeColourR
    amplitudeColourG = amplitudeColour.amplitudeColourG
    amplitudeColourB = amplitudeColour.amplitudeColourB

    enable = BoolField(default_value=True)
    en = enable

    intResults = BoolField(default_value=False)
    intRes = intResults

    inIterations = LongField(default_value=0)
    inIter = inIterations
