# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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


class TranslateOutPPPlugOperator(
    CompoundPlugOperator["TranslateOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOutPP", "outArray"),
        ("rotationOutPP", "ourRotPP"),
    )

    positionOutPP = DataVectorArrayField()
    outArray = positionOutPP

    rotationOutPP = DataVectorArrayField()
    ourRotPP = rotationOutPP


class TranslateOutPPAttrOperator(
    CompoundAttrOperator[TranslateOutPPPlugOperator]
):
    __slots__ = ()

    positionOutPP = DataVectorArrayField()
    outArray = positionOutPP

    rotationOutPP = DataVectorArrayField()
    ourRotPP = rotationOutPP


class TranslateOutPPField(
    CompoundField[TranslateOutPPAttrOperator, TranslateOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateOutPPAttrOperator
    PLUG_CLS = TranslateOutPPPlugOperator

    positionOutPP = DataVectorArrayField()
    outArray = positionOutPP

    rotationOutPP = DataVectorArrayField()
    ourRotPP = rotationOutPP


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "inArray"),
        ("rotationInPP", "rotationInPP"),
    )

    positionInPP = DataVectorArrayField()
    inArray = positionInPP

    rotationInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()
    inArray = positionInPP

    rotationInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()
    inArray = positionInPP

    rotationInPP = DataVectorArrayField()


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

    scaleRamp_Interp = EnumField()
    scaleRampi = scaleRamp_Interp


class ScaleRampAttrOperator(
    CompoundAttrOperator[ScaleRampPlugOperator]
):
    __slots__ = ()

    scaleRamp_Position = FloatField()
    scaleRampp = scaleRamp_Position

    scaleRamp_FloatValue = FloatField()
    scaleRampfv = scaleRamp_FloatValue

    scaleRamp_Interp = EnumField()
    scaleRampi = scaleRamp_Interp


class ScaleRampField(
    CompoundField[ScaleRampAttrOperator, ScaleRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleRampAttrOperator
    PLUG_CLS = ScaleRampPlugOperator
