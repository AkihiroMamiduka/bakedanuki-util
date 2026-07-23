# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class ViewUpdateEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ON = 0
    OFF = 2


class ViewUpdateEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ON = 0
    OFF = 2

    NAME_MAP = {
        ON: "ON",
        OFF: "OFF",
    }


class ViewUpdateEnumField(
    EnumField[ViewUpdateEnumAttrOperator, ViewUpdateEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewUpdateEnumAttrOperator
    PLUG_CLS = ViewUpdateEnumPlugOperator


class _GeneratedToonLineAttributes(DG):
    __slots__ = ()

    NODE_TYPE = "toonLineAttributes"

    lineWidth = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    lwd = lineWidth

    lineVisibility = BoolField(default_value=True)
    lv = lineVisibility

    viewUpdate = ViewUpdateEnumField(default_value=0)
    vu = viewUpdate
