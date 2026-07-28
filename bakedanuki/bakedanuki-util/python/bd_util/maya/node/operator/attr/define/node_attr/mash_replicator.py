# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class PositionRamp_InterpEnumPlugOperator(EnumPlugOperator["PositionRamp_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PositionRamp_InterpEnumAttrOperator(EnumAttrOperator[PositionRamp_InterpEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class PositionRamp_InterpEnumField(
    EnumField[PositionRamp_InterpEnumAttrOperator, PositionRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionRamp_InterpEnumAttrOperator
    PLUG_CLS = PositionRamp_InterpEnumPlugOperator


class ScaleRamp_InterpEnumPlugOperator(EnumPlugOperator["ScaleRamp_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ScaleRamp_InterpEnumAttrOperator(EnumAttrOperator[ScaleRamp_InterpEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class ScaleRamp_InterpEnumField(
    EnumField[ScaleRamp_InterpEnumAttrOperator, ScaleRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleRamp_InterpEnumAttrOperator
    PLUG_CLS = ScaleRamp_InterpEnumPlugOperator


class RotationRamp_InterpEnumPlugOperator(EnumPlugOperator["RotationRamp_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RotationRamp_InterpEnumAttrOperator(EnumAttrOperator[RotationRamp_InterpEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class RotationRamp_InterpEnumField(
    EnumField[RotationRamp_InterpEnumAttrOperator, RotationRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationRamp_InterpEnumAttrOperator
    PLUG_CLS = RotationRamp_InterpEnumPlugOperator


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "positionInPP"),
        ("scaleInPP", "scaleInPP"),
        ("rotationInPP", "rotationInPP"),
        ("idInPP", "idInPP"),
        ("visibilityInPP", "visibilityInPP"),
    )

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateOutPPPlugOperator(
    CompoundPlugOperator["TranslateOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOutPP", "positionOutPP"),
        ("scaleOutPP", "scaleOutPP"),
        ("rotationOutPP", "rotationOutPP"),
        ("idOutPP", "idOutPP"),
        ("visibilityOutPP", "visibilityOutPP"),
    )

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class TranslateOutPPAttrOperator(
    CompoundAttrOperator[TranslateOutPPPlugOperator]
):
    __slots__ = ()

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class TranslateOutPPField(
    CompoundField[TranslateOutPPAttrOperator, TranslateOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateOutPPAttrOperator
    PLUG_CLS = TranslateOutPPPlugOperator

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class DriverTranslateInPPPlugOperator(
    CompoundPlugOperator["DriverTranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("driverPositionInPP", "driverPositionInPP"),
        ("driverScaleInPP", "driverScaleInPP"),
        ("driverRotationInPP", "driverRotationInPP"),
    )

    driverPositionInPP = DataVectorArrayField()

    driverScaleInPP = DataVectorArrayField()

    driverRotationInPP = DataVectorArrayField()


class DriverTranslateInPPAttrOperator(
    CompoundAttrOperator[DriverTranslateInPPPlugOperator]
):
    __slots__ = ()

    driverPositionInPP = DataVectorArrayField()

    driverScaleInPP = DataVectorArrayField()

    driverRotationInPP = DataVectorArrayField()


class DriverTranslateInPPField(
    CompoundField[DriverTranslateInPPAttrOperator, DriverTranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DriverTranslateInPPAttrOperator
    PLUG_CLS = DriverTranslateInPPPlugOperator

    driverPositionInPP = DataVectorArrayField()

    driverScaleInPP = DataVectorArrayField()

    driverRotationInPP = DataVectorArrayField()


class RotateAroundPlugOperator(
    Float3CompoundBasePlugOperator["RotateAroundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateAround0", "rotateAround0"),
        ("rotateAround1", "rotateAround1"),
        ("rotateAround2", "rotateAround2"),
    )

    rotateAround0 = FloatField(default_value=0.0)

    rotateAround1 = FloatField(default_value=0.0)

    rotateAround2 = FloatField(default_value=0.0)


class RotateAroundAttrOperator(
    Float3CompoundBaseAttrOperator[RotateAroundPlugOperator]
):
    __slots__ = ()

    rotateAround0 = FloatField(default_value=0.0)

    rotateAround1 = FloatField(default_value=0.0)

    rotateAround2 = FloatField(default_value=0.0)


class RotateAroundField(
    Float3CompoundBaseField[RotateAroundAttrOperator, RotateAroundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAroundAttrOperator
    PLUG_CLS = RotateAroundPlugOperator

    rotateAround0 = FloatField(default_value=0.0)

    rotateAround1 = FloatField(default_value=0.0)

    rotateAround2 = FloatField(default_value=0.0)


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class PositionRampPlugOperator(
    CompoundPlugOperator["PositionRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionRamp_Position", "positionRampp"),
        ("positionRamp_FloatValue", "positionRampfv"),
        ("positionRamp_Interp", "positionRampi"),
    )

    positionRamp_Position = FloatField(default_value=0.0)
    positionRampp = positionRamp_Position

    positionRamp_FloatValue = FloatField(default_value=0.0)
    positionRampfv = positionRamp_FloatValue

    positionRamp_Interp = PositionRamp_InterpEnumField(default_value=1)
    positionRampi = positionRamp_Interp


class PositionRampAttrOperator(
    CompoundAttrOperator[PositionRampPlugOperator]
):
    __slots__ = ()

    positionRamp_Position = FloatField(default_value=0.0)
    positionRampp = positionRamp_Position

    positionRamp_FloatValue = FloatField(default_value=0.0)
    positionRampfv = positionRamp_FloatValue

    positionRamp_Interp = PositionRamp_InterpEnumField(default_value=1)
    positionRampi = positionRamp_Interp


class PositionRampField(
    CompoundField[PositionRampAttrOperator, PositionRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionRampAttrOperator
    PLUG_CLS = PositionRampPlugOperator


class ScaleRampPlugOperator(
    CompoundPlugOperator["ScaleRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleRamp_Position", "scaleRampp"),
        ("scaleRamp_FloatValue", "scaleRampfv"),
        ("scaleRamp_Interp", "scaleRampi"),
    )

    scaleRamp_Position = FloatField(default_value=0.0)
    scaleRampp = scaleRamp_Position

    scaleRamp_FloatValue = FloatField(default_value=0.0)
    scaleRampfv = scaleRamp_FloatValue

    scaleRamp_Interp = ScaleRamp_InterpEnumField(default_value=1)
    scaleRampi = scaleRamp_Interp


class ScaleRampAttrOperator(
    CompoundAttrOperator[ScaleRampPlugOperator]
):
    __slots__ = ()

    scaleRamp_Position = FloatField(default_value=0.0)
    scaleRampp = scaleRamp_Position

    scaleRamp_FloatValue = FloatField(default_value=0.0)
    scaleRampfv = scaleRamp_FloatValue

    scaleRamp_Interp = ScaleRamp_InterpEnumField(default_value=1)
    scaleRampi = scaleRamp_Interp


class ScaleRampField(
    CompoundField[ScaleRampAttrOperator, ScaleRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleRampAttrOperator
    PLUG_CLS = ScaleRampPlugOperator


class RotationRampPlugOperator(
    CompoundPlugOperator["RotationRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationRamp_Position", "rotationRampp"),
        ("rotationRamp_FloatValue", "rotationRampfv"),
        ("rotationRamp_Interp", "rotationRampi"),
    )

    rotationRamp_Position = FloatField(default_value=0.0)
    rotationRampp = rotationRamp_Position

    rotationRamp_FloatValue = FloatField(default_value=0.0)
    rotationRampfv = rotationRamp_FloatValue

    rotationRamp_Interp = RotationRamp_InterpEnumField(default_value=1)
    rotationRampi = rotationRamp_Interp


class RotationRampAttrOperator(
    CompoundAttrOperator[RotationRampPlugOperator]
):
    __slots__ = ()

    rotationRamp_Position = FloatField(default_value=0.0)
    rotationRampp = rotationRamp_Position

    rotationRamp_FloatValue = FloatField(default_value=0.0)
    rotationRampfv = rotationRamp_FloatValue

    rotationRamp_Interp = RotationRamp_InterpEnumField(default_value=1)
    rotationRampi = rotationRamp_Interp


class RotationRampField(
    CompoundField[RotationRampAttrOperator, RotationRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationRampAttrOperator
    PLUG_CLS = RotationRampPlugOperator


class UpVectorPlugOperator(
    Float3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVector0", "uVec0"),
        ("upVector1", "uVec1"),
        ("upVector2", "uVec2"),
    )

    upVector0 = FloatField(default_value=0.0)
    uVec0 = upVector0

    upVector1 = FloatField(default_value=0.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=1.0)
    uVec2 = upVector2


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField(default_value=0.0)
    uVec0 = upVector0

    upVector1 = FloatField(default_value=0.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=1.0)
    uVec2 = upVector2


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField(default_value=0.0)
    uVec0 = upVector0

    upVector1 = FloatField(default_value=0.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=1.0)
    uVec2 = upVector2


class RotationOffsetPlugOperator(
    Float3CompoundBasePlugOperator["RotationOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationOffset0", "rotationOffset0"),
        ("rotationOffset1", "rotationOffset1"),
        ("rotationOffset2", "rotationOffset2"),
    )

    rotationOffset0 = FloatField(default_value=0.0)

    rotationOffset1 = FloatField(default_value=0.0)

    rotationOffset2 = FloatField(default_value=90.0)


class RotationOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[RotationOffsetPlugOperator]
):
    __slots__ = ()

    rotationOffset0 = FloatField(default_value=0.0)

    rotationOffset1 = FloatField(default_value=0.0)

    rotationOffset2 = FloatField(default_value=90.0)


class RotationOffsetField(
    Float3CompoundBaseField[RotationOffsetAttrOperator, RotationOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationOffsetAttrOperator
    PLUG_CLS = RotationOffsetPlugOperator

    rotationOffset0 = FloatField(default_value=0.0)

    rotationOffset1 = FloatField(default_value=0.0)

    rotationOffset2 = FloatField(default_value=90.0)


class ForwardVectorPlugOperator(
    Float3CompoundBasePlugOperator["ForwardVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forwardVector0", "forwardVector0"),
        ("forwardVector1", "forwardVector1"),
        ("forwardVector2", "forwardVector2"),
    )

    forwardVector0 = FloatField(default_value=0.0)

    forwardVector1 = FloatField(default_value=0.0)

    forwardVector2 = FloatField(default_value=0.0)


class ForwardVectorAttrOperator(
    Float3CompoundBaseAttrOperator[ForwardVectorPlugOperator]
):
    __slots__ = ()

    forwardVector0 = FloatField(default_value=0.0)

    forwardVector1 = FloatField(default_value=0.0)

    forwardVector2 = FloatField(default_value=0.0)


class ForwardVectorField(
    Float3CompoundBaseField[ForwardVectorAttrOperator, ForwardVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForwardVectorAttrOperator
    PLUG_CLS = ForwardVectorPlugOperator

    forwardVector0 = FloatField(default_value=0.0)

    forwardVector1 = FloatField(default_value=0.0)

    forwardVector2 = FloatField(default_value=0.0)
