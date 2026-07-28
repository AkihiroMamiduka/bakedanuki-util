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
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class FrequencyGraph_InterpEnumPlugOperator(
    EnumPlugOperator["FrequencyGraph_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FrequencyGraph_InterpEnumAttrOperator(
    EnumAttrOperator[FrequencyGraph_InterpEnumPlugOperator]
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


class FrequencyGraph_InterpEnumField(
    EnumField[
        FrequencyGraph_InterpEnumAttrOperator,
        FrequencyGraph_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FrequencyGraph_InterpEnumAttrOperator
    PLUG_CLS = FrequencyGraph_InterpEnumPlugOperator


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


class FrequencyGraphPlugOperator(
    CompoundPlugOperator["FrequencyGraphAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frequencyGraph_Position", "frequencyGraphp"),
        ("frequencyGraph_FloatValue", "frequencyGraphfv"),
        ("frequencyGraph_Interp", "frequencyGraphi"),
    )

    frequencyGraph_Position = FloatField(default_value=0.0)
    frequencyGraphp = frequencyGraph_Position

    frequencyGraph_FloatValue = FloatField(default_value=0.0)
    frequencyGraphfv = frequencyGraph_FloatValue

    frequencyGraph_Interp = FrequencyGraph_InterpEnumField(default_value=1)
    frequencyGraphi = frequencyGraph_Interp


class FrequencyGraphAttrOperator(
    CompoundAttrOperator[FrequencyGraphPlugOperator]
):
    __slots__ = ()

    frequencyGraph_Position = FloatField(default_value=0.0)
    frequencyGraphp = frequencyGraph_Position

    frequencyGraph_FloatValue = FloatField(default_value=0.0)
    frequencyGraphfv = frequencyGraph_FloatValue

    frequencyGraph_Interp = FrequencyGraph_InterpEnumField(default_value=1)
    frequencyGraphi = frequencyGraph_Interp


class FrequencyGraphField(
    CompoundField[FrequencyGraphAttrOperator, FrequencyGraphPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrequencyGraphAttrOperator
    PLUG_CLS = FrequencyGraphPlugOperator
