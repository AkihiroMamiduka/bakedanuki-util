# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class ViewUpdateEnumPlugOperator(EnumPlugOperator["ViewUpdateEnumAttrOperator"]):
    __slots__ = ()

    ON = 0
    OFF = 2


class ViewUpdateEnumAttrOperator(EnumAttrOperator[ViewUpdateEnumPlugOperator]):
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


class GeneratedToonLineAttributes(DG):
    __slots__ = ()

    NODE_TYPE = "toonLineAttributes"

    lineWidth = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    lwd = lineWidth

    lineVisibility = BoolField(default_value=True)
    lv = lineVisibility

    viewUpdate = ViewUpdateEnumField(default_value=0)
    vu = viewUpdate
