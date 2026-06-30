# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_noise import (
    MColourField,
    OffsetValuesField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class NoiseTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NOISE = 1
    RANDOM_SEEK = 3
    FBM_NOISE = 4
    NOISE_LOOPING = 5


class NoiseTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NOISE = 1
    RANDOM_SEEK = 3
    FBM_NOISE = 4
    NOISE_LOOPING = 5

    NAME_MAP = {
        NOISE: "Noise",
        RANDOM_SEEK: "Random Seek",
        FBM_NOISE: "fBM Noise",
        NOISE_LOOPING: "Noise (looping)",
    }


class NoiseTypeEnumField(
    EnumField[NoiseTypeEnumAttrOperator, NoiseTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseTypeEnumAttrOperator
    PLUG_CLS = NoiseTypeEnumPlugOperator


class MASH_Noise(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Noise"

    savedData = TypedField()

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

    Envelope = FloatField()

    randEnvelope = FloatField()

    StepEnvelope = FloatField()

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField()

    enableStrengthY = BoolField()

    enableStrengthZ = BoolField()

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField()

    outputPoints = TypedField()

    inputPoints = TypedField()

    outputArray = DataVectorArrayField()
    outArray = outputArray

    inputArray = DataVectorArrayField()
    inArray = inputArray

    strengthAffectsAmplitude = BoolField()

    strengthAffectsFrequency = BoolField()

    strengthAffectsStep = BoolField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    uniformNoise = BoolField()

    offsetValues = OffsetValuesField()
    ofVal = offsetValues
    offsetValues0 = offsetValues.offsetValues0
    ofVal0 = offsetValues0
    offsetValues1 = offsetValues.offsetValues1
    ofVal1 = offsetValues1
    offsetValues2 = offsetValues.offsetValues2
    ofVal2 = offsetValues2

    modular = LongField()
    mod = modular

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    mosaicx = BoolField()

    mosaicy = BoolField()

    mosaicz = BoolField()

    switchTime = LongField()

    switchVariance = FloatField()

    distanceVariance = FloatField()

    fov = FloatField()

    octaves = LongField()
    oct = octaves

    seed = LongField()
    see = seed

    positiveNoise = BoolField()
    posNoi = positiveNoise

    intResults = BoolField()
    intRes = intResults

    enable = BoolField()
    en = enable

    noiseType = NoiseTypeEnumField()

    persistence = FloatField()

    loopNoiseRadius = FloatField()

    step = FloatField()
    st = step

    amplitudeX = FloatField()
    ampX = amplitudeX

    frequencyX = FloatField()
    freqX = frequencyX

    amplitudeY = FloatField()
    ampY = amplitudeY

    frequencyY = FloatField()
    freqY = frequencyY

    amplitudeZ = FloatField()
    ampZ = amplitudeZ

    frequencyZ = FloatField()
    freqZ = frequencyZ
