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
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ScaleRamp_InterpEnumPlugOperator(
    EnumPlugOperator["ScaleRamp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ScaleRamp_InterpEnumAttrOperator(
    EnumAttrOperator[ScaleRamp_InterpEnumPlugOperator]
):
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
    EnumField[
        ScaleRamp_InterpEnumAttrOperator, ScaleRamp_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ScaleRamp_InterpEnumAttrOperator
    PLUG_CLS = ScaleRamp_InterpEnumPlugOperator


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


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
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
    Float3CompoundBaseField[
        FalloffObjectAttrOperator, FalloffObjectPlugOperator
    ]
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

    upVector1 = FloatField(default_value=1.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=0.0)
    uVec2 = upVector2


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField(default_value=0.0)
    uVec0 = upVector0

    upVector1 = FloatField(default_value=1.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=0.0)
    uVec2 = upVector2


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField(default_value=0.0)
    uVec0 = upVector0

    upVector1 = FloatField(default_value=1.0)
    uVec1 = upVector1

    upVector2 = FloatField(default_value=0.0)
    uVec2 = upVector2


class ScaleRampPlugOperator(CompoundPlugOperator["ScaleRampAttrOperator"]):
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


class ScaleRampAttrOperator(CompoundAttrOperator[ScaleRampPlugOperator]):
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
