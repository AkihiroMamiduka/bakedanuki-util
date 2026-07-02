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
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class EnvelopeRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class EnvelopeRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class EnvelopeRamp_InterpEnumField(
    EnumField[EnvelopeRamp_InterpEnumAttrOperator, EnvelopeRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeRamp_InterpEnumAttrOperator
    PLUG_CLS = EnvelopeRamp_InterpEnumPlugOperator


class BeatRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BeatRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class BeatRamp_InterpEnumField(
    EnumField[BeatRamp_InterpEnumAttrOperator, BeatRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BeatRamp_InterpEnumAttrOperator
    PLUG_CLS = BeatRamp_InterpEnumPlugOperator


class MuteRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class MuteRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class MuteRamp_InterpEnumField(
    EnumField[MuteRamp_InterpEnumAttrOperator, MuteRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MuteRamp_InterpEnumAttrOperator
    PLUG_CLS = MuteRamp_InterpEnumPlugOperator


class VelocityRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class VelocityRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class VelocityRamp_InterpEnumField(
    EnumField[VelocityRamp_InterpEnumAttrOperator, VelocityRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityRamp_InterpEnumAttrOperator
    PLUG_CLS = VelocityRamp_InterpEnumPlugOperator


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


class EnvelopeRampPlugOperator(
    CompoundPlugOperator["EnvelopeRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeRamp_Position", "envelopeRampp"),
        ("envelopeRamp_FloatValue", "envelopeRampfv"),
        ("envelopeRamp_Interp", "envelopeRampi"),
    )

    envelopeRamp_Position = FloatField()
    envelopeRampp = envelopeRamp_Position

    envelopeRamp_FloatValue = FloatField()
    envelopeRampfv = envelopeRamp_FloatValue

    envelopeRamp_Interp = EnvelopeRamp_InterpEnumField()
    envelopeRampi = envelopeRamp_Interp


class EnvelopeRampAttrOperator(
    CompoundAttrOperator[EnvelopeRampPlugOperator]
):
    __slots__ = ()

    envelopeRamp_Position = FloatField()
    envelopeRampp = envelopeRamp_Position

    envelopeRamp_FloatValue = FloatField()
    envelopeRampfv = envelopeRamp_FloatValue

    envelopeRamp_Interp = EnvelopeRamp_InterpEnumField()
    envelopeRampi = envelopeRamp_Interp


class EnvelopeRampField(
    CompoundField[EnvelopeRampAttrOperator, EnvelopeRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeRampAttrOperator
    PLUG_CLS = EnvelopeRampPlugOperator


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


class BeatRampPlugOperator(
    CompoundPlugOperator["BeatRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("beatRamp_Position", "beatRampp"),
        ("beatRamp_FloatValue", "beatRampfv"),
        ("beatRamp_Interp", "beatRampi"),
    )

    beatRamp_Position = FloatField()
    beatRampp = beatRamp_Position

    beatRamp_FloatValue = FloatField()
    beatRampfv = beatRamp_FloatValue

    beatRamp_Interp = BeatRamp_InterpEnumField()
    beatRampi = beatRamp_Interp


class BeatRampAttrOperator(
    CompoundAttrOperator[BeatRampPlugOperator]
):
    __slots__ = ()

    beatRamp_Position = FloatField()
    beatRampp = beatRamp_Position

    beatRamp_FloatValue = FloatField()
    beatRampfv = beatRamp_FloatValue

    beatRamp_Interp = BeatRamp_InterpEnumField()
    beatRampi = beatRamp_Interp


class BeatRampField(
    CompoundField[BeatRampAttrOperator, BeatRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BeatRampAttrOperator
    PLUG_CLS = BeatRampPlugOperator


class MuteRampPlugOperator(
    CompoundPlugOperator["MuteRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("muteRamp_Position", "muteRampp"),
        ("muteRamp_FloatValue", "muteRampfv"),
        ("muteRamp_Interp", "muteRampi"),
    )

    muteRamp_Position = FloatField()
    muteRampp = muteRamp_Position

    muteRamp_FloatValue = FloatField()
    muteRampfv = muteRamp_FloatValue

    muteRamp_Interp = MuteRamp_InterpEnumField()
    muteRampi = muteRamp_Interp


class MuteRampAttrOperator(
    CompoundAttrOperator[MuteRampPlugOperator]
):
    __slots__ = ()

    muteRamp_Position = FloatField()
    muteRampp = muteRamp_Position

    muteRamp_FloatValue = FloatField()
    muteRampfv = muteRamp_FloatValue

    muteRamp_Interp = MuteRamp_InterpEnumField()
    muteRampi = muteRamp_Interp


class MuteRampField(
    CompoundField[MuteRampAttrOperator, MuteRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MuteRampAttrOperator
    PLUG_CLS = MuteRampPlugOperator


class VelocityRampPlugOperator(
    CompoundPlugOperator["VelocityRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityRamp_Position", "velocityRampp"),
        ("velocityRamp_FloatValue", "velocityRampfv"),
        ("velocityRamp_Interp", "velocityRampi"),
    )

    velocityRamp_Position = FloatField()
    velocityRampp = velocityRamp_Position

    velocityRamp_FloatValue = FloatField()
    velocityRampfv = velocityRamp_FloatValue

    velocityRamp_Interp = VelocityRamp_InterpEnumField()
    velocityRampi = velocityRamp_Interp


class VelocityRampAttrOperator(
    CompoundAttrOperator[VelocityRampPlugOperator]
):
    __slots__ = ()

    velocityRamp_Position = FloatField()
    velocityRampp = velocityRamp_Position

    velocityRamp_FloatValue = FloatField()
    velocityRampfv = velocityRamp_FloatValue

    velocityRamp_Interp = VelocityRamp_InterpEnumField()
    velocityRampi = velocityRamp_Interp


class VelocityRampField(
    CompoundField[VelocityRampAttrOperator, VelocityRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityRampAttrOperator
    PLUG_CLS = VelocityRampPlugOperator
