# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


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


class ToonLineAttributes(DG):
    __slots__ = ()

    NODE_TYPE = "toonLineAttributes"

    lineWidth = FloatField()
    lwd = lineWidth

    lineVisibility = BoolField()
    lv = lineVisibility

    viewUpdate = ViewUpdateEnumField()
    vu = viewUpdate
