# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_signal import (
    MColourField,
    SignalScaleMultiplierField,
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


class MapDirectionEnumPlugOperator(EnumPlugOperator["MapDirectionEnumAttrOperator"]):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator[MapDirectionEnumPlugOperator]):
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


class TransformationSpaceEnumPlugOperator(EnumPlugOperator["TransformationSpaceEnumAttrOperator"]):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator[TransformationSpaceEnumPlugOperator]):
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


class SignalTypeEnumPlugOperator(EnumPlugOperator["SignalTypeEnumAttrOperator"]):
    __slots__ = ()

    _4D_NOISE = 1
    LOOPING_NOISE = 2
    FRACTIONAL_BROWNIAN_MOTION = 3
    TRIGONOMETRY = 4
    CURL_NOISE = 5


class SignalTypeEnumAttrOperator(EnumAttrOperator[SignalTypeEnumPlugOperator]):
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


class TrigonometryModeXEnumPlugOperator(EnumPlugOperator["TrigonometryModeXEnumAttrOperator"]):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeXEnumAttrOperator(EnumAttrOperator[TrigonometryModeXEnumPlugOperator]):
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


class TrigonometryModeYEnumPlugOperator(EnumPlugOperator["TrigonometryModeYEnumAttrOperator"]):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeYEnumAttrOperator(EnumAttrOperator[TrigonometryModeYEnumPlugOperator]):
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


class TrigonometryModeZEnumPlugOperator(EnumPlugOperator["TrigonometryModeZEnumAttrOperator"]):
    __slots__ = ()

    SIN = 1
    COS = 2
    TAN = 3


class TrigonometryModeZEnumAttrOperator(EnumAttrOperator[TrigonometryModeZEnumPlugOperator]):
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


class GeneratedMASH_Signal(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Signal"

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

    time = TimeField(default_value=0.0)

    enable = BoolField(default_value=True)

    signalScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    advection = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=1.0)

    signalScaleMultiplier = SignalScaleMultiplierField(default_value=(1.0, 1.0, 1.0))
    signalScaleMultiplier0 = signalScaleMultiplier.signalScaleMultiplier0
    signalScaleMultiplier1 = signalScaleMultiplier.signalScaleMultiplier1
    signalScaleMultiplier2 = signalScaleMultiplier.signalScaleMultiplier2

    noiseOctaves = LongField(default_value=1, min_value=1, soft_max_value=10)

    noisePersistance = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    positionX = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    positionY = FloatField(default_value=5.0, min_value=0.0, soft_max_value=10.0)

    positionZ = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    rotationX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    scaleX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    scaleY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    scaleZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    timeScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    enableStep = BoolField(default_value=True)

    stepAmount = FloatField(default_value=150.0, min_value=0.0, soft_max_value=200.0)

    loopFrames = LongField(default_value=120, min_value=2, soft_max_value=250)

    signalType = SignalTypeEnumField(default_value=1)

    trigonometryModeX = TrigonometryModeXEnumField(default_value=1)

    trigonometryModeY = TrigonometryModeYEnumField(default_value=1)

    trigonometryModeZ = TrigonometryModeZEnumField(default_value=1)

    uniformScale = BoolField(default_value=True)

    positiveScale = BoolField(default_value=True)
