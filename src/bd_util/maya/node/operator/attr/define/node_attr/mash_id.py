# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
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


class ProbabilityRampPlugOperator(
    CompoundPlugOperator["ProbabilityRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("probabilityRamp_Position", "probabilityRampp"),
        ("probabilityRamp_FloatValue", "probabilityRampfv"),
        ("probabilityRamp_Interp", "probabilityRampi"),
    )

    probabilityRamp_Position = FloatField()
    probabilityRampp = probabilityRamp_Position

    probabilityRamp_FloatValue = FloatField()
    probabilityRampfv = probabilityRamp_FloatValue

    probabilityRamp_Interp = EnumField()
    probabilityRampi = probabilityRamp_Interp


class ProbabilityRampAttrOperator(
    CompoundAttrOperator[ProbabilityRampPlugOperator]
):
    __slots__ = ()

    probabilityRamp_Position = FloatField()
    probabilityRampp = probabilityRamp_Position

    probabilityRamp_FloatValue = FloatField()
    probabilityRampfv = probabilityRamp_FloatValue

    probabilityRamp_Interp = EnumField()
    probabilityRampi = probabilityRamp_Interp


class ProbabilityRampField(
    CompoundField[ProbabilityRampAttrOperator, ProbabilityRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProbabilityRampAttrOperator
    PLUG_CLS = ProbabilityRampPlugOperator
