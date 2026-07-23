# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_audio import (
    FalloffObjectField,
    FrequencyGraphField,
    MColourField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
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


class _GeneratedMASH_Audio(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Audio"

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

    falloffOut = TypedField(writable=False)

    inputPoints = TypedField()

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    modifiedTime = TimeField(default_value=1.0, writable=False)
    moTi = modifiedTime

    inIterations = LongField(default_value=0)
    inIter = inIterations

    enable = BoolField(default_value=True)
    en = enable

    eqOutput = FloatField(multi=True, default_value=0.0, writable=False)

    enableX = BoolField(default_value=False)
    enX = enableX

    enableY = BoolField(default_value=True)
    enY = enableY

    enableZ = BoolField(default_value=False)
    enZ = enableZ

    enablePosition = BoolField(default_value=True)

    enableRotation = BoolField(default_value=True)

    enableScale = BoolField(default_value=True)

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    eqBOutput = BoolField(default_value=False)

    falloffMessage = MessageField()
    fmsg = falloffMessage

    falloffInfo = TypedField()

    soundLength = FloatField(default_value=0.0, writable=False)

    maxBands = LongField(default_value=64, min_value=0, soft_max_value=100)

    outVolume = FloatField(default_value=0.0, writable=False)

    timeStep = BoolField(default_value=True)

    legacy2016 = BoolField(default_value=False)

    legacy2017 = BoolField(default_value=False)

    filterStrength = FilterStrengthEnumField(default_value=1)

    minThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=30.0)

    maxThreshold = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    filename = DataStringField()

    timeOffset = TimeField(default_value=0.0)

    outputMode = OutputModeEnumField(default_value=0)

    sampleRate = SampleRateEnumField(default_value=1)

    nodeMode = NodeModeEnumField(default_value=0)

    fourierScaling = FourierScalingEnumField(default_value=0)

    volumeMode = VolumeModeEnumField(default_value=0)

    frequencyGraph = FrequencyGraphField(multi=True, default_value=(0.0, 0.0, 1.0))

    timeSmoothing = LongField(default_value=1, min_value=1, soft_max_value=5)

    ampScale = FloatField(default_value=30.0, soft_min_value=0.0, soft_max_value=100.0)
    as_ = ampScale

    amplitudeLeft = FloatField(default_value=0.0, writable=False)
    ampL = amplitudeLeft

    amplitudeRight = FloatField(default_value=0.0, writable=False)
    ampR = amplitudeRight

    positionX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    positionY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    positionZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    rotationX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    scaleX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    scaleY = FloatField(default_value=30.0, min_value=0.0, soft_max_value=10.0)

    scaleZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
