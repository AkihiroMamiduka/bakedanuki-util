# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_mute import (
    BeatRampField,
    EnvelopeRampField,
    FalloffObjectField,
    MColourField,
    MuteRampField,
    VelocityRampField,
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
from ...attr.define.std.dt.double_array import DataDoubleArrayField
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


class MASH_Mute(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Mute"

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

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    inputArray2 = DataVectorArrayField()
    inArray2 = inputArray2

    inputArray3 = DataVectorArrayField()
    inArray3 = inputArray3

    inStrengthPP = DataVectorArrayField()

    inStrengthDoublePP = DataDoubleArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    envelopeRamp = EnvelopeRampField(multi=True)

    noiseEnvelope = FloatField()

    noiseEnvelopeScale = FloatField()

    EnvelopeX = FloatField()
    envX = EnvelopeX

    EnvelopeY = FloatField()
    envY = EnvelopeY

    EnvelopeZ = FloatField()
    envZ = EnvelopeZ

    randEnvelopeX = FloatField()
    raEnX = randEnvelopeX

    randEnvelopeY = FloatField()
    raEnY = randEnvelopeY

    randEnvelopeZ = FloatField()
    raEnZ = randEnvelopeZ

    StepEnvelopeX = FloatField()
    StEnvX = StepEnvelopeX

    StepEnvelopeY = FloatField()
    StEnvY = StepEnvelopeY

    StepEnvelopeZ = FloatField()
    StEnvZ = StepEnvelopeZ

    lifespan = FloatField()

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

    reverse = BoolField()

    persistentFalloff = BoolField()

    loopBeat = BoolField()

    useStrengthGraph = BoolField()

    falloffMessage = MessageField()
    fmsg = falloffMessage

    beatRamp = BeatRampField(multi=True)

    muteRamp = MuteRampField(multi=True)

    beatFrame = LongField()

    timeStagger = LongField()

    rampXStrength = FloatField()

    rampYStrength = FloatField()

    rampZStrength = FloatField()

    enableX = BoolField()

    enableY = BoolField()

    enableZ = BoolField()

    maxVelocity = FloatField()

    velocityStrength = FloatField()

    velocityRamp = VelocityRampField(multi=True)

    uniformVelocity = BoolField()

    falloffInfo = TypedField()

    stringKill = DataStringField()
    skill = stringKill

    stringkeep = DataStringField()
    skeep = stringkeep
