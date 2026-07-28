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
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ProbabilityRamp_InterpEnumPlugOperator(
    EnumPlugOperator["ProbabilityRamp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ProbabilityRamp_InterpEnumAttrOperator(
    EnumAttrOperator[ProbabilityRamp_InterpEnumPlugOperator]
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


class ProbabilityRamp_InterpEnumField(
    EnumField[
        ProbabilityRamp_InterpEnumAttrOperator,
        ProbabilityRamp_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ProbabilityRamp_InterpEnumAttrOperator
    PLUG_CLS = ProbabilityRamp_InterpEnumPlugOperator


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


class ProbabilityRampPlugOperator(
    CompoundPlugOperator["ProbabilityRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("probabilityRamp_Position", "probabilityRampp"),
        ("probabilityRamp_FloatValue", "probabilityRampfv"),
        ("probabilityRamp_Interp", "probabilityRampi"),
    )

    probabilityRamp_Position = FloatField(default_value=0.0)
    probabilityRampp = probabilityRamp_Position

    probabilityRamp_FloatValue = FloatField(default_value=0.0)
    probabilityRampfv = probabilityRamp_FloatValue

    probabilityRamp_Interp = ProbabilityRamp_InterpEnumField(default_value=1)
    probabilityRampi = probabilityRamp_Interp


class ProbabilityRampAttrOperator(
    CompoundAttrOperator[ProbabilityRampPlugOperator]
):
    __slots__ = ()

    probabilityRamp_Position = FloatField(default_value=0.0)
    probabilityRampp = probabilityRamp_Position

    probabilityRamp_FloatValue = FloatField(default_value=0.0)
    probabilityRampfv = probabilityRamp_FloatValue

    probabilityRamp_Interp = ProbabilityRamp_InterpEnumField(default_value=1)
    probabilityRampi = probabilityRamp_Interp


class ProbabilityRampField(
    CompoundField[ProbabilityRampAttrOperator, ProbabilityRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProbabilityRampAttrOperator
    PLUG_CLS = ProbabilityRampPlugOperator
