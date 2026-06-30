# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class RampRGBPlugOperator(
    CompoundPlugOperator["RampRGBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampRGB_Position", "aiRampRGBp"),
        ("rampRGB_FloatValue", "aiRampRGBfv"),
        ("rampRGB_Interp", "aiRampRGBi"),
    )

    rampRGB_Position = FloatField()
    aiRampRGBp = rampRGB_Position

    rampRGB_FloatValue = FloatField()
    aiRampRGBfv = rampRGB_FloatValue

    rampRGB_Interp = EnumField()
    aiRampRGBi = rampRGB_Interp


class RampRGBAttrOperator(
    CompoundAttrOperator[RampRGBPlugOperator]
):
    __slots__ = ()

    rampRGB_Position = FloatField()
    aiRampRGBp = rampRGB_Position

    rampRGB_FloatValue = FloatField()
    aiRampRGBfv = rampRGB_FloatValue

    rampRGB_Interp = EnumField()
    aiRampRGBi = rampRGB_Interp


class RampRGBField(
    CompoundField[RampRGBAttrOperator, RampRGBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampRGBAttrOperator
    PLUG_CLS = RampRGBPlugOperator


class RampRPlugOperator(
    CompoundPlugOperator["RampRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampR_Position", "aiRampRp"),
        ("rampR_FloatValue", "aiRampRfv"),
        ("rampR_Interp", "aiRampRi"),
    )

    rampR_Position = FloatField()
    aiRampRp = rampR_Position

    rampR_FloatValue = FloatField()
    aiRampRfv = rampR_FloatValue

    rampR_Interp = EnumField()
    aiRampRi = rampR_Interp


class RampRAttrOperator(
    CompoundAttrOperator[RampRPlugOperator]
):
    __slots__ = ()

    rampR_Position = FloatField()
    aiRampRp = rampR_Position

    rampR_FloatValue = FloatField()
    aiRampRfv = rampR_FloatValue

    rampR_Interp = EnumField()
    aiRampRi = rampR_Interp


class RampRField(
    CompoundField[RampRAttrOperator, RampRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampRAttrOperator
    PLUG_CLS = RampRPlugOperator


class RampGPlugOperator(
    CompoundPlugOperator["RampGAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampG_Position", "aiRampGp"),
        ("rampG_FloatValue", "aiRampGfv"),
        ("rampG_Interp", "aiRampGi"),
    )

    rampG_Position = FloatField()
    aiRampGp = rampG_Position

    rampG_FloatValue = FloatField()
    aiRampGfv = rampG_FloatValue

    rampG_Interp = EnumField()
    aiRampGi = rampG_Interp


class RampGAttrOperator(
    CompoundAttrOperator[RampGPlugOperator]
):
    __slots__ = ()

    rampG_Position = FloatField()
    aiRampGp = rampG_Position

    rampG_FloatValue = FloatField()
    aiRampGfv = rampG_FloatValue

    rampG_Interp = EnumField()
    aiRampGi = rampG_Interp


class RampGField(
    CompoundField[RampGAttrOperator, RampGPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampGAttrOperator
    PLUG_CLS = RampGPlugOperator


class RampBPlugOperator(
    CompoundPlugOperator["RampBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rampB_Position", "aiRampBp"),
        ("rampB_FloatValue", "aiRampBfv"),
        ("rampB_Interp", "aiRampBi"),
    )

    rampB_Position = FloatField()
    aiRampBp = rampB_Position

    rampB_FloatValue = FloatField()
    aiRampBfv = rampB_FloatValue

    rampB_Interp = EnumField()
    aiRampBi = rampB_Interp


class RampBAttrOperator(
    CompoundAttrOperator[RampBPlugOperator]
):
    __slots__ = ()

    rampB_Position = FloatField()
    aiRampBp = rampB_Position

    rampB_FloatValue = FloatField()
    aiRampBfv = rampB_FloatValue

    rampB_Interp = EnumField()
    aiRampBi = rampB_Interp


class RampBField(
    CompoundField[RampBAttrOperator, RampBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampBAttrOperator
    PLUG_CLS = RampBPlugOperator
