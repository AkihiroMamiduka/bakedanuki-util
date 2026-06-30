# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_signal import (
    MColourField,
    SignalScaleMultiplierField,
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


class SignalTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _4D_NOISE = 1
    LOOPING_NOISE = 2
    FRACTIONAL_BROWNIAN_MOTION = 3
    TRIGONOMETRY = 4
    CURL_NOISE = 5


class SignalTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _4D_NOISE = 1
    LOOPING_NOISE = 2
    FRACTIONAL_BROWNIAN_MOTION = 3
    TRIGONOMETRY = 4
    CURL_NOISE = 5

    NAME_MAP = {
        _4D_NOISE: "4D Noise",
        LOOPING_NOISE: "Looping Noise",
        FRACTIONAL_BROWNIAN_MOTION: "Fractional Brownian Motion",
        TRIGONOMETRY: "Trigonometry",
        CURL_NOISE: "Curl Noise",
    }


class SignalTypeEnumField(
    EnumField[SignalTypeEnumAttrOperator, SignalTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SignalTypeEnumAttrOperator
    PLUG_CLS = SignalTypeEnumPlugOperator


class TrigonometryModeXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3

    NAME_MAP = {
        SIN: "Sin",
        COS: "Cos",
        TAN: "Tan",
    }


class TrigonometryModeXEnumField(
    EnumField[TrigonometryModeXEnumAttrOperator, TrigonometryModeXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrigonometryModeXEnumAttrOperator
    PLUG_CLS = TrigonometryModeXEnumPlugOperator


class TrigonometryModeYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3

    NAME_MAP = {
        SIN: "Sin",
        COS: "Cos",
        TAN: "Tan",
    }


class TrigonometryModeYEnumField(
    EnumField[TrigonometryModeYEnumAttrOperator, TrigonometryModeYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrigonometryModeYEnumAttrOperator
    PLUG_CLS = TrigonometryModeYEnumPlugOperator


class TrigonometryModeZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3

    NAME_MAP = {
        SIN: "Sin",
        COS: "Cos",
        TAN: "Tan",
    }


class TrigonometryModeZEnumField(
    EnumField[TrigonometryModeZEnumAttrOperator, TrigonometryModeZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrigonometryModeZEnumAttrOperator
    PLUG_CLS = TrigonometryModeZEnumPlugOperator


class MASH_Signal(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Signal"

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

    time = TimeField()

    enable = BoolField()

    signalScale = FloatField()

    advection = FloatField()

    signalScaleMultiplier = SignalScaleMultiplierField()
    signalScaleMultiplier0 = signalScaleMultiplier.signalScaleMultiplier0
    signalScaleMultiplier1 = signalScaleMultiplier.signalScaleMultiplier1
    signalScaleMultiplier2 = signalScaleMultiplier.signalScaleMultiplier2

    noiseOctaves = LongField()

    noisePersistance = FloatField()

    positionX = FloatField()

    positionY = FloatField()

    positionZ = FloatField()

    rotationX = FloatField()

    rotationY = FloatField()

    rotationZ = FloatField()

    scaleX = FloatField()

    scaleY = FloatField()

    scaleZ = FloatField()

    timeScale = FloatField()

    enableStep = BoolField()

    stepAmount = FloatField()

    loopFrames = LongField()

    signalType = SignalTypeEnumField()

    trigonometryModeX = TrigonometryModeXEnumField()

    trigonometryModeY = TrigonometryModeYEnumField()

    trigonometryModeZ = TrigonometryModeZEnumField()

    uniformScale = BoolField()

    positiveScale = BoolField()
