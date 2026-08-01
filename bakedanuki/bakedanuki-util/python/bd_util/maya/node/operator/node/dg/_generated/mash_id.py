# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_id import (
    FalloffObjectField,
    MColourField,
    ProbabilityRampField,
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


class MapDirectionEnumPlugOperator(
    EnumPlugOperator["MapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(
    EnumAttrOperator[MapDirectionEnumPlugOperator]
):
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


class TransformationSpaceEnumPlugOperator(
    EnumPlugOperator["TransformationSpaceEnumAttrOperator"]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(
    EnumAttrOperator[TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[
        TransformationSpaceEnumAttrOperator,
        TransformationSpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class IdtypeEnumPlugOperator(EnumPlugOperator["IdtypeEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 1
    RANDOM = 2
    CYCLE = 4
    FIXED = 5


class IdtypeEnumAttrOperator(EnumAttrOperator[IdtypeEnumPlugOperator]):
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


class LoopTypeEnumPlugOperator(EnumPlugOperator["LoopTypeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 1
    STOP_AT_END = 2
    OSCILLATE = 3


class LoopTypeEnumAttrOperator(EnumAttrOperator[LoopTypeEnumPlugOperator]):
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


class GeneratedMASHId(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Id"

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

    Envelope = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )

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

    falloffInfo = TypedField()

    outputArray = DataVectorArrayField()
    outArray = outputArray

    outIdDoublesPP = DataDoubleArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    timeScale = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )

    enable = BoolField(default_value=True)
    en = enable

    oscillate = BoolField(default_value=False)

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

    falloffMessage = MessageField()
    fmsg = falloffMessage

    stopCycleEnd = BoolField(default_value=False)
    sce = stopCycleEnd

    seed = LongField(default_value=1, min_value=0, soft_max_value=100)
    see = seed

    grpsize = LongField(default_value=1, min_value=1, soft_max_value=100)
    gsz = grpsize

    numObjects = LongField(default_value=1, min_value=1, soft_max_value=30)
    nuob = numObjects

    indexAnimateGap = LongField(
        default_value=0, min_value=0, soft_max_value=30
    )
    inAnG = indexAnimateGap

    randomCycleLimit = LongField(
        default_value=0, min_value=0, soft_max_value=30
    )

    fixed = LongField(default_value=0, min_value=0, soft_max_value=30)
    fix = fixed

    randomCycle = BoolField(default_value=True)
    ranCyc = randomCycle

    idtype = IdtypeEnumField(default_value=1)
    idt = idtype

    loopType = LoopTypeEnumField(default_value=1)

    useProbability = BoolField(default_value=False)

    probabilityRamp = ProbabilityRampField(
        multi=True, default_value=(0.0, 0.0, 1.0)
    )
