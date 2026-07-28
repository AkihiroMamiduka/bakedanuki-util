# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_blend import (
    AltTranslateInPPField,
    FalloffObjectField,
    MColourField,
    TranslateInPPField,
    TranslateOutPPField,
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


class MergeTypeEnumPlugOperator(EnumPlugOperator["MergeTypeEnumAttrOperator"]):
    __slots__ = ()

    CROSSFADE = 1
    ADD = 2
    SUBTRACT = 3


class MergeTypeEnumAttrOperator(EnumAttrOperator[MergeTypeEnumPlugOperator]):
    __slots__ = ()

    CROSSFADE = 1
    ADD = 2
    SUBTRACT = 3

    NAME_MAP = {
        CROSSFADE: "Crossfade",
        ADD: "Add",
        SUBTRACT: "Subtract",
    }


class MergeTypeEnumField(
    EnumField[MergeTypeEnumAttrOperator, MergeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeTypeEnumAttrOperator
    PLUG_CLS = MergeTypeEnumPlugOperator


class RotationInterpolationEnumPlugOperator(EnumPlugOperator["RotationInterpolationEnumAttrOperator"]):
    __slots__ = ()

    MATRIX_LERP = 1
    QUATERNION_SLERP = 2


class RotationInterpolationEnumAttrOperator(EnumAttrOperator[RotationInterpolationEnumPlugOperator]):
    __slots__ = ()

    MATRIX_LERP = 1
    QUATERNION_SLERP = 2

    NAME_MAP = {
        MATRIX_LERP: "Matrix Lerp",
        QUATERNION_SLERP: "Quaternion Slerp",
    }


class RotationInterpolationEnumField(
    EnumField[RotationInterpolationEnumAttrOperator, RotationInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationInterpolationEnumAttrOperator
    PLUG_CLS = RotationInterpolationEnumPlugOperator


class GeneratedMASH_Blend(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Blend"

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

    altInputPoints = TypedField()

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    altTranslateInPP = AltTranslateInPPField()
    altPositionInPP = altTranslateInPP.altPositionInPP
    altScaleInPP = altTranslateInPP.altScaleInPP
    altRotationInPP = altTranslateInPP.altRotationInPP
    altIdInPP = altTranslateInPP.altIdInPP
    altVisibilityInPP = altTranslateInPP.altVisibilityInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    idOutPP = translateOutPP.idOutPP
    visibilityOutPP = translateOutPP.visibilityOutPP

    mergeType = MergeTypeEnumField(default_value=1)

    rotationInterpolation = RotationInterpolationEnumField(default_value=1)

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

    enableId = BoolField(default_value=True)

    enableVisibility = BoolField(default_value=False)

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffPosition = BoolField(default_value=True)

    falloffRotation = BoolField(default_value=True)

    falloffScale = BoolField(default_value=False)

    falloffId = BoolField(default_value=False)

    falloffVisibility = BoolField(default_value=False)

    falloffMessage = MessageField()
    fmsg = falloffMessage
