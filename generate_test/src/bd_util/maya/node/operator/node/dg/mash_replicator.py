# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_replicator import (
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
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
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


class MASH_Replicator(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Replicator"

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

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    timeMachineValue = FloatField()

    rotateAround = RotateAroundField()
    rotateAround0 = rotateAround.rotateAround0
    rotateAround1 = rotateAround.rotateAround1
    rotateAround2 = rotateAround.rotateAround2

    enable = BoolField()
    en = enable

    offset = LongField()

    patternModulus = LongField()

    patternOffsetX = FloatField()

    patternOffsetY = FloatField()

    patternOffsetZ = FloatField()

    patternScaleX = FloatField()

    patternScaleY = FloatField()

    patternScaleZ = FloatField()

    patternRotationX = FloatField()

    patternRotationY = FloatField()

    patternRotationZ = FloatField()

    patternAffectsPosition = BoolField()

    patternAffectsRotation = BoolField()

    patternAffectsScale = BoolField()

    patternAffectsID = BoolField()

    patternRotateTogether = BoolField()

    scaleTogether = BoolField()

    curveScale = FloatField()

    timeSlide = FloatField()
    tsli = timeSlide

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

    falloffInfo = TypedField()

    offsetPositionX = FloatField()

    offsetPositionY = FloatField()

    offsetPositionZ = FloatField()

    scalePointsX = FloatField()

    scalePointsY = FloatField()

    scalePointsZ = FloatField()

    rotatePointsX = FloatField()

    rotatePointsY = FloatField()

    rotatePointsZ = FloatField()

    replicants = LongField()

    positionRamp = PositionRampField(multi=True)

    scaleRamp = ScaleRampField(multi=True)

    rotationRamp = RotationRampField(multi=True)

    upVector = UpVectorField()
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    rotationOffset = RotationOffsetField()
    rotationOffset0 = rotationOffset.rotationOffset0
    rotationOffset1 = rotationOffset.rotationOffset1
    rotationOffset2 = rotationOffset.rotationOffset2

    forwardVector = ForwardVectorField()
    forwardVector0 = forwardVector.forwardVector0
    forwardVector1 = forwardVector.forwardVector1
    forwardVector2 = forwardVector.forwardVector2

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    useCurve = BoolField()
    useC = useCurve

    idIsReplicant = BoolField()

    rotateOrder = RotateOrderEnumField()
    ro = rotateOrder
