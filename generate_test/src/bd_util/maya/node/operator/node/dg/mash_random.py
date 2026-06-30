# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_random import (
    FalloffObjectField,
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


class MASH_Random(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Random"

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

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    inIterations = LongField()
    inIter = inIterations

    falloffInfo = TypedField()

    enable = BoolField()
    en = enable

    enableX = BoolField()

    enableY = BoolField()

    enableZ = BoolField()

    positionX = FloatField()

    positionY = FloatField()

    positionZ = FloatField()

    rotationX = FloatField()

    rotationY = FloatField()

    rotationZ = FloatField()

    scaleX = FloatField()

    scaleY = FloatField()

    scaleZ = FloatField()

    absoluteScale = BoolField()

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    wholeNumbers = BoolField()
    whoNum = wholeNumbers

    normaliseRandom = BoolField()

    uniformRandom = BoolField()
    uniRand = uniformRandom

    randomSeed = LongField()
    seed = randomSeed

    maxNumber = FloatField()
    max = maxNumber

    minNumber = FloatField()
    min = minNumber

    maxNumberX = FloatField()
    maxX = maxNumberX

    minNumberX = FloatField()
    minX = minNumberX

    maxNumberY = FloatField()
    maxY = maxNumberY

    minNumberY = FloatField()
    minY = minNumberY

    maxNumberZ = FloatField()
    maxZ = maxNumberZ

    minNumberZ = FloatField()
    minZ = minNumberZ
