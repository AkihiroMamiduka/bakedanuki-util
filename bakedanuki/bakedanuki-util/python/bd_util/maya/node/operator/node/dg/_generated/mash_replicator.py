# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_replicator import (
    DriverTranslateInPPField,
    FalloffObjectField,
    ForwardVectorField,
    MColourField,
    PositionRampField,
    RotateAroundField,
    RotationOffsetField,
    RotationRampField,
    ScaleRampField,
    TranslateInPPField,
    TranslateOutPPField,
    UpVectorField,
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
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
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


class RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class _GeneratedMASH_Replicator(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Replicator"

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

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    idOutPP = translateOutPP.idOutPP
    visibilityOutPP = translateOutPP.visibilityOutPP

    driverTranslateInPP = DriverTranslateInPPField()
    driverPositionInPP = driverTranslateInPP.driverPositionInPP
    driverScaleInPP = driverTranslateInPP.driverScaleInPP
    driverRotationInPP = driverTranslateInPP.driverRotationInPP

    replicantsPP = DataVectorArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    timeMachineValue = FloatField(default_value=0.0, min_value=0.0, soft_max_value=30.0)

    rotateAround = RotateAroundField(default_value=(0.0, 0.0, 0.0))
    rotateAround0 = rotateAround.rotateAround0
    rotateAround1 = rotateAround.rotateAround1
    rotateAround2 = rotateAround.rotateAround2

    enable = BoolField(default_value=True)
    en = enable

    offset = LongField(default_value=0, min_value=0, soft_max_value=30)

    patternModulus = LongField(default_value=2, min_value=2, soft_max_value=10)

    patternOffsetX = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternOffsetY = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternOffsetZ = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternScaleX = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternScaleY = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternScaleZ = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)

    patternRotationX = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    patternRotationY = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    patternRotationZ = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    patternAffectsPosition = BoolField(default_value=True)

    patternAffectsRotation = BoolField(default_value=True)

    patternAffectsScale = BoolField(default_value=True)

    patternAffectsID = BoolField(default_value=False)

    patternRotateTogether = BoolField(default_value=False)

    scaleTogether = BoolField(default_value=False)

    curveScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    timeSlide = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    tsli = timeSlide

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

    falloffInfo = TypedField()

    offsetPositionX = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)

    offsetPositionY = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)

    offsetPositionZ = FloatField(default_value=-2.0, soft_min_value=-10.0, soft_max_value=10.0)

    scalePointsX = FloatField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    scalePointsY = FloatField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    scalePointsZ = FloatField(default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0)

    rotatePointsX = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    rotatePointsY = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    rotatePointsZ = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    replicants = LongField(default_value=0, min_value=0, soft_max_value=100)

    positionRamp = PositionRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    scaleRamp = ScaleRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    rotationRamp = RotationRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    upVector = UpVectorField(default_value=(0.0, 0.0, 1.0))
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    rotationOffset = RotationOffsetField(default_value=(0.0, 0.0, 90.0))
    rotationOffset0 = rotationOffset.rotationOffset0
    rotationOffset1 = rotationOffset.rotationOffset1
    rotationOffset2 = rotationOffset.rotationOffset2

    forwardVector = ForwardVectorField(default_value=(0.0, 0.0, 0.0))
    forwardVector0 = forwardVector.forwardVector0
    forwardVector1 = forwardVector.forwardVector1
    forwardVector2 = forwardVector.forwardVector2

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    useCurve = BoolField(default_value=False)
    useC = useCurve

    idIsReplicant = BoolField(default_value=False)

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder
