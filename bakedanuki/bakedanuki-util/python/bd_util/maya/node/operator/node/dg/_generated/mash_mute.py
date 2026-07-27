# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_mute import (
    BeatRampField,
    EnvelopeRampField,
    FalloffObjectField,
    MColourField,
    MuteRampField,
    VelocityRampField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
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


class GeneratedMASH_Mute(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Mute"

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

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    enable = BoolField(default_value=True)
    en = enable

    envelopeRamp = EnvelopeRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    noiseEnvelope = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    noiseEnvelopeScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    EnvelopeX = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    envX = EnvelopeX

    EnvelopeY = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    envY = EnvelopeY

    EnvelopeZ = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    envZ = EnvelopeZ

    randEnvelopeX = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    raEnX = randEnvelopeX

    randEnvelopeY = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    raEnY = randEnvelopeY

    randEnvelopeZ = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    raEnZ = randEnvelopeZ

    StepEnvelopeX = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    StEnvX = StepEnvelopeX

    StepEnvelopeY = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    StEnvY = StepEnvelopeY

    StepEnvelopeZ = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    StEnvZ = StepEnvelopeZ

    lifespan = FloatField(default_value=1.0, min_value=0.01, soft_max_value=10.0)

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

    reverse = BoolField(default_value=False)

    persistentFalloff = BoolField(default_value=False)

    loopBeat = BoolField(default_value=True)

    useStrengthGraph = BoolField(default_value=False)

    falloffMessage = MessageField()
    fmsg = falloffMessage

    beatRamp = BeatRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    muteRamp = MuteRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    beatFrame = LongField(default_value=25, min_value=1, soft_max_value=30)

    timeStagger = LongField(default_value=0, min_value=0, soft_max_value=30)

    rampXStrength = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    rampYStrength = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    rampZStrength = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    enableX = BoolField(default_value=True)

    enableY = BoolField(default_value=True)

    enableZ = BoolField(default_value=True)

    maxVelocity = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    velocityStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    velocityRamp = VelocityRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    uniformVelocity = BoolField(default_value=True)

    falloffInfo = TypedField()

    stringKill = DataStringField()
    skill = stringKill

    stringkeep = DataStringField()
    skeep = stringkeep
