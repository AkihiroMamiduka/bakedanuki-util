# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class OffsetPlugOperator(
    CompoundPlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
        ("offsetZ", "oz"),
    )

    offsetX = FloatField()
    ox = offsetX

    offsetY = FloatField()
    oy = offsetY

    offsetZ = FloatField()
    oz = offsetZ


class OffsetAttrOperator(
    CompoundAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField()
    ox = offsetX

    offsetY = FloatField()
    oy = offsetY

    offsetZ = FloatField()
    oz = offsetZ


class OffsetField(
    CompoundField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField()
    ox = offsetX

    offsetY = FloatField()
    oy = offsetY

    offsetZ = FloatField()
    oz = offsetZ
