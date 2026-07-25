# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField


class OffsetPlugOperator(
    CompoundPlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
        ("offsetZ", "oz"),
    )

    offsetX = FloatField(default_value=0.0)
    ox = offsetX

    offsetY = FloatField(default_value=0.0)
    oy = offsetY

    offsetZ = FloatField(default_value=0.0)
    oz = offsetZ


class OffsetAttrOperator(
    CompoundAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField(default_value=0.0)
    ox = offsetX

    offsetY = FloatField(default_value=0.0)
    oy = offsetY

    offsetZ = FloatField(default_value=0.0)
    oz = offsetZ


class OffsetField(
    CompoundField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField(default_value=0.0)
    ox = offsetX

    offsetY = FloatField(default_value=0.0)
    oy = offsetY

    offsetZ = FloatField(default_value=0.0)
    oz = offsetZ
