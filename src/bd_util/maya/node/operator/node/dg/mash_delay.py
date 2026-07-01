# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_delay import (
    FalloffObjectField,
    MColourField,
    TranslateInPPField,
    TranslateOutPPField,
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


class DelayModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    FOLLOW_THE_LEADER = 2


class DelayModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 1
    FOLLOW_THE_LEADER = 2

    NAME_MAP = {
        NORMAL: "Normal",
        FOLLOW_THE_LEADER: "Follow the Leader",
    }


class DelayModeEnumField(
    EnumField[DelayModeEnumAttrOperator, DelayModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DelayModeEnumAttrOperator
    PLUG_CLS = DelayModeEnumPlugOperator


class MASH_Delay(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Delay"

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

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    enablePosition = BoolField()

    enableScale = BoolField()

    enableRotation = BoolField()

    targetMode = BoolField()

    falloffInfo = TypedField()

    delayMode = DelayModeEnumField()

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

    falloffMessage = MessageField()
    fmsg = falloffMessage

    timeStep = FloatField()
    ts = timeStep

    offset = FloatField()
    off = offset

    timeVariance = FloatField()
    tva = timeVariance

    inTargetMatrix = MatrixField()
    targetInMatrix = inTargetMatrix
