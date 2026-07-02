# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ScaleRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ScaleRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class RotationRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RotationRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class BiasRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BiasRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class BiasRamp_InterpEnumField(
    EnumField[BiasRamp_InterpEnumAttrOperator, BiasRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRamp_InterpEnumAttrOperator
    PLUG_CLS = BiasRamp_InterpEnumPlugOperator


class BiasRampX_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BiasRampX_InterpEnumAttrOperator(EnumAttrOperator):
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


class BiasRampX_InterpEnumField(
    EnumField[BiasRampX_InterpEnumAttrOperator, BiasRampX_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampX_InterpEnumAttrOperator
    PLUG_CLS = BiasRampX_InterpEnumPlugOperator


class BiasRampY_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BiasRampY_InterpEnumAttrOperator(EnumAttrOperator):
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


class BiasRampY_InterpEnumField(
    EnumField[BiasRampY_InterpEnumAttrOperator, BiasRampY_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampY_InterpEnumAttrOperator
    PLUG_CLS = BiasRampY_InterpEnumPlugOperator


class BiasRampZ_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BiasRampZ_InterpEnumAttrOperator(EnumAttrOperator):
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


class BiasRampZ_InterpEnumField(
    EnumField[BiasRampZ_InterpEnumAttrOperator, BiasRampZ_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampZ_InterpEnumAttrOperator
    PLUG_CLS = BiasRampZ_InterpEnumPlugOperator


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
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


class RadialOffsetPlugOperator(
    Float3CompoundBasePlugOperator["RadialOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("radialOffset0", "radialOffset0"),
        ("radialOffset1", "radialOffset1"),
        ("radialOffset2", "radialOffset2"),
    )

    radialOffset0 = FloatField()

    radialOffset1 = FloatField()

    radialOffset2 = FloatField()


class RadialOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[RadialOffsetPlugOperator]
):
    __slots__ = ()

    radialOffset0 = FloatField()

    radialOffset1 = FloatField()

    radialOffset2 = FloatField()


class RadialOffsetField(
    Float3CompoundBaseField[RadialOffsetAttrOperator, RadialOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RadialOffsetAttrOperator
    PLUG_CLS = RadialOffsetPlugOperator

    radialOffset0 = FloatField()

    radialOffset1 = FloatField()

    radialOffset2 = FloatField()


class UpVectorPlugOperator(
    Float3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVector0", "uVec0"),
        ("upVector1", "uVec1"),
        ("upVector2", "uVec2"),
    )

    upVector0 = FloatField()
    uVec0 = upVector0

    upVector1 = FloatField()
    uVec1 = upVector1

    upVector2 = FloatField()
    uVec2 = upVector2


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField()
    uVec0 = upVector0

    upVector1 = FloatField()
    uVec1 = upVector1

    upVector2 = FloatField()
    uVec2 = upVector2


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField()
    uVec0 = upVector0

    upVector1 = FloatField()
    uVec1 = upVector1

    upVector2 = FloatField()
    uVec2 = upVector2


class PfxUpVectorPlugOperator(
    Float3CompoundBasePlugOperator["PfxUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pfxUpVector0", "pfxUpVector0"),
        ("pfxUpVector1", "pfxUpVector1"),
        ("pfxUpVector2", "pfxUpVector2"),
    )

    pfxUpVector0 = FloatField()

    pfxUpVector1 = FloatField()

    pfxUpVector2 = FloatField()


class PfxUpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[PfxUpVectorPlugOperator]
):
    __slots__ = ()

    pfxUpVector0 = FloatField()

    pfxUpVector1 = FloatField()

    pfxUpVector2 = FloatField()


class PfxUpVectorField(
    Float3CompoundBaseField[PfxUpVectorAttrOperator, PfxUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PfxUpVectorAttrOperator
    PLUG_CLS = PfxUpVectorPlugOperator

    pfxUpVector0 = FloatField()

    pfxUpVector1 = FloatField()

    pfxUpVector2 = FloatField()


class ForwardVectorPlugOperator(
    Float3CompoundBasePlugOperator["ForwardVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forwardVector0", "forwardVector0"),
        ("forwardVector1", "forwardVector1"),
        ("forwardVector2", "forwardVector2"),
    )

    forwardVector0 = FloatField()

    forwardVector1 = FloatField()

    forwardVector2 = FloatField()


class ForwardVectorAttrOperator(
    Float3CompoundBaseAttrOperator[ForwardVectorPlugOperator]
):
    __slots__ = ()

    forwardVector0 = FloatField()

    forwardVector1 = FloatField()

    forwardVector2 = FloatField()


class ForwardVectorField(
    Float3CompoundBaseField[ForwardVectorAttrOperator, ForwardVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForwardVectorAttrOperator
    PLUG_CLS = ForwardVectorPlugOperator

    forwardVector0 = FloatField()

    forwardVector1 = FloatField()

    forwardVector2 = FloatField()


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class ScaleRampPlugOperator(
    CompoundPlugOperator["ScaleRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleRamp_Position", "scaleRampp"),
        ("scaleRamp_FloatValue", "scaleRampfv"),
        ("scaleRamp_Interp", "scaleRampi"),
    )

    scaleRamp_Position = FloatField()
    scaleRampp = scaleRamp_Position

    scaleRamp_FloatValue = FloatField()
    scaleRampfv = scaleRamp_FloatValue

    scaleRamp_Interp = ScaleRamp_InterpEnumField()
    scaleRampi = scaleRamp_Interp


class ScaleRampAttrOperator(
    CompoundAttrOperator[ScaleRampPlugOperator]
):
    __slots__ = ()

    scaleRamp_Position = FloatField()
    scaleRampp = scaleRamp_Position

    scaleRamp_FloatValue = FloatField()
    scaleRampfv = scaleRamp_FloatValue

    scaleRamp_Interp = ScaleRamp_InterpEnumField()
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

    rotationRamp_Position = FloatField()
    rotationRampp = rotationRamp_Position

    rotationRamp_FloatValue = FloatField()
    rotationRampfv = rotationRamp_FloatValue

    rotationRamp_Interp = RotationRamp_InterpEnumField()
    rotationRampi = rotationRamp_Interp


class RotationRampAttrOperator(
    CompoundAttrOperator[RotationRampPlugOperator]
):
    __slots__ = ()

    rotationRamp_Position = FloatField()
    rotationRampp = rotationRamp_Position

    rotationRamp_FloatValue = FloatField()
    rotationRampfv = rotationRamp_FloatValue

    rotationRamp_Interp = RotationRamp_InterpEnumField()
    rotationRampi = rotationRamp_Interp


class RotationRampField(
    CompoundField[RotationRampAttrOperator, RotationRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationRampAttrOperator
    PLUG_CLS = RotationRampPlugOperator


class BiasRampPlugOperator(
    CompoundPlugOperator["BiasRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("biasRamp_Position", "bRmpp"),
        ("biasRamp_FloatValue", "bRmpfv"),
        ("biasRamp_Interp", "bRmpi"),
    )

    biasRamp_Position = FloatField()
    bRmpp = biasRamp_Position

    biasRamp_FloatValue = FloatField()
    bRmpfv = biasRamp_FloatValue

    biasRamp_Interp = BiasRamp_InterpEnumField()
    bRmpi = biasRamp_Interp


class BiasRampAttrOperator(
    CompoundAttrOperator[BiasRampPlugOperator]
):
    __slots__ = ()

    biasRamp_Position = FloatField()
    bRmpp = biasRamp_Position

    biasRamp_FloatValue = FloatField()
    bRmpfv = biasRamp_FloatValue

    biasRamp_Interp = BiasRamp_InterpEnumField()
    bRmpi = biasRamp_Interp


class BiasRampField(
    CompoundField[BiasRampAttrOperator, BiasRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampAttrOperator
    PLUG_CLS = BiasRampPlugOperator


class BiasRampXPlugOperator(
    CompoundPlugOperator["BiasRampXAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("biasRampX_Position", "bRmpXp"),
        ("biasRampX_FloatValue", "bRmpXfv"),
        ("biasRampX_Interp", "bRmpXi"),
    )

    biasRampX_Position = FloatField()
    bRmpXp = biasRampX_Position

    biasRampX_FloatValue = FloatField()
    bRmpXfv = biasRampX_FloatValue

    biasRampX_Interp = BiasRampX_InterpEnumField()
    bRmpXi = biasRampX_Interp


class BiasRampXAttrOperator(
    CompoundAttrOperator[BiasRampXPlugOperator]
):
    __slots__ = ()

    biasRampX_Position = FloatField()
    bRmpXp = biasRampX_Position

    biasRampX_FloatValue = FloatField()
    bRmpXfv = biasRampX_FloatValue

    biasRampX_Interp = BiasRampX_InterpEnumField()
    bRmpXi = biasRampX_Interp


class BiasRampXField(
    CompoundField[BiasRampXAttrOperator, BiasRampXPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampXAttrOperator
    PLUG_CLS = BiasRampXPlugOperator


class BiasRampYPlugOperator(
    CompoundPlugOperator["BiasRampYAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("biasRampY_Position", "bRmpYp"),
        ("biasRampY_FloatValue", "bRmpYfv"),
        ("biasRampY_Interp", "bRmpYi"),
    )

    biasRampY_Position = FloatField()
    bRmpYp = biasRampY_Position

    biasRampY_FloatValue = FloatField()
    bRmpYfv = biasRampY_FloatValue

    biasRampY_Interp = BiasRampY_InterpEnumField()
    bRmpYi = biasRampY_Interp


class BiasRampYAttrOperator(
    CompoundAttrOperator[BiasRampYPlugOperator]
):
    __slots__ = ()

    biasRampY_Position = FloatField()
    bRmpYp = biasRampY_Position

    biasRampY_FloatValue = FloatField()
    bRmpYfv = biasRampY_FloatValue

    biasRampY_Interp = BiasRampY_InterpEnumField()
    bRmpYi = biasRampY_Interp


class BiasRampYField(
    CompoundField[BiasRampYAttrOperator, BiasRampYPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampYAttrOperator
    PLUG_CLS = BiasRampYPlugOperator


class BiasRampZPlugOperator(
    CompoundPlugOperator["BiasRampZAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("biasRampZ_Position", "bRmpZp"),
        ("biasRampZ_FloatValue", "bRmpZfv"),
        ("biasRampZ_Interp", "bRmpZi"),
    )

    biasRampZ_Position = FloatField()
    bRmpZp = biasRampZ_Position

    biasRampZ_FloatValue = FloatField()
    bRmpZfv = biasRampZ_FloatValue

    biasRampZ_Interp = BiasRampZ_InterpEnumField()
    bRmpZi = biasRampZ_Interp


class BiasRampZAttrOperator(
    CompoundAttrOperator[BiasRampZPlugOperator]
):
    __slots__ = ()

    biasRampZ_Position = FloatField()
    bRmpZp = biasRampZ_Position

    biasRampZ_FloatValue = FloatField()
    bRmpZfv = biasRampZ_FloatValue

    biasRampZ_Interp = BiasRampZ_InterpEnumField()
    bRmpZi = biasRampZ_Interp


class BiasRampZField(
    CompoundField[BiasRampZAttrOperator, BiasRampZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BiasRampZAttrOperator
    PLUG_CLS = BiasRampZPlugOperator
