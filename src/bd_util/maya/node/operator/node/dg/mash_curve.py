# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_curve import (
    FalloffObjectField,
    MColourField,
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


class MASH_Curve(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Curve"

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
    outArray = positionOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    ourRotPP = rotationOutPP

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    inArray = positionInPP
    rotationInPP = translateInPP.rotationInPP

    outAgePP = TypedField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    SimpleUEnvelope = FloatField()
    SimUEnv = SimpleUEnvelope

    SimpleValue = FloatField()
    SimpleVal = SimpleValue

    offsetAlongCurve = FloatField()

    clipStart = FloatField()

    falloffInfo = TypedField()

    clipEnd = FloatField()

    curveLengthAffectsSpeed = BoolField()

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

    proportionalMulti = BoolField()

    equalSpacing = BoolField()

    falloffMessage = MessageField()
    fmsg = falloffMessage

    timeStepVar = FloatField()
    tstev = timeStepVar

    velocityVariation = FloatField()

    velocityNoise = FloatField()

    velocityNoiseScale = FloatField()

    curveScale = FloatField()

    curveRoll = FloatField()

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    calculateRotation = BoolField()
    calRot = calculateRotation

    upVector = UpVectorField()
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    stopAtEnd = BoolField()
    sae = stopAtEnd

    localMode = BoolField()

    parametricLength = BoolField()

    timeStep = FloatField()
    ts = timeStep

    inCurves = DataNurbsCurveField(multi=True)

    aimCurve = DataNurbsCurveField()

    timeSlide = FloatField()
    tsli = timeSlide

    legacy2016 = BoolField()

    scaleRamp = ScaleRampField(multi=True)
