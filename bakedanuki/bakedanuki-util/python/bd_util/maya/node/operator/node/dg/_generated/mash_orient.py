# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_orient import (
    FalloffObjectField,
    MColourField,
    TargetInputField,
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


class OrientModeEnumPlugOperator(EnumPlugOperator["OrientModeEnumAttrOperator"]):
    __slots__ = ()

    VELOCITY = 1
    AIM_AT_TARGET = 2
    ORIENT_TO_MESH = 3


class OrientModeEnumAttrOperator(EnumAttrOperator[OrientModeEnumPlugOperator]):
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


class UpVectorMenuEnumPlugOperator(EnumPlugOperator["UpVectorMenuEnumAttrOperator"]):
    __slots__ = ()

    X = 1
    Y = 2
    Z = 3


class UpVectorMenuEnumAttrOperator(EnumAttrOperator[UpVectorMenuEnumPlugOperator]):
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


class GeneratedMASH_Orient(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Orient"

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
    rotationInPP = translateInPP.rotationInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    rotationOutPP = translateOutPP.rotationOutPP

    falloffInfo = TypedField()

    fallPosArray = DataVectorArrayField(readable=False)
    fArray = fallPosArray

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    enable = BoolField(default_value=True)
    en = enable

    smoothing = BoolField(default_value=False)

    muteIncoming = BoolField(default_value=True)

    inputMesh = DataMeshField()
    inM = inputMesh

    steeringForce = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

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

    targetX = BoolField(default_value=True)

    targetY = BoolField(default_value=True)

    targetZ = BoolField(default_value=True)

    falloffMessage = MessageField()
    fmsg = falloffMessage

    bankingStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    rotationXStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    rotationYStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    rotationZStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    inRotationPP = DataVectorArrayField()
    inRot = inRotationPP

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    targetMode = BoolField(default_value=False)
    rMode = targetMode

    orientMode = OrientModeEnumField(default_value=2)

    upVectorMenu = UpVectorMenuEnumField(default_value=2)

    flipAxis = BoolField(default_value=False)

    targetInput = TargetInputField(default_value=(0.0, 0.0, 0.0))
    tin = targetInput
    targetInput0 = targetInput.targetInput0
    tin0 = targetInput0
    targetInput1 = targetInput.targetInput1
    tin1 = targetInput1
    targetInput2 = targetInput.targetInput2
    tin2 = targetInput2
