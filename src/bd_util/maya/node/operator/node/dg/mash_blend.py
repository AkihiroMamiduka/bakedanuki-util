# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_blend import (
    AltTranslateInPPField,
    FalloffObjectField,
    MColourField,
    TranslateInPPField,
    TranslateOutPPField,
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


class MergeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CROSSFADE = 1
    ADD = 2
    SUBTRACT = 3


class MergeTypeEnumAttrOperator(EnumAttrOperator):
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


class RotationInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MATRIX_LERP = 1
    QUATERNION_SLERP = 2


class RotationInterpolationEnumAttrOperator(EnumAttrOperator):
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


class MASH_Blend(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Blend"

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

    mergeType = MergeTypeEnumField()

    rotationInterpolation = RotationInterpolationEnumField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    enable = BoolField()
    en = enable

    enablePosition = BoolField()

    enableRotation = BoolField()

    enableScale = BoolField()

    enableId = BoolField()

    enableVisibility = BoolField()

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffPosition = BoolField()

    falloffRotation = BoolField()

    falloffScale = BoolField()

    falloffId = BoolField()

    falloffVisibility = BoolField()

    falloffMessage = MessageField()
    fmsg = falloffMessage
