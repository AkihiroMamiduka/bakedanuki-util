# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_offset import (
    CentreOfRotationField,
    FalloffObjectField,
    HighClampField,
    LowClampField,
    MColourField,
    OffsetInputsField,
    OffsetsField,
    RayDirectionField,
    ReorderDistancePointField,
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
from ....attr.define.std.dt.mesh import DataMeshField
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


class OffsetTypeEnumPlugOperator(EnumPlugOperator["OffsetTypeEnumAttrOperator"]):
    __slots__ = ()

    OFFSET = 1
    MULTIPLY = 2
    OVERWRITE = 4
    CLOSEST_POINT_ON_MESH = 5
    MULTIPLY_BY_TIME = 6


class OffsetTypeEnumAttrOperator(EnumAttrOperator[OffsetTypeEnumPlugOperator]):
    __slots__ = ()

    OFFSET = 1
    MULTIPLY = 2
    OVERWRITE = 4
    CLOSEST_POINT_ON_MESH = 5
    MULTIPLY_BY_TIME = 6

    NAME_MAP = {
        OFFSET: "Offset",
        MULTIPLY: "Multiply",
        OVERWRITE: "Overwrite",
        CLOSEST_POINT_ON_MESH: "Closest Point on Mesh",
        MULTIPLY_BY_TIME: "Multiply by Time",
    }


class OffsetTypeEnumField(
    EnumField[OffsetTypeEnumAttrOperator, OffsetTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetTypeEnumAttrOperator
    PLUG_CLS = OffsetTypeEnumPlugOperator


class ReorderPointsEnumPlugOperator(EnumPlugOperator["ReorderPointsEnumAttrOperator"]):
    __slots__ = ()

    OFF = 1
    X = 2
    Y = 3
    Z = 4
    DISTANCE_TO_POINT = 5
    DISTANCE_TO_MESH = 6
    RANDOM = 7


class ReorderPointsEnumAttrOperator(EnumAttrOperator[ReorderPointsEnumPlugOperator]):
    __slots__ = ()

    OFF = 1
    X = 2
    Y = 3
    Z = 4
    DISTANCE_TO_POINT = 5
    DISTANCE_TO_MESH = 6
    RANDOM = 7

    NAME_MAP = {
        OFF: "Off",
        X: "X",
        Y: "Y",
        Z: "Z",
        DISTANCE_TO_POINT: "Distance to Point",
        DISTANCE_TO_MESH: "Distance to Mesh",
        RANDOM: "Random",
    }


class ReorderPointsEnumField(
    EnumField[ReorderPointsEnumAttrOperator, ReorderPointsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReorderPointsEnumAttrOperator
    PLUG_CLS = ReorderPointsEnumPlugOperator


class ClosestPointModeEnumPlugOperator(EnumPlugOperator["ClosestPointModeEnumAttrOperator"]):
    __slots__ = ()

    CLOSEST_POINT_ON_MESH = 1
    RAY_CAST = 2


class ClosestPointModeEnumAttrOperator(EnumAttrOperator[ClosestPointModeEnumPlugOperator]):
    __slots__ = ()

    CLOSEST_POINT_ON_MESH = 1
    RAY_CAST = 2

    NAME_MAP = {
        CLOSEST_POINT_ON_MESH: "Closest Point on Mesh",
        RAY_CAST: "Ray Cast",
    }


class ClosestPointModeEnumField(
    EnumField[ClosestPointModeEnumAttrOperator, ClosestPointModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClosestPointModeEnumAttrOperator
    PLUG_CLS = ClosestPointModeEnumPlugOperator


class GeneratedMASH_Offset(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Offset"

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

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    enable = BoolField(default_value=True)
    en = enable

    enablePosition = BoolField(default_value=True)

    enableRotation = BoolField(default_value=True)

    enableScale = BoolField(default_value=True)

    holdValue = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    startFrame = LongField(default_value=0, soft_min_value=0, soft_max_value=100)

    useTime = BoolField(default_value=True)

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

    enableId = BoolField(default_value=False)

    idOffset = LongField(default_value=0, soft_min_value=0, soft_max_value=20)

    enableLC = BoolField(default_value=False)
    enLC = enableLC

    enableHC = BoolField(default_value=False)
    enHC = enableHC

    lowClamp = LowClampField(default_value=(1.0, 1.0, 1.0))
    lcl = lowClamp
    lowClamp0 = lowClamp.lowClamp0
    lcl0 = lowClamp0
    lowClamp1 = lowClamp.lowClamp1
    lcl1 = lowClamp1
    lowClamp2 = lowClamp.lowClamp2
    lcl2 = lowClamp2

    strengthAffectsOffsets = BoolField(default_value=False)

    highClamp = HighClampField(default_value=(10.0, 10.0, 10.0))
    hcl = highClamp
    highClamp0 = highClamp.highClamp0
    hcl0 = highClamp0
    highClamp1 = highClamp.highClamp1
    hcl1 = highClamp1
    highClamp2 = highClamp.highClamp2
    hcl2 = highClamp2

    offsetType = OffsetTypeEnumField(default_value=1)
    oft = offsetType

    reorderPoints = ReorderPointsEnumField(default_value=1)

    reversePointOrder = BoolField(default_value=False)

    reorderDistancePoint = ReorderDistancePointField(default_value=(0.0, 0.0, 0.0))
    reorderDistancePointX = reorderDistancePoint.reorderDistancePointX
    reorderDistancePointx = reorderDistancePointX
    reorderDistancePointY = reorderDistancePoint.reorderDistancePointY
    reorderDistancePointy = reorderDistancePointY
    reorderDistancePointZ = reorderDistancePoint.reorderDistancePointZ
    reorderDistancePointz = reorderDistancePointZ

    reorderInputMesh = DataMeshField()

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)

    offsets = OffsetsField(default_value=(0.0, 0.0, 0.0))
    off = offsets
    offsets0 = offsets.offsets0
    off0 = offsets0
    offsets1 = offsets.offsets1
    off1 = offsets1
    offsets2 = offsets.offsets2
    off2 = offsets2

    closestPointMode = ClosestPointModeEnumField(default_value=1)

    rayDirection = RayDirectionField(default_value=(0.0, -1.0, 0.0))
    rayDirection0 = rayDirection.rayDirection0
    rayDirection1 = rayDirection.rayDirection1
    rayDirection2 = rayDirection.rayDirection2

    hideOnRayMiss = BoolField(default_value=False)

    offsetInputs = OffsetInputsField()
    positionOffset = offsetInputs.positionOffset
    rotationOffset = offsetInputs.rotationOffset
    scaleOffset = offsetInputs.scaleOffset

    inputMesh = DataMeshField()
    inM = inputMesh

    centreOfRotation = CentreOfRotationField(default_value=(0.0, 0.0, 0.0))
    centreOfRotation0 = centreOfRotation.centreOfRotation0
    centreOfRotation1 = centreOfRotation.centreOfRotation1
    centreOfRotation2 = centreOfRotation.centreOfRotation2

    falloffInfo = TypedField()
