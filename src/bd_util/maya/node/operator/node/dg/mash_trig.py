# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_trig import (
    AmplitudeColourField,
    MColourField,
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


class MASH_Trig(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Trig"

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

    inUtilityPositions = DataVectorArrayField()

    time = TimeField()
    ti = time

    xAxis = LongField()
    xAx = xAxis

    yAxis = LongField()
    yAx = yAxis

    zAxis = LongField()
    zAx = zAxis

    positiveNoise = BoolField()
    posNoi = positiveNoise

    strengthAffectsAmplitude = BoolField()

    strengthAffectsFrequency = BoolField()

    strengthAffectsStep = BoolField()

    modular = LongField()
    mod = modular

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

    step = FloatField()
    st = step

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    amplitudeColour = AmplitudeColourField()
    amplitudeColourR = amplitudeColour.amplitudeColourR
    amplitudeColourG = amplitudeColour.amplitudeColourG
    amplitudeColourB = amplitudeColour.amplitudeColourB

    enable = BoolField()
    en = enable

    intResults = BoolField()
    intRes = intResults

    inIterations = LongField()
    inIter = inIterations
