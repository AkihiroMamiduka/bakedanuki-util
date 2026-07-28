# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_random import (
    FalloffObjectField,
    MColourField,
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
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


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


class GeneratedMASH_Random(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Random"

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

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    inIterations = LongField(default_value=0)
    inIter = inIterations

    falloffInfo = TypedField()

    enable = BoolField(default_value=True)
    en = enable

    enableX = BoolField(default_value=True)

    enableY = BoolField(default_value=True)

    enableZ = BoolField(default_value=True)

    positionX = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    positionY = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    positionZ = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    rotationX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    rotationZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=180.0)

    scaleX = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    scaleY = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    scaleZ = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    absoluteScale = BoolField(default_value=True)

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    wholeNumbers = BoolField(default_value=False)
    whoNum = wholeNumbers

    normaliseRandom = BoolField(default_value=False)

    uniformRandom = BoolField(default_value=False)
    uniRand = uniformRandom

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)
    seed = randomSeed

    maxNumber = FloatField(default_value=10.0, soft_min_value=-100.0, soft_max_value=100.0)
    max = maxNumber

    minNumber = FloatField(default_value=-10.0, soft_min_value=-100.0, soft_max_value=100.0)
    min = minNumber

    maxNumberX = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    maxX = maxNumberX

    minNumberX = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    minX = minNumberX

    maxNumberY = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    maxY = maxNumberY

    minNumberY = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    minY = minNumberY

    maxNumberZ = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    maxZ = maxNumberZ

    minNumberZ = FloatField(default_value=0.0, soft_min_value=-100.0, soft_max_value=100.0)
    minZ = minNumberZ
