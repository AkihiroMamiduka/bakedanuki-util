# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_audio import (
    FalloffObjectField,
    FrequencyGraphField,
    MColourField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
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


class FilterStrengthEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4


class FilterStrengthEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4

    NAME_MAP = {
        NONE: "None",
        WEAK: "Weak",
        MODERATE: "Moderate",
        STRONG: "Strong",
    }


class FilterStrengthEnumField(
    EnumField[FilterStrengthEnumAttrOperator, FilterStrengthEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterStrengthEnumAttrOperator
    PLUG_CLS = FilterStrengthEnumPlugOperator


class OutputModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    MULTIPLY = 1


class OutputModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    MULTIPLY = 1

    NAME_MAP = {
        NORMAL: "Normal",
        MULTIPLY: "Multiply",
    }


class OutputModeEnumField(
    EnumField[OutputModeEnumAttrOperator, OutputModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputModeEnumAttrOperator
    PLUG_CLS = OutputModeEnumPlugOperator


class SampleRateEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _48000 = 0
    _44100 = 1
    _22050 = 2
    _64000 = 3
    _96000 = 4


class SampleRateEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _48000 = 0
    _44100 = 1
    _22050 = 2
    _64000 = 3
    _96000 = 4

    NAME_MAP = {
        _48000: "48000",
        _44100: "44100",
        _22050: "22050",
        _64000: "64000",
        _96000: "96000",
    }


class SampleRateEnumField(
    EnumField[SampleRateEnumAttrOperator, SampleRateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SampleRateEnumAttrOperator
    PLUG_CLS = SampleRateEnumPlugOperator


class NodeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SPECTRUM = 0
    AVERAGE = 1


class NodeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SPECTRUM = 0
    AVERAGE = 1

    NAME_MAP = {
        SPECTRUM: "Spectrum",
        AVERAGE: "Average",
    }


class NodeModeEnumField(
    EnumField[NodeModeEnumAttrOperator, NodeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NodeModeEnumAttrOperator
    PLUG_CLS = NodeModeEnumPlugOperator


class FourierScalingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    SQUARE_ROOT = 1
    LOGARITHMIC = 2


class FourierScalingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    SQUARE_ROOT = 1
    LOGARITHMIC = 2

    NAME_MAP = {
        NORMAL: "Normal",
        SQUARE_ROOT: "Square Root",
        LOGARITHMIC: "Logarithmic",
    }


class FourierScalingEnumField(
    EnumField[FourierScalingEnumAttrOperator, FourierScalingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FourierScalingEnumAttrOperator
    PLUG_CLS = FourierScalingEnumPlugOperator


class VolumeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AVERAGE = 0
    LOUDEST = 1


class VolumeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AVERAGE = 0
    LOUDEST = 1

    NAME_MAP = {
        AVERAGE: "Average",
        LOUDEST: "Loudest",
    }


class VolumeModeEnumField(
    EnumField[VolumeModeEnumAttrOperator, VolumeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeModeEnumAttrOperator
    PLUG_CLS = VolumeModeEnumPlugOperator


class MASH_Audio(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Audio"

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

    falloffOut = TypedField()

    inputPoints = TypedField()

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    modifiedTime = TimeField()
    moTi = modifiedTime

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    eqOutput = FloatField(multi=True)

    enableX = BoolField()
    enX = enableX

    enableY = BoolField()
    enY = enableY

    enableZ = BoolField()
    enZ = enableZ

    enablePosition = BoolField()

    enableRotation = BoolField()

    enableScale = BoolField()

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    eqBOutput = BoolField()

    falloffMessage = MessageField()
    fmsg = falloffMessage

    falloffInfo = TypedField()

    soundLength = FloatField()

    maxBands = LongField()

    outVolume = FloatField()

    timeStep = BoolField()

    legacy2016 = BoolField()

    legacy2017 = BoolField()

    filterStrength = FilterStrengthEnumField()

    minThreshold = FloatField()

    maxThreshold = FloatField()

    filename = DataStringField()

    timeOffset = TimeField()

    outputMode = OutputModeEnumField()

    sampleRate = SampleRateEnumField()

    nodeMode = NodeModeEnumField()

    fourierScaling = FourierScalingEnumField()

    volumeMode = VolumeModeEnumField()

    frequencyGraph = FrequencyGraphField(multi=True)

    timeSmoothing = LongField()

    ampScale = FloatField()
    as_ = ampScale

    amplitudeLeft = FloatField()
    ampL = amplitudeLeft

    amplitudeRight = FloatField()
    ampR = amplitudeRight

    positionX = FloatField()

    positionY = FloatField()

    positionZ = FloatField()

    rotationX = FloatField()

    rotationY = FloatField()

    rotationZ = FloatField()

    scaleX = FloatField()

    scaleY = FloatField()

    scaleZ = FloatField()
