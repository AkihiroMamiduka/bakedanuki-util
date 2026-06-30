# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_id import (
    FalloffObjectField,
    MColourField,
    ProbabilityRampField,
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


class IdtypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    RANDOM = 2
    CYCLE = 4
    FIXED = 5


class IdtypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    RANDOM = 2
    CYCLE = 4
    FIXED = 5

    NAME_MAP = {
        LINEAR: "Linear",
        RANDOM: "Random",
        CYCLE: "Cycle",
        FIXED: "Fixed",
    }


class IdtypeEnumField(
    EnumField[IdtypeEnumAttrOperator, IdtypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdtypeEnumAttrOperator
    PLUG_CLS = IdtypeEnumPlugOperator


class LoopTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    STOP_AT_END = 2
    OSCILLATE = 3


class LoopTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 1
    STOP_AT_END = 2
    OSCILLATE = 3

    NAME_MAP = {
        NORMAL: "Normal",
        STOP_AT_END: "Stop at end",
        OSCILLATE: "Oscillate",
    }


class LoopTypeEnumField(
    EnumField[LoopTypeEnumAttrOperator, LoopTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LoopTypeEnumAttrOperator
    PLUG_CLS = LoopTypeEnumPlugOperator


class MASH_Id(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Id"

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

    falloffInfo = TypedField()

    outputArray = DataVectorArrayField()
    outArray = outputArray

    outIdDoublesPP = DataDoubleArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    timeScale = FloatField()

    enable = BoolField()
    en = enable

    oscillate = BoolField()

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

    stopCycleEnd = BoolField()
    sce = stopCycleEnd

    seed = LongField()
    see = seed

    grpsize = LongField()
    gsz = grpsize

    numObjects = LongField()
    nuob = numObjects

    indexAnimateGap = LongField()
    inAnG = indexAnimateGap

    randomCycleLimit = LongField()

    fixed = LongField()
    fix = fixed

    randomCycle = BoolField()
    ranCyc = randomCycle

    idtype = IdtypeEnumField()
    idt = idtype

    loopType = LoopTypeEnumField()

    useProbability = BoolField()

    probabilityRamp = ProbabilityRampField(multi=True)
