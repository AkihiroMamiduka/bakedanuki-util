# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_curve import (
    FalloffObjectField,
    MColourField,
    ScaleRampField,
    TranslateInPPField,
    TranslateOutPPField,
    UpVectorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
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


class _GeneratedMASH_Curve(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Curve"

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

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    enable = BoolField(default_value=True)
    en = enable

    SimpleUEnvelope = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    SimUEnv = SimpleUEnvelope

    SimpleValue = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    SimpleVal = SimpleValue

    offsetAlongCurve = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    clipStart = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    falloffInfo = TypedField()

    clipEnd = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    curveLengthAffectsSpeed = BoolField(default_value=False)

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

    proportionalMulti = BoolField(default_value=True)

    equalSpacing = BoolField(default_value=False)

    falloffMessage = MessageField()
    fmsg = falloffMessage

    timeStepVar = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    tstev = timeStepVar

    velocityVariation = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    velocityNoise = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    velocityNoiseScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    curveScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    curveRoll = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    calculateRotation = BoolField(default_value=True)
    calRot = calculateRotation

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    stopAtEnd = BoolField(default_value=False)
    sae = stopAtEnd

    localMode = BoolField(default_value=False)

    parametricLength = BoolField(default_value=False)

    timeStep = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    ts = timeStep

    inCurves = DataNurbsCurveField(multi=True)

    aimCurve = DataNurbsCurveField()

    timeSlide = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    tsli = timeSlide

    legacy2016 = BoolField(default_value=False)

    scaleRamp = ScaleRampField(multi=True, default_value=(0.0, 0.0, 1.0))
