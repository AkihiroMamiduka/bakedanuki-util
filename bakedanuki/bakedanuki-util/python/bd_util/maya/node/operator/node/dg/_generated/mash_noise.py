# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_noise import (
    MColourField,
    OffsetValuesField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
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


class _GeneratedMASH_Noise(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Noise"

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

    strengthAffectsAmplitude = BoolField(default_value=True)

    strengthAffectsFrequency = BoolField(default_value=False)

    strengthAffectsStep = BoolField(default_value=False)

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    uniformNoise = BoolField(default_value=False)

    offsetValues = OffsetValuesField(default_value=(0.0, 0.0, 0.0))
    ofVal = offsetValues
    offsetValues0 = offsetValues.offsetValues0
    ofVal0 = offsetValues0
    offsetValues1 = offsetValues.offsetValues1
    ofVal1 = offsetValues1
    offsetValues2 = offsetValues.offsetValues2
    ofVal2 = offsetValues2

    modular = LongField(default_value=1, min_value=1, soft_max_value=20)
    mod = modular

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    mosaicx = BoolField(default_value=True)

    mosaicy = BoolField(default_value=True)

    mosaicz = BoolField(default_value=True)

    switchTime = LongField(default_value=45, min_value=2, soft_max_value=100)

    switchVariance = FloatField(default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0)

    distanceVariance = FloatField(default_value=0.699999988079071, min_value=0.0, soft_max_value=1.0)

    fov = FloatField(default_value=120.0, min_value=0.0, max_value=360.0)

    octaves = LongField(default_value=1, min_value=1, soft_max_value=5)
    oct = octaves

    seed = LongField(default_value=1, min_value=1, soft_max_value=100)
    see = seed

    positiveNoise = BoolField(default_value=False)
    posNoi = positiveNoise

    intResults = BoolField(default_value=False)
    intRes = intResults

    enable = BoolField(default_value=True)
    en = enable

    noiseType = NoiseTypeEnumField(default_value=1)

    persistence = FloatField(default_value=4.0, min_value=0.01, soft_max_value=5.0)

    loopNoiseRadius = FloatField(default_value=120.0, min_value=0.001, soft_max_value=250.0)

    step = FloatField(default_value=1000.0, soft_min_value=0.0, soft_max_value=2000.0)
    st = step

    amplitudeX = FloatField(default_value=1.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampX = amplitudeX

    frequencyX = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    freqX = frequencyX

    amplitudeY = FloatField(default_value=1.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampY = amplitudeY

    frequencyY = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    freqY = frequencyY

    amplitudeZ = FloatField(default_value=1.0, soft_min_value=-20.0, soft_max_value=20.0)
    ampZ = amplitudeZ

    frequencyZ = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    freqZ = frequencyZ
