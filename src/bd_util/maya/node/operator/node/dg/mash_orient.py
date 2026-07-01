# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_orient import (
    FalloffObjectField,
    MColourField,
    TargetInputField,
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
from ...attr.define.std.dt.mesh import DataMeshField
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


class OrientModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VELOCITY = 1
    AIM_AT_TARGET = 2
    ORIENT_TO_MESH = 3


class OrientModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    VELOCITY = 1
    AIM_AT_TARGET = 2
    ORIENT_TO_MESH = 3

    NAME_MAP = {
        VELOCITY: "Velocity",
        AIM_AT_TARGET: "Aim at Target",
        ORIENT_TO_MESH: "Orient To Mesh",
    }


class OrientModeEnumField(
    EnumField[OrientModeEnumAttrOperator, OrientModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OrientModeEnumAttrOperator
    PLUG_CLS = OrientModeEnumPlugOperator


class UpVectorMenuEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 1
    Y = 2
    Z = 3


class UpVectorMenuEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 1
    Y = 2
    Z = 3

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class UpVectorMenuEnumField(
    EnumField[UpVectorMenuEnumAttrOperator, UpVectorMenuEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorMenuEnumAttrOperator
    PLUG_CLS = UpVectorMenuEnumPlugOperator


class MASH_Orient(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Orient"

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
    rotationInPP = translateInPP.rotationInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    rotationOutPP = translateOutPP.rotationOutPP

    falloffInfo = TypedField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    smoothing = BoolField()

    muteIncoming = BoolField()

    inputMesh = DataMeshField()
    inM = inputMesh

    steeringForce = FloatField()

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

    targetX = BoolField()

    targetY = BoolField()

    targetZ = BoolField()

    falloffMessage = MessageField()
    fmsg = falloffMessage

    bankingStrength = FloatField()

    rotationXStrength = FloatField()

    rotationYStrength = FloatField()

    rotationZStrength = FloatField()

    inRotationPP = DataVectorArrayField()
    inRot = inRotationPP

    upVector = UpVectorField()
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    targetMode = BoolField()
    rMode = targetMode

    orientMode = OrientModeEnumField()

    upVectorMenu = UpVectorMenuEnumField()

    flipAxis = BoolField()

    targetInput = TargetInputField()
    tin = targetInput
    targetInput0 = targetInput.targetInput0
    tin0 = targetInput0
    targetInput1 = targetInput.targetInput1
    tin1 = targetInput1
    targetInput2 = targetInput.targetInput2
    tin2 = targetInput2
