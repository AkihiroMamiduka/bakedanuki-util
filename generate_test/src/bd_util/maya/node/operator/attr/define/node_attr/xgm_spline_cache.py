# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField


class WidthRampPlugOperator(
    CompoundPlugOperator["WidthRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("widthRamp_Position", "wdrp"),
        ("widthRamp_FloatValue", "wdrfv"),
        ("widthRamp_Interp", "wdri"),
    )

    widthRamp_Position = FloatField()
    wdrp = widthRamp_Position

    widthRamp_FloatValue = FloatField()
    wdrfv = widthRamp_FloatValue

    widthRamp_Interp = EnumField()
    wdri = widthRamp_Interp


class WidthRampAttrOperator(
    CompoundAttrOperator[WidthRampPlugOperator]
):
    __slots__ = ()

    widthRamp_Position = FloatField()
    wdrp = widthRamp_Position

    widthRamp_FloatValue = FloatField()
    wdrfv = widthRamp_FloatValue

    widthRamp_Interp = EnumField()
    wdri = widthRamp_Interp


class WidthRampField(
    CompoundField[WidthRampAttrOperator, WidthRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WidthRampAttrOperator
    PLUG_CLS = WidthRampPlugOperator
